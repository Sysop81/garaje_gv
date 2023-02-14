# -*- coding: utf-8 -*-
{
    'name': "garajeGV",

    'summary': """
            Módulo para gestión de vehículos. Trabajo final SGE 2ºDAM.
    """,

    'description': """
            Este es un módulo destinado a la gestión de los vehículos del garaje, así como la revisiones de los mismos
            teniendo en cuenta a los mecánicos que realizan y a los consumibles empleados para realizar dichas revisiones.
    """,
    'application': True,
    'author': "José Ramón López Guillén, Francisco José Martínez Valencia.",
    'website': "http://www.yourcompany.com",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mecanico_view.xml',
        'views/consumible_view.xml',
        'views/vehiculo_view.xml',
        'views/revision_view.xml',
        'views/inicio_view.xml',
        'reports/revision_report.xml',   
    ],
   
}