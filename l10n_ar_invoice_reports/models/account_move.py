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
