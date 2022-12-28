# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointService(models.Model):
    _name = "carpoint.rental.cars"
    _description = "CarPoint Rental Cars Model"

    car_name = fields.Text('Service Name',copy=False,required=True)
    car_type=fields.Selection(string='Select type of car..',selection=[('sedan','Sedan'),('suv','SUV'),('muv','MUV'),('compsedan','Compact Sedan'),('minibus','Mini Bus'),('sportscar','Sports Car'),('luxcar','Luxury Car')])
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('booked','Booked'), ('available','Available')],default='new')
    car_prev_client=fields.Char('Previous Client',copy=False)
    car_prev_service= fields.Date('Previous Service',default=lambda self:fields.Datetime.today())
    car_next_service = fields.Date('Next Service',default=lambda self:fields.Datetime.today())
    car_km=fields.Char('Total KMs')
    car_price=fields.Integer('Base Price of the car',required=True)



    
