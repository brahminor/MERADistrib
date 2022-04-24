# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):

    _inherit = 'res.company'
    
    siret = fields.Char(string='SIRET', size=20)