# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt



import frappe
from frappe import _

def execute(filters=None):
	sql="""SELECT name,week(date) as date,"week" type,(avg(filling)+avg(batch_makeing))/2 as percent,avg(batch_makeing) batch_makeing,avg(filling) filling  FROM `tabRecycle Report`
			group by  Week(date)

			union all
			SELECT name,month(date) as date,"month" type,(avg(filling)+avg(batch_makeing))/2 as percent,avg(batch_makeing) batch_makeing,avg(filling) filling FROM `tabRecycle Report`
			group by  month(date)
			union all
			SELECT name,date(date) as date,"daily" type,percentage as percent,batch_makeing,filling  FROM `tabRecycle Report` where date >=Date(now()- interval 7 day)
		"""
	res=[]
	import datetime
	current = datetime.datetime.now()
	today= ("{}-{}-{}".format(current.month,current.day,current.year))
	week_number = current.isocalendar()[1]  
	res.append({
				"date":"<strong>{0}</strong>".format("Date"),
				"batch_making":"<strong>{0}</strong>".format("Week"),
				"filling":"",
				"percent":"",
				"type":""	
				})
	res.append({
				"date":"<strong>{0}</strong>".format(today),
				"batch_making":"<strong>{0}</strong>".format(week_number),
				"filling":"",
				"percent":"",
					"type":"green"	
				})
	res.append({
			"date":"",
			"batch_making":"",
			"filling":"",
			"percent":"",
			"type":""	
			})

	res.append({
			"date":"<strong>Daily Recycle Report</strong>",
			"batch_making":"",
			"filling":"",
			"percent":"",
			"type":""	
			})
	res.append({
		"date":"<strong>Date</strong>",
		"batch_making":"<strong>Batch Making %</strong>",
		"filling":"<strong>Filling %</strong>",
		"percent":"<strong>%</strong>",
		"type":""	
		})
	
	for i in frappe.db.sql(sql,as_dict=True):
		if i.type=="daily":
			res.append({
				"date":i.date,
				"batch_making": round(float(i.batch_makeing),2),
				"filling":round(float(i.filling),2),
				"percent":round(float(i.percent),2),
				"type":i.type
				
			})
	
	res.append({
		"date":"",
		"batch_making":"",
		"filling":"",
		"percent":"",
		"type":""	
		})
	res.append({
			"date":"<strong>Weekly Recycle Report</strong>",
			"batch_making":"",
			"filling":"",
			"percent":"",
			"type":""
			})
	res.append({
		"date":"<strong>Week</strong>",
		"batch_making":"<strong>Batch Making %</strong>",
		"filling":"<strong>Filling %</strong>",
		"percent":"<strong>%</strong>",
		"type":""	
		})
	for i in frappe.db.sql(sql,as_dict=True):
		if i.type=="week":
			res.append({
				"date":i.date,
				"batch_making": round(float(i.batch_makeing),2),
				"filling":round(float(i.filling),2),
				"percent":round(float(i.percent),2),
				"type":i.type
				
			})
	res.append({
		"date":"",
		"batch_making":"",
		"filling":"",
		"percent":"",
		"type":""	
		})
	res.append({
			"date":"<strong>Monthly Recycle Report</strong>",
			"batch_making":"",
			"filling":"",
			"percent":"",
			"type":""
			
			})
	res.append({
		"date":"<strong>Month</strong>",
		"batch_making":"<strong>Batch Making %</strong>",
		"filling":"<strong>Filling %</strong>",
		"percent":"<strong>%</strong>",
		"type":""	
		})
	for i in frappe.db.sql(sql,as_dict=True):
		if i.type=="month":
			res.append({
				"date":i.date,
				"batch_making": round(float(i.batch_makeing),2),
				"filling":round(float(i.filling),2),
				"percent":round(float(i.percent),2),
				"type":i.type
				
			})
	columns =get_columns()
	chart=get_chart(res)
	message = ["<br>","<br>","<br>"]
	return columns, res,message,chart


def get_columns():
	columns=[]

	columns+= [

		{
	 		'fieldname': 'date',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 200,
		},
		{
	 		'fieldname': 'batch_making',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'filling',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'percent',
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
	from akzo.akzo.report.summary_recycle.summary_recycle import execute
	
	return execute()

def grf():
	from akzo.akzo.report.summary_recycle.summary_recycle import execute
	f,s=execute()
	wkl=[]
	pre=['per','weekly']
	wkl.append(pre)  
	for i in s:
		if i["type"]=="week":
			to_ap=[i["date"],float(i["percent"])]
			wkl.append(to_ap)  
	return wkl 



