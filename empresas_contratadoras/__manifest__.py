# -*- coding: utf-8 -*-
{
    'name': "empresas_contratadoras",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Adán Pérez Hernández",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/regla_programador.xml',
        'reports/empresas_report.xml',
        'reports/empresas_report_view.xml',
        'data/project_tags_data.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',

    # assets
    'assets': {
        'web.assets_common': [
            'empresas_contratadoras/static/src/scss/style1.scss',
        ],
    }
}
