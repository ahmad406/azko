# Copyright (c) 2023, parijat and contributors
# For license information, please see license.txt



import frappe
from frappe import _

def execute(filters=None):
	cond=""
	if  filters:
		cond='where  line like "%{0}%" '.format(filters.get("line"))
	oee="""select line,CONVERT(availability, FLOAT) availability,CONVERT(performance, FLOAT) performance,CONVERT(oee, FLOAT) oee from `tabOEE Report` {0} """.format(cond)
	res=[]

	res.append({
			"line":"<strong>OEE Data</strong>",
			"number":"",
			"volume":"",
			"hr":"",
			"type":""
			
			})

	res.append({
		"line":"<strong>Line</strong>",
		"number":"<strong>Availabilty</strong>",
		"volume":"<strong>Performance</strong>",
		"hr":"<strong>OEE</strong>",
		"type":""	
		})
	oa=0
	opt=0
	oeet=0
	for o in frappe.db.sql(oee,as_dict=True):
		res.append({
			"line":o.line,
			"number": o.availability,
			"volume":o.performance,
			"hr":o.oee,
			"type":"oee"
			
			})
		oa+=o.availability
		opt+=o.performance
		oeet=o.oee
	res.append({
			"line":"Total",
			"number": round(opt,2),
			"volume":round(oa,2),
			"hr":round(oeet,2),
			"type":"oee"
			
			})
		
	
	res.append({
		"line":"",
		"number":"",
		"volume":"",
		"hr":"",
		"type":""	
		})
	res.append({
				"line":"<strong>Availability Data</strong>",
				"number":"",
				"volume":"",
				"hr":"",
				"type":""
				
				})
	res.append({
		"line":"<strong>Line</strong>",
		"number":"<strong>Operating Time</strong>",
		"volume":"<strong>Availability Losses</strong>",
		"hr":"<strong></strong>",
		"type":""	
		})
	avl="""select line,CONVERT(operatingtime, FLOAT) operatingtime,CONVERT(availabilitylosses, FLOAT) availabilitylosses from `tabtabAvailability` {0} """.format(cond)
	
	aot=0
	aal=0

	for a in frappe.db.sql(avl,as_dict=True):
		res.append({
			"line":a.line,
			"number": a.operatingtime,
			"volume":a.availabilitylosses,
			"type":"availabilitylosses"
			
		})
		aot+=a.operatingtime
		aal+=a.availabilitylosses
	res.append({
			"line":"Total",
			"number": round(aot,2),
			"volume":round(aal,2),
			"type":"availabilitylosses"
			
		})
	

	
	
	res.append({
		"line":"",
		"number":"",
		"volume":"",
		"hr":"",
		"type":""	
		})
	res.append({
			"line":"<strong>Performance Data</strong>",
			"number":"",
			"volume":"",
			"hr":"",
			"type":""
			
			})
	res.append({
		"line":"<strong>Line</strong>",
		"number":"<strong>Number of can filled </strong>",
		"volume":"<strong>Volume Filled</strong>",
		"hr":"<strong>Volume/HR</strong>",
		"avg":"<strong>Average Can Size</strong>",	
		"std":"<strong>Standard Speed</strong>",
		"type":"Performance",
		})
	perf="""select line,CONVERT(no_of_cans_filled, FLOAT) no_of_cans_filled,CONVERT(volume_field, FLOAT) volume_field,CONVERT(volume_hour, FLOAT) volume_hour,
	CONVERT(average_can_size, FLOAT) average_can_size,CONVERT(standrad_speed, FLOAT) standrad_speed
	from `tabPerformance` {0} """.format(cond)

	pno=0
	pv=0
	pvf=0
	pvh=0
	pav=0
	pstd=0
	for p in frappe.db.sql(perf,as_dict=True):
		res.append({
			"line":p.line,
			"number": p.no_of_cans_filled,
			"volume":p.volume_field,
			"hr":p.volume_hour,
			"avg":p.average_can_size,
			"std":p.standrad_speed,
			"type":"performance",		
		})
		pno+=p.no_of_cans_filled
		pv+=p.volume_field
		pvh+=p.volume_hour
		pav+=p.average_can_size
		pstd+=p.standrad_speed
	
	res.append({
			"line":"Total",
			"number":round(pno,2),
			"volume":round(pv,2),
			"hr":round(pvh,2),
			"avg":round(pav,2),
			"std":round(pstd,2),
			"type":"performance",		
		})
	
	columns =get_columns()

	return columns, res


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
	 		'fieldname': 'number',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'volume',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},
		{
	 		'fieldname': 'hr',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},{
	 		'fieldname': 'avg',
			'label':('  '),
			'fieldtype': 'Data',
			'width': 170,
		},{
	 		'fieldname': 'std',
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






