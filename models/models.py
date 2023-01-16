# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class garaje_gv(models.Model):
#     _name = 'garaje_gv.garaje_gv'
#     _description = 'garaje_gv.garaje_gv'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
