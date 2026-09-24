from odoo import fields, models


class HospitalPatientMultiCompany(models.Model):
    _inherit = 'hospital.patient'
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        check_company=True,
    )

    doctor_ids = fields.Many2many(
        'hospital.doctor',
        check_company=True,
    )


class HospitalDoctorMultiCompany(models.Model):
    _inherit = 'hospital.doctor'
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )


class HospitalAppointmentMultiCompany(models.Model):
    _inherit = 'hospital.appointment'
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )

    patient_id = fields.Many2one(
        'hospital.patient',
        check_company=True,
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        check_company=True,
    )


class HospitalConsultationMultiCompany(models.Model):
    _inherit = 'hospital.consultation'
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )

    patient_id = fields.Many2one(
        'hospital.patient',
        check_company=True,
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        check_company=True,
    )

    service_product_id = fields.Many2one(
        'product.product',
        check_company=True,
    )

    sales_product_id = fields.Many2one(
        'product.product',
        check_company=True,
    )


class HospitalSaleOrderMultiCompany(models.Model):
    _inherit = 'sale.order'
    _check_company_auto = True

    hospital_patient_id = fields.Many2one(
        'hospital.patient',
        check_company=True,
    )

    hospital_consultation_id = fields.Many2one(
        'hospital.consultation',
        check_company=True,
    )