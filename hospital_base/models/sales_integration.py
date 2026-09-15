from odoo import Command, _, api, fields, models
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    _inherit = "hospital.patient"

    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        ondelete="set null",
        index=True,
    )

    sale_order_ids = fields.One2many(
        "sale.order",
        "hospital_patient_id",
        string="Sales Orders",
    )

    sale_order_count = fields.Integer(
        string="Sales Orders",
        compute="_compute_sale_order_count",
    )

    @api.depends("sale_order_ids")
    def _compute_sale_order_count(self):
        for patient in self:
            patient.sale_order_count = len(patient.sale_order_ids)

    def action_view_sales_orders(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Sales Orders"),
            "res_model": "sale.order",
            "view_mode": "list,form",
            "domain": [("hospital_patient_id", "=", self.id)],
            "context": {
                "default_hospital_patient_id": self.id,
                "default_partner_id": self.partner_id.id,
            },
        }


class HospitalConsultation(models.Model):
    _inherit = "hospital.consultation"

    sale_order_ids = fields.One2many(
        "sale.order",
        "hospital_consultation_id",
        string="Quotations",
    )

    quotation_count = fields.Integer(
        string="Quotations",
        compute="_compute_quotation_count",
    )

    @api.depends("sale_order_ids")
    def _compute_quotation_count(self):
        for consultation in self:
            consultation.quotation_count = len(consultation.sale_order_ids)

    def action_create_quotation(self):
        self.ensure_one()

        if not self.patient_id:
            raise UserError(_("Please set a patient before creating a quotation."))

        patient = self.patient_id

        if not patient.partner_id:
            raise UserError(
                _("Please link this patient to a customer before creating a quotation.")
            )

        if not self.service_product_id:
            raise UserError(
                _("Please select a service product before creating a quotation.")
            )

        existing_order = self.env["sale.order"].search(
            [
                ("hospital_consultation_id", "=", self.id),
                ("state", "!=", "cancel"),
            ],
            order="id desc",
            limit=1,
        )

        if existing_order:
            return {
                "type": "ir.actions.act_window",
                "name": _("Quotation"),
                "res_model": "sale.order",
                "view_mode": "form",
                "res_id": existing_order.id,
            }

        order = self.env["sale.order"].create(
            {
                "partner_id": patient.partner_id.id,
                "hospital_patient_id": patient.id,
                "hospital_consultation_id": self.id,
                "order_line": [
                    Command.create(
                        {
                            "product_id": self.service_product_id.id,
                            "product_uom_qty": 1.0,
                        }
                    )
                ],
            }
        )

        return {
            "type": "ir.actions.act_window",
            "name": _("Quotation"),
            "res_model": "sale.order",
            "view_mode": "form",
            "res_id": order.id,
        }

    def action_view_quotations(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Quotations"),
            "res_model": "sale.order",
            "view_mode": "list,form",
            "domain": [("hospital_consultation_id", "=", self.id)],
            "context": {
                "default_hospital_consultation_id": self.id,
                "default_hospital_patient_id": self.patient_id.id,
                "default_partner_id": self.patient_id.partner_id.id,
            },
        }


class SaleOrder(models.Model):
    _inherit = "sale.order"

    hospital_patient_id = fields.Many2one(
        "hospital.patient",
        string="Hospital Patient",
        ondelete="set null",
        index=True,
    )

    hospital_consultation_id = fields.Many2one(
        "hospital.consultation",
        string="Hospital Consultation",
        ondelete="set null",
        index=True,
    )