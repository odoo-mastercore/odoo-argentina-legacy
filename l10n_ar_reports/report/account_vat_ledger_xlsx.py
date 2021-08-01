##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
# import time

class AccountVatLedgerXlsx(models.AbstractModel):

    _name = 'report.l10n_ar_account_vat_ledger.account_vat_ledger_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = "Xlsx Account VAT Ledger"

    def generate_xlsx_report(self, workbook, data, account_vat):
        for obj in account_vat:
            report_name = obj.name
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True, 'border':1})
            line = workbook.add_format({'border': 1})
            date_line = workbook.add_format(
                {'border': 1, 'num_format': 'd mmmm yyyy'})
            sheet.set_column(1, 4, 20)
            sheet.set_column(5, 12, 13)
            

            #
            sheet.write(0, 0, obj.name, bold)
            sheet.write(1, 0, obj.company_id.name, bold)
            sheet.write(2, 0, obj.company_id.vat, bold)

            sheet.write(4, 0, 'Fecha', bold)
            sheet.write(4, 1, 'Comprobante', bold)
            sheet.write(4, 2, 'Nombre', bold)
            sheet.write(4, 3, 'Cond. IVA', bold)
            sheet.write(4, 4, 'CUIT o Doc', bold)
            sheet.write(4, 5, 'No Gravado', bold)
            sheet.write(4, 6, 'Grav. 2,5%', bold)
            sheet.write(4, 7, 'IVA 2,5%', bold)
            sheet.write(4, 8, 'Grav. 5%', bold)
            sheet.write(4, 9, 'IVA 5%', bold)
            sheet.write(4, 10, 'Grav. 10,5%', bold)
            sheet.write(4, 11, 'IVA 10,5%', bold)
            sheet.write(4, 12, 'Grav. 21%', bold)
            sheet.write(4, 13, 'IVA 21%', bold)
            sheet.write(4, 14, 'Grav. 27%', bold)
            sheet.write(4, 15, 'IVA 27%', bold)
            sheet.write(4, 16, 'Perc IVA', bold)
            sheet.write(4, 17, 'Otros Imp', bold)
            sheet.write(4, 18, 'Total Compr.', bold)

            row = 5
            total_amount_base_2 = 0
            total_amount_base_5 = 0
            total_amount_base_10 = 0
            total_amount_base_21 = 0
            total_amount_base_27 = 0
            total_amount_untaxed = 0
            total_amount_tax_2 = 0
            total_amount_tax_5 = 0
            total_amount_tax_10 = 0
            total_amount_tax_21 = 0
            total_amount_tax_27 = 0
            total_amount_perc = 0
            total_amount_other_tax = 0
            total_amount = 0

            for invoice in obj.invoice_ids:
                # Write lines
                sheet.write(row, 0, invoice.invoice_date, date_line)
                sheet.write(row, 1, invoice.move_name, line)
                sheet.write(row, 2, invoice.partner_name, line)
                sheet.write(row, 3, invoice.afip_responsibility_type_name, line)
                sheet.write(row, 4, invoice.cuit, line)


                if invoice.state == 'cancel':
                    sheet.write(row, 5, 'ANULADA', line)
                    sheet.write(row, 6, '0,00', line)
                    sheet.write(row, 7, '0,00', line)
                    sheet.write(row, 8, '0,00', line)
                    sheet.write(row, 9, '0,00', line)
                    sheet.write(row, 10, '0,00', line)
                    sheet.write(row, 11, '0,00', line)
                    sheet.write(row, 12, '0,00', line)
                    sheet.write(row, 13, '0,00', line)
                    sheet.write(row, 14, '0,00', line)
                    sheet.write(row, 15, '0,00', line)
                else:
                    # Creating environment variables
                    untaxed = (invoice.type == 'in_invoice' and 1.0
                        or -1.0) * invoice.not_taxed
                    if invoice.type == 'in_refund':
                        base_2 = invoice.base_25
                        base_5 = invoice.base_5
                        base_10 = invoice.base_10
                        base_21 = invoice.base_21
                        base_27 = invoice.base_27
                        tax_2 = invoice.vat_25
                        tax_5 = invoice.vat_5
                        tax_10 = invoice.vat_10
                        tax_21 = invoice.vat_21
                        tax_27 = invoice.vat_27
                        perc = invoice.vat_per
                        other_tax = invoice.other_taxes
                        total = invoice.total
                    
                    else:
                        base_2 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.base_25
                        base_5 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.base_5
                        base_10 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.base_10
                        base_21 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.base_21
                        base_27 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.base_27
                        tax_5 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.vat_5
                        tax_10 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.vat_10
                        tax_21 = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.vat_21
                        tax_27 = (invoice.type == 'in_invoice' and 1.0
                            or 1.0) * invoice.vat_27
                        perc = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.vat_per
                        other_tax = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.other_taxes
                        total = (invoice.type == 'in_invoice' and 1.0
                            or -1.0) * invoice.total

                    # Write line                     
                    sheet.write(row, 5, untaxed, line)
                    sheet.write(row, 6, base_2, line)
                    sheet.write(row, 7, tax_2, line)
                    sheet.write(row, 8, base_5, line)
                    sheet.write(row, 9, tax_5, line)
                    sheet.write(row, 10, base_10, line)
                    sheet.write(row, 11, tax_10, line)
                    sheet.write(row, 12, base_21, line)
                    sheet.write(row, 13, tax_21, line)
                    sheet.write(row, 14, base_27, line)
                    sheet.write(row, 15, tax_27, line)
                    sheet.write(row, 16, perc, line)
                    sheet.write(row, 17, other_tax, line)
                    sheet.write(row, 18, total, line)
                    
                    # Adding totals
                    total_amount_untaxed += untaxed 
                    total_amount_base_2 = base_2
                    total_amount_tax_2 = tax_2
                    total_amount_base_5 = base_5
                    total_amount_tax_5 = tax_5
                    total_amount_base_10 = base_10
                    total_amount_tax_10 = tax_10
                    total_amount_base_21 = base_21
                    total_amount_tax_21 = tax_21
                    total_amount_base_27 = base_27
                    total_amount_tax_27 = tax_27
                    total_amount_perc += perc
                    total_amount_other_tax += other_tax
                    total_amount += total
                    row += 1
            
            # Write totals lines
            sheet.write(row, 5, total_amount_untaxed, bold)
            sheet.write(row, 6, total_amount_base_2, bold)
            sheet.write(row, 7, total_amount_tax_2, bold)
            sheet.write(row, 8, total_amount_base_5, bold)
            sheet.write(row, 9, total_amount_tax_5, bold)
            sheet.write(row, 10, total_amount_base_10, bold)
            sheet.write(row, 11, total_amount_tax_10, bold)
            sheet.write(row, 12, total_amount_base_21, bold)
            sheet.write(row, 13, total_amount_tax_21, bold)
            sheet.write(row, 14, total_amount_base_27, bold)
            sheet.write(row, 15, total_amount_tax_27, bold)
            sheet.write(row, 16, total_amount_perc, bold)
            sheet.write(row, 17, total_amount_other_tax, bold)
            sheet.write(row, 18, total_amount, bold)
