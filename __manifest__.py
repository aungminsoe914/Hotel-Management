# -*- coding: utf-8 -*-
{
    'name': "Hotel Management System",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Aung Min Soe",
    'website': "https://www.sunacademy.com",

    'category': 'Uncategorized',
    'version': '0.1',

    
    'depends': ['base','mail'],

    
    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/hotel_floor_view.xml',
        'views/hotel_room_view.xml',
        'views/hotel_amenity_view.xml',
        'views/hotel_customer_view.xml',
        'views/customer_kanban_view.xml',
        'views/hotel_booking_view.xml',

        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

