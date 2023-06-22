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

    pick_zone = fields.Many2one('stock.location', string='Pick zone', help='Field that allows to choose a stock location, this field is set from the first line of the stock move line', compute='_zone_assignment', store=True) #Campo relacionado con el modelo de Ubicaciones
    sale_date = fields.Datetime(string="Sale Date",help='Field that show the sale date',compute="_get_date_created")
    has_guide_number = fields.Boolean(string="Has guide number compute", help='Field set true if the sale has a guide number by compute', compute='_check_guide_number')#
    has_guide_number_index = fields.Boolean(string="Has guide number?", help='Field set true if the sale has a guide number')#
    is_colecta = fields.Boolean(string="Is Colecta", help=" This field shows if the pick comes from a 'colecta Meli order'.")
    priority_check = fields.Boolean(string="Colecta script check", help="TThis field gonna show true if the script was run")

    #Funcion para jalar la fecha de creacion de la venta.
    @api.depends('sale_id')
    def _get_date_created(self):
        for rec in self:
            if 'PICK' in rec.name:
                if rec.sale_id:
                    rec.sale_date = rec.sale_id.create_date
                else:
                    rec.sale_date = None
            else:
                rec.sale_date = None

    # Funcion para revisar si cuenta con numero de guia la venta.
    @api.depends('sale_id')
    def _check_guide_number(self):
        for rec in self:
            if 'PICK' in rec.name:
                if rec.sale_id != False:
                    if rec.sale_id.yuju_carrier_tracking_ref:
                        rec.has_guide_number = True
                        rec.has_guide_number_index = rec.has_guide_number
                    else:
                        rec.has_guide_number = False
                        rec.has_guide_number_index = rec.has_guide_number
                else:
                    rec.has_guide_number = False
                    rec.has_guide_number_index = rec.has_guide_number
            else:
                rec.has_guide_number = False
                rec.has_guide_number_index = rec.has_guide_number


    # Funcion para jalar la zona de pickeo.
    def _zone_assignment(self):
        for rec in self:
            if 'PICK' in rec.name:
                if rec.move_line_ids_without_package:
                    move_id = rec.move_line_ids_without_package.location_id.location_id.ids
                    rec.pick_zone = move_id[0]
                else:
                    rec.pick_zone = None
            else:
                rec.pick_zone = None


