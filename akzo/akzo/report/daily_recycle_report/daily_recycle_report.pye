# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [], []
	return columns, data

import frappe
import datetime
def execute(filters=None):
	columns = [
	{'fieldname':'date','label':'Date','fieldtype':'Date'},
	{'fieldname':'filling','label':'Filling','fieldtype':'Int'},
	{'fieldname':'batch_makeing','label':'Batch Making','fieldtype':'Int'},
	{'fieldname':'percentage','label':'%','fieldtype':'Data'}
	]
	data = frappe.db.get_all('Recycle Report', ['date','filling','batch_makeing','percentage'])
#       chart = {'data':{'labels':['d','o','g','s'],'datasets':[{'values':[3,6,4,7]}]},'type':'bar'}
	chart = {
		'data':{
		'labels':['Week 1','Week 2','Week 3','Week 4','Week 5','Week 6'],
		'datasets':[
            #In axis-mixed charts you have to list the bar type first
		{'name':'Percentage','values':[70,75,92,82,95,80],'chartColor':['red'],'chartType':'bar'},
		{'name':'Ref','values':[90,90,90,90,90,90],'ChartColor':['green'],'chartType':'line'}
		]
		},
	'type':'axis-mixed',
	'height': 250,
	'colors': ['#7cd6fd', '#008000']
	}
	return columns, data, None, chart

