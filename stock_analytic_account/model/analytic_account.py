# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Matmoz d.o.o.
# Copyright 2017 Luxim d.o.o.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    move_ids = fields.One2many(
        'stock.move',
        'analytic_account_id',
        'Moves for this analytic account',
        readonly=True
    )

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        default['move_ids'] = []
        return super(AccountAnalyticAccount, self).copy(default=default)
