# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",

    'summary': """
        Sencilla Lista de tareas""",

    'description': """
        Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """,

    'author': "Tu Nombre",
    'website': "https://www.tuweb.com",

    'category': 'Productivity',
    'version': '0.1',

    # Módulos necesarios para que este funcione
    'depends': ['base'],

    # Archivos que se cargan siempre
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}