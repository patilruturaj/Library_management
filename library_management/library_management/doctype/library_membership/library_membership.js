// Copyright (c) 2021, Ruturaj Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
		frm.add_custom_button("Create Transaction",()=>{
			frappe.new_doc("Library Transaction",{
				library_transaction:frm.doc.name
			})
		})
	}
});
