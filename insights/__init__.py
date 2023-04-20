# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe

__version__ = "0.7.2"


def notify(**kwargs):
    frappe.publish_realtime(
        event="insights_notification",
        user=frappe.session.user,
        message={
            "message": kwargs.get("message"),
            "title": kwargs.get("title"),
            "type": kwargs.get("type", "success"),
            "user": frappe.session.user,
        },
    )
