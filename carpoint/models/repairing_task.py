# -*- coding: utf-8 -*-

from odoo import models,fields,api

class repairingTask(models.Model):
    _name = "carpoint.repairing.task"
    _description = "Carpoint Repairing Description"
    _inherit = ['mail.thread','mail.activity.mixin']

    seq_name = fields.Char(string='Task Reference', required=True,readonly=True, default=lambda self: ('New'))
    task_user_id = fields.Many2one("carpoint.users",required=True)
    repairing_category = fields.Selection(selection=[
        ('servicing','General Servicing'),
        ('engine','Engine Repairing'),
        ('transmission','Transmission Repairing'),
        ('gearbox','Gearbox Repairing'),
        ('exhaust','Exhaust Repairing'),
        ('wheels','Wheels Work'),
        ])
    repairing_desc = fields.Text(string="Description")
    repairing_car = fields.Char(string="Car Name")
    repairing_car_brand = fields.Char(string="Car Brand")
    repairing_car_noplate = fields.Char()
    repairing_date = fields.Date()
    repairing_status = fields.Selection(
        selection=[
            ('new','New'),
            ('in_progress','In Progress'),
            ('done','Done'),
            ('review','Review'),
            ('close','Close')]
    )
    tags_ids=fields.Many2many("carpoint.repairing.tags","repairing_task_id")

    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('carpoint.rental.task')
        return super(repairingTask,self).create(vals)
    
