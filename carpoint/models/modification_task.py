# -*- coding: utf-8 -*-

from odoo import models,fields

class modificationTask(models.Model):
    _name = "carpoint.modification.task"
    _description = "Carpoint Modifications Description"
    _inherits = {"carpoint.users":"user_id"}
    _inherit = ['mail.thread','mail.activity.mixin']


    user_id = fields.Many2one("carpoint.users",required=True,ondelete='restrict', auto_join=True, index=True)

    modification_category = fields.Selection(selection=[
        ('exterior','Exterior'),
        ('interior','Interior'),
        ('painting','Painting'),
        ('engine','Engine Mods'),
        ('trans','Transmission Upgrade'),
        ('exhaust','Exhaust Mods'),
        ('custom','Custom Mods'),
        ])
    modification_desc = fields.Text(string="Description")
    modification_car = fields.Char(string="Car Name")
    modification_car_brand = fields.Char(string="Car Brand")
    modification_car_noplate = fields.Char()
    modification_date = fields.Date()
    modification_status = fields.Selection(
        selection=[
            ('new','New'),
            ('in_progress','In Progress'),
            ('done','Done'),
            ('review','Review'),
            ('close','Close')]
    )
    
