# -*- coding: utf-8 -*-
{
	'name': "CLEAN - 2019 - SERVICE ORIENTED",

	'summary': """
        Clean for the Openhealth System
	""",
	
	'description': """

        5 Sep 2019

		For Openhealth system. Matrix Object Oriented. 
		Cleans:
			- HR 
	""",


	'author': "My Company",

	'website': "http://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '0.1',


	# any module necessary for this one to work correctly
	#'depends': ['base'],
	#'depends': ['base', 'hr'],
    'depends': ['base', 'oehealth'],



	# always loaded
	'data': [
		# 'security/ir.model.access.csv',
		#'views/views.xml',
		#'views/templates.xml',
		#'views/menus_hr.xml',
		#$'views/menus_res.xml',


		'views/actions.xml',
		'views/menus_dev.xml',
	],



	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}