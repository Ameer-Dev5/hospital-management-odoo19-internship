from odoo import api, fields, models


class HospitalBilling(models.Model):
    _name = 'hospital.billing'
    _description = 'Hospital Billing'
    _order = 'billing_date desc'

    name = fields.Char(
        string='Bill Reference',
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
    billing_date = fields.Datetime(
        string='Billing Date',
        required=True,
        default=fields.Datetime.now,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('paid', 'Paid'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True,
    )
    line_ids = fields.One2many(
        'hospital.billing.line',
        'billing_id',
        string='Billing Lines',
    )
    amount_total = fields.Float(
        string='Total',
        compute='_compute_amount_total',
        store=True,
    )

    @api.depends('line_ids.subtotal')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(record.line_ids.mapped('subtotal'))

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_paid(self):
        self.write({'state': 'paid'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})


class HospitalBillingLine(models.Model):
    _name = 'hospital.billing.line'
    _description = 'Hospital Billing Line'

    billing_id = fields.Many2one(
        'hospital.billing',
        string='Bill',
        required=True,
        ondelete='cascade',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
    )
    quantity = fields.Float(
        string='Quantity',
        required=True,
        default=1.0,
    )
    price_unit = fields.Float(
        string='Unit Price',
        compute='_compute_price_unit',
    )
    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True,
    )

    @api.depends('product_id')
    def _compute_price_unit(self):
        for line in self:
            line.price_unit = line.product_id.list_price if line.product_id else 0.0

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit