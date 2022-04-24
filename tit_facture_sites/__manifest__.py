# -*- encoding: utf-8 -*-
# Copyright 2021
{
    'name': "Tit factures sites",
    "version": "1.0.1",
    "author": "Sogesi",
    "website": "https://www.sogesi-dz.com",
    "sequence": 0,
    "depends": [
            "account", "tit_pos_order"
    ],
    "category": "Account",
    'license': 'LGPL-3',
    "description": """
    Ce module permet d'afficher toutes les factures client comptabilisées de tous les sites 
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/factures_sites_view.xml',
    ],
    'images': ['static/description/images/icon.png'],
    "auto_install": False,
    "installable": True,
    "application": False, 
}