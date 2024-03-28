# -- coding: utf-8 --
{
    'name': "purchase order",
     'sequence':'-100',
    'summary': """
    purchase order system
        """,

    'description': """
    purchase order system
    """,

    'author': "shehab nasser",
    'website': "http://www.yourcompany.com",


    'category': 'purchase order',
    'version': '1.0.0',

    'depends': ['mail','product','purchase'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/cencel_purchase.xml',
        'views/menu.xml',
        'views/purchase_request.xml'

    ],
    # 'data': [
    #     # 'data/data.xml',
    # ],
    'application':True,
    'auto_install':False,
    'license':'LGPL-3'
}
