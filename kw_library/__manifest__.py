{
    'name': 'kw_library',
    'version': '15.0.1.0.0',
    'category': 'Customizations',
    'license': 'OPL-1',
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [],
    },

    'website': 'http://www.example.com',
    'author': 'Phoenix Inc.',
    # 'maintainer': 'Phoenix Inc.',  # usually same as author
    # 'support': 'Phoenix Inc.',  # current support

    'summary': """
        Short (1 phrase/line) summary of the module's purpose
    """,

    'data': [
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/book.xml',
        'views/author.xml',
    ],

    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
        'static/description/cover.png',
    ],
}
