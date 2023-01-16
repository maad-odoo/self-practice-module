# -*- coding: utf-8 -*-

from odoo import fields,models

class rentalDriver(models.Model):
    _name="rental.driver"
    _description="Drivers of the rented car"
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = "id desc"


    driver_name = fields.Char(string="Name")
    driver_add=fields.Text(string="Address")
    driver_contact=fields.Char(string="Contact")
    driver_status=fields.Selection(selection=[('off_trip','Off Trip'),('on_trip','On Trip'),('on_leave','On Leave')],tracking=True)
    driver_DOJ=fields.Date()
    

    def action_to_off_trip(self):
        for record in self:
            record.status ='off_trip'

    def action_to_on_trip(self):
        for record in self:
            record.status ='on_trip'

    def action_to_on_leave(self):
        for record in self:
            record.status ='on_leave'
