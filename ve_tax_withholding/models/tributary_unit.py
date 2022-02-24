# -*- coding: utf-8 -*- 
import datetime 
from odoo import models, fields, api


class TributaryUnit(models.Model):
    _name = 'tax.tributary_unit'
    _description = 'model for tributary  unit'
    
    unit = fields.Float(string='Valor de la Unidad Tributaria', required = True, store= True)
    minimum = fields.Text(string='Minimo', default= lambda self: self._compute_minimum() , store= True)
    
    gaceta = fields.Char(string='Nro. Gaceta', store= True)
    gaceta_fecha = fields.Date(string='Fecha de la Gaceta', store= True)
    
    @api.onchange('unit')
    def _compute_minimum(self):
        for record in self:
            #configs = self.env['res.config.settings']
            configs = self.env['res.company']
            record.minimum = configs
            