# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class LibraryMembers(Document):
	# The menthod present in this class is run every time when form is saved.
	def before_save(self):
		self.full_name=f'{self.first_name} {self.last_name or ""}'