from odoo import fields, models


class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Hospital Prescription'
    _order = 'date desc'

    name = fields.Char(
        string='Prescription Reference',
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
    date = fields.Datetime(
        string='Prescription Date',
        required=True,
        default=fields.Datetime.now,
    )
    line_ids = fields.One2many(
        'hospital.prescription.line',
        'prescription_id',
        string='Medicines',
    )
    notes = fields.Text(string='Notes')


class HospitalPrescriptionLine(models.Model):
    _name = 'hospital.prescription.line'
    _description = 'Hospital Prescription Line'

    prescription_id = fields.Many2one(
        'hospital.prescription',
        string='Prescription',
        required=True,
        ondelete='cascade',
    )
    medicine_id = fields.Many2one(
        'product.product',
        string='Medicine',
        required=True,
        domain="[('categ_id.name', '=', 'Medicines'), ('type', '!=', 'service')]",
    )
    quantity = fields.Float(
        string='Quantity',
        required=True,
        default=1.0,
    )
    notes = fields.Char(string='Notes')