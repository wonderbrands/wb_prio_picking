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
    'category': 'Tools',
    'version': '15.1',

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
