# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
	# def before_save(self):
	# 	if self.type=="Issue":
	# 		print("\n\n\n\n\n\n\n############## ISSUE ####################\n\n\n\n\n\n\n\n\n")
	# 		self.validate_issue()
	# 		self.validate_maximum_limit()

	# 		article = frappe.get_doc("Article",self.article)
	# 		article.status=="Issued"
	# 		article.save()
		
	# 	elif self.type=="Return":
	# 		self.validate_return()

	# 		article.frappe.get_doc("Article",self.article)
	# 		article.status="Available"
	# 		article.save()
	
	def before_submit(self):
		if self.type=="Issue":
			print("\n\n\n\n\n\n\n############## ISSUE ####################\n\n\n\n\n\n\n\n\n")
			self.validate_issue()
			self.validate_maximum_limit()

			article = frappe.get_doc("Article",self.article)
			article.status="Issued"
			article.save()
		
		elif self.type=="Return":
			self.validate_return()

			article.frappe.get_doc("Article",self.article)
			article.status="Available"
			article.save()
	
	def validate_issue(self):
		self.validate_membership()
		article=frappe.get_doc("Article", self.article)
		if article.status=="Issued":
			frappe.throw("Article is already by another member")
	
	def validate_return(self):
		article=frappe.get_doc("Article",self.article)

		if article.status=="Available":
			frappe.throw("Article can not returned without being Issued")
	
	def validate_maximum_limit(self):
		max_articles=frappe.db.get_single_value("Library Settings","max_articles")
		
		count=frappe.db.count(
			"Library Transaction",
			{
				"library_members":self.library_members,
				"type":"Issue",
				"docstatus":1
			}
		)

		print("\n\n\n\n\t\t\t",count,"\n",max_articles,"\n\n\n\t\t")
		if count>=max_articles:
			frappe.throw("Maximum limit reached for issuing articles")
	
	def validate_membership(self):
		valid_memberships = frappe.db.exists(
			"Library Membership",
            {
				"library_members":self.library_members,
				"docstatus":1,
				"from_date":("<",self.date),
				"to_date":(">",self.date)
			}
		)
		if not valid_memberships:
			frappe.throw("The member does not have valid membership")