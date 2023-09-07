# -*- coding: utf-8 -*-
{
    'name': "Modulo de priorizacion de picks para Somos Reyes",

    'summary': """
        Modulo de priorizacion de picks para Somos Reyes, validacion de piezas para despacho de out, Zonas de pickeo
        """,

    'description': """
        Este módulo agrega diferentes modificaciones y campos al formulario de traslados
    """,

    'author': "Wonderbrands",
    'website': "https://www.wonderbrands.co",
    'category': 'Tools',
    'version': '15.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product',
                'sale',
                'stock',
                'madkting'],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
        'report/ticket_prepicking.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
