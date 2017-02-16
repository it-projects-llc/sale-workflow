# -*- coding: utf-8 -*-
# © 2015 Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class procurement_order(models.Model):
    _inherit = 'procurement.order'

    lot_id = fields.Many2one('stock.production.lot', 'Lot')

    @api.model
    def _run_move_create(self, procurement):
        res = super(
            procurement_order, self)._run_move_create(procurement)
        res['restrict_lot_id'] = procurement.lot_id.id
        return res
