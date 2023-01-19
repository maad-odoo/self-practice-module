# -*- coding: utf-8 -*-

from odoo import models, fields,api
from dateutil.relativedelta import relativedelta

class carpointUser(models.Model):
    _name = "carpoint.rental.task"
    _description = "Car Point Task Module"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name="seq_name"
    _order = "id desc"

    seq_name = fields.Char(string='Task Reference', required=True,readonly=True, default=lambda self: ('New'))
    start_location=fields.Char()
    end_location=fields.Char()
    car_color = fields.Char(related="car_name_id.car_color")
    car_no_plate = fields.Char(related="car_name_id.car_no_plate")
    active = fields.Boolean(default=True)
    task_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today())
    task_end = fields.Date(compute="compute_deadline",inverse="inverse_deadline")
    fuel_price = fields.Float(string="Today's Fuel Price:")
    total_price = fields.Float(compute="compute_total_price",default=0)
    validity=fields.Integer(string="Duration",tracking=True)
    car_avg_milage = fields.Integer(related="car_name_id.car_avg_milage")
    total_distance = fields.Integer(string="Total Distance: ")
    car_transmission = fields.Selection(related="car_name_id.car_transmission")
    car_category = fields.Selection(related="car_name_id.car_category")
    car_seating = fields.Selection(related="car_name_id.car_seating")
    car_fuel = fields.Selection(related="car_name_id.car_fuel")
    mode=fields.Selection(selection=[('withdriver','With Driver'),('selfdriver','Self Driving')],tracking=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('close','Close')],default='new',tracking=True)
    tags=fields.Many2many("carpoint.tags",string="Tags")
    task_user = fields.Many2one('carpoint.users',required=True,tracking=True)
    car_name_id = fields.Many2one("carpoint.cars.rental",string="Car Name")

    def action_to_in_progress(self):
        for record in self:
            record.state ='inprogress'
    
    def action_to_close(self):
        for record in self:
            record.state ='close'
    
    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('carpoint.rental.task')
        return super(carpointUser,self).create(vals)

    @api.depends('fuel_price')
    def compute_total_price(self):
        for record in self:
            fuel_cost = (record.total_distance/record.car_avg_milage*record.fuel_price)
            if record.mode == 'withdriver':
                self.total_price = 2.4*fuel_cost
            else:
                self.total_price = 2.0*fuel_cost
    """ Fuel_cost = total_distance/car_milage * fuel_price
        240% consists of :
            100% Fuel Cost
            45% Drivers Fee
            35% Maintainance
            35% Profit
            15% Taxes
            10% Insurance
        200% consists of :
            100% Fuel Cost
            40% Maintainance
            35% Profit
            15% Taxes
            10% Insurance
    """ 


    
    @api.depends('validity','task_end')
    def compute_deadline(self):
        for record in self:
            record.task_end= record.task_DOS + relativedelta(days=record.validity)
    
    def inverse_deadline(self):
        for record in self:
            record.validity = (record.task_end - record.task_DOS).days