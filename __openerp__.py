# -*- coding: utf-8 -*-
{
    'name': "Promotion",

    'summary': """
        Promotion schemes for marketing""",

    'description': """
        Jewelry Channel dedicated for Jewelry Show and Knowledge
        we offers Jewelry Shopping experience, variety program, gems
        and gemology knowledge on the air training. The channel is owned
        by Image Focus Co.,Ltd. and operate it's content production.
    """,

    'author': "Jewelry Channel",
    'website': "http://www.jwctv.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/promotion.xml',
        'views/order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
