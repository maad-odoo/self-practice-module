# -*- coding: utf-8 -*-

from odoo import models,fields

class modificationTask(models.Model):
    _name = "carpoint.modification.task"
    
    modification_user = fields.Many2one("carpoint.users",string="User")
    modification_category = fields.Selection(selection=[
        ('exterior','Exterior'),
        ('interior','Interior'),
        ('painting','Painting'),
        ('engine','Engine Mods'),
        ('trans','Transmission Upgrade'),
        ('exhaust','Exhaust Mods')
        ])
    modification_desc = fields.Text(string="Description")
    modification_car = fields.Char(string="Car Name")
    modification_car_brand = fields.Char(string="Car Brand")
    modification_car_noplate = feilds.Char()
    modification_date = fields.Date()
    modification_status = fields.Selection(
        selection=[
            ('new','New'),
            ('in_progress','In Progress'),
            ('done','Done'),
            ('review','Review'),
            ('close','Close')]
    )