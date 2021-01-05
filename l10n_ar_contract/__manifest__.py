# -*- coding: utf-8 -*-
###############################################################################
# Author      : SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2021-Present.
# License URL : AGPL-3
###############################################################################

{
    'name': 'Vinculo entre contract y Factura Electrónica de Servicios',
    'version': '13.0.0.1',
    'description': """
    Módulo técnico que vincula el modulo de contract con el de facturación 
    electrónica

    Para la facturación recurrente de Servicios este módulo evalúa la 
    configuración del contrato y en caso de aplicar setea los campos de 
    Fecha Desde y Fecha hasta del mens inmediato anterior. 
    **Escríbenos** a info@mastercore.net
    """,
    'author': 'MASTERCORE SAS || SINAPSYS GLOBAL SA',
    'website': 'www.mastercore.net',
    'license': 'Other OSI approved licence',
    'category': 'Localization / Argentina',
    'depends': [
        'contract',
        'l10n_ar_afipws_fe',
    ],
    'data': [
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
