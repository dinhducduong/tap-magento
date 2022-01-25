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
    
    schema = 



    "adjustment_negative": 0,
"adjustment_positive": 0,
"applied_rule_ids": "string",
"base_adjustment_negative": 0,
"base_adjustment_positive": 0,
"base_currency_code": "string",
"base_discount_amount": 0,
"base_discount_canceled": 0,
"base_discount_invoiced": 0,
"base_discount_refunded": 0,
"base_grand_total": 0,
"base_discount_tax_compensation_amount": 0,
"base_discount_tax_compensation_invoiced": 0,
"base_discount_tax_compensation_refunded": 0,
"base_shipping_amount": 0,
"base_shipping_canceled": 0,
"base_shipping_discount_amount": 0,
"base_shipping_discount_tax_compensation_amnt": 0,
"base_shipping_incl_tax": 0,
"base_shipping_invoiced": 0,
"base_shipping_refunded": 0,
"base_shipping_tax_amount": 0,
"base_shipping_tax_refunded": 0,
"base_subtotal": 0,
"base_subtotal_canceled": 0,
"base_subtotal_incl_tax": 0,
"base_subtotal_invoiced": 0,
"base_subtotal_refunded": 0,
"base_tax_amount": 0,
"base_tax_canceled": 0,
"base_tax_invoiced": 0,
"base_tax_refunded": 0,
"base_total_canceled": 0,
"base_total_due": 0,
"base_total_invoiced": 0,
"base_total_invoiced_cost": 0,
"base_total_offline_refunded": 0,
"base_total_online_refunded": 0,
"base_total_paid": 0,
"base_total_qty_ordered": 0,
"base_total_refunded": 0,
"base_to_global_rate": 0,
"base_to_order_rate": 0,
"billing_address_id": 0,
"can_ship_partially": 0,
"can_ship_partially_item": 0,
"coupon_code": "string",
"created_at": "string",
"customer_dob": "string",
"customer_email": "string",
"customer_firstname": "string",
"customer_gender": 0,
"customer_group_id": 0,
"customer_id": 0,
"customer_is_guest": 0,
"customer_lastname": "string",
"customer_middlename": "string",
"customer_note": "string",
"customer_note_notify": 0,
"customer_prefix": "string",
"customer_suffix": "string",
"customer_taxvat": "string",
"discount_amount": 0,
"discount_canceled": 0,
"discount_description": "string",
"discount_invoiced": 0,
"discount_refunded": 0,
"edit_increment": 0,
"email_sent": 0,
"entity_id": 0,
"ext_customer_id": "string",
"ext_order_id": "string",
"forced_shipment_with_invoice": 0,
"global_currency_code": "string",
"grand_total": 0,
"discount_tax_compensation_amount": 0,
"discount_tax_compensation_invoiced": 0,
"discount_tax_compensation_refunded": 0,
"hold_before_state": "string",
"hold_before_status": "string",
"increment_id": "string",
"is_virtual": 0,
"order_currency_code": "string",
"original_increment_id": "string",
"payment_authorization_amount": 0,
"payment_auth_expiration": 0,
"protect_code": "string",
"quote_address_id": 0,
"quote_id": 0,
"relation_child_id": "string",
"relation_child_real_id": "string",
"relation_parent_id": "string",
"relation_parent_real_id": "string",
"remote_ip": "string",
"shipping_amount": 0,
"shipping_canceled": 0,
"shipping_description": "string",
"shipping_discount_amount": 0,
"shipping_discount_tax_compensation_amount": 0,
"shipping_incl_tax": 0,
"shipping_invoiced": 0,
"shipping_refunded": 0,
"shipping_tax_amount": 0,
"shipping_tax_refunded": 0,
"state": "string",
"status": "string",
"store_currency_code": "string",
"store_id": 0,
"store_name": "string",
"store_to_base_rate": 0,
"store_to_order_rate": 0,
"subtotal": 0,
"subtotal_canceled": 0,
"subtotal_incl_tax": 0,
"subtotal_invoiced": 0,
"subtotal_refunded": 0,
"tax_amount": 0,
"tax_canceled": 0,
"tax_invoiced": 0,
"tax_refunded": 0,
"total_canceled": 0,
"total_due": 0,
"total_invoiced": 0,
"total_item_count": 0,
"total_offline_refunded": 0,
"total_online_refunded": 0,
"total_paid": 0,
"total_qty_ordered": 0,
"total_refunded": 0,
"updated_at": "string",
"weight": 0,
"x_forwarded_for": "string",
"items": [],
"billing_address": {},
"payment": {},
"status_histories": [],
"extension_attributes": {}
}
