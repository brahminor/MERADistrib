# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date

class factures_sites(models.Model):
    _name = "factures.sites"
    _rec_name = 'numero'
    _description = "Cet objet permet d'afficher la liste des factures clients comptabilisées de tous les sites"

    facture_id = fields.Many2one('account.move', "Facture")
    numero = fields.Char("Numéro", related='facture_id.name')
    client_id = fields.Many2one('res.partner', "Client", related='facture_id.partner_id')
    date_facturation = fields.Date("Date de facturation", related='facture_id.invoice_date')
    date_echeance = fields.Date("Date d’échéance", related='facture_id.invoice_date_due')
    societe = fields.Many2one('res.company', "Société", related='facture_id.company_id')
    amount_total = fields.Float("Montant total",compute="get_montant_du_total")
    amount = fields.Float("Montant dû",compute="get_montant_du_total")
    payment_state = fields.Selection(selection=[
        ('not_paid', 'Non payées'),
        ('in_payment', 'En paiement'),
        ('paid', 'Payé'),
        ('partial', 'Partiellement réglé'),
        ('reversed', 'Extourné'),
        ('invoicing_legacy', 'Invoicing App Legacy')],
        string="Etat du paiement", copy=False, tracking=True,
        related='facture_id.payment_state')

    @api.depends('facture_id')
    def get_montant_du_total(self):
        """Cette fonction permet de trouver le montant dû et le montant totale de la facture et 
        l'affecter au champ Montant dû et montant total"""
        for record in self:
            record.amount = record.facture_id.amount_residual
            record.amount_total = record.facture_id.amount_total