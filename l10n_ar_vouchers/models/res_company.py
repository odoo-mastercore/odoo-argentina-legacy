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

from odoo import models, api


class ResCompany(models.Model):
    """
        Modificación del registro de la Compañia default para la inclusión de
        la plantilla «boxed».
    """
    _inherit = 'res.company'

    @api.model
    def set_report_layout(self):
        self.browse(1).write({
            'external_report_layout_id': self.env.ref(
                'web.external_layout_background').id
        })
