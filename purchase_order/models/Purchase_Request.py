from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "purchase request"

    Request_name = fields.Char(string="Name")
    Requested_by = fields.Many2one('res.users', string="Requested_by", default=lambda self: self.env.user)
    Start_Date = fields.Date(string='Start Date', default=fields.Date.context_today)
    End_date = fields.Date(string="End Date")
    Rejection_Reason = fields.Text(string="Rejection Reason", readonly=True)
    orderlines_ids = fields.One2many('order.lines', 'purchase_id', string='orderlines')
    Total_Price = fields.Float(string='total price', compute='compute_total_price')
    state = fields.Selection(
        [('draft', 'draft'), ('to be approved', 'to be approved'), ('reject', 'reject'), ('approve', 'approve'),
         ('cancel', 'Cancelled')],
        string='state', default='draft', required=True)

    def action_in_to_be_approved(self):
        for r in self:
            r.state = 'to be approved'

    def action_draft(self):
        for r in self:
            r.state = 'draft'

    def action_approve(self):
        for r in self:
            r.state = 'approve'

    def action_cancel(self):
        for r in self:
            r.state = 'cancel'

    def action_reject(self):
        for r in self:
            r.state = 'reject'

    @api.depends('orderlines_ids.Total')
    def compute_total_price(self):
        for request in self:
            request.Total_Price = sum(request.orderlines_ids.mapped('Total'))


class Orderlines(models.Model):
    _name = "order.lines"
    _description = "order lines"

    product_id = fields.Many2one('product.product')
    Description = fields.Char(related='product_id.name')
    Quantity = fields.Integer(string='Quantity', default=1)
    Cost_Price = fields.Float(readonly=True, related='product_id.list_price')
    Total = fields.Float(readonly=True, compute='compute_total')
    purchase_id = fields.Many2one('purchase.request')

    @api.depends('Quantity', 'Cost_Price')
    def compute_total(self):
        for r in self:
            r.Total = r.Cost_Price * r.Quantity
