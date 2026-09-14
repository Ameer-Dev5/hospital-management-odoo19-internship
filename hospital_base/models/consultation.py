from odoo import fields, models


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