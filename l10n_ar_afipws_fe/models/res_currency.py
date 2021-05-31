##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api, _
from odoo.exceptions import UserError
import requests
from requests.structures import CaseInsensitiveDict
import logging

_logger = logging.getLogger(__name__)


class ResCurrency(models.Model):
    _inherit = "res.currency"
    
    # This method use an API from https://api.estadisticasbcra.com
    # It's require a access token to use it
    # We will store the token at ir.config_parameter key
    # api.estadisticasbcra.com.token
    def get_usd_of_minorista(self):

        access_token = self.env['ir.config_parameter'].sudo().get_param(
                        'api.estadisticasbcra.com.token', '')
        url = 'https://api.estadisticasbcra.com/usd_of_minorista'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = 'Bearer ' + access_token

        resp = requests.get(url, headers=headers)

        if resp.ok:
            coti = resp.json()[-1]['v']
        
        return coti or 1.0

    # This method is for use on ir.cron to automatic 
    # USD minorista vendor currency rate update
    @api.model
    def automatic_usd_minorista_currency_rate(self, w_arancel=1.0):
        currency = self.env['res.currency'].search(
            [('name', '=', 'USD')],
            limit=1)
        values = {
            'rate': float(1 / (currency.get_usd_of_minorista()*w_arancel)),
            'currency_id': self.env.ref('base.USD').id
        }
        record = self.env['res.currency.rate'].create(values)
        return record

        