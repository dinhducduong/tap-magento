"""Stream type classes for tap-magento."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_magento.client import MagentoStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class UsersStream(MagentoStream):
    """Define custom stream."""

    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType, description="The user's system ID"),
        th.Property("age", th.IntegerType, description="The user's age in years"),
        th.Property("email", th.StringType, description="The user's email address"),
        th.Property("street", th.StringType),
        th.Property("city", th.StringType),
        th.Property(
            "state", th.StringType, description="State name in ISO 3166-2 format"
        ),
        th.Property("zip", th.StringType),
    ).to_dict()


class OrdersStream(MagentoStream):
    """Define Order Stream"""

    name = "orders"
    path = "/orders"
    primary_keys = []  # TODO
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("adjustment_negative", th.IntegerType),
        th.Property("adjustment_positive", th.IntegerType),
        th.Property("applied_rule_ids", th.StringType),
        th.Property("base_adjustment_negative", th.IntegerType),
        th.Property("base_adjustment_positive", th.IntegerType),
        th.Property("base_currency_code", th.StringType),
        th.Property("base_discount_amount", th.NumberType),
        th.Property("base_discount_canceled", th.NumberType),
        th.Property("base_discount_invoiced", th.NumberType),
        th.Property("base_discount_refunded", th.NumberType),
        th.Property("base_grand_total", th.NumberType),
        th.Property("base_discount_tax_compensation_amount", th.NumberType),
        th.Property("base_discount_tax_compensation_invoiced", th.NumberType),
        th.Property("base_discount_tax_compensation_refunded", th.NumberType),
        th.Property("base_shipping_amount", th.NumberType),
        th.Property("base_shipping_canceled", th.NumberType),
        th.Property("base_shipping_discount_amount", th.NumberType),
        th.Property("base_shipping_discount_tax_compensation_amnt", th.NumberType),
        th.Property("base_shipping_incl_tax", th.NumberType),
        th.Property("base_shipping_invoiced", th.NumberType),
        th.Property("base_shipping_refunded", th.NumberType),
        th.Property("base_shipping_tax_amount", th.NumberType),
        th.Property("base_shipping_tax_refunded", th.NumberType),
        th.Property("base_subtotal", th.NumberType),
        th.Property("base_subtotal_canceled", th.NumberType),
        th.Property("base_subtotal_incl_tax", th.NumberType),
        th.Property("base_subtotal_invoiced", th.NumberType),
        th.Property("base_subtotal_refunded", th.NumberType),
        th.Property("base_tax_amount", th.NumberType),
        th.Property("base_tax_canceled", th.NumberType),
        th.Property("base_tax_invoiced", th.NumberType),
        th.Property("base_tax_refunded", th.NumberType),
        th.Property("base_total_canceled", th.NumberType),
        th.Property("base_total_due", th.NumberType),
        th.Property("base_total_invoiced", th.NumberType),
        th.Property("base_total_invoiced_cost", th.NumberType),
        th.Property("base_total_offline_refunded", th.NumberType),
        th.Property("base_total_online_refunded", th.NumberType),
        th.Property("base_total_paid", th.NumberType),
        th.Property("base_total_qty_ordered", th.NumberType),
        th.Property("base_total_refunded", th.NumberType),
        th.Property("base_to_global_rate", th.NumberType),
        th.Property("base_to_order_rate", th.NumberType),
        th.Property("billing_address_id", th.IntegerType),
        th.Property("can_ship_partially", th.IntegerType),
        th.Property("can_ship_partially_item", th.IntegerType),
        th.Property("coupon_code", th.StringType),
        th.Property("created_at", th.DateTimeType),
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
        th.Property("discount_amount", th.NumberType),
        th.Property("discount_canceled", th.NumberType),
        th.Property("discount_description", th.StringType),
        th.Property("discount_invoiced", th.NumberType),
        th.Property("discount_refunded", th.NumberType),
        th.Property("edit_increment", th.IntegerType),
        th.Property("email_sent", th.IntegerType),
        th.Property("entity_id", th.IntegerType),
        th.Property("ext_customer_id", th.StringType),
        th.Property("ext_order_id", th.StringType),
        th.Property("forced_shipment_with_invoice", th.IntegerType),
        th.Property("global_currency_code", th.StringType),
        th.Property("grand_total", th.NumberType),
        th.Property("discount_tax_compensation_amount", th.NumberType),
        th.Property("discount_tax_compensation_invoiced", th.NumberType),
        th.Property("discount_tax_compensation_refunded", th.NumberType),
        th.Property("hold_before_state", th.StringType),
        th.Property("hold_before_status", th.StringType),
        th.Property("increment_id", th.StringType),
        th.Property("is_virtual", th.IntegerType),
        th.Property("order_currency_code", th.StringType),
        th.Property("original_increment_id", th.StringType),
        th.Property("payment_authorization_amount", th.NumberType),
        th.Property("payment_auth_expiration", th.IntegerType),
        th.Property("protect_code", th.StringType),
        th.Property("quote_address_id", th.IntegerType),
        th.Property("quote_id", th.IntegerType),
        th.Property("relation_child_id", th.StringType),
        th.Property("relation_child_real_id", th.StringType),
        th.Property("relation_parent_id", th.StringType),
        th.Property("relation_parent_real_id", th.StringType),
        th.Property("remote_ip", th.StringType),
        th.Property("shipping_amount", th.NumberType),
        th.Property("shipping_canceled", th.NumberType),
        th.Property("shipping_description", th.StringType),
        th.Property("shipping_discount_amount", th.NumberType),
        th.Property("shipping_discount_tax_compensation_amount", th.NumberType),
        th.Property("shipping_incl_tax", th.NumberType),
        th.Property("shipping_invoiced", th.NumberType),
        th.Property("shipping_refunded", th.NumberType),
        th.Property("shipping_tax_amount", th.NumberType),
        th.Property("shipping_tax_refunded", th.NumberType),
        th.Property("state", th.StringType),
        th.Property("status", th.StringType),
        th.Property("store_currency_code", th.StringType),
        th.Property("store_id", th.IntegerType),
        th.Property("store_name", th.StringType),
        th.Property("store_to_base_rate", th.NumberType),
        th.Property("store_to_order_rate", th.NumberType),
        th.Property("subtotal", th.NumberType),
        th.Property("subtotal_canceled", th.NumberType),
        th.Property("subtotal_incl_tax", th.NumberType),
        th.Property("subtotal_invoiced", th.NumberType),
        th.Property("subtotal_refunded", th.NumberType),
        th.Property("tax_amount", th.NumberType),
        th.Property("tax_canceled", th.NumberType),
        th.Property("tax_invoiced", th.NumberType),
        th.Property("tax_refunded", th.NumberType),
        th.Property("total_canceled", th.NumberType),
        th.Property("total_due", th.NumberType),
        th.Property("total_invoiced", th.NumberType),
        th.Property("total_item_count", th.NumberType),
        th.Property("total_offline_refunded", th.NumberType),
        th.Property("total_online_refunded", th.NumberType),
        th.Property("total_paid", th.NumberType),
        th.Property("total_qty_ordered", th.IntegerType),
        th.Property("total_refunded", th.NumberType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("weight", th.NumberType),
        th.Property("x_forwarded_for", th.StringType),
        th.Property(
            "items",
            th.ArrayType(th.CustomType({"type": ["null", "object"]}))
        ),
        th.Property(
            "billing_address",
            th.CustomType({"type": ["object", "string"]})
        ),
        th.Property(
            "payment",
            th.CustomType({"type": ["object", "string"]})
        ),
        th.Property(
            "status_histories",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
        th.Property(
            "extension_attributes",
            th.CustomType({"type": ["object", "string"]})
        ),
    ).to_dict()


class ProductsStream(MagentoStream):

    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("name", th.StringType),
        th.Property("attribute_set_id", th.IntegerType),
        th.Property("price", th.NumberType),
        th.Property("status", th.IntegerType),
        th.Property("visibility", th.IntegerType),
        th.Property("type_id", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("weight", th.NumberType),
        th.Property(
            "extension_attributes",
            th.CustomType({"type": ["object", "string"]})
        ),
        th.Property(
            "product_links",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
        th.Property(
            "options",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
        th.Property(
            "media_gallery_entries",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
        th.Property(
            "tier_prices",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
        th.Property(
            "custom_attributes",
            th.ArrayType(
                th.CustomType({"type": ["null", "object"]})
            ),
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "product_sku": record["sku"],
        }
class ProductItemStocksStream(MagentoStream):

    name = "product_item_stocks"
    path = "/stockItems/{product_sku}"
    primary_keys = ["item_id"]
    records_jsonpath: str = "$[*]"
    replication_key = None
    parent_stream_type = ProductsStream
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("item_id", th.IntegerType),
        th.Property("product_id", th.IntegerType),
        th.Property("stock_id", th.IntegerType),
        th.Property("qty", th.IntegerType),
        th.Property("is_in_stock", th.BooleanType),
        th.Property("is_qty_decimal", th.BooleanType),
        th.Property("show_default_notification_message", th.BooleanType),
        th.Property("use_config_min_qty", th.BooleanType),
        th.Property("min_qty", th.IntegerType),
        th.Property("use_config_min_sale_qty", th.IntegerType),
        th.Property("min_sale_qty", th.IntegerType),
        th.Property("use_config_max_sale_qty", th.BooleanType),
        th.Property("max_sale_qty", th.IntegerType),
        th.Property("use_config_backorders", th.BooleanType),
        th.Property("backorders", th.IntegerType),
        th.Property("use_config_notify_stock_qty", th.BooleanType),
        th.Property("notify_stock_qty", th.IntegerType),
        th.Property("use_config_qty_increments", th.BooleanType),
        th.Property("qty_increments", th.IntegerType),
        th.Property("use_config_enable_qty_inc", th.BooleanType),
        th.Property("enable_qty_increments", th.BooleanType),
        th.Property("use_config_manage_stock", th.BooleanType),
        th.Property("manage_stock", th.BooleanType),
        th.Property("low_stock_date", th.DateTimeType),
        th.Property("is_decimal_divided", th.BooleanType),
        th.Property("stock_status_changed_auto", th.IntegerType),
    ).to_dict()
