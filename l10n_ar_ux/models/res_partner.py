from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
import re
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gross_income_jurisdiction_ids = fields.Many2many(
        'res.country.state',
        string='Gross Income Jurisdictions',
        help='The state of the company is cosidered the main jurisdiction',
    )

    # AFIP Padron
    start_date = fields.Date('Start-up Date')
    estado_padron = fields.Char('Estado AFIP')
    imp_ganancias_padron = fields.Selection([
        ('NI', 'No Inscripto'),
        ('AC', 'Activo'),
        ('EX', 'Exento'),
        ('NC', 'No corresponde')], 'Ganancias')
    imp_iva_padron = fields.Selection([
        ('NI', 'No Inscripto'),
        ('AC', 'Activo'),
        ('EX', 'Exento'),
        ('NA', 'No alcanzado'),
        ('XN', 'Exento no alcanzado'),
        ('AN', 'Activo no alcanzado')], 'IVA')
    integrante_soc_padron = fields.Selection([('N', 'No'), ('S', 'Si')], 'Integrante Sociedad')
    monotributo_padron = fields.Selection([('N', 'No'), ('S', 'Si')], 'Monotributo')
    actividad_monotributo_padron = fields.Char()
    empleador_padron = fields.Boolean()
    actividades_padron = fields.Many2many(
        'afip.activity',
        'res_partner_afip_activity_rel',
        'partner_id', 'afip_activity_id',
        'Actividades',
    )
    impuestos_padron = fields.Many2many(
        'afip.tax',
        'res_partner_afip_tax_rel',
        'partner_id', 'afip_tax_id',
        'Impuestos')
    last_update_padron = fields.Date()

    @api.constrains('gross_income_jurisdiction_ids', 'state_id')
    def check_gross_income_jurisdictions(self):
        for rec in self:
            if rec.state_id and rec.state_id in rec.gross_income_jurisdiction_ids:
                raise ValidationError(_(
                    'Jurisdiction %s is considered the main jurisdiction '
                    'because it is the state of the company, please remove it '
                    'from the jurisdiction list') % rec.state_id.name)

    @api.model
    def try_write_commercial(self, data):
        """ User for website. capture the validation errors and return them.
        return (error, error_message) = (dict[fields], list(str())) """
        error = dict()
        error_message = []
        vat = data.get('vat')
        l10n_latam_identification_type_id = data.get('l10n_latam_identification_type_id')
        l10n_ar_afip_responsibility_type_id = data.get('l10n_ar_afip_responsibility_type_id', False)

        if vat and l10n_latam_identification_type_id:
            commercial_partner = self.env['res.partner'].sudo().browse(int(data.get('commercial_partner_id')))
            try:
                values = {
                    'vat': vat,
                    'l10n_latam_identification_type_id': int(l10n_latam_identification_type_id),
                    'l10n_ar_afip_responsibility_type_id':
                        int(l10n_ar_afip_responsibility_type_id) if l10n_ar_afip_responsibility_type_id else False}
                commercial_fields = ['vat', 'l10n_latam_identification_type_id', 'l10n_ar_afip_responsibility_type_id']
                values = commercial_partner.remove_readonly_required_fields(commercial_fields, values)
                with self.env.cr.savepoint():
                    commercial_partner.write(values)
            except Exception as exception_error:
                _logger.error(exception_error)
                error['vat'] = 'error'
                error['l10n_latam_identification_type_id'] = 'error'
                error_message.append(_(exception_error))
        return error, error_message

    def remove_readonly_required_fields(self, required_fields, values):
        """ In some cases we have information showed to the user in the for that is required but that is already set
        and readonly. We do not really update this fields and then here we are trying to write them: the problem is
        that this fields has a constraint if we are trying to re-write them (even when is the same value).

        This method remove this (field, values) for the values to write in order to do avoid the constraint and not
        re-writted again when they has been already writted.

        param: @required_fields: (list) fields of the fields that we want to check
        param: @values (dict) the values of the web form

        return: the same values to write and they do not include required/readonly fields.
        """
        self.ensure_one()
        for r_field in required_fields:
            value = values.get(r_field)
            if r_field.endswith('_id'):
                if self[r_field].id == value:
                    values.pop(r_field, False)
            else:
                if self[r_field] == value:
                    values.pop(r_field, False)
        return values

    def update_partner_data_from_afip(self):
        """
        Funcion que llama al wizard para actualizar data de partners desde afip
        sin abrir wizard.
        Podríamos mejorar  pasando un argumento para sobreescribir o no valores
        que esten o no definidos
        Podriamos mejorarlo moviendo lógica del wizard a esta funcion y que el
        wizard use este método.
        """

        for rec in self:
            wiz = rec.env[
                'res.partner.update.from.padron.wizard'
            ].with_context(
                active_ids=rec.ids, active_model=rec._name
            ).create({})
            wiz.change_partner()
            wiz.update_selection()

    def get_data_from_padron_afip(self):
        self.ensure_one()
        cuit = re.sub('[^0-9]', '', self.vat)
        # GET COMPANY
        # if there is certificate for user company, use that one, if not
        # use the company for the first certificate found
        company = self.env.user.company_id
        env_type = company._get_environment_type()
        try:
            certificate = company.get_key_and_certificate(
                company._get_environment_type())
        except Exception:
            certificate = self.env['afipws.certificate'].search([
                ('alias_id.type', '=', env_type),
                ('state', '=', 'confirmed'),
            ], limit=1)
            if not certificate:
                raise UserError(_(
                    'Not confirmed certificate found on database'))
            company = certificate.alias_id.company_id
        _logger.debug("____Calling ws_sr_padron_a5_____")
        padron = company.get_connection('ws_sr_padron_a5').connect()
        _logger.debug("____Called ws_sr_padron_a5_____")
        
        try:
            padron.Consultar(cuit)
        except Exception as exception_error:
            raise UserError("Error en la Consulta: " + exception_error)
        
        # porque imp_iva activo puede ser S o AC
        imp_iva = padron.imp_iva
        if imp_iva == 'S':
            imp_iva = 'AC'
        elif imp_iva == 'N':
            # por ej. monotributista devuelve N
            imp_iva = 'NI'
        vals = {
            'name': padron.denominacion,
            # 'name': padron.tipo_persona,
            # 'name': padron.tipo_doc,
            # 'name': padron.dni,
            'estado_padron': padron.estado,
            'street': padron.direccion,
            'city': padron.localidad,
            'zip': padron.cod_postal,
            'actividades_padron': self.actividades_padron.search(
                [('code', 'in', padron.actividades)]).ids,
            'impuestos_padron': self.impuestos_padron.search(
                [('code', 'in', padron.impuestos)]).ids,
            'imp_iva_padron': imp_iva,
            # TODAVIA no esta funcionando
            # 'imp_ganancias_padron': padron.imp_ganancias,
            'monotributo_padron': padron.monotributo,
            'actividad_monotributo_padron': padron.actividad_monotributo,
            'empleador_padron': padron.empleador == 'S' and True,
            'integrante_soc_padron': padron.integrante_soc,
            'last_update_padron': fields.Date.today(),
        }
        ganancias_inscripto = [10, 11]
        ganancias_exento = [12]
        if set(ganancias_inscripto) & set(padron.impuestos):
            vals['imp_ganancias_padron'] = 'AC'
        elif set(ganancias_exento) & set(padron.impuestos):
            vals['imp_ganancias_padron'] = 'EX'
        elif padron.monotributo == 'S':
            vals['imp_ganancias_padron'] = 'NC'
        else:
            _logger.debug(
                "We couldn't get impuesto a las ganancias from padron, you"
                "must set it manually")
        if padron.provincia:
            # if not localidad then it should be CABA.
            if not padron.localidad:
                state = self.env['res.country.state'].search([
                    ('code', '=', 'ABA'),
                    ('country_id.code', '=', 'AR')], limit=1)
            # If localidad cant be caba
            else:
                state = self.env['res.country.state'].search([
                    ('name', 'ilike', padron.provincia),
                    ('code', '!=', 'ABA'),
                    ('country_id.code', '=', 'AR')], limit=1)
            if state:
                vals['state_id'] = state.id
        if imp_iva == 'NI' and padron.monotributo == 'S':
            vals['afip_responsability_type_id'] = self.env.ref(
                'l10n_ar_account.res_RM').id
        elif imp_iva == 'AC':
            vals['afip_responsability_type_id'] = self.env.ref(
                'l10n_ar_account.res_IVARI').id
        elif imp_iva == 'EX':
            vals['afip_responsability_type_id'] = self.env.ref(
                'l10n_ar_account.res_IVAE').id
        else:
            _logger.debug(
                "We couldn't infer the AFIP responsability from padron, you"
                "must set it manually.")
        return vals

    def update_constancia_from_padron_afip(self):
        self.ensure_one()
        return True