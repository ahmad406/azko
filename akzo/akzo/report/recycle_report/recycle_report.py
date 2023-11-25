# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt

# import frappe



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
#	chart = {'data':{'labels':['d','o','g','s'],'datasets':[{'values':[3,6,4,7]}]},'type':'bar'}
	chart = {
			'data':{
			'labels':['d','o','g','s'],
			'datasets':[
            #In axis-mixed charts you have to list the bar type first
			{'name':'Number','values':[3,6,4,7],'chartType':'bar'},
			{'name':'Vowel','values':[0,1,0,0],'chartType':'line'}
			]
			},
		'type':'axis-mixed'
		}
	return columns, data, chart
