# -*- coding: utf-8 -*-
from odoo import models, fields, api
class AccountMove( models.Model):
    _inherit = 'account.move'
    control_number = fields.Char(string='Numero de control', required=True, store=True, default='00')
    