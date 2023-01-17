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
    task_user = fields.Many2one('carpoint.users',required=True,tracking=True)
    validity=fields.Integer(string="Duration",tracking=True)
    tags=fields.Many2many("carpoint.tags",string="Tags")
    task_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today())
    task_end = fields.Date(compute="compute_deadline",inverse="inverse_deadline")
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
    car_color = fields.Float(related="car_name_id.car_color")
    car_price = fields.Float(related="car_name_id.car_base_price")
    total_price = fields.Float(compute="compute_total_price")

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

    @api.depends('car_price','validity')
    def compute_total_price(self):
        for record in self:
            self.total_price = record.validity*record.car_price
    
    @api.depends('validity','task_end')
    def compute_deadline(self):
        for record in self:
            record.task_end= record.task_DOS + relativedelta(days=record.validity)
    
    def inverse_deadline(self):
        for record in self:
            record.validity = (record.task_end - record.task_DOS).days