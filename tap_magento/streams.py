"""Stream type classes for tap-magento."""

from pathlib import Path
import string
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
    primary_keys = []  #TODO
    replication_key = None
    
    schema = th.PropertiesList(
        th.Property("adjustment_negative", th.IntegerType),
        th.Property("adjustment_positive", th.IntegerType),
        th.Property("applied_rule_ids", "string"),
        th.Property("base_adjustment_negative", th.IntegerType),
        th.Property("base_adjustment_positive", th.IntegerType),
        th.Property("base_currency_code", th.StringType),
        th.Property("base_discount_amount", th.IntegerType),
        th.Property("base_discount_canceled", th.IntegerType),
        th.Property("base_discount_invoiced", th.IntegerType),
        th.Property("base_discount_refunded", th.IntegerType),
        th.Property("base_grand_total", th.IntegerType),
        th.Property("base_discount_tax_compensation_amount", th.IntegerType),
        th.Property("base_discount_tax_compensation_invoiced", th.IntegerType),
        th.Property("base_discount_tax_compensation_refunded", th.IntegerType),
        th.Property("base_shipping_amount", th.IntegerType),
        th.Property("base_shipping_canceled", th.IntegerType),
        th.Property("base_shipping_discount_amount", th.IntegerType),
        th.Property("base_shipping_discount_tax_compensation_amnt", th.IntegerType),
        th.Property("base_shipping_incl_tax", th.IntegerType),
        th.Property("base_shipping_invoiced", th.IntegerType),
        th.Property("base_shipping_refunded", th.IntegerType),
        th.Property("base_shipping_tax_amount", th.IntegerType),
        th.Property("base_shipping_tax_refunded", th.IntegerType),
        th.Property("base_subtotal", th.IntegerType),
        th.Property("base_subtotal_canceled", th.IntegerType),
        th.Property("base_subtotal_incl_tax", th.IntegerType),
        th.Property("base_subtotal_invoiced", th.IntegerType),
        th.Property("base_subtotal_refunded", th.IntegerType),
        th.Property("base_tax_amount", th.IntegerType),
        th.Property("base_tax_canceled", th.IntegerType),
        th.Property("base_tax_invoiced", th.IntegerType),
        th.Property("base_tax_refunded", th.IntegerType),
        th.Property("base_total_canceled", th.IntegerType),
        th.Property("base_total_due", th.IntegerType),
        th.Property("base_total_invoiced", th.IntegerType),
        th.Property("base_total_invoiced_cost", th.IntegerType),
        th.Property("base_total_offline_refunded", th.IntegerType),
        th.Property("base_total_online_refunded", th.IntegerType),
        th.Property("base_total_paid", th.IntegerType),
        th.Property("base_total_qty_ordered", th.IntegerType),
        th.Property("base_total_refunded", th.IntegerType),
        th.Property("base_to_global_rate", th.IntegerType),
        th.Property("base_to_order_rate", th.IntegerType),
        th.Property("billing_address_id", th.IntegerType),
        th.Property("can_ship_partially", th.IntegerType),
        th.Property("can_ship_partially_item", th.IntegerType),
        th.Property("coupon_code", th.StringType),
        th.Property("created_at", th.StringType),
        th.Property("customer_dob", th.StringType),
        th.Property("customer_email", th.StringType),
        th.Property("customer_firstname", th.StringType),
        th.Property("customer_gender", th.IntegerType),
        th.Property("customer_group_id", th.IntegerType),
        th.Property("customer_id", th.IntegerType),
        th.Property("customer_is_guest", th.IntegerType),
        th.Property("customer_lastname", th.StringType),
        th.Property("customer_middlename", th.StringType),
        th.Property("customer_note", th.StringType),
        th.Property("customer_note_notify", th.IntegerType),
        th.Property("customer_prefix", th.StringType),
        th.Property("customer_suffix", th.StringType),
        th.Property("customer_taxvat", th.StringType),
        th.Property("discount_amount", th.IntegerType),
        th.Property("discount_canceled", th.IntegerType),
        th.Property("discount_description", th.StringType),
        th.Property("discount_invoiced", th.IntegerType),
        th.Property("discount_refunded", th.IntegerType),
        th.Property("edit_increment", th.IntegerType),
        th.Property("email_sent", th.IntegerType),
        th.Property("entity_id", th.IntegerType),
        th.Property("ext_customer_id", th.StringType),
        th.Property("ext_order_id", th.StringType),
        th.Property("forced_shipment_with_invoice", th.IntegerType),
        th.Property("global_currency_code", th.StringType),
        th.Property("grand_total", th.IntegerType),
        th.Property("discount_tax_compensation_amount", th.IntegerType),
        th.Property("discount_tax_compensation_invoiced", th.IntegerType),
        th.Property("discount_tax_compensation_refunded", th.IntegerType),
        th.Property("hold_before_state", th.StringType),
        th.Property("hold_before_status", th.StringType),
        th.Property("increment_id", th.StringType),
        th.Property("is_virtual", th.IntegerType),
        th.Property("order_currency_code", th.StringType),
        th.Property("original_increment_id", th.StringType),
        th.Property("payment_authorization_amount", th.IntegerType),
        th.Property("payment_auth_expiration", th.IntegerType),
        th.Property("protect_code", th.StringType),
        th.Property("quote_address_id", th.IntegerType),
        th.Property("quote_id", th.IntegerType),
        th.Property("relation_child_id", th.StringType),
        th.Property("relation_child_real_id", th.StringType),
        th.Property("relation_parent_id", th.StringType),
        th.Property("relation_parent_real_id", th.StringType),
        th.Property("remote_ip", th.StringType),
        th.Property("shipping_amount", th.IntegerType),
        th.Property("shipping_canceled", th.IntegerType),
        th.Property("shipping_description", th.StringType),
        th.Property("shipping_discount_amount", th.IntegerType),
        th.Property("shipping_discount_tax_compensation_amount", th.IntegerType),
        th.Property("shipping_incl_tax", th.IntegerType),
        th.Property("shipping_invoiced", th.IntegerType),
        th.Property("shipping_refunded", th.IntegerType),
        th.Property("shipping_tax_amount", th.IntegerType),
        th.Property("shipping_tax_refunded", th.IntegerType),
        th.Property("state", th.StringType),
        th.Property("status", th.StringType),
        th.Property("store_currency_code", th.StringType),
        th.Property("store_id", th.IntegerType),
        th.Property("store_name", th.StringType),
        th.Property("store_to_base_rate", th.IntegerType),
        th.Property("store_to_order_rate", th.IntegerType),
        th.Property("subtotal", th.IntegerType),
        th.Property("subtotal_canceled", th.IntegerType),
        th.Property("subtotal_incl_tax", th.IntegerType),
        th.Property("subtotal_invoiced", th.IntegerType),
        th.Property("subtotal_refunded", th.IntegerType),
        th.Property("tax_amount", th.IntegerType),
        th.Property("tax_canceled", th.IntegerType),
        th.Property("tax_invoiced", th.IntegerType),
        th.Property("tax_refunded", th.IntegerType),
        th.Property("total_canceled", th.IntegerType),
        th.Property("total_due", th.IntegerType),
        th.Property("total_invoiced", th.IntegerType),
        th.Property("total_item_count", th.IntegerType),
        th.Property("total_offline_refunded", th.IntegerType),
        th.Property("total_online_refunded", th.IntegerType),
        th.Property("total_paid", th.IntegerType),
        th.Property("total_qty_ordered", th.IntegerType),
        th.Property("total_refunded", th.IntegerType),
        th.Property("updated_at", th.StringType),
        th.Property("weight", th.IntegerType),
        th.Property("x_forwarded_for", th.StringType),
        
    )
