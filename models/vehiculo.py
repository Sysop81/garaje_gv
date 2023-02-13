# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api



class Vehiculo(models.Model):
     _name = 'vehiculo'
     _description = 'Vehiculo de garaje GV'

     _order = 'marca'
    
     bastidor = fields.Char('Bastidor',required=True)
     matricula = fields.Char('Matricula',required=True)
     marca = fields.Char('Marca',required=True)
     modelo = fields.Char('Modelo',required=True)
     combustible = fields.Selection([
        ('diesel','Diésel'),
        ('gasolina','Gasolina'),
        ('electrico','Eléctrico')
     ],"Combustible", default="diesel")
     cilindrada = fields.Integer('Cilindrada')
     estado = fields.Selection( [
          ('nuevo', 'Vehículo nuevo'),
          ('seminuevo', 'Vehículo seminuevo'),
          ('usado', 'Vehículo usado')
          ],'Estado vehículo', default = 'nuevo')
     potencia = fields.Integer('Potencia') 
     tipo = fields.Selection([
        ('berlina','Berlina'),
        ('station','Station Wagon'),
        ('suv','Suv'),
        ('compacto','Compacto'),
        ('monovolumen','Monovolumen'),
        ('todoterreno','Todoterreno')
        ],'Tipo vehículo',default='berlina')
     kml = fields.Integer('Kilómetros',required=True)
     plazas = fields.Integer('Nº plazas')   
     fecha_mat = fields.Date('Fecha matriculación', default = lambda self:fields.Date.today())
     valor_compra = fields.Float('Valor nuevo')
     valor_actual = fields.Float('Valor actual',compute='_calculate_current_value')
     activo = fields.Boolean(default = True)    
     descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)

     _rec_name = 'bastidor'

     @api.depends('valor_compra') 
     def _calculate_current_value(self):
          for r in self:
              try:
                  edad_vehiculo = relativedelta(datetime.now(), r.fecha_mat)
                  
                  depreciacion_anio = 0.1

                  resultado = r.valor_compra - r.valor_compra * (depreciacion_anio * edad_vehiculo.years)

                  r.valor_actual = resultado if resultado > 0 else 0.0
              except:
                   r.valor_actual = 0.0      