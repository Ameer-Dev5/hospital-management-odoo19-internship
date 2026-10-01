from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged
from datetime import date, timedelta
from odoo import fields


@tagged("post_install", "-at_install")
class TestHospitalPatient(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Patient = self.env["hospital.patient"]
        self.Appointment = self.env["hospital.appointment"]
        self.Doctor = self.env["hospital.doctor"]

        self.patient = self.Patient.create({
            "name": "Test Patient",
            "gender": "male",
            "phone": "03001234567",
            "email": "patient@example.com",
        })
        self.doctor = self.Doctor.create({
            "name": "Test Doctor",
        })

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "Test Patient")
        self.assertEqual(self.patient.gender, "male")
        self.assertTrue(self.patient.active)

    def test_appointment_creation(self):
        appointment = self.Appointment.create({
            "patient_id": self.patient.id,
            "doctor_id": self.doctor.id,
            'appointment_date': fields.Datetime.to_string(
                fields.Datetime.now() + timedelta(days=1)
            ),
        })
        self.assertTrue(appointment)
        self.assertEqual(appointment.patient_id, self.patient)
        self.assertEqual(appointment.doctor_id, self.doctor)

    def test_invalid_patient_dob(self):
        with self.assertRaises(ValidationError):
            self.Patient.create({
                "name": "Future DOB Patient",
                "gender": "male",
                "dob": date.today() + timedelta(days=1),
            })

    def test_business_action(self):
        appointment = self.Appointment.create({
            "patient_id": self.patient.id,
            "doctor_id": self.doctor.id,
            'appointment_date': fields.Datetime.to_string(
                fields.Datetime.now() + timedelta(days=1)
            ),
        })
        appointment.action_confirm()
        self.assertEqual(appointment.state, "confirmed")

    def test_security_restriction(self):
        restricted_user = self.env["res.users"].create({
            "name": "Restricted User",
            "login": "restricted_test_user",
            "group_ids": [(6, 0, [self.env.ref("base.group_public").id])],
        })
        with self.assertRaises(Exception):
            self.Patient.with_user(restricted_user).create({
                "name": "Unauthorized Patient",
                "gender": "male",
            })
