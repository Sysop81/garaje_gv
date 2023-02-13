# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Revision(models.Model):
     _name = 'revision'
     _description = 'Revisión de un vehículo de garaje GV'

     _order = 'codigo desc, fecha'
    
     codigo = fields.Integer('Código',required=True)
     kml = fields.Integer('Kilómetros actuales',related="bastidor.kml",store=True)
     kml_p = fields.Integer('Kilómetros próxima')
     fecha = fields.Date('Fecha', default = lambda self:fields.Date.today())
     horas_taller = fields.Integer('Horas taller',required=True)
     valor_total = fields.Float('Total',compute='_add_prices_to_total')
     bastidor = fields.Many2one('vehiculo', domain="[('activo','=','True')]",required=True)   
     mecanico = fields.Many2one('mecanico', domain="[('activo','=','True')]",required=True)
     consumibles = fields.Many2many('consumible',string='Consumbles',domain="[('disponible', '=', 'si')]",required=True)  
     descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
     val = fields.Float()
        
     _sql_constraints = [
        ('codigo_uniq', 'UNIQUE (codigo)', 'El código de factura ya existe.')
    ]

     @api.onchange('consumibles','horas_taller')
     def _add_prices_to_total(self):
          precio_hora = 25
          for r in self:
               r.valor_total = 0
               for item in r.consumibles:
                    r.valor_total = r.valor_total + item.pvp
               if r.horas_taller and r.horas_taller > 0:
                    r.valor_total = r.valor_total + (r.horas_taller * precio_hora)
               r.val = r.valor_total     
               