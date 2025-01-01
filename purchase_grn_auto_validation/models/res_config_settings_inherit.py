from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_purchase_grn = fields.Boolean('Auto Receipt',config_parameter='purchase_grn_auto_validating.enable_purchase_grn_id')
