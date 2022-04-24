# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class pos_transporteur(models.Model):
    _name = "pos.transporteur"

    name = fields.Char(string = 'Transporteur', help = "Ce champ permet d'indiquer le nom du transporteur")
    