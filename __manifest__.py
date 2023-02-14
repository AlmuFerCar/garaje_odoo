# -*- coding: utf-8 -*-
{
    'name': "Gestión de Garajes",

    'summary': """
        Gestión de colecciones de coches en aparcamientos""",

    'description': """
        ESte es el modulo que trata a cerca de como constituir un modulo en odoo 16
    """,

    'author': "AlmuDani",
    'website': "https://www.youtube.com/@meetmap",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/garaje_aparcamiento_report.xml',
        'data/garaje_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #Indicamos que es una aplicacion
    'application':True,
}

