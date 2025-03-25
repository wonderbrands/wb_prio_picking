# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_easyship = fields.Boolean(string='Es Easyship?', default=False)
