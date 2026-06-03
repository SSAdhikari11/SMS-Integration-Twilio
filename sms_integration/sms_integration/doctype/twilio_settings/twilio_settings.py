# Copyright (c) 2026, Suraj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from twilio.rest import Client
from frappe import _


class TwilioSettings(Document):
	pass


@frappe.whitelist()
def send_customer_sms(customer):
    account_sid = frappe.get_single_value(
        "Twilio Settings", "account_sid"
    )
    auth_token = frappe.get_single_value(
        "Twilio Settings", "auth_token"
    )
    from_no = frappe.get_single_value(
        "Twilio Settings", "twilio_number"
    )

    # Remove formatting characters from Twilio number
    from_no = (
        from_no.replace("-", "")
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
    )

    # Get customer's primary contact
    contact_name = frappe.db.get_value(
        "Dynamic Link",
        {
            "link_doctype": "Customer",
            "link_name": customer,
            "parenttype": "Contact",
        },
        "parent",
    )

    if not contact_name:
        frappe.throw(_("No Contact found for this Customer"))

    # Get phone/mobile from Contact
    to_number = frappe.db.get_value(
        "Contact",
        contact_name,
        "phone"
    )

    if not to_number:
        frappe.throw(_("Contact does not have a phone number"))

    # Remove formatting characters from recipient number
    to_number = (
        to_number.replace("-", "")
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
    )

    # Add country code if missing
    if not to_number.startswith("+"):
        to_number = f"+91{to_number}"           #For indian numbers 

    message_body = f"Hello from Frappe. Customer: {customer}"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_body,
        from_=from_no,
        to=to_number
    )

    return message.sid