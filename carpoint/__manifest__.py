# -*- coding: utf-8 -*-
{
    'name' : 'Car Point',
    'description' : 'Rental Car Module',
    'application' : True, 
    'depends': ['base', 'mail'], 
    'data' : [
        'views/menu_actions.xml',
        'views/menu_views.xml',
        'views/user_view.xml',
        'views/rental_task_view.xml',
        'views/cars_rental_view.xml',
        'views/rental_driver.xml',
        'views/tags.xml',
        'views/settings.xml',
        'security/ir.model.access.csv',    
    ],
    'demo' : [
        'demo/carpoint_user_demodata.xml',
    ]
}
