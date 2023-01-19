# -*- coding: utf-8 -*-
{
    'name' : 'Car Point',
    'description' : 'Rental Car Module',
    'application' : True, 
    'depends': ['base', 'mail'], 
    'data' : [
        'security/ir.model.access.csv',    
        'views/menu_actions.xml',
        'views/menu_views.xml',
        'views/user_view.xml',
        'views/rental_task_view.xml',
        'views/cars_rental_view.xml',
        'views/rental_driver.xml',
        'views/tags.xml',
        'data/sequence_data.xml',
        # 'views/settings.xml',
    ],
    'demo' : [
        'demo/carpoint_user_demodata.xml',
    ]
}
