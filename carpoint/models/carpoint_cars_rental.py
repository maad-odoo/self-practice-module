# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointRentalCar(models.Model):
    _name = "carpoint.cars.rental"
    _description = "Car Point User Module"
    _inherit = ['mail.thread','mail.activity.mixin']
    # _inherits="carpoint.fuel"
    _order = "id desc"

    name = fields.Char(string="Car Name:",required=True,tracking=True)
    car_manuf_year = fields.Date(string="Cars Manufacturing Date:")
    car_company = fields.Char(string="Car Company:")
    car_color = fields.Char(string="Car Color:")
    car_transmission = fields.Selection(selection=[
        ('AT','Automatic Transmission (AT)'),
        ('MT','Manual Transmission (MT)'),
        ('AMT','Automatic Manual Transmission'),
        ('CVT','Continously Variable Transmission (CVT)'),
        ('DCT','Dual Clutch Transmission')])
    car_category = fields.Selection(selection=[
        ('sedan','Sedan'),
        ('suv','Semi Urban Vehical (SUV)'),
        ('sportscar','Sports Car'),
        ('luxurycar','Luxury Car'),
        ('offroad','Off-Roader'),
        ('muv','Multi-Utility Vehical'),
        ('compactsedan','Comapact Sedan'),
        ('minibus','Mini Bus')])
    # car_image=fields.Image(string="Image")
    car_seating = fields.Selection(selection=[('2','2'),('4','4'),('5','5'),('7','7'),('12','12'),('14','14')])
    car_totalkm = fields.Integer('Total KM:')
    car_availability = fields.Selection(selection=[('available','Available'),('booked','Booked'),('undermain','Under Maintainance')],tracking=True)
    car_engine = fields.Integer('Engine Displacement (cc):')
    car_avg_milage = fields.Integer('Average Milage:')
    car_fitness = fields.Date(string="Cars Fitness:")
    car_insurance = fields.Date(string="Insurance Date",tracking=True)
    car_insurance_Expirey = fields.Date(string="Insurance expirey",tracking=True)
    car_service = fields.Date("Latest Service Date:",tracking=True)
    car_next_service = fields.Date("Upcomming Service:",tracking=True)
    car_no_plate = fields.Char("Number Plate:")
    car_base_price = fields.Float("Base Fair (Per KM):")
    active = fields.Boolean(default=True,tracking=True)
    state=fields.Selection(selection=[('vacant', 'Vacant'), ('on_road', 'On Road'),('on_service', 'On Service'),('in_active', 'In Active')],tracking=True)
    car_history=fields.One2many("carpoint.rental.task","car_name_id",string="Previous Activities",readonly=True)
    disel=fields.

    def action_to_vacant(self):
        for record in self:
            record.state ='vacant'
    
    def action_to_on_road(self):
        for record in self:
            record.state ='on_road'
    
    def action_to_on_service(self):
        for record in self:
            record.state ='on_service'
    
    def action_to_in_active(self):
        for record in self:
            record.state ='in_active'
