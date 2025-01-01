{
    'name': 'Purchase GRN Auto Validating',
    'version': '1.1',
    'category': 'Receipt',
    'author': 'Pann Phyu',
    'summary': 'Purchase Receipt Management',
    'description': """
    	This module contains the modification about purchase receipt.The grn is auto validate when we confirm purchase order is confirmed.
    """,
    'depends':  ['base','purchase'],
    'data': [

        'views/res_config_view_form_inherit.xml',

    ],

    'installable': True,
    'auto_install': False
}
