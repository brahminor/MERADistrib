# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class product_product(models.Model):
	_inherit = "product.product"

	@api.model
	def get_product_acompte(self):
		#cette fonstion permet de retourner id du produit acompte paramétré dans la config de vente
		res_config_record = self.env['res.config.settings'].search([])
		if res_config_record:
			if not res_config_record.deposit_default_product_id:
				raise ValidationError(_("Veuillez configurer le produit acompte dans la partie du vente"))
			else:
				return res_config_record.deposit_default_product_id[0].id
		return 0