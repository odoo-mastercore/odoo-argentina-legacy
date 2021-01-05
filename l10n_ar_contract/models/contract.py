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


class ContractContract(models.Model):
    _inherit = "contract.contract"

    def _prepare_invoice(self, date_invoice, journal=None):
        """Prepare in a Form the values for the generated invoice record.
        :return: A tuple with the vals dictionary and the Form with the
          preloaded values for being used in lines.
        """
        self.ensure_one()
        if not journal:
            journal = (
                self.journal_id
                if self.journal_id.type == self.contract_type
                else self.env["account.journal"].search(
                    [
                        ("type", "=", self.contract_type),
                        ("company_id", "=", self.company_id.id),
                    ],
                    limit=1,
                )
            )
        if not journal:
            raise ValidationError(
                _("Please define a %s journal for the company '%s'.")
                % (self.contract_type, self.company_id.name or "")
            )
        invoice_type = "out_invoice"
        if self.contract_type == "purchase":
            invoice_type = "in_invoice"
        move_form = Form(
            self.env["account.move"].with_context(
                force_company=self.company_id.id, default_type=invoice_type
            )
        )
        move_form.partner_id = self.invoice_partner_id
        if self.payment_term_id:
            move_form.invoice_payment_term_id = self.payment_term_id
        if self.fiscal_position_id:
            move_form.fiscal_position_id = self.fiscal_position_id
        invoice_vals = move_form._values_to_save(all_fields=True)
        if self.recurring_rule_type == 'monthly' and self.\
            recurring_interval == 1 and not self.line_recurrence and \
            self.recurring_invoicing_type == 'post-paid':
            l10n_ar_afip_service_start = date_invoice + \
                relativedelta(day=1, months=-1)
            l10n_ar_afip_service_end = date_invoice + \
                relativedelta(day=1, days=-1)
            invoice_vals.update(
                {
                    "ref": self.code,
                    "company_id": self.company_id.id,
                    "currency_id": self.currency_id.id,
                    "invoice_date": date_invoice,
                    "journal_id": journal.id,
                    "invoice_origin": self.name,
                    "user_id": self.user_id.id,
                    "l10n_ar_afip_service_start": l10n_ar_afip_service_start,
                    "l10n_ar_afip_service_end": l10n_ar_afip_service_end,
                }
            )
        else:
            invoice_vals.update(
                {
                    "ref": self.code,
                    "company_id": self.company_id.id,
                    "currency_id": self.currency_id.id,
                    "invoice_date": date_invoice,
                    "journal_id": journal.id,
                    "invoice_origin": self.name,
                    "user_id": self.user_id.id,
                }
            )
        return invoice_vals, move_form
