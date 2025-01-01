from odoo import api, fields, models, _
from odoo.exceptions import UserError,ValidationError

class Purchase(models.Model):
    _inherit = 'purchase.order'

    def validate_purchase_grn(self,picking_ids):
        if picking_ids:
            picking = picking_ids[0]
            for move_line in picking.move_ids_without_package:
                move_line.quantity_done = move_line.product_uom_qty
            picking.action_assign()
            picking.button_validate()

    def button_confirm(self):
        auto_grn = self.env['ir.config_parameter'].sudo().get_param('purchase_grn_auto_validating.enable_purchase_grn_id')
        res = super(Purchase, self).button_confirm()
        if auto_grn:
            self.validate_purchase_grn(self.picking_ids)
        return res





