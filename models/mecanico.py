# -*- coding: utf-8 -*-

from odoo import models, fields



class Mecanico(models.Model):
     _name = 'mecanico'
     _description = 'Mecánico de garaje GV'

     _order = 'nombre'
    
     dni = fields.Char('Dni Empleado',required=True)
     nombre = fields.Char('Nombre',required=True)
     apellido1 = fields.Char('Primer Apellido',required=True)
     apellido2 = fields.Char('Segundo Apellido',required=True)
     cargo = fields.Selection( [
          ('jefetaller', 'Jefe de taller'),
          ('encargado', 'Encargado'),
          ('mecanicoof1', 'Mecánico Oficial 1'),
          ('mecanicoof2', 'Mecánico Oficial 2'),
          ('aprendiz', 'Aprendiz')],
          'Cargo Empleado', default = 'mecanicoof1')
     fechainicio = fields.Date('Fecha inicio', default = lambda self:fields.Date.today()) 
     fechafin = fields.Date('Fecha cese', default = lambda self:fields.Date.today())
     activo = fields.Boolean(default = True) 
     foto = fields.Binary('Foto')   

     _rec_name = 'nombre'

     _sql_constraints = [
        ('dni_uniq', 'UNIQUE (dni)', 'El DNI introducido ya existe.')
     ]
