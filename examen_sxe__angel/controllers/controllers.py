# -*- coding: utf-8 -*-
# from odoo import http


# class ExamenSxeAngel(http.Controller):
#     @http.route('/examen_sxe__angel/examen_sxe__angel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_sxe__angel/examen_sxe__angel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_sxe__angel.listing', {
#             'root': '/examen_sxe__angel/examen_sxe__angel',
#             'objects': http.request.env['examen_sxe__angel.examen_sxe__angel'].search([]),
#         })

#     @http.route('/examen_sxe__angel/examen_sxe__angel/objects/<model("examen_sxe__angel.examen_sxe__angel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_sxe__angel.object', {
#             'object': obj
#         })

