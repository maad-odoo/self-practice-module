# -*- coding: utf-8 -*-

from odoo import models, fields,api

class carpointUser(models.Model):
    _name = "carpoint.rental.task"
    _description = "Car Point Task Module"
    _inherit = ['mail.thread','mail.activity.mixin']


    # name = fields.Char(string='Order Reference', required=True,readonly=True, default=lambda self: ('100'))
    task_user = fields.Many2one('carpoint.users',required=True,tracking=True)
    # car_type = field.Many2  
    validity=fields.Integer(string="Duration",tracking=True)
    tags=fields.Many2many("carpoint.tags",string="Tags")
    task_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today())
    task_end = fields.Date()
    mode=fields.Selection(selection=[('withdriver','With Driver'),('selfdriver','Self Driving')],tracking=True)
    start_location=fields.Char()
    end_location=fields.Char()
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('close','Close')],default='new',tracking=True)
    car_name_id = fields.Many2one("carpoint.cars.rental",string="Car Name")
    car_transmission = fields.Selection(related="car_name_id.car_transmission")
    car_no_plate = fields.Char(related="car_name_id.car_no_plate")
    car_category = fields.Selection(related="car_name_id.car_category")
    car_seating = fields.Selection(related="car_name_id.car_seating")
    car_color = fields.Char(related="car_name_id.car_color")

    def action_to_in_progress(self):
        for record in self:
            record.state ='inprogress'
    
    def action_to_close(self):
        for record in self:
            record.state ='close'
    
    
    