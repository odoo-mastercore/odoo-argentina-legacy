# -*- coding: utf-8 -*-
###############################################################################
# Author      : SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyright(c): 2019-Present.
# License URL : AGPL-3
###############################################################################

from odoo import models, api, _

class AccountMove(models.Model):
    _inherit = "account.move"


    def _get_report_base_filename(self, copy=None):
        self.ensure_one()
        if copy:
            res = self.type == 'out_invoice' and self.invoice_payment_state in (
                 'open', 'in_payment', 'paid') and _(
                     'Copia Factura - %s') % (self.number)
            return res
        else:
            return super(AccountMove, self)._get_report_base_filename()
