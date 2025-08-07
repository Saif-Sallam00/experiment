# message.py

import frappe
from frappe.model.document import Document

class Message(Document):
    def validate(self):
        if not self.message_text:
            frappe.msgprint(
                "The message text must have a value",
                title="Error",
                indicator="orange",
            )

        if self.use_indicator:
            frappe.msgprint(
                "The 'Use Indicator' field must not be checked",
                indicator=self.indicator_color,
            )
