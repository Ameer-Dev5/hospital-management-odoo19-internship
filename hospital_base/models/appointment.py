from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _order = 'appointment_date desc'

    name = fields.Char(
        string='Appointment Reference',
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

    appointment_date = fields.Datetime(
        string='Appointment Date & Time',
        required=True,
    )

    appointment_type = fields.Selection(
        [
            ('consultation', 'Consultation'),
            ('checkup', 'Checkup'),
            ('follow_up', 'Follow-up'),
            ('emergency', 'Emergency'),
        ],
        string='Appointment Type',
        required=True,
        default='consultation',
    )

    priority = fields.Selection(
        [
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High'),
        ],
        string='Priority',
        default='0',
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
    )

    notes = fields.Text(string='Notes')

    @api.constrains('appointment_date')
    def _check_appointment_date(self):
        for record in self:
            if record.appointment_date and record.appointment_date < fields.Datetime.now():
                raise ValidationError(
                    'Appointment date and time cannot be in the past.'
                )

    def action_confirm(self):
        template = self.env.ref(
            'hospital_base.mail_template_appointment_confirmation',
            raise_if_not_found=False,
        )

        for record in self:
            record.state = 'confirmed'

            if template and record.patient_id.email:
                template.send_mail(record.id, force_send=True)

        return True

    def action_complete(self):
        self.write({'state': 'completed'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})
