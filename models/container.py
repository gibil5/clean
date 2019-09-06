# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Container(models.Model):

	_name = 'clean.container'

	#_inherit = 'stock.move'


	name = fields.Char()


	@api.multi
	def encode_error(self):
		print()
		print('Encode Error')

		name = "ECOGRAFIAS MUSCULOESQUELETICAS - Muñeca (Unilateral) - 1 sesion"
		print(name)


