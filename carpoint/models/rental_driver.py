# -*- coding: utf-8 -*-

from odoo import fields,models

class rentalDriver(models.Model):
    _name="rental.driver"
    _description="Drivers of the rented car"

    driver_name = fields.Char(string="Name")
    driver_add=fields.Text(string="Address")
    driver_contact=fields.Integer(string="Contact")
    driver_status=fields.Selection(selection=[('off_Trip','Off Trip'),('on_trip','On Trip'),('on_leave','On Leave')])
    driver_DOJ=fields.Date()
    
