# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class account_move(models.Model):
    _inherit = "account.move"
    
    def get_total_for_tva(self):
        # Fonction qui retourne la liste des tva des articles
        liste_tva = []
        liste_final = []
        for l in self.invoice_line_ids:
           for tva in l.tax_ids:
               liste_tva.append(tva)
        for t in set(liste_tva):
            somme = 0
            base = 0
            cpt = 0
            for l in self.invoice_line_ids:
                if t in l.tax_ids:
                    tva = (l.price_unit * t.amount)/100
                    base += l.price_subtotal
                    somme += tva
                    cpt += 1
            liste_final.append({'tva': t.amount, 'base': round(base, 2), 'amount': round(somme, 2)})
        return liste_final

    def get_lot(self, invoice_id, product):
        """  Fonction qui retourne le num de lot d'article
        param : 
            invoice_id : represente le id du facture
            product : represente le id du produit 
        """ 
        num_lot = ""
        for ligne in self.env['purchase.order'].search([]):
            for l in ligne.invoice_ids:
                if l.id == invoice_id:
                    for f in self.env['stock.production.lot'].search([('product_id', '=', product)]):
                        for x in f.purchase_order_ids:
                            if x.name == ligne.name: 
                                num_lot = f.name
                else:
                    for y in self.pos_order_ids:
                        for c in y.lines:
                            if c.product_id.id == product:
                                for z in c.pack_lot_ids:
                                    num_lot = z.display_name
        return num_lot
    def get_poids_net(self, product, qty):
        """Fonction qui retourne le poids net du produit
        param : 
            product : represente le id du produit 
            qty : represente la quantité achetée
        """
        poids_net = 0
        for l in self.env['product.template'].browse(product):
            poids_net = l.weight * qty
        return poids_net

