# -*- coding: utf-8 -*-

from odoo import fields,models

class rentalDriver(models.Model):
    _name="carpoint.employee"
    _description="Drivers of the rented car"
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = "id desc"


    name = fields.Char(string="Name")
    role=fields.Char(string="Role")
    contact=fields.Char(string="Contact")
    doj=fields.Date(string="Date of Joining")
    yearsofexp = fields.Integer(string="Years of Experience")
    address=fields.Text(string="Address")
    status=fields.Selection(selection=[('off_trip','Off Trip'),('on_trip','On Trip'),('on_leave','On Leave')],tracking=True)
    department = fields.Selection(selection=[
        ('servicing','Servicing'),
        ('mechanics','Mechanics'),
        ('fabrication','Fabrication'),
        ('bodywork','BodyWork'),
        ('exterior','Exterior'),
        ('official','Officail'),
        ('driver','Driver'),
        ('maintainance','Maintainance')
    ],string="Department")
    
    def action_to_off_trip(self):
        for record in self:
            record.status ='off_trip'

    def action_to_on_trip(self):
        for record in self:
            record.status ='on_trip'

    def action_to_on_leave(self):
        for record in self:
            record.status ='on_leave'
