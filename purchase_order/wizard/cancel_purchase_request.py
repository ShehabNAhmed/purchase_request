from odoo import models, fields, api
from datetime import date


class CancelPurchaseWizard(models.TransientModel):
    _name = "cancel.purchase.wizard"
    _description = "cancel purchase wizard"

    Rejection_Reason = fields.Text(string="Rejection Reason", )

    # def action_cancel(self):
    #     self.Rejection_Reason = self.purchase_id.Rejection_Reason


    def action_add_rejection(self):
        active_id = self.env.context.get('active_id')
        print(active_id)
        current_real = self.env['purchase.request'].search([('id', '=', active_id)])
        print(current_real)
        current_real.Rejection_Reason = self.Rejection_Reason