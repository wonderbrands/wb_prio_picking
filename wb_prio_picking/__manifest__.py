# -*- coding: utf-8 -*-
{
    'name': "Modificaciones para la priorizacion de despacho de picks",

    'summary': """
        Modificaciones para la priorizacion de despacho de picks""",

    'description': """
        Este módulo agrega diferentes modificaciones y campos al formulario de traslados
    """,

    'author': "Wonderbrands",
    'website': "https://www.wonderbrands.co",
    'category': 'Inventory',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product',
                'sale',
                'stock',
                'madkting'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
