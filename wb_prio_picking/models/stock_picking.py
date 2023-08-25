# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, SUPERUSER_ID
from odoo import models, fields, api, _
from odoo.exceptions import Warning
from datetime import datetime
import time
import logging
import json
import requests


class Picking(models.Model):
    _inherit = 'stock.picking'

    pick_zone = fields.Many2one('stock.location', string='Zona de Pickeo',
                                help='Field that allows to choose a stock location, this field is set from the first line of the stock move line',
                                compute='_zone_assignment')  # Campo relacionado con el modelo de Ubicaciones
    pick_zone_index = fields.Many2one('stock.location', string='Zona de Pickeo',
                                      help='Field that allows to choose a stock location, this field is set from the first line of the stock move line',
                                      store=True)
    has_shipping_label = fields.Boolean(string="Has shipping label compute",
                                        help='Field set true if the sale has a guide number by compute',
                                        compute='_get_sale_info')  #
    has_shipping_label_index = fields.Boolean(string="Has shipping label?",
                                              help='Field set true if the sale has a guide number')  #
    is_colecta = fields.Boolean(string="Is Colecta",
                                help='This field shows if the pick comes from a "colecta Meli order".')
    priority_check = fields.Boolean(string="Colecta script check",
                                    help='This field gonna show true if the script was run')
    # campo nuevo 31/07/2023
    pick_up_date = fields.Datetime(string="Pick-Up Date",
                                   help='Field that show the Pick-Up date')  # Este campo se le asignara un valor desde el script
    # campo nuevo 25/08/2023
    restocked = fields.Boolean(string="Es Resurtido?",
                               help='Este campo permite identificar los movimientos de resurtido a marketplace')
    fulfillment_type = fields.Selection([
        ('fbf', 'Flex'),
        ('mix', 'Mix'),
        ('fbm', 'Seller'),
        ('fbc', 'Full'),
    ], string="Fulfillment", compute="_get_sale_info")

    # Funcion para revisar si cuenta con numero de guia la venta.
    @api.depends('sale_id')
    def _get_sale_info(self):
        for rec in self:
            if '/PICK/' or '/INT/' in rec.name:
                if rec.sale_id != False:
                    if rec.sale_id.yuju_carrier_tracking_ref or rec.restocked:
                        rec.has_shipping_label = True
                        rec.has_shipping_label_index = rec.has_shipping_label
                    else:
                        rec.has_shipping_label = False
                        rec.restocked = False
                        rec.has_shipping_label_index = rec.has_shipping_label

                    if rec.sale_id.fulfillment:
                        rec.fulfillment_type = rec.sale_id.fulfillment
                    else:
                        rec.fulfillment_type = None
                else:
                    rec.fulfillment_type = None
                    rec.has_shipping_label = False
                    rec.has_shipping_label_index = rec.has_shipping_label
            else:
                rec.has_shipping_label = False
                rec.fulfillment_type = None
                rec.has_shipping_label_index = rec.has_shipping_label

    # Funcion para jalar la zona de pickeo.
    @api.depends('move_line_ids_without_package.location_id')
    def _zone_assignment(self):
        for rec in self:
            if '/PICK/' in rec.name:
                if rec.move_line_ids_without_package:
                    move_id = rec.move_line_ids_without_package.location_id.location_id.ids
                    rec.pick_zone = move_id[0]
                    rec.pick_zone_index = rec.pick_zone
                else:
                    rec.pick_zone = None
                    rec.pick_zone_index = rec.pick_zone
            else:
                rec.pick_zone = None
                rec.pick_zone_index = rec.pick_zone

    # Print "Ticket Prepick" report
    def prepicking_ticket(self):
        self.ensure_one()
        return self.env.ref('wb_prio_picking.action_picking_label_report').report_action(self)