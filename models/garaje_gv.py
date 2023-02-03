# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Garaje_gv(models.Model):
     _name = 'garaje.gv'
     _description = 'Clase de inicio de Garaje GV'

     def mecanicos(self):
          r = 'hola'
          #self.ensure_one()
          #list_view = self.env.ref('')