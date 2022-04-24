# -*- encoding: utf-8 -*-
from odoo import fields, models

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	ctifl = fields.Char(string = "CTIFL", help = "Taxe de type CTIFL")
	interfel = fields.Char(string = "INTERFEL", help = "Taxe de type INTERFEL")