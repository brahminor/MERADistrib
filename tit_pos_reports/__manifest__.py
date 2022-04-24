# -*- encoding: utf-8 -*-
# Copyright 2021
{
    'name': "Tit POS Repports",
    "version": "1.0",
    'summary': "",
    'category': 'Point Of Sale',
    "sequence": 1,
    "license": "LGPL-3",
    'description': """
        Changer le modèle de la facture
    """,
    'author': "Sogesi",
    "website": "https://www.sogesi-dz.com",
    'depends': ['base', 'point_of_sale', 'tit_pos_order'],
    'data': [
        'reports/pos_report.xml',
        'reports/model_facture.xml',
        'views/res_company.xml',
        'views/product_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
