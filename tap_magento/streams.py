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


class OrdersStream(magentoStream):
    """Define Order Stream"""

    name = "orders"
    path = "orders"
    primary_keys = []  # TODO
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
        th.Property(
            "items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("additional_data", th.StringType),
                    th.Property("amount_refunded", th.IntegerType),
                    th.Property("applied_rule_ids", th.StringType),
                    th.Property("base_amount_refunded", th.IntegerType),
                    th.Property("base_cost", th.IntegerType),
                    th.Property("base_discount_amount", th.IntegerType),
                    th.Property("base_discount_invoiced", th.IntegerType),
                    th.Property("base_discount_refunded", th.IntegerType),
                    th.Property(
                        "base_discount_tax_compensation_amount", th.IntegerType
                    ),
                    th.Property(
                        "base_discount_tax_compensation_invoiced", th.IntegerType
                    ),
                    th.Property(
                        "base_discount_tax_compensation_refunded", th.IntegerType
                    ),
                    th.Property("base_original_price", th.IntegerType),
                    th.Property("base_price", th.IntegerType),
                    th.Property("base_price_incl_tax", th.IntegerType),
                    th.Property("base_row_invoiced", th.IntegerType),
                    th.Property("base_row_total", th.IntegerType),
                    th.Property("base_row_total_incl_tax", th.IntegerType),
                    th.Property("base_tax_amount", th.IntegerType),
                    th.Property("base_tax_before_discount", th.IntegerType),
                    th.Property("base_tax_invoiced", th.IntegerType),
                    th.Property("base_tax_refunded", th.IntegerType),
                    th.Property("base_weee_tax_applied_amount", th.IntegerType),
                    th.Property("base_weee_tax_applied_row_amnt", th.IntegerType),
                    th.Property("base_weee_tax_disposition", th.IntegerType),
                    th.Property("base_weee_tax_row_disposition", th.IntegerType),
                    th.Property("created_at", th.StringType),
                    th.Property("description", th.StringType),
                    th.Property("discount_amount", th.IntegerType),
                    th.Property("discount_invoiced", th.IntegerType),
                    th.Property("discount_percent", th.IntegerType),
                    th.Property("discount_refunded", th.IntegerType),
                    th.Property("event_id", th.IntegerType),
                    th.Property("ext_order_item_id", th.StringType),
                    th.Property("free_shipping", th.IntegerType),
                    th.Property("gw_base_price", th.IntegerType),
                    th.Property("gw_base_price_invoiced", th.IntegerType),
                    th.Property("gw_base_price_refunded", th.IntegerType),
                    th.Property("gw_base_tax_amount", th.IntegerType),
                    th.Property("gw_base_tax_amount_invoiced", th.IntegerType),
                    th.Property("gw_base_tax_amount_refunded", th.IntegerType),
                    th.Property("gw_id", th.IntegerType),
                    th.Property("gw_price", th.IntegerType),
                    th.Property("gw_price_invoiced", th.IntegerType),
                    th.Property("gw_price_refunded", th.IntegerType),
                    th.Property("gw_tax_amount", th.IntegerType),
                    th.Property("gw_tax_amount_invoiced", th.IntegerType),
                    th.Property("gw_tax_amount_refunded", th.IntegerType),
                    th.Property("discount_tax_compensation_amount", th.IntegerType),
                    th.Property("discount_tax_compensation_canceled", th.IntegerType),
                    th.Property("discount_tax_compensation_invoiced", th.IntegerType),
                    th.Property("discount_tax_compensation_refunded", th.IntegerType),
                    th.Property("is_qty_decimal", th.IntegerType),
                    th.Property("is_virtual", th.IntegerType),
                    th.Property("item_id", th.IntegerType),
                    th.Property("locked_do_invoice", th.IntegerType),
                    th.Property("locked_do_ship", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("no_discount", th.IntegerType),
                    th.Property("order_id", th.IntegerType),
                    th.Property("original_price", th.IntegerType),
                    th.Property("parent_item_id", th.IntegerType),
                    th.Property("price", th.IntegerType),
                    th.Property("price_incl_tax", th.IntegerType),
                    th.Property("product_id", th.IntegerType),
                    th.Property("product_type", th.StringType),
                    th.Property("qty_backordered", th.IntegerType),
                    th.Property("qty_canceled", th.IntegerType),
                    th.Property("qty_invoiced", th.IntegerType),
                    th.Property("qty_ordered", th.IntegerType),
                    th.Property("qty_refunded", th.IntegerType),
                    th.Property("qty_returned", th.IntegerType),
                    th.Property("qty_shipped", th.IntegerType),
                    th.Property("quote_item_id", th.IntegerType),
                    th.Property("row_invoiced", th.IntegerType),
                    th.Property("row_total", th.IntegerType),
                    th.Property("row_total_incl_tax", th.IntegerType),
                    th.Property("row_weight", th.IntegerType),
                    th.Property("sku", th.StringType),
                    th.Property("store_id", th.IntegerType),
                    th.Property("tax_amount", th.IntegerType),
                    th.Property("tax_before_discount", th.IntegerType),
                    th.Property("tax_canceled", th.IntegerType),
                    th.Property("tax_invoiced", th.IntegerType),
                    th.Property("tax_percent", th.IntegerType),
                    th.Property("tax_refunded", th.IntegerType),
                    th.Property("updated_at", th.StringType),
                    th.Property("weee_tax_applied", th.StringType),
                    th.Property("weee_tax_applied_amount", th.IntegerType),
                    th.Property("weee_tax_applied_row_amount", th.IntegerType),
                    th.Property("weee_tax_disposition", th.IntegerType),
                    th.Property("weee_tax_row_disposition", th.IntegerType),
                    th.Property("weight", th.IntegerType),
                    th.Property("parent_item", th.ObjectType),
                    th.Property(
                        "product_option",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "extension_attributes",
                                    th.ObjectType(
                                        th.Property(
                                            "custom_options",
                                            th.ArrayType(th.StringType),
                                            th.Property(
                                                "bundle_options",
                                                th.ArrayType(th.StringType),
                                                th.Property(
                                                    "downloadable_option",
                                                    th.ObjectType(
                                                        th.Property(
                                                            "downloadable_links",
                                                            th.ArrayType(th.StringType),
                                                        ),
                                                    ),
                                                ),
                                                th.Property("giftcard_item_option", th.ObjectType(
                                                    th.Property("giftcard_amount", th.StringType),
                                                    th.Property("custom_giftcard_amount", th.StringType),
                                                    th.Property("giftcard_sender_name", th.StringType),
                                                    th.Property("giftcard_recipient_name", th.StringType),
                                                    th.Property("giftcard_sender_email", th.StringType),
                                                    th.Property("giftcard_recipient_email", th.StringType),
                                                    th.Property("giftcard_message", th.StringType),
                                                    th.Property("extension_attributes", th.StringType)
                                                )
                                                ),
                                                th.Property("configurable_item_options", th.ArrayType(th.StringType))   
                                            ),
                                        )
                                    ),
                                )
                            )
                        ),
                    ),
                    th.Property("extension_attributes", th.ObjectType(
                        th.Property("gift_message", th.ObjectType(
                            th.Property("gift_message_id", th.IntegerType),
                            th.Property("customer_id", th.IntegerType),
                            th.Property("sender", th.StringType),
                            th.Property("recipient", th.StringType),
                            th.Property("message", th.StringType),
                            th.Property("extension_attributes", th.ObjectType(
                                th.Property("entity_id", th.StringType),
                                th.Property("entity_type", th.StringType),
                                th.Property("wrapping_id", th.StringType),
                                th.Property("wrapping_allow_gift_receipt", th.StringType),
                                th.Property("wrapping_add_printed_card", th.StringType)
                            ))
                        )),
                        th.Property("gw_id", th.StringType),
                        th.Property("gw_base_price", th.StringType),
                        th.Property("gw_price", th.StringType),
                        th.Property("gw_base_tax_amount", th.StringType),
                        th.Property("gw_tax_amount", th.StringType),
                        th.Property("gw_base_price_invoiced", th.StringType),
                        th.Property("gw_price_invoiced", th.StringType),
                        th.Property("gw_base_tax_amount_invoiced", th.StringType),
                        th.Property("gw_tax_amount_invoiced", th.StringType),
                        th.Property("gw_base_price_refunded", th.StringType),
                        th.Property("gw_price_refunded", th.StringType),
                        th.Property("gw_base_tax_amount_refunded", th.StringType),
                        th.Property("gw_tax_amount_refunded", th.StringType),
                        th.Property("vertex_tax_codes", th.ArrayType(th.StringType)),
                        th.Property("invoice_text_codes", th.ArrayType(th.StringType)),
                        th.Property("tax_codes", th.ArrayType(th.StringType)),
                        th.Property("vertex_commodity_code", th.ObjectType(
                            th.Property("code", th.StringType),
                            th.Property("type", th.StringType)
                        ))

                    ))
                )
            ),
        ),
        th.Property("billing_address", th.ObjectType(
            th.Property("address_type", th.StringType),
            th.Property("city", th.StringType),
            th.Property("company", th.StringType),
            th.Property("country_id", th.StringType),
            th.Property("customer_address_id", th.IntegerType),
            th.Property("customer_id", th.IntegerType),
            th.Property("email", th.StringType),
            th.Property("entity_id", th.IntegerType),
            th.Property("fax", th.StringType),
            th.Property("firstname", th.StringType),
            th.Property("lastname", th.StringType),
            th.Property("middlename", th.StringType),
            th.Property("parent_id", th.IntegerType),
            th.Property("postcode", th.StringType),
            th.Property("prefix", th.StringType),
            th.Property("region", th.StringType),
            th.Property("region_code", th.StringType),
            th.Property("region_id", th.IntegerType
        ))
    )
