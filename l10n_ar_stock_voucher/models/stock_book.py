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


class StockPicking(models.Model):
    _inherit = 'stock.book'

    pre_printed = fields.Boolean(string="it's a pre-printed book?")
