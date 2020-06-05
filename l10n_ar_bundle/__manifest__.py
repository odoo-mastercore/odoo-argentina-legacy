# -*- coding: utf-8 -*-
################################################################################
# Author      : SINPASYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2019-Present.
# License URL : MIT
################################################################################

{
    'name': 'Bundle de Localizacion Argentina',
    'version': '13.0.0.1',
    'description': """
    **Bundle de Localización Argentina**

    Con este módulo puedes realizar fácilmente la instalación de todo el paquete 
    de aplicaciones de la **Localización Argentina**

    **Escríbenos** a info@mastercore.net
    """,
    'author': 'MASTERCORE SAS || SINAPSYS GLOBAL SA',
    'website': 'www.mastercore.net',
    'license': 'Other OSI approved licence',
    'category': 'Localization / Argentina',
    'depends': [
        'l10n_ar',
        'l10n_ar_afipws',
        'l10n_ar_afipws_fe',
        'l10n_ar_invoice_reports',
        'l10n_ar_reports', 
        'l10n_ar_bank',
        'account_payment_fix',
        'account_financial_amount',
        'account_withholding',
        'account_payment_group',
        'account_withholding_automatic',
        'account_check',
        'account_payment_group_document',
        'l10n_ar_ux',
        'l10n_ar_account_withholding',
    ],
    'data': [
            ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
