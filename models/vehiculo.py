# -*- coding: utf-8 -*-

from odoo import models, fields



class Vehiculo(models.Model):
     _name = 'vehiculo'
     _description = 'Vehiculo de garaje GV'

    
     bastidor = fields.Char('Bastidor')
     matricula = fields.Char('Matricula')
     marca = fields.Char('Marca')
     modelo = fields.Char('Modelo')
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
     kml = fields.Integer('Kilómetros')
     plazas = fields.Integer('Nº plazas')   
     fecha_mat = fields.Date('Fecha matriculación', default = lambda self:fields.Date.today())
     valor_compra = fields.Float('Valor nuevo')
     valor_actual = fields.Float('Valor actual')
     activo = fields.Boolean(default = True)    
     descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)

     _rec_name = 'bastidor'