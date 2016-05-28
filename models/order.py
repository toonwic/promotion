# -*- coding: utf-8 -*-
from openerp import fields, models

class Order(models.Model):
    _inherit = 'sale.order'

    promos = fields.Boolean("Promotion", default=False)

    # rule_id = fields.Many2one('openacademy.rule', string="Ruled", readonly=True)
