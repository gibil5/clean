# -*- coding: utf-8 -*-
"""
	Management - Correct Errors

	Created: 			 6 Seo 2019
	Last updated: 		 6 Sep 2019

"""
from __future__ import print_function

from openerp import models, fields, api

class Management(models.Model):
	"""
	Correct Errors
		- Create Doctor Data
	"""
	_inherit = 'openhealth.management'



# ----------------------------------------------------------- Create Doctor Data ------------
	def create_doctor_data(self, doctor_name, orders):
		print()
		print('Create Doctor Data - Corrected')


		# Init Loop
		amount = 0
		count = 0
		tickets = 0
		doctor = self.doctor_line.create({
											'name': doctor_name,
											'management_id': self.id,
										})

		# Loop
		for order in orders:

			# Tickets
			tickets = tickets + 1

			# Filter Block
			if not order.x_block_flow:


				# Parse Data


				# Amount with State
				if order.state in ['credit_note']:
					amount = amount + order.x_amount_flow

				elif order.state in ['sale']:
					amount = amount + order.amount_total


				# Id Doc
				if order.x_type in ['ticket_invoice', 'invoice']:
					receptor = order.patient.x_firm.upper()
					id_doc = order.patient.x_ruc
					id_doc_type = 'ruc'
					id_doc_type_code = '6'
				else:
					receptor = order.patient.name
					id_doc = order.patient.x_id_doc
					id_doc_type = order.patient.x_id_doc_type
					id_doc_type_code = order.patient.x_id_doc_type_code

					# Pre-Electronic
					if id_doc_type is False or id_doc is False:
						id_doc = order.patient.x_dni
						id_doc_type = 'dni'
						id_doc_type_code = '1'




				# State equal to Sale
				if order.state in ['sale']:  	# Sale - Do Line Analysis

					print('SALE')

					# Order Lines
					for line in order.order_line:

						count = count + 1

						# Price
						price_unit = line.price_unit						


						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_id': 			line.product_id.id,
																'product_uom_qty': 		line.product_uom_qty,

																# Price
																'price_unit': 			price_unit,
															})

						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)

						if line.product_id.pl_price_list in ['2019']:
							order_line.pl_update_fields()

						elif line.product_id.pl_price_list in ['2018']:
							order_line.update_fields()

					# Line Analysis Sale - End

				# Conditional State Sale - End




				# State equal to Credit Note
				elif order.state in ['credit_note']:

					print('CREDIT NOTE')


					# Order Lines
					for line in order.order_line:

						# Price
						price_unit = order.x_amount_flow

						# Create
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,

																# Line
																'product_uom_qty': 		1,

																# Price
																'price_unit': 			price_unit,
															})


						#print(line)
						#print(line.product_id)
						#print(line.product_id.name)

						if line.product_id.pl_price_list in ['2019']:
							order_line.pl_update_fields()

						elif line.product_id.pl_price_list in ['2018']:
							order_line.update_fields()

					# Line Analysis Credit Note - End

				# Conditional State - End


			# Filter Block - End
		# Loop - End



		# Stats
		doctor.amount = amount
		doctor.x_count = count

		# Percentage
		if self.total_amount != 0: 
			doctor.per_amo = (doctor.amount / self.total_amount)

	# create_doctor_data
