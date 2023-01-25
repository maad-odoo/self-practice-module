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
        'views/modification_task.xml',
        'views/repairing_task.xml',
        'views/cars_rental_view.xml',
        'views/rental_driver.xml',
        'views/modification_tags.xml',
        'views/repairing_tags.xml',
        'views/rental_task_tags.xml',
        'data/sequence_data.xml',
    ],
    'demo' : [
        'demo/modification_tags.xml',
        'demo/rental_cars.xml',
        'demo/rental_tags.xml',
        'demo/repairing_tags.xml',
    ],
}
