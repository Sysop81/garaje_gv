# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Revision(models.Model):
     _name = 'revision'
     _description = 'Revisión de un vehículo de garaje GV'

    
     codigo = fields.Integer('Código')
     kml = fields.Integer('Kilómetros actuales')
     kml_p = fields.Integer('Kilómetros próxima')
     fecha = fields.Date('Fecha', default = lambda self:fields.Date.today())
     horas_taller = fields.Integer('Horas taller')
     valor_total = fields.Float('Total',compute='_add_prices_to_total')
     bastidor = fields.Many2one('vehiculo')   
     mecanico = fields.Many2one('mecanico')
     consumibles = fields.Many2many('consumible',string='Consumbles')  
     descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
        

     @api.onchange('consumibles','horas_taller')
     def _add_prices_to_total(self):
          precio_hora = 25
          for r in self:
               r.valor_total = 0
               for item in r.consumibles:
                    r.valor_total = r.valor_total + item.pvp
               if r.horas_taller and r.horas_taller > 0:
                    r.valor_total = r.valor_total + (r.horas_taller * precio_hora)
               