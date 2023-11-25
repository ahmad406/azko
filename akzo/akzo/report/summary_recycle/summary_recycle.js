// Copyright (c) 2023, parijat and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Summary Recycle"] = {
	"filters": [

	],"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname == "percent" && parseFloat(data.percent) < 90) {
			value = "<span style='color:red'>" + value + "</span>";
		}
		else if (column.fieldname == "percent" && parseFloat(data.percent) > 90) {
			value = "<span style='color:green'>" + value + "</span>";
		}

		return value;
	},
};
