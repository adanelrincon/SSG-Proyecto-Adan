# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empresas_contratadoras(models.Model):
    _name = 'empresas_contratadoras'
    _description = 'Empresa Contratadora'

    name = fields.Char(string="Nombre de la Empresa.")
    proyectos = fields.Many2many("project.project",string="Proyectos")
    cantidad_tareas = fields.Integer(string="Cantidad de Tareas", compute="_compute_cantidad_tareas", store=True)
    empresa_tipo = fields.Selection(string="Tipo de Empresa", selection=[('Regional', 'Regional'), ('Nacional', 'Nacional'), ('Internacional', 'Internacional')])
    
    @api.depends('proyectos.tareas')
    def _compute_cantidad_tareas(self):
        for empresa in self:
            cantidad_tareas = 0
            for proyecto in empresa.proyectos:
                cantidad_tareas += len(proyecto.tareas)
            empresa.cantidad_tareas = cantidad_tareas


class Proyectos(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresas_contratadoras = fields.Many2one("empresas_contratadoras",string="Empresa Contratadora",inverse_name='proyectos')
    tareas = fields.One2many('project.task', 'project_id', string='Tareas')


class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   empresa_tipo = fields.Boolean(string="Tipo de Empresa",
       config_parameter='empresas_contratadoras.empresa_tipo')
