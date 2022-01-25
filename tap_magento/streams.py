"""Stream type classes for tap-magento."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_magento.client import magentoStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UsersStream(magentoStream):
    """Define custom stream."""
    name = "users"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_D:IR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID"
        ),
        th.Property(
            "age",
            th.IntegerType,
            description="The user's age in years"
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address"
        ),
        th.Property("street", th.StringType),
        th.Property("city", th.StringType),
        th.Property(
            "state",
            th.StringType,
            description="State name in ISO 3166-2 format"
        ),
        th.Property("zip", th.StringType),
    ).to_dict()





class OrdersStream(magentoStream):
    """Define Order Stream"""
    name = "orders"
    path = "orders"
    primary_keys = [] #TODO
    replication_key = None
    
    schema = th.PropertiesList()



    