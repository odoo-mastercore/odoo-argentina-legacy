# -*- coding: utf-8 -*-
################################################################################
# Author      : SINPASYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2019-Present.
# License URL : MIT
################################################################################

{
    'name': 'Comprobantes para Factura Electrónica',
    'version': '13.0.0.1',
    'description': """
    **Comprobantes para Factura Electrónica**

    ¡Felicidades!. Este es el módulo para Generar Comprobantes PDF de
    Factura Electrónica para la implementación de la **Localización Argentina**

    **Escríbenos** a info@mastercore.net
    """,
    'author': 'MASTERCORE SAS || SINAPSYS GLOBAL SA',
    'website': 'www.mastercore.net',
    'license': 'Other OSI approved licence',
    'category': 'Localization / Argentina',
    'depends': [
        'base',
        'account',
        'l10n_ar_afipws_fe',
    ],
    'data': [
        'template/report_invoice_ar.xml',
        'template/report_invoice.xml',
        'data/external_layout_report.xml',
        'views/account_move.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
