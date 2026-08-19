from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(
        string='Patient Name',
        required=True,
        help='Enter the full name of the patient.'
    )

    ref = fields.Char(
        string='Patient Reference',
        index=True,
        copy=False,
        help='Unique reference used to identify the patient.'
    )

    dob = fields.Date(
        string='Date of Birth',
        help='Enter the patient date of birth.'
    )

    age = fields.Integer(
        string='Age',
        help='Enter the patient age in years.'
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string='Gender'
    )

    phone = fields.Char(
        string='Phone',
        help='Enter the patient phone number.'
    )

    email = fields.Char(
        string='Email',
        help='Enter the patient email address.'
    )

    address = fields.Char(
        string='Address',
        help='Enter the patient address.'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    notes = fields.Text(
        string='Notes',
        help='Additional notes about the patient.'
    )
