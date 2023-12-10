# -*- coding: utf-8 -*-
# from odoo import http


# class EmpresasContratadoras(http.Controller):
#     @http.route('/empresas_contratadoras/empresas_contratadoras', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresas_contratadoras/empresas_contratadoras/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresas_contratadoras.listing', {
#             'root': '/empresas_contratadoras/empresas_contratadoras',
#             'objects': http.request.env['empresas_contratadoras.empresas_contratadoras'].search([]),
#         })

#     @http.route('/empresas_contratadoras/empresas_contratadoras/objects/<model("empresas_contratadoras.empresas_contratadoras"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresas_contratadoras.object', {
#             'object': obj
#         })
