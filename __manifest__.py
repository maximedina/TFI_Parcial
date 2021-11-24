# -*- coding: utf-8 -*-
{
    'name': "Gestion veterinaria",

    'summary': """
        MedVet 
    """,
    'description': """
        MedVet
    """,

    'author': "Maximiliano Medina",
    'category': '',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing','base','mail','document'],

    # always loaded
    'data': [
        'views/seq.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/animal.xml',
        'views/appointment.xml',
        'views/evaluation.xml',
        'views/evaluation_stages.xml',
        'views/menu.xml',
        'reports/report.xml',
        'data/evaluation_stage.xml',
    ],
}
