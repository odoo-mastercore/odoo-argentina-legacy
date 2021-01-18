# -*- coding: utf-8 -*-
###############################################################################
# Author      : SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2021-Present.
# License URL : AGPL-3
###############################################################################

{
    'name': 'Modulo para imprimir Remitos',
    'version': '13.0.0.1',
    'description': """
    Módulo técnico que modifica el modulo stock para una correcta impresión
    de los remitos con la normativa de la Republica Argentina.

    **Escríbenos** a info@mastercore.net
    """,
    'author': 'MASTERCORE SAS || SINAPSYS GLOBAL SA',
    'website': 'www.mastercore.net',
    'license': 'Other OSI approved licence',
    'category': 'Localization / Argentina',
    'depends': [
        'stock_voucher',
    ],
    'data': [
        'report/paperformat.xml',
        'report/stock_picking_remittance.xml',
        'views/stock_book_views.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
