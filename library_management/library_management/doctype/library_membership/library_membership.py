# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe.utils
from frappe.model.document import Document

class LibraryMembership(Document):
	
	def before_submit(self):
		print(self.library_members,self.from_date)
		exists=frappe.db.exists(
			"Library Membership",{
				"library_members": self.library_members,
				"docstatus":1,
				"to_date":(">",self.from_date)
			}
		)
		if exists:
			frappe.throw("There is an active membership for this member")

		loan_period=frappe.db.get_single_value("Library Settings","loan_period")
		self.to_date=frappe.utils.add_days(self.from_date,loan_period or 30)