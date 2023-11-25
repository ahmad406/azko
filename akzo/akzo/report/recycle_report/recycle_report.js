// Copyright (c) 2023, parijat and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["recycle report"] = {
	"filters": [

	]
};

frappe.query_reports["recycle report"] = {
        "formatter": function(value, row, column, data, default_formatter) {
                value = default_formatter(value, row, column, data);
                if (column.id == "percentage" && value < 90) {
                        value = "<span style='background-color:red;color:white;font-weight:bold;'>" + value + "</span>";
//                      var $value = $value + $(value).css("background-color", "#75ff3a");
//              value = $value.wrap("<p></p>").parent().html();
                }
                 if (column.id == "percentage" && value > 90) {

                value = "<span style='background-color:green;color:white;font-weight:bold;'>" + value + "</span>";
                }
                return value;
        },
};


