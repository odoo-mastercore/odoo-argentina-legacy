# -*- coding: utf-8 -*-
###############################################################################
# Author      : SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2021-Present.
# License URL : AGPL-3
###############################################################################

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tests import Form
from dateutil.relativedelta import relativedelta
from odoo.tools.translate import _
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def get_date(self):
        return datetime.strftime(self.date_done, '%d/%m/%Y')

    def do_print_voucher(self):
        '''This function prints the voucher'''
        if self.book_id.pre_printed:
            return self.env.ref(
                'l10n_ar_stock_voucher.report_printed_remittance').\
                report_action(self, config=False)
        else:
            return super(StockPicking, self).do_print_voucher()

    def get_data_report(self):
        '''This function get data to prints the voucher'''
        for rec in self:
            data_report = []
            limit = rec.book_id.lines_per_voucher

            if rec.state == 'done':
                move_lines = rec.move_line_ids_without_package
            else:
                move_lines = rec.move_ids_without_package

            for p in range(rec.get_estimated_number_of_pages()):
                i = 1
                list_line = []
                number_of_packages = declared_value = 0
                for line in move_lines:
                    if i <= int(limit * (p+1)) and i > int(limit * p):
                        number_of_packages += line.qty_done
                        declared_value += rec.sale_id.order_line.filtered(
                            lambda x: x.product_id == line.product_id).\
                                price_subtotal
                        if rec.state == 'done':
                            product_lot = line.lot_id.name or '',
                        else:
                            product_lot = ','.join(
                                line.move_line_ids.mapped('lot_id.name')) or ''
                        vals = {
                            'qty': int(line.qty_done),
                            'default_code': line.product_id.default_code,
                            'product_name': line.product_id.name,
                            'product_lot':  product_lot
                        }
                        list_line.append(vals)
                    i+=1
                partner = rec.partner_id
                page_vals = {
                    'partner_name': partner.display_name,
                    'partner_id_zip': partner.zip,
                    'partner_id_street': partner.street,
                    'partner_id_vat': partner.vat,
                    'partner_id_city': partner.city,
                    'partner_id_l10n_ar_formatted_vat': \
                        partner.l10n_ar_formatted_vat,
                    'partner_id_state_id': partner.state_id.name,
                    'partner_id_l10n_ar_afip_responsibility_type_id': \
                        partner.l10n_ar_afip_responsibility_type_id.name,
                    'lines': list_line,
                    'number_of_packages': number_of_packages,
                    'declared_value': "{:.2f}".format(declared_value),
                    'client_order_ref': rec.sale_id.client_order_ref,
                }
                data_report.append(page_vals)
        
        return data_report
