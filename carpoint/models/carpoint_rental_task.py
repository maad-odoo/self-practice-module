# -*- coding: utf-8 -*-

from odoo import models, fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


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
    fuel_price = fields.Float(string="Today's Fuel Price:",required=True)
    total_price = fields.Float(compute="compute_total_price",default=0,store=True)
    validity=fields.Integer(string="Duration",tracking=True,required=True)
    car_avg_milage = fields.Integer(related="car_name_id.car_avg_milage")
    total_distance = fields.Integer(string="Total Distance: ",required=True)
    car_transmission = fields.Selection(related="car_name_id.car_transmission")
    car_category = fields.Selection(related="car_name_id.car_category")
    car_seating = fields.Selection(related="car_name_id.car_seating")
    car_fuel = fields.Selection(related="car_name_id.car_fuel")
    mode=fields.Selection(selection=[('with_driver','With Driver'),('self_driver','Self Driving')],tracking=True,required=True,default="self_driver")
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('close','Close')],default='new',tracking=True)
    tags_ids=fields.Many2many("carpoint.tags",string="Tags")
    task_user_id = fields.Many2one('carpoint.users',required=True,tracking=True)
    car_name_id = fields.Many2one("carpoint.cars.rental",string="Car Name",required=True,domain=[('state','in',['vacant'])])
    driver_id = fields.Many2one("rental.driver",string="Driver",domain=[('driver_status','in',['off_trip'])])

    @api.depends('state','car_name_id.state','driver_id.driver_status')
    def action_to_in_progress(self):
        for record in self:
            record.state ='inprogress'
            self.car_name_id.state = 'on_road'
            if record.mode == 'with_driver':
                self.driver_id.driver_status = 'on_trip'
    
    @api.depends('state','car_namr_id.state','driver_id.driver_status')
    def action_to_close(self):
        for record in self:
            record.state ='close'
            self.car_name_id.state = 'vacant'
            if record.mode == 'with_driver':
                self.driver_id.driver_status = 'off_trip'
    
    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('carpoint.rental.task')
        # if self.env['carpoint.rental.task'].browse(vals['state']) = 'new'
        #     print("Hello")
        return super(carpointUser,self).create(vals)

    @api.depends('fuel_price')
    def compute_total_price(self):
        for record in self:
            if(record.total_distance == 0):
                raise ValidationError("Fill the Total Distance")
            if(record.car_avg_milage == 0):
                raise ValidationError("Please select a car name")
            fuel_cost = (record.total_distance/record.car_avg_milage*record.fuel_price)
            if record.validity==0:
                if record.mode == 'withdriver':
                    self.total_price = eval('2.4*fuel_cost+400')
                else:
                    self.total_price = eval('2.0*fuel_cost+400')
            else:
                if record.mode == 'withdriver':
                    self.total_price = eval('2.4*fuel_cost+1.4*fuel_cost+record.validity*800')
                else:
                    self.total_price = eval('2.0*fuel_cost+1.4*fuel_cost+record.validity*400')
     
    @api.depends('validity','task_end')
    def compute_deadline(self):
        for record in self:
            record.task_end= record.task_DOS + relativedelta(days=record.validity)
    
    def inverse_deadline(self):
        for record in self:
            record.validity = (record.task_end - record.task_DOS).days

    @api.constrains('validity')
    def _check_constrains_SP(self):
        for record in self:
            if record.validity > 10 : 
                raise ValidationError("A trip cannot be greater than 10 days.")


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
