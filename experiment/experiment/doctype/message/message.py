# Copyright (c) 2025, saif and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Message(Document):
	
	def validate(self):

		if not self.message_text:
			frappe.msgprint(
				"the messge text must have value",
				title="Error",
				indicator="orange",
				#raise_exception=True
			)
		
		if self.use_indicator:
			frappe.msgprint(
				"the use indicator must not be checked",
				indicator=self.indicator_color,
				#raise_exception=True
			)

		if self.list_data:
					# We split the string by comma to get a Python list
					list_items = [item.strip() for item in self.list_data.split(',') if item.strip()]

					frappe.msgprint(
						# The message itself is now a list
						list_items,
						title="Title",
						indicator="green",
						as_list=True,
						primary_action={
							'label': "Go to Google",
							# The 'action' key is a string containing valid JavaScript
							'action': "frappe.open_url('https://www.google.com')"
						}
					)