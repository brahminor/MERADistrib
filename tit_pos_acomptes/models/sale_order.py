# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class sale_order(models.Model):
    _inherit = "sale.order"
    
    acompte = fields.Monetary('Acompte', compute = "get_montants")
    montant_du = fields.Monetary('Montant dû', compute = 'get_montants')
    trait_tot = fields.Selection([('trait_total', "Traité totalement"),('trait_part','Traité partiellement')], store=True, default='trait_part', string='traité totalement depuis le pos',  copy = False, help = "Ce champ permet de déterminer si le traitement du sale order est terminé depuis le pos tel que tous les produits sont vendus ", compute='_get_tarit_totalement')

    @api.depends('montant_du')
    def _get_tarit_totalement(self):
        for record in self:
            if record.montant_du <= 0:
                record.trait_tot = 'trait_total'
            else:
                record.trait_tot = 'trait_part'
    
    @api.model
    def creer_facture_totale(self, sale_order_id):
        """
        Cette fonction permet de créer une facture normale (ie une facture associée
        au montant dû du sale order en débitant les acomptes déjà payés)
        @param:
        -sale_order_id: l'id du sale order à créer leur facture normale
        Cette fonction permet de retourner des valeurs négatifs lors des erreurs 
        et le résultat obtenue suite à l'appel de la fontion qui permet de créer 
        la facture pour l'acompte payé associé au SO
        """
        amount = int(sale_order_id)
        sale_order_record = self.env['sale.order'].browse(sale_order_id)
        so = []
        invoice_generated = 0
        for i in sale_order_record:
            so.append(int(i.id))
        if sale_order_record:
            payment_record = {
            'advance_payment_method': 'delivered',
            'deduct_down_payments': True,
            }
            pay = self.env['sale.advance.payment.inv'].with_context({'active_id': sale_order_record.id,'active_ids': so,'active_model': 'sale.order'}).create(payment_record)
            invoice_generated = pay.create_invoices_from_pos()
            sale_order_record.trait_tot = 'trait_total'
            return invoice_generated
    
    @api.depends('amount_total','order_line')
    def get_montants(self):
        """
        cette fonction eprmet de calculer le montant du et l'acompte à partir des 
        acomptes payés et marqués dans les lignes des articles associées au SO
        """
        product_id = int(self.env['ir.config_parameter'].sudo().get_param('sale.default_deposit_product_id'))
        if product_id > 0:
            for record in self:
                somme_montant_paye = 0
                somme_du_paye = 0
                for  pod_order_record in record.order_line:
                    if pod_order_record.product_id.id == product_id:
                        somme_montant_paye += pod_order_record.price_unit
                record.acompte = somme_montant_paye
                
                for facture_record in record.invoice_ids:
                    somme_du_paye += facture_record.amount_total
                record.montant_du = record.amount_total - somme_du_paye
        else:
            raise ValidationError(_("Veuillez configurer le produit acompte s.v.p !"))