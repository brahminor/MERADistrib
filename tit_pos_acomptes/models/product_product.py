# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class product_product(models.Model):
	_inherit = "product.product"

	@api.model
	def get_product_acompte(self):
		#cette fonstion permet de retourner id du produit acompte paramétré dans la config de vente
		product_id = int(self.env['ir.config_parameter'].sudo().get_param('sale.default_deposit_product_id'))
		if product_id > 0:
			return product_id
		else:
			raise ValidationError(_("Veuillez configurer le produit acompte dans la partie du vente"))