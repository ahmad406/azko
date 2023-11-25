// Copyright (c) 2023, parijat and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Performance OEE Availability"] = {
	"filters": [
		{
			"fieldname":"line",
			"label": __("Line"),
			"fieldtype": "Data",
		
		}

	],"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname == "hr" && parseFloat(data.hr) < 40 && data.type=="oee") {
			value = "<span style='color:red'>" + value + "</span>";
		}
		else if (column.fieldname == "hr" && parseFloat(data.hr) > 40 && data.type=="oee") {
			value = "<span style='color:green'>" + value + "</span>";
		}
		else if (data.line =="Total"){
			value = "<span style='font-weight: bold'>" + value + "</span>";

		}

		return value;
	},
};
