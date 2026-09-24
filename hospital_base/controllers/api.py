from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request


class HospitalAPI(http.Controller):

    @http.route(
        "/api/hospital/test",
        type="http",
        auth="bearer",
        methods=["GET"],
    )
    def test_api(self):
        return request.make_json_response({
            "success": True,
            "message": "Hospital API is working.",
            "user_id": request.env.user.id,
            "user_name": request.env.user.name,
        })

    @http.route(
        "/api/hospital/patients",
        type="http",
        auth="bearer",
        methods=["GET"],
    )
    def get_patients(self):
        try:
            patients = request.env["hospital.patient"].search(
                [],
                order="id desc",
            )
        except AccessError:
            return request.make_json_response(
                {
                    "success": False,
                    "error": "Access denied.",
                },
                status=403,
            )

        data = [
            {
                "id": patient.id,
                "name": patient.name,
                "reference": patient.ref or False,
                "gender": patient.gender or False,
                "status": patient.state,
            }
            for patient in patients
        ]

        return request.make_json_response({
            "success": True,
            "patients": data,
        })

    @http.route(
        "/api/hospital/patient/<int:patient_id>",
        type="http",
        auth="bearer",
        methods=["GET"],
    )
    def get_patient(self, patient_id):
        try:
            patient = request.env["hospital.patient"].search(
                [("id", "=", patient_id)],
                limit=1,
            )
        except AccessError:
            return request.make_json_response(
                {
                    "success": False,
                    "error": "Access denied.",
                },
                status=403,
            )

        if not patient:
            return request.make_json_response(
                {
                    "success": False,
                    "error": "Patient not found.",
                },
                status=404,
            )

        return request.make_json_response({
            "success": True,
            "patient": {
                "id": patient.id,
                "name": patient.name,
                "reference": patient.ref or False,
                "gender": patient.gender or False,
                "status": patient.state,
            },
        })

    @http.route(
        "/api/hospital/appointments",
        type="http",
        auth="bearer",
        methods=["GET"],
    )
    def get_appointments(self):
        try:
            appointments = request.env["hospital.appointment"].search(
                [],
                order="appointment_date desc",
            )
        except AccessError:
            return request.make_json_response(
                {
                    "success": False,
                    "error": "Access denied.",
                },
                status=403,
            )

        data = [
            {
                "id": appointment.id,
                "appointment": appointment.name,
                "doctor": appointment.doctor_id.name if appointment.doctor_id else False,
                "appointment_date": str(appointment.appointment_date)
                if appointment.appointment_date
                else False,
                "status": appointment.state,
            }
            for appointment in appointments
        ]

        return request.make_json_response({
            "success": True,
            "appointments": data,
        })
