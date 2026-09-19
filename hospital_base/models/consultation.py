from odoo import api, fields, models


class HospitalConsultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Hospital Consultation'
    _order = 'consultation_date desc'

    name = fields.Char(
        string='Consultation Reference',
        required=True,
        copy=False,
        default='New',
    )
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        ondelete='cascade',
    )
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor',
        required=True,
        ondelete='restrict',
    )
    service_product_id = fields.Many2one(
        'product.product',
        string='Medical Service',
        domain="[('categ_id.name', '=', 'Medical Services'), ('type', '=', 'service')]",
    )
    consultation_date = fields.Datetime(
        string='Consultation Date',
        required=True,
        default=fields.Datetime.now,
    )
    findings = fields.Text(string='Findings')
    plan = fields.Text(string='Plan')

    service_amount = fields.Monetary(
        string='Service Amount',
        currency_field='currency_id',
        default=0.0,
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Transaction Currency',
        required=True,
        default=lambda self: self.env.company.currency_id,
        domain=[('active', '=', True)],
    )

    company_currency_id = fields.Many2one(
        'res.currency',
        string='Company Currency',
        related='company_id.currency_id',
        readonly=True,
    )

    conversion_date = fields.Date(
        string='Conversion Date',
        required=True,
        default=fields.Date.context_today,
    )

    company_amount = fields.Monetary(
        string='Company Currency Amount',
        currency_field='company_currency_id',
        compute='_compute_company_amount',
    )

    @api.onchange('company_id')
    def _onchange_company_id_currency(self):
        if self.company_id:
            self.currency_id = self.company_id.currency_id

    @api.depends(
        'service_amount',
        'currency_id',
        'company_id.currency_id',
        'conversion_date',
    )
    def _compute_company_amount(self):
        for record in self:
            if not record.currency_id or not record.company_currency_id:
                record.company_amount = 0.0
                continue

            record.company_amount = record.currency_id._convert(
                record.service_amount,
                record.company_currency_id,
                record.company_id,
                record.conversion_date,
            )
