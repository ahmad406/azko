// Copyright (c) 2023, parijat and contributors
// For license information, please see license.txt

frappe.ui.form.on('Recycle Report', {
	// refresh: function(frm) {

	// }
	batch_makeing:function(frm){
		frm.trigger("cal")
	},
	filling:function(frm){
		frm.trigger("cal")
	},
	
	cal:function(frm){
		if (frm.doc.filling && frm.doc.batch_makeing){
		// frm.doc.percentage = (frm.doc.filling + frm.doc.batch_makeing)/2;
		cur_frm.set_value("percentage",(frm.doc.filling + frm.doc.batch_makeing)/2)
		}

	}
});
