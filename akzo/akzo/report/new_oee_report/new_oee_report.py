# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _

def execute(filters=None):
	sql="""SELECT * FROM `tabOEE Report`
		"""
	res=[]
	res.append({
		"line":"<strong>Line</strong>",
		"availability":"<strong>Availability</strong>",
		"performance":"<strong>Performance</strong>",
		"oee":"<strong>OEE</strong>",
		"type":""	
		})
	
	for i in frappe.db.sql(sql,as_dict=True):
			res.append({
				"line":i.line,
				"availability": float(i.availability),
				"performance":float(i.performance),
				"oee":float(i.oee),
				"type":type
				
			})
	
	res.append({
		"line":"",
		"availability":"",
		"performance":"",
		"oee":"",
		"type":""	
		})
	res.append({
		"line":"",
		"availability":"",
		"performance":"",
		"oee":"",
		"type":""	
		})

	columns =get_columns()
	message = ["<br>","<br>","<br>"]
	return columns, res,message


def get_columns():
	columns=[]

	columns+= [

		{
	 		'fieldname': 'line',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 200,
		},
		{
	 		'fieldname': 'availability',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'performance',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'oee',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'type',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
			'hidden':1
		}
		
		
		
	]



	
	return columns




def prnt():
	from akzo.akzo.report.new_oee_report.new_oee_report import execute
	
	return execute()



