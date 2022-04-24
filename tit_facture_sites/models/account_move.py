# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class account_move(models.Model):
    _inherit = "account.move"

    def action_post(self):
        res = super(account_move, self).action_post()
        """
        -vérifier si on n'a pas ajouté la facture à la liste des factures appartenant à 
        tous les sites, si c'est le cas ou l'ajoute
        """
        if not self.env['factures.sites'].search([('facture_id', '=', self.id)]):
            self.env['factures.sites'].create({
                'facture_id': self.id,
                })
        return res

    def button_draft(self):
        res = super(account_move, self).button_draft()
        """
        -vérifier si on n'a pas ajouté la facture à la liste des factures appartenant à 
        tous les sites, si c'est le cas ou l'ajoute
        """
        factures_sites_record = self.env['factures.sites'].search([('facture_id', '=', self.id)])
        if factures_sites_record:
            factures_sites_record.unlink()
        return res