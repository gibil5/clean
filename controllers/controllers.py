# -*- coding: utf-8 -*-
from openerp import http

# class Clean(http.Controller):
#     @http.route('/clean/clean/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clean/clean/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clean.listing', {
#             'root': '/clean/clean',
#             'objects': http.request.env['clean.clean'].search([]),
#         })

#     @http.route('/clean/clean/objects/<model("clean.clean"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clean.object', {
#             'object': obj
#         })