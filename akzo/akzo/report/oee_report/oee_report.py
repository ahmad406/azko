# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _

def execute(filters=None):
	sql="""SELECT line, avialability, performance, oee filling FROM `tabOEE Report` """


	res=[]
	import datetime
	current = datetime.datetime.now()
	today= ("{}-{}-{}".format(current.day,current.month,current.year))
	week_number = current.isocalendar()[1]  
	res.append({
		"line":"<strong>Line</strong>",
		"availability":"<strong>Availability</strong>",
		"performance":"<strong>Performance</strong>",
		"oee":"<strong>OEE</strong>",
		"type":""	
		})
	
	for i in frappe.db.sql(sql,as_dict=True):
		if i.type=="daily":
			res.append({
				"line":i.line,
				"availability": round(float(i.availability),2),
				"performance":round(float(i.performance),2),
				"oee":round(float(i.oee),2),
				"type":i.type
				
			})
	
	res.append({
		"line":"",
		"availability":"",
		"performance":"",
		"oee":"",
		"type":""	
		})
	columns =get_columns()
	chart=get_chart(res)
	message = ["<br>","<br>","<br>"]
	return columns, res,message,chart

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

def get_chart(res):
	week_l=[]
	val=[]
	for i in res:
		if i["type"]=="week":
			week_l.append("Week "+i["date"])
			val.append(round(float(i["percent"]),2))
	chart = {
		'data':{
		'labels':week_l,
		'datasets':[
            #In axis-mixed charts you have to list the bar type first
		{'name':'Percentage','values':val,'chartColor':['red'],'chartType':'bar'},
		{'name':'Targeted','values':[90,90,90,90,90,90],'ChartColor':['green'],'chartType':'line'}
		]
		},
	'type':'axis-mixed',
	'height': 250,
	'colors': ['#7cd6fd', '#008000']
	}
	return chart



def prnt():
	from akzo.akzo.report.oee_report.oee_report import execute
	
	return execute()

def grf():
	from akzo.akzo.report.oee_report.oee_report import execute
	f,s=execute()
	wkl=[]
	pre=['per','weekly']
	wkl.append(pre)  
	for i in s:
		if i["type"]=="week":
			to_ap=[i["date"],float(i["percent"])]
			wkl.append(to_ap)  
	return wkl 