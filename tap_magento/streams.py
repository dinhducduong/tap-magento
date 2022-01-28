"""Stream type classes for tap-magento."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_magento.client import MagentoStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UsersStream(MagentoStream):
    """Define custom stream."""
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
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


class OrdersStream(MagentoStream):
    """Define Order Stream"""

    name = "orders"
    path = "/orders"
    primary_keys = []  # TODO
    replication_key = None

    schema = th.PropertiesList(
        th.Property("adjustment_negative", th.IntegerType),
        th.Property("adjustment_positive", th.IntegerType),
        th.Property("applied_rule_ids", th.StringType),
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
                    th.Property("parent_item", th.ObjectType()),
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
                                                th.Property(
                                                    "giftcard_item_option",
                                                    th.ObjectType(
                                                        th.Property(
                                                            "giftcard_amount",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "custom_giftcard_amount",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "giftcard_sender_name",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "giftcard_recipient_name",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "giftcard_sender_email",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "giftcard_recipient_email",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "giftcard_message",
                                                            th.StringType,
                                                        ),
                                                        th.Property(
                                                            "extension_attributes",
                                                            th.StringType,
                                                        ),
                                                    ),
                                                ),
                                                th.Property(
                                                    "configurable_item_options",
                                                    th.ArrayType(th.StringType),
                                                ),
                                            ),
                                        )
                                    ),
                                )
                            )
                        ),
                    ),
                    th.Property(
                        "extension_attributes",
                        th.ObjectType(
                            th.Property(
                                "gift_message",
                                th.ObjectType(
                                    th.Property("gift_message_id", th.IntegerType),
                                    th.Property("customer_id", th.IntegerType),
                                    th.Property("sender", th.StringType),
                                    th.Property("recipient", th.StringType),
                                    th.Property("message", th.StringType),
                                    th.Property(
                                        "extension_attributes",
                                        th.ObjectType(
                                            th.Property("entity_id", th.StringType),
                                            th.Property("entity_type", th.StringType),
                                            th.Property("wrapping_id", th.StringType),
                                            th.Property(
                                                "wrapping_allow_gift_receipt",
                                                th.StringType,
                                            ),
                                            th.Property(
                                                "wrapping_add_printed_card",
                                                th.StringType,
                                            ),
                                        ),
                                    ),
                                ),
                            ),
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
                            th.Property(
                                "vertex_tax_codes", th.ArrayType(th.StringType)
                            ),
                            th.Property(
                                "invoice_text_codes", th.ArrayType(th.StringType)
                            ),
                            th.Property("tax_codes", th.ArrayType(th.StringType)),
                            th.Property(
                                "vertex_commodity_code",
                                th.ObjectType(
                                    th.Property("code", th.StringType),
                                    th.Property("type", th.StringType),
                                ),
                            ),
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "billing_address",
            th.ObjectType(
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
                th.Property("region_id", th.IntegerType),
                th.Property("street", th.ArrayType(th.StringType)),
                th.Property("suffix", th.StringType),
                th.Property("telephone", th.StringType),
                th.Property("vat_id", th.StringType),
                th.Property("vat_is_valid", th.IntegerType),
                th.Property("vat_request_date", th.StringType),
                th.Property("vat_request_id", th.StringType),
                th.Property("vat_request_success", th.IntegerType),
                th.Property(
                    "extension_attributes",
                    th.ObjectType(
                        th.Property("vertex_vat_country_code", th.StringType)
                    ),
                ),
            ),
        ),
        th.Property(
            "payment",
            th.ObjectType(
                th.Property("account_status", th.StringType),
                th.Property("additional_data", th.StringType),
                th.Property("additional_information", th.ArrayType(th.StringType)),
                th.Property("address_status", th.StringType),
                th.Property("amount_authorized", th.IntegerType),
                th.Property("amount_canceled", th.IntegerType),
                th.Property("amount_ordered", th.IntegerType),
                th.Property("amount_paid", th.IntegerType),
                th.Property("amount_refunded", th.IntegerType),
                th.Property("anet_trans_method", th.StringType),
                th.Property("base_amount_authorized", th.IntegerType),
                th.Property("base_amount_canceled", th.IntegerType),
                th.Property("base_amount_ordered", th.IntegerType),
                th.Property("base_amount_paid", th.IntegerType),
                th.Property("base_amount_paid_online", th.IntegerType),
                th.Property("base_amount_refunded", th.IntegerType),
                th.Property("base_amount_refunded_online", th.IntegerType),
                th.Property("base_shipping_amount", th.IntegerType),
                th.Property("base_shipping_captured", th.IntegerType),
                th.Property("base_shipping_refunded", th.IntegerType),
                th.Property("cc_approval", th.StringType),
                th.Property("cc_avs_status", th.StringType),
                th.Property("cc_cid_status", th.StringType),
                th.Property("cc_debug_request_body", th.StringType),
                th.Property("cc_debug_response_body", th.StringType),
                th.Property("cc_debug_response_serialized", th.StringType),
                th.Property("cc_exp_month", th.StringType),
                th.Property("cc_exp_year", th.StringType),
                th.Property("cc_last4", th.StringType),
                th.Property("cc_number_enc", th.StringType),
                th.Property("cc_owner", th.StringType),
                th.Property("cc_secure_verify", th.StringType),
                th.Property("cc_ss_issue", th.StringType),
                th.Property("cc_ss_start_month", th.StringType),
                th.Property("cc_ss_start_year", th.StringType),
                th.Property("cc_status", th.StringType),
                th.Property("cc_status_description", th.StringType),
                th.Property("cc_trans_id", th.StringType),
                th.Property("cc_type", th.StringType),
                th.Property("echeck_account_name", th.StringType),
                th.Property("echeck_account_type", th.StringType),
                th.Property("echeck_bank_name", th.StringType),
                th.Property("echeck_routing_number", th.StringType),
                th.Property("echeck_type", th.StringType),
                th.Property("entity_id", th.IntegerType),
                th.Property("last_trans_id", th.StringType),
                th.Property("method", th.StringType),
                th.Property("parent_id", th.IntegerType),
                th.Property("po_number", th.StringType),
                th.Property("protection_eligibility", th.StringType),
                th.Property("quote_payment_id", th.IntegerType),
                th.Property("shipping_amount", th.IntegerType),
                th.Property("shipping_captured", th.IntegerType),
                th.Property("shipping_refunded", th.IntegerType),
                th.Property(
                    "extension_attributes",
                    th.ObjectType(
                        th.Property("notification_message", th.StringType),
                        th.Property(
                            "vault_payment_token",
                            th.ObjectType(
                                th.Property("entity_id", th.IntegerType),
                                th.Property("customer_id", th.IntegerType),
                                th.Property("public_hash", th.StringType),
                                th.Property("payment_method_code", th.StringType),
                                th.Property("type", th.StringType),
                                th.Property("created_at", th.StringType),
                                th.Property("expires_at", th.StringType),
                                th.Property("gateway_token", th.StringType),
                                th.Property("token_details", th.StringType),
                                th.Property("is_active", th.BooleanType),
                                th.Property("is_visible", th.BooleanType),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        th.Property(
            "status_histories",
            th.ArrayType(
                th.ObjectType(
                    th.Property("comment", th.StringType),
                    th.Property("created_at", th.StringType),
                    th.Property("entity_id", th.IntegerType),
                    th.Property("entity_name", th.StringType),
                    th.Property("is_customer_notified", th.IntegerType),
                    th.Property("is_visible_on_front", th.IntegerType),
                    th.Property("parent_id", th.IntegerType),
                    th.Property("status", th.StringType),
                    th.Property("extension_attributes", th.ObjectType()),
                )
            ),
        ),
        th.Property(
            "extension_attributes",
            th.ObjectType(
                th.Property(
                    "shipping_assignments",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property(
                                "shipping",
                                th.ObjectType(
                                    th.Property(
                                        "address",
                                        th.ObjectType(
                                            th.Property("address_type", th.StringType),
                                            th.Property("city", th.StringType),
                                            th.Property("company", th.StringType),
                                            th.Property("country_id", th.StringType),
                                            th.Property(
                                                "customer_address_id", th.IntegerType
                                            ),
                                            th.Property("customer_id", th.StringType),
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
                                            th.Property("region_id", th.IntegerType),
                                            th.Property(
                                                "street", th.ArrayType(th.StringType)
                                            ),
                                            th.Property("suffix", th.StringType),
                                            th.Property("telephone", th.StringType),
                                            th.Property("vat_id", th.StringType),
                                            th.Property("vat_is_valid", th.StringType),
                                            th.Property(
                                                "vat_request_date", th.StringType
                                            ),
                                            th.Property(
                                                "vat_request_id", th.StringType
                                            ),
                                            th.Property(
                                                "vat_request_success", th.StringType
                                            ),
                                            th.Property(
                                                "extension_attributes", th.StringType
                                            ),
                                        ),
                                    ),
                                    th.Property("method", th.StringType),
                                    th.Property(
                                        "total",
                                        th.ObjectType(
                                            th.Property(
                                                "base_shipping_amount", th.IntegerType
                                            ),
                                            th.Property(
                                                "base_shipping_canceled", th.StringType
                                            ),
                                            th.Property(
                                                "base_shipping_discount_amount",
                                                th.IntegerType,
                                            ),
                                            th.Property(
                                                "base_shipping_discount_tax_compensation_amnt",
                                                th.IntegerType,
                                            ),
                                            th.Property(
                                                "base_shipping_incl_tax", th.IntegerType
                                            ),
                                            th.Property(
                                                "base_shipping_invoiced", th.StringType
                                            ),
                                            th.Property(
                                                "base_shipping_refunded", th.StringType
                                            ),
                                            th.Property(
                                                "base_shipping_tax_amount",
                                                th.IntegerType,
                                            ),
                                            th.Property(
                                                "base_shipping_tax_refunded",
                                                th.StringType,
                                            ),
                                            th.Property(
                                                "shipping_amount", th.IntegerType
                                            ),
                                            th.Property(
                                                "shipping_canceled", th.StringType
                                            ),
                                            th.Property(
                                                "shipping_discount_amount",
                                                th.IntegerType,
                                            ),
                                            th.Property(
                                                "shipping_discount_tax_compensation_amount",
                                                th.IntegerType,
                                            ),
                                            th.Property(
                                                "shipping_incl_tax", th.IntegerType
                                            ),
                                            th.Property(
                                                "shipping_invoiced", th.StringType
                                            ),
                                            th.Property(
                                                "shipping_refunded", th.StringType
                                            ),
                                            th.Property(
                                                "shipping_tax_amount", th.IntegerType
                                            ),
                                            th.Property(
                                                "shipping_tax_refunded", th.IntegerType
                                            ),
                                            th.Property(
                                                "extension_attributes", th.StringType
                                            ),
                                        ),
                                    ),
                                    th.Property(
                                        "extension_attributes", th.StringType
                                    ),
                                ),
                            )
                        )
                    ),
                ),
                th.Property(
                    "payment_additional_info",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("key", th.StringType),
                            th.Property("value", th.StringType),
                        )
                    ),
                ),
                th.Property(
                    "company_order_attributes",
                    th.ObjectType(
                        th.Property("order_id", th.IntegerType),
                        th.Property("company_id", th.IntegerType),
                        th.Property("company_name", th.StringType),
                        th.Property("extension_attributes", th.ObjectType()),
                    ),
                ),
                th.Property(
                    "applied_taxes",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("code", th.StringType),
                            th.Property("title", th.StringType),
                            th.Property("percent", th.IntegerType),
                            th.Property("amount", th.IntegerType),
                            th.Property("base_amount", th.IntegerType),
                            th.Property(
                                "extension_attributes",
                                th.ObjectType(
                                    th.Property("rates", th.ArrayType(
                                        th.ObjectType(
                                            th.Property("code", th.StringType),
                                            th.Property("title", th.StringType),
                                            th.Property("percent", th.IntegerType),
                                            th.Property("extension_attributes", th.ObjectType())
                                        )
                                    ))
                                ),
                            ),
                        )
                    ),
                ),
                th.Property(
                    "item_applied_taxes",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("type", th.StringType),
                            th.Property("item_id", th.IntegerType),
                            th.Property("associated_item_id", th.IntegerType),
                            th.Property(
                                "applied_taxes",
                                th.ArrayType(
                                    th.ObjectType(
                                        th.Property("code", th.StringType),
                                        th.Property("title", th.StringType),
                                        th.Property("percent", th.StringType),
                                        th.Property("amount", th.StringType),
                                        th.Property("base_amount", th.StringType),
                                        th.Property(
                                            "extension_attributes", th.StringType
                                        ),
                                    )
                                ),
                            ),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property("converting_from_quote", th.BooleanType),
                th.Property("base_customer_balance_amount", th.IntegerType),
                th.Property("customer_balance_amount", th.IntegerType),
                th.Property("base_customer_balance_invoiced", th.IntegerType),
                th.Property("customer_balance_invoiced", th.IntegerType),
                th.Property("base_customer_balance_refunded", th.IntegerType),
                th.Property("customer_balance_refunded", th.IntegerType),
                th.Property("base_customer_balance_total_refunded", th.IntegerType),
                th.Property("customer_balance_total_refunded", th.IntegerType),
                th.Property(
                    "giftcards",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("code", th.StringType),
                            th.Property("amount", th.IntegerType),
                            th.Property("base_amount", th.IntegerType),
                        )
                    ),
                ),
                th.Property("base_gift_cards_amount", th.IntegerType),
                th.Property("gift_cards_amount", th.IntegerType),
                th.Property("base_gift_cards_invoiced", th.IntegerType),
                th.Property("gift_cards_invoiced", th.IntegerType),
                th.Property("base_gift_cards_refunded", th.IntegerType),
                th.Property("gift_cards_refunded", th.IntegerType),
                th.Property(
                    "gift_message",
                    th.ObjectType(
                        th.Property("gift_message_id", th.IntegerType),
                        th.Property("customer_id", th.IntegerType),
                        th.Property("sender", th.StringType),
                        th.Property("recipient", th.StringType),
                        th.Property("message", th.StringType),
                        th.Property(
                            "extension_attributes",
                            th.ObjectType(
                                th.Property("entity_id", th.StringType),
                                th.Property("entity_type", th.StringType),
                                th.Property("wrapping_id", th.IntegerType),
                                th.Property(
                                    "wrapping_allow_gift_receipt", th.BooleanType
                                ),
                                th.Property(
                                    "wrapping_add_printed_card", th.BooleanType
                                ),
                            ),
                        ),
                    ),
                ),
                th.Property("gw_id", th.StringType),
                th.Property("gw_allow_gift_receipt", th.StringType),
                th.Property("gw_add_card", th.StringType),
                th.Property("gw_base_price", th.StringType),
                th.Property("gw_price", th.StringType),
                th.Property("gw_items_base_price", th.StringType),
                th.Property("gw_items_price", th.StringType),
                th.Property("gw_card_base_price", th.StringType),
                th.Property("gw_card_price", th.StringType),
                th.Property("gw_base_tax_amount", th.StringType),
                th.Property("gw_tax_amount", th.StringType),
                th.Property("gw_items_base_tax_amount", th.StringType),
                th.Property("gw_items_tax_amount", th.StringType),
                th.Property("gw_card_base_tax_amount", th.StringType),
                th.Property("gw_card_tax_amount", th.StringType),
                th.Property("gw_base_price_incl_tax", th.StringType),
                th.Property("gw_price_incl_tax", th.StringType),
                th.Property("gw_items_base_price_incl_tax", th.StringType),
                th.Property("gw_items_price_incl_tax", th.StringType),
                th.Property("gw_card_base_price_incl_tax", th.StringType),
                th.Property("gw_card_price_incl_tax", th.StringType),
                th.Property("gw_base_price_invoiced", th.StringType),
                th.Property("gw_price_invoiced", th.StringType),
                th.Property("gw_items_base_price_invoiced", th.StringType),
                th.Property("gw_items_price_invoiced", th.StringType),
                th.Property("gw_card_base_price_invoiced", th.StringType),
                th.Property("gw_card_price_invoiced", th.StringType),
                th.Property("gw_base_tax_amount_invoiced", th.StringType),
                th.Property("gw_tax_amount_invoiced", th.StringType),
                th.Property("gw_items_base_tax_invoiced", th.StringType),
                th.Property("gw_items_tax_invoiced", th.StringType),
                th.Property("gw_card_base_tax_invoiced", th.StringType),
                th.Property("gw_card_tax_invoiced", th.StringType),
                th.Property("gw_base_price_refunded", th.StringType),
                th.Property("gw_price_refunded", th.StringType),
                th.Property("gw_items_base_price_refunded", th.StringType),
                th.Property("gw_items_price_refunded", th.StringType),
                th.Property("gw_card_base_price_refunded", th.StringType),
                th.Property("gw_card_price_refunded", th.StringType),
                th.Property("gw_base_tax_amount_refunded", th.StringType),
                th.Property("gw_tax_amount_refunded", th.StringType),
                th.Property("gw_items_base_tax_refunded", th.StringType),
                th.Property("gw_items_tax_refunded", th.StringType),
                th.Property("gw_card_base_tax_refunded", th.StringType),
                th.Property("gw_card_tax_refunded", th.StringType),
                th.Property("pickup_location_code", th.StringType),
                th.Property("notification_sent", th.IntegerType),
                th.Property("send_notification", th.IntegerType),
                th.Property("reward_points_balance", th.IntegerType),
                th.Property("reward_currency_amount", th.IntegerType),
                th.Property("base_reward_currency_amount", th.IntegerType),
                th.Property(
                    "amazon_order_reference_id",
                    th.ObjectType(
                        th.Property("amazon_order_reference_id", th.StringType),
                        th.Property("order_id", th.StringType),
                    ),
                ),
            ),
        ),
    ).to_dict()


class ProductsStream(MagentoStream):

    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("name", th.StringType),
        th.Property("attribute_set_id", th.IntegerType),
        th.Property("price", th.IntegerType),
        th.Property("status", th.IntegerType),
        th.Property("visibility", th.IntegerType),
        th.Property("type_id", th.StringType),
        th.Property("created_at", th.StringType),
        th.Property("updated_at", th.StringType),
        th.Property("weight", th.IntegerType),
        th.Property(
            "extension_attributes",
            th.ObjectType(
                th.Property("website_ids", th.ArrayType(th.IntegerType)),
                th.Property(
                    "category_links",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("position", th.IntegerType),
                            th.Property("category_id", th.StringType),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property(
                    "bundle_product_options",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("option_id", th.IntegerType),
                            th.Property("title", th.StringType),
                            th.Property("required", th.BooleanType),
                            th.Property("type", th.StringType),
                            th.Property("position", th.IntegerType),
                            th.Property("sku", th.StringType),
                            th.Property(
                                "product_links",
                                th.ArrayType(
                                    th.ObjectType(
                                        th.Property("id", th.StringType),
                                        th.Property("sku", th.StringType),
                                        th.Property("option_id", th.StringType),
                                        th.Property("qty", th.StringType),
                                        th.Property("position", th.StringType),
                                        th.Property("is_default", th.StringType),
                                        th.Property("price", th.StringType),
                                        th.Property("price_type", th.StringType),
                                        th.Property(
                                            "can_change_quantity", th.StringType
                                        ),
                                        th.Property(
                                            "extension_attributes", th.StringType
                                        ),
                                    )
                                ),
                            ),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property(
                    "stock_item",
                    th.ObjectType(
                        th.Property("item_id", th.IntegerType),
                        th.Property("product_id", th.IntegerType),
                        th.Property("stock_id", th.IntegerType),
                        th.Property("qty", th.IntegerType),
                        th.Property("is_in_stock", th.BooleanType),
                        th.Property("is_qty_decimal", th.BooleanType),
                        th.Property(
                            "show_default_notification_message", th.BooleanType
                        ),
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
                        th.Property("low_stock_date", th.StringType),
                        th.Property("is_decimal_divided", th.BooleanType),
                        th.Property("stock_status_changed_auto", th.IntegerType),
                        th.Property("extension_attributes", th.ObjectType()),
                    ),
                ),
                th.Property(
                    "downloadable_product_links",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("title", th.StringType),
                            th.Property("sort_order", th.IntegerType),
                            th.Property("is_shareable", th.IntegerType),
                            th.Property("price", th.IntegerType),
                            th.Property("number_of_downloads", th.IntegerType),
                            th.Property("link_type", th.StringType),
                            th.Property("link_file", th.StringType),
                            th.Property(
                                "link_file_content",
                                th.ObjectType(
                                    th.Property("file_data", th.StringType),
                                    th.Property("name", th.StringType),
                                    th.Property("extension_attributes", th.ObjectType()),
                                ),
                            ),
                            th.Property("link_url", th.StringType),
                            th.Property("sample_type", th.StringType),
                            th.Property("sample_file", th.StringType),
                            th.Property(
                                "sample_file_content",
                                th.ObjectType(
                                    th.Property("file_data", th.StringType),
                                    th.Property("name", th.StringType),
                                    th.Property("extension_attributes", th.ObjectType()),
                                ),
                            ),
                            th.Property("sample_url", th.StringType),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property(
                    "downloadable_product_samples",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("title", th.StringType),
                            th.Property("sort_order", th.IntegerType),
                            th.Property("sample_type", th.StringType),
                            th.Property("sample_file", th.StringType),
                            th.Property(
                                "sample_file_content",
                                th.ObjectType(
                                    th.Property("file_data", th.StringType),
                                    th.Property("name", th.StringType),
                                    th.Property("extension_attributes", th.ObjectType()),
                                ),
                            ),
                            th.Property("sample_url", th.StringType),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property(
                    "giftcard_amounts",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("attribute_id", th.IntegerType),
                            th.Property("website_id", th.IntegerType),
                            th.Property("value", th.IntegerType),
                            th.Property("website_value", th.IntegerType),
                            th.Property("extension_attributes", th.ObjectType()),
                        )
                    ),
                ),
                th.Property(
                    "configurable_product_options",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("attribute_id", th.StringType),
                            th.Property("label", th.StringType),
                            th.Property("position", th.IntegerType),
                            th.Property("is_use_default", th.BooleanType),
                            th.Property("values", th.ArrayType(th.ObjectType())),
                            th.Property("extension_attributes", th.ObjectType()),
                            th.Property("product_id", th.IntegerType),
                        )
                    ),
                ),
                th.Property("configurable_product_links", th.ArrayType(th.IntegerType)),
                th.Property(
                    "vertex_commodity_code",
                    th.ObjectType(
                        th.Property("code", th.StringType),
                        th.Property("type", th.StringType),
                    ),
                ),
            ),
        ),
        th.Property(
            "product_links",
            th.ArrayType(
                th.ObjectType(
                    th.Property("sku", th.StringType),
                    th.Property("link_type", th.StringType),
                    th.Property("linked_product_sku", th.StringType),
                    th.Property("linked_product_type", th.StringType),
                    th.Property("position", th.IntegerType),
                    th.Property(
                        "extension_attributes",
                        th.ObjectType(th.Property("qty", th.IntegerType)),
                    ),
                )
            ),
        ),
        th.Property(
            "options",
            th.ArrayType(
                th.ObjectType(
                    th.Property("product_sku", th.StringType),
                    th.Property("option_id", th.IntegerType),
                    th.Property("title", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("sort_order", th.IntegerType),
                    th.Property("is_require", th.BooleanType),
                    th.Property("price", th.IntegerType),
                    th.Property("price_type", th.StringType),
                    th.Property("sku", th.StringType),
                    th.Property("file_extension", th.StringType),
                    th.Property("max_characters", th.IntegerType),
                    th.Property("image_size_x", th.IntegerType),
                    th.Property("image_size_y", th.IntegerType),
                    th.Property(
                        "values",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("title", th.StringType),
                                th.Property("sort_order", th.IntegerType),
                                th.Property("price", th.IntegerType),
                                th.Property("price_type", th.StringType),
                                th.Property("sku", th.StringType),
                                th.Property("option_type_id", th.IntegerType),
                            )
                        ),
                    ),
                    th.Property(
                        "extension_attributes",
                        th.ObjectType(th.Property("vertex_flex_field", th.StringType)),
                    ),
                )
            ),
        ),
        th.Property(
            "media_gallery_entries",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("media_type", th.StringType),
                    th.Property("label", th.StringType),
                    th.Property("position", th.IntegerType),
                    th.Property("disabled", th.BooleanType),
                    th.Property("types", th.ArrayType(th.StringType)),
                    th.Property("file", th.StringType),
                    th.Property(
                        "content",
                        th.ObjectType(
                            th.Property("base64_encoded_data", th.StringType),
                            th.Property("type", th.StringType),
                            th.Property("name", th.StringType),
                        ),
                    ),
                    th.Property(
                        "extension_attributes",
                        th.ObjectType(
                            th.Property("video_content",
                                th.ObjectType(
                                    th.Property("media_type", th.StringType),
                                    th.Property("video_provider", th.StringType),
                                    th.Property("video_url", th.StringType),
                                    th.Property("video_title", th.StringType),
                                    th.Property("video_description", th.StringType),
                                    th.Property("video_metadata", th.StringType),
                                ),
                            )
                        )
                        
                    ),
                )
            ),
        ),
        th.Property(
            "tier_prices",
            th.ArrayType(
                th.ObjectType(
                    th.Property("customer_group_id", th.IntegerType),
                    th.Property("qty", th.IntegerType),
                    th.Property("value", th.IntegerType),
                    th.Property(
                        "extension_attributes",
                        th.ObjectType(
                            th.Property("percentage_value", th.IntegerType),
                            th.Property("website_id", th.IntegerType),
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "custom_attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("attribute_code", th.StringType),
                    # th.Property("value", th.StringType),
                )
            ),
        ),
    ).to_dict()
