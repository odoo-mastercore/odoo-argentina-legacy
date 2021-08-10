# -*- coding: utf-8 -*-
##############################################################################
# Author: SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################
{
    'name': "Descuentos Globales en facturas Argentinas",
    'version': "13.0.0.1",
    'author': 'SINAPSYS GLOBAL SA || MASTERCORE SAS',
    'website': "http://sinapsys.global",
    'sequence': 10,
    'category': "account",
    'summary': ' Depende del modulo de OCA account_global_discount',
    'depends': [
        'l10n_ar_afipws_fe',
        'account_global_discount',
    ],
    'data': [
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}

