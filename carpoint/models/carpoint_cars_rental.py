# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointRentalCar(models.Model):
    _name = "carpoint.cars.rental"
    _description = "Car Point User Module"

    # rentcar_uid = fields.Integer(string="Car ID:", default='increment_rental_cars_field_sequence' self: self.env['ir.sequence'].next_by_code('increment_rental_cars_field'))
    car_name = fields.Char(string="Car Name:",required=True)
    car_manuf_year = fields.Date(string="Cars Manufacturing Date:")
    car_company = fields.Char(string="Car Company:")
    car_color = fields.Char(string="Car Color:")
    car_tranmission = fields.Selection(selection=[
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
    car_seating = fields.Selection(selection=[('2','2'),('4','4'),('5','5'),('7','7'),('12','12'),('14','14')])
    car_totalkm = fields.Integer('Total KM:')
    car_availability = fields.Selection(selection=[('available','Available'),('booked','Booked'),('undermain','Under Maintainance')])
    car_engine = fields.Integer('Engine Displacement (cc):')
    car_avg_milage = fields.Integer('Average Milage:')
    car_fitness = fields.Date(string="Cars Fitness:")
    car_insurance = fields.Date(string="Insurance Date")
    car_insurance_Expirey = fields.Date(string="Insurance expirey")
    car_service = fields.Date("Latest Service Date:")
    car_next_service = fields.Date("Upcomming Service:")
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('active', 'Active'), ('inactive', 'In Active')],default='active')