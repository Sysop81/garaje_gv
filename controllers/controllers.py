# -*- coding: utf-8 -*-
# from odoo import http


# class GarajeGv(http.Controller):
#     @http.route('/garaje_gv/garaje_gv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/garaje_gv/garaje_gv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('garaje_gv.listing', {
#             'root': '/garaje_gv/garaje_gv',
#             'objects': http.request.env['garaje_gv.garaje_gv'].search([]),
#         })

#     @http.route('/garaje_gv/garaje_gv/objects/<model("garaje_gv.garaje_gv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garaje_gv.object', {
#             'object': obj
#         })
