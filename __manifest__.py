{

  'name': "Real-Estate Management",

  'version': '1.0',

  'depends': ['base'],

  'author': "Adeel Ahmad",

  'category': 'module',

  'description': """

  This is a test module of Real-Estate Management!

  Written for the Odoo Quickstart Tutorial.

  """,

  # data files always loaded at installation

  'data': [
    
    'security/ir.model.access.csv',
    'views/property.xml',
    'views/menu.xml',
    'views/propertytype.xml',
    'views/buyer.xml',
    'views/saleman.xml'
   

  ],

  'installable': True,

  'auto_install': True,

  'application': True,

}