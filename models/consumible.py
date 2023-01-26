from odoo import models, fields, api

class Consumible(models.Model):
    _name = 'consumible'
    _description = 'Consumibles de Garaje GV'

    codigo = fields.Integer('Código producto')
    nombre = fields.Char('Nombre producto')
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    disponible = fields.Selection([
        ('si','Disponible'),
        ('no','No disponible')
        ],'Disponible',default='si')
    base_i= fields.Float ('Base Imponible')
    iva = fields.Integer('IVA')
    pvp = fields.Float('Pvp', default = 0.0, compute = '_calculate_pvp')

    _read_name = nombre

    @api.onchange('base_i','iva')
    def _calculate_pvp(self):
        for record in self:
            if record.base_i and record.base_i > 0:
                record.pvp = record.base_i * ((record.iva / 100) + 1)


