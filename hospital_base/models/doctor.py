from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(
        string='Doctor Name',
        required=True
    )

    license_ref = fields.Char(
        string='License/Reference',
        copy=False
    )

    specialization = fields.Char(
        string='Specialization'
    )

    phone = fields.Char(
        string='Phone'
    )

    email = fields.Char(
        string='Email'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    patient_ids = fields.One2many(
        'hospital.patient',
        'doctor_id',
        string='Primary Patients'
    )