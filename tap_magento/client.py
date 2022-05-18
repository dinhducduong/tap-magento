"""REST client handling, including MagentoStream base class."""

import requests
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from datetime import datetime


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

logging.getLogger("backoff").setLevel(logging.CRITICAL)

class MagentoStream(RESTStream):
    """Magento stream class."""
    access_token = None
    expires_in = None

    # OR use a dynamic url_base:
    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        store_url = self.config["store_url"]
        return f"{store_url}/rest/all/V1"

    records_jsonpath = "$.items[*]"  # Or override `parse_response`.
    # next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        if  self.config.get('username') and self.config.get('password') is not None:   
            token = self.get_token()
        else:
            token = self.config.get('api_key')    
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=token
        )

    def get_token(self):
        now = round(datetime.utcnow().timestamp())
        if not self.access_token:
            s = requests.Session()
            payload = {
                "Content-Type": "application/json",
                "username": self.config.get('username'),
                "password": self.config.get('password'),
                }
            login = s.post(f"{self.config['store_url']}/index.php/rest/V1/integration/admin/token", json=payload).json()
            self.access_token = login

        return self.access_token

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {
            "Content-Type": "application/json",
            # "Authorization": f"Bearer {self.config.get('api_key')}"
            }
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        next_page_token = None
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            json_data = response.json()
            total_count = json_data.get("total_count", 0)
            if json_data.get("search_criteria"):
                current_page = json_data.get("search_criteria").get("current_page")
            else:
                current_page = 1    
            if total_count > current_page * 300:
                next_page_token = current_page + 1
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {}
        params["searchCriteria[pageSize]"] = 300
        if not next_page_token:
            params["searchCriteria[currentPage]"] = 1
        else:
            params["searchCriteria[currentPage]"] = next_page_token
        
        if self.replication_key:
            start_date = self.get_starting_timestamp(context)
            if start_date is not None:
                start_date = start_date.strftime("%Y-%m-%d %H:%M:%S")
                params["sort"] = "asc"
                params["searchCriteria[filterGroups][0][filters][0][field]"] = self.replication_key
                params["searchCriteria[filterGroups][0][filters][0][value]"] = start_date
                params["searchCriteria[filterGroups][0][filters][0][conditionType]"] = "gt"
            params["order_by"] = self.replication_key
        return params

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row
