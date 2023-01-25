# -*- coding: utf-8 -*-

from odoo import models,fields

class repairingTask(models.Model):
    _name = "carpoint.repairing.task"
    _description = "Carpoint Repairing Description"
    _inherit = ['mail.thread','mail.activity.mixin']

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
    
