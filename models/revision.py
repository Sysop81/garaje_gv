# -*- coding: utf-8 -*-

from odoo import models, fields



class Revision(models.Model):
     _name = 'revision'
     _description = 'Revisión de un vehículo de garaje GV'

    
     codigo = fields.Integer('Código')
     kml = fields.Integer('Kilómetros actuales')
     kml_p = fields.Integer('Kilómetros próxima')
     fecha = fields.Date('Fecha', default = lambda self:fields.Date.today())
     horas_taller = fields.Integer('Horas taller')
     valor_total = fields.Float('Total')
     bastidor = fields.Many2one('vehiculo')   
     mecanico = fields.Many2one('mecanico')  
     descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)