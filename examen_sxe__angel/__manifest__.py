# -*- coding: utf-8 -*-
{
    'name': "examenSXE_Angel",

    'summary': "información sobre alumnos y sus proyectos",

    'description': """
Este módulo consiste en un modelo de
datos que permite añadir información sobre alumnos y sus proyectos n de
ciclo. 
    """,

    'author': "Angel Jose Piñeiro Andion",
    'website': "https://github.com/apineiroandion/examenSXE_ModulosOdoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

