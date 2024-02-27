# -*- coding: utf-8 -*-

from odoo import models, fields, api


class empresas_contratadoras(models.Model):
    _name = 'empresas_contratadoras'
    _description = 'Empresa Contratadora'

    name = fields.Char(string="Nombre de la Empresa.")
    proyectos = fields.Many2many("project.project",string="Proyectos")
    cantidad_tareas = fields.Integer(string="Cantidad de Tareas", compute="_compute_cantidad_tareas", store=True)
    empresa_tipo = fields.Selection(string="Tipo de Empresa", selection=[('Regional', 'Regional'), ('Nacional', 'Nacional'), ('Internacional', 'Internacional')])
    # ch = fields.Boolean(string="ch", related='res_config_settings_id.ch', store=True)

    # res_config_settings_id = fields.Many2one(
    #     'res.config.settings',
    #     string='Configuration Settings',
    #     help='Technical field for storing the related configuration settings record.'
    # )

    @api.depends('proyectos.tareas')
    def _compute_cantidad_tareas(self):
        for empresa in self:
            cantidad_tareas = 0
            for proyecto in empresa.proyectos:
                cantidad_tareas += len(proyecto.tareas)
                empresa.cantidad_tareas = cantidad_tareas

    @api.model
    def create(self, vals):
        registro_vals = {
            'usuario': self.env.user.name,
            'nombre_empresa': vals.get('name'),
            'fecha_hora': fields.Datetime.now(),
            'tipo_accion': 'creacion',
        }
        self.env['empresa_registro'].create(registro_vals)
        return super(empresas_contratadoras, self).create(vals)

    def write(self, vals):
        for empresa in self:
            registro_vals = {
                'usuario': self.env.user.name,
                'nombre_empresa': empresa.name,
                'fecha_hora': fields.Datetime.now(),
                'tipo_accion': 'modificacion',
            }
            self.env['empresa_registro'].create(registro_vals)
        return super(empresas_contratadoras, self).write(vals)


class Proyectos(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresas_contratadoras = fields.Many2one(
        "empresas_contratadoras",
        string="Empresa Contratadora",
        inverse_name='proyectos'
    )

    tareas = fields.One2many(
        'project.task', 
        'project_id', 
        string='Tareas'
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    registros = fields.Many2many("empresa_registro",string="Registros")

    @api.model
    def default_get(self, fields):
        defaults = super(ResConfigSettings, self).default_get(fields)
        empresa_registros = self.env['empresa_registro'].search([])
        defaults['registros'] = [(6, 0, empresa_registros.ids)]
        return defaults

class EmpresaRegistro(models.Model):
    _name = 'empresa_registro'
    _description = 'Registro de Creación y Modificación de Empresas'

    usuario = fields.Char(string="Usuario")
    nombre_empresa = fields.Char(string="Nombre de la Empresa")
    fecha_hora = fields.Datetime(string="Fecha/Hora")
    tipo_accion = fields.Selection([('creacion', 'Creación'), ('modificacion', 'Modificación')], string="Tipo de Acción")
