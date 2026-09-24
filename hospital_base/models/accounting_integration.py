from odoo import Command, _, api, fields, models
from odoo.exceptions import UserError


class HospitalConsultation(models.Model):
    _inherit = "hospital.consultation"

    invoice_ids = fields.One2many(
        "account.move",
        "hospital_consultation_id",
        string="Invoices",
        domain=[("move_type", "=", "out_invoice")],
    )

    invoice_count = fields.Integer(
        string="Invoices",
        compute="_compute_invoice_count",
    )

    @api.depends("invoice_ids")
    def _compute_invoice_count(self):
        for consultation in self:
            consultation.invoice_count = len(consultation.invoice_ids)

    def action_create_invoice(self):
        self.ensure_one()

        if not self.patient_id:
            raise UserError(
                _("Please set a patient before creating an invoice.")
            )

        patient = self.patient_id

        if not patient.partner_id:
            raise UserError(
                _("Please link this patient to a customer before creating an invoice.")
            )

        if not self.service_product_id:
            raise UserError(
                _("Please select a service product before creating an invoice.")
            )

        service_product = self.service_product_id

        if service_product.list_price <= 0:
            raise UserError(
                _("The selected service product must have a valid price greater than zero.")
            )

        existing_invoice = self.env["account.move"].search(
            [
                ("hospital_consultation_id", "=", self.id),
                ("move_type", "=", "out_invoice"),
                ("state", "!=", "cancel"),
            ],
            order="id desc",
            limit=1,
        )

        if existing_invoice:
            if not existing_invoice.invoice_line_ids:
                existing_invoice.write({
                    "partner_id": patient.partner_id.id,
                    "invoice_date": fields.Date.context_today(self),
                    "hospital_patient_id": patient.id,
                    "invoice_line_ids": [
                        Command.create({
                            "product_id": service_product.id,
                            "name": service_product.display_name,
                            "quantity": 1.0,
                            "price_unit": service_product.list_price,
                        })
                    ],
                })

            return {
                "type": "ir.actions.act_window",
                "name": _("Customer Invoice"),
                "res_model": "account.move",
                "view_mode": "form",
                "res_id": existing_invoice.id,
            }

        invoice = self.env["account.move"].create({
            "move_type": "out_invoice",
            "partner_id": patient.partner_id.id,
            "invoice_date": fields.Date.context_today(self),
            "hospital_consultation_id": self.id,
            "hospital_patient_id": patient.id,
            "invoice_line_ids": [
                Command.create({
                    "product_id": service_product.id,
                    "name": service_product.display_name,
                    "quantity": 1.0,
                    "price_unit": service_product.list_price,
                })
            ],
        })

        return {
            "type": "ir.actions.act_window",
            "name": _("Customer Invoice"),
            "res_model": "account.move",
            "view_mode": "form",
            "res_id": invoice.id,
        }

    def action_view_invoices(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": _("Customer Invoices"),
            "res_model": "account.move",
            "view_mode": "list,form",
            "domain": [
                ("hospital_consultation_id", "=", self.id),
                ("move_type", "=", "out_invoice"),
            ],
            "context": {
                "default_move_type": "out_invoice",
                "default_hospital_consultation_id": self.id,
                "default_hospital_patient_id": self.patient_id.id,
                "default_partner_id": self.patient_id.partner_id.id,
            },
        }


class AccountMove(models.Model):
    _inherit = "account.move"

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
