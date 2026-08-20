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

    def action_create_demo_patients(self):
        Patient = self.env['hospital.patient']
        Patient.create({'name': 'Ali Raza', 'ref': 'PAT-001', 'age': 30, 'gender': 'male'})
        Patient.create({'name': 'Sana Khan', 'ref': 'PAT-002', 'age': 25, 'gender': 'female'})
        Patient.create([
            {'name': 'Bilal Ahmed', 'ref': 'PAT-003', 'age': 40, 'gender': 'male'},
            {'name': 'Ayesha Noor', 'ref': 'PAT-004', 'age': 22, 'gender': 'female'},
        ])

    def action_read_demo_patients(self):
        patients = self.env['hospital.patient'].search([])
        for patient in patients:
            print(patient.id, patient.name, patient.age, patient.gender)

    def action_search_demo_patients(self):
        Patient = self.env['hospital.patient']
        active_patients = Patient.search([('active', '=', True)])
        male_patients = Patient.search([('gender', '=', 'male')])
        by_name = Patient.search([('name', 'like', 'Ali')])
        recent = Patient.search([], limit=5, order='id desc')
        return active_patients, male_patients, by_name, recent

    def action_update_demo_patients(self):
        Patient = self.env['hospital.patient']
        patient = Patient.search([('ref', '=', 'PAT-001')], limit=1)
        if patient:
            patient.write({'age': 31})

        male_patients = Patient.search([('gender', '=', 'male')])
        male_patients.write({'active': True})

    def action_delete_demo_patients(self):
        Patient = self.env['hospital.patient']
        test_patients = Patient.search([('ref', 'like', 'PAT-00')])
        test_patients.unlink()

    def action_count_and_browse_demo(self):
        Patient = self.env['hospital.patient']
        count = Patient.search_count([('gender', '=', 'female')])
        patient = Patient.browse(1)  # use a real existing ID
        exists = patient.exists()
        return count, patient, exists

    def action_orm_demo(self):
        Patient = self.env['hospital.patient']

        new_patient = Patient.create({'name': 'Demo Patient', 'ref': 'PAT-DEMO', 'age': 28, 'gender': 'male'})

        found = Patient.search([('ref', '=', 'PAT-DEMO')])

        for p in found:
            print(p.name, p.age)

        found.write({'age': 29})

        total = Patient.search_count([])

        found.unlink()

        return total
