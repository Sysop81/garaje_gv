from odoo import models, fields, api

class Consumible(models.Model):
    _name = 'consumible'
    _description = 'Consumibles de Garaje GV'

    _order = 'nombre'

    codigo = fields.Integer('Código producto', required=True)
    nombre = fields.Char('Nombre producto', required=True)
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    disponible = fields.Selection([
        ('si','Disponible'),
        ('no','No disponible')
        ],'Disponible',default='si', required=True)
    base_i= fields.Float ('Base Imponible')
    iva = fields.Selection([
            ('4','4% Superreducido'),
            ('10','10% Reducido'),
            ('21','21% General')
            ],'IVA',default='21', required=True)
    pvp = fields.Float('PVP', default = 0.0, compute = '_calculate_pvp')

    _rec_name='nombre'

    _sql_constraints = [
        ('codigo_uniq', 'UNIQUE (codigo)', 'El código del producto ya existe.'),
        ('nombre_uniq', 'UNIQUE (nombre)', 'El nombre del producto ya existe.')
    ]

    @api.onchange('base_i','iva')
    def _calculate_pvp(self):
        for record in self:
            if record.base_i and record.base_i > 0:
                record.pvp = record.base_i * ((int(record.iva) / 100) + 1)
            else:
                record.pvp = 0    


