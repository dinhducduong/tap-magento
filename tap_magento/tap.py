"""Magento tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_magento.streams import (
    MagentoStream,
    UsersStream,
    OrdersStream,
    ProductsStream,
    ProductItemStocksStream,
    CategoryStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    # UsersStream,
    OrdersStream,
    ProductsStream,
    ProductItemStocksStream,
    CategoryStream
]


class TapMagento(Tap):
    """Magento tap class."""
    name = "tap-magento"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        
        th.Property(
            "api_key",
            th.StringType,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "username",
            th.StringType
        ),
        th.Property(
            "password",
            th.StringType
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
        th.Property(
            "store_url",
            th.StringType,
            required=True,
            description="The store url"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapMagento.cli()