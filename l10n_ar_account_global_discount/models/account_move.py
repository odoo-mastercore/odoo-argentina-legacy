# -*- coding: utf-8 -*-
##############################################################################
# Author: SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################
from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging
import sys
import re
import base64
import traceback
from datetime import datetime
_logger = logging.getLogger(__name__)

try:
    from pysimplesoap.client import SoapFault
except ImportError:
    _logger.debug('Can not `from pyafipws.soap import SoapFault`.')


class AccountMove(models.Model):
    _inherit = "account.move"

    def _l10n_ar_get_amounts(self, company_currency=False):
        """ Method used to prepare data to present amounts and taxes related amounts when creating an
        electronic invoice for argentinian and the txt files for digital VAT books. Only take into account the argentinian taxes """
        self.ensure_one()
        amount_field = company_currency and 'balance' or 'price_subtotal'
        # if we use balance we need to correct sign (on price_subtotal is positive for refunds and invoices)
        sign = -1 if (company_currency and self.is_inbound()) else 1
        tax_lines = self.line_ids.filtered('tax_line_id')
        vat_taxes = tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_vat_afip_code)

        vat_taxable = self.env['account.move.line']
        for line in self.invoice_line_ids:
            if any(tax.tax_group_id.l10n_ar_vat_afip_code and tax.tax_group_id.l10n_ar_vat_afip_code not in ['0', '1', '2'] for tax in line.tax_ids):
                vat_taxable |= line

        profits_tax_group = self.env.ref('l10n_ar.tax_group_percepcion_ganancias')
        return {'vat_amount': sign * sum(vat_taxes.mapped(amount_field)),
                # For invoices of letter C should not pass VAT
                'vat_taxable_amount': sign * sum(vat_taxable.mapped(amount_field)) if self.l10n_latam_document_type_id.l10n_ar_letter != 'C' or not self.global_discount_ids else self.amount_untaxed,
                'vat_exempt_base_amount': sign * sum(self.invoice_line_ids.filtered(lambda x: x.tax_ids.filtered(lambda y: y.tax_group_id.l10n_ar_vat_afip_code == '2')).mapped(amount_field)),
                'vat_untaxed_base_amount': sign * sum(self.invoice_line_ids.filtered(lambda x: x.tax_ids.filtered(lambda y: y.tax_group_id.l10n_ar_vat_afip_code == '1')).mapped(amount_field)),
                # used on FE
                'not_vat_taxes_amount': sign * sum((tax_lines - vat_taxes).mapped(amount_field)),
                # used on BFE + TXT
                'iibb_perc_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '07').mapped(amount_field)),
                'mun_perc_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '08').mapped(amount_field)),
                'intern_tax_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '04').mapped(amount_field)),
                'other_taxes_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '99').mapped(amount_field)),
                'profits_perc_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id == profits_tax_group).mapped(amount_field)),
                'vat_perc_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '06').mapped(amount_field)),
                'other_perc_amount': sign * sum(tax_lines.filtered(lambda r: r.tax_line_id.tax_group_id.l10n_ar_tribute_afip_code == '09' and r.tax_line_id.tax_group_id != profits_tax_group).mapped(amount_field)),
                }

    def _get_vat(self, company_currency=False):
        """ Applies on wsfe web service and in the VAT digital books """
        amount_field = company_currency and 'balance' or 'price_subtotal'
        # if we use balance we need to correct sign (on price_subtotal is positive for refunds and invoices)
        sign = -1 if (company_currency and self.is_inbound()) else 1
        res = []
        vat_taxable = self.env['account.move.line']
        # get all invoice lines that are vat taxable
        for line in self.line_ids:
            if any(tax.tax_group_id.l10n_ar_vat_afip_code and tax.tax_group_id.l10n_ar_vat_afip_code not in ['0', '1', '2'] for tax in line.tax_line_id) and line[amount_field]:
                vat_taxable |= line
        for vat in vat_taxable:
            if self.global_discount_ids:
                base_imp= self.amount_untaxed_before_global_discounts
            else:
                base_imp = sum(self.invoice_line_ids.filtered(lambda x: x.tax_ids.filtered(lambda y: y.tax_group_id.l10n_ar_vat_afip_code == vat.tax_line_id.tax_group_id.l10n_ar_vat_afip_code)).mapped(amount_field))
            
            res += [{'Id': vat.tax_line_id.tax_group_id.l10n_ar_vat_afip_code,
                     'BaseImp': sign * base_imp,
                     'Importe': sign * vat[amount_field]}]

        # Report vat 0%
        vat_base_0 = sign * sum(self.invoice_line_ids.filtered(lambda x: x.tax_ids.filtered(lambda y: y.tax_group_id.l10n_ar_vat_afip_code == '3')).mapped(amount_field))
        if vat_base_0:
            res += [{'Id': '3', 'BaseImp': vat_base_0, 'Importe': 0.0}]

        return res if res else []