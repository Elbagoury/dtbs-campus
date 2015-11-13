# -*- coding: utf-8 -*-
{
    'name': "Sistem Informasi Akademik",

    'summary': """
        Aplikasi Sistem Informasi Akademik""",

    'description': """
        Aplikasi untuk me-manage administrasi siswa
    """,

    'author': "DTBS",
    'website': "http://www.dtbsindo.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'School',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant','hr'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'security/security.xml',
        'templates.xml',
        'views/menu.xml',
        'views/registran.xml',
        'views/education.xml',
        'views/religion.xml',
        'views/faculty.xml',
        'views/department.xml',
        'views/study.xml',
        'views/acyear.xml',
        'views/filter.xml',
        'views/classroom.xml',
        'views/student.xml',
        'views/teacher.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
