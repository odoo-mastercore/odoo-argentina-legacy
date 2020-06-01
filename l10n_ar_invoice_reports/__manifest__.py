# -*- coding: utf-8 -*-
################################################################################
# Author      : SINPASYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2019-Present.
# License URL : MIT
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
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
    'license': 'AGPL-3',
    'category': 'Localization / Argentina',
    'depends': [
        'base',
        'account',
        #'sale', -- se necesita para report_saleorder_ar
        'l10n_ar_afipws_fe',
    ],
    'data': [
        'template/report_invoice_ar.xml',
        'template/report_invoice.xml',
        #'template/report_saleorder_ar.xml', -- Para una version posterior --
        'data/external_layout_report.xml',
        'views/account_move.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
