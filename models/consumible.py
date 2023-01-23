from odoo import models, fields, api

class Consumible(models.Model):
    _name = 'consumible'
    _description = 'Consumibles de Garaje GV'

    codigo = fields.Integer('Código producto')
    nombre = fields.Char('Nombre producto')
    descripcion = fields.Char('Descripción')
    #base_i= fields.float ('Base Imponible')
    #iva = fields.Integer('IVA')
    #pvp = fields.float('Pvp', default = 0.0, compute = '_calculate_pvp')

    #_read_name = nombre

    #@api.onChange('base_i')
    #def _calculate_pvp(self):
    #    for record in self:
     #       if record.base_i and record.base_i > 0:
      #          record.pvp = record.base_i * record.iva



