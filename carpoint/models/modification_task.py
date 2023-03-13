# -*- coding: utf-8 -*-

from odoo import models,fields,api

class modificationTask(models.Model):
    _name = "carpoint.modification.task"
    _description = "Carpoint Modifications Description"
    _rec_name = "mod_name"
    _inherit = ['mail.thread','mail.activity.mixin']
    

    mod_name = fields.Char(string='Task Reference', required=True,readonly=True, default=lambda self: ('New'))
    task_user_id = fields.Many2one("carpoint.users",required=True)
    modification_category = fields.Selection(selection=[
        ('exterior','Exterior'),
        ('interior','Interior'),
        ('painting','Painting'),
        ('engine','Engine Mods'),
        ('trans','Transmission Upgrade'),
        ('exhaust','Exhaust Mods'),
        ('custom','Custom Mods'),
        ],string="Category")
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
    tags_ids = fields.Many2many("carpoint.modification.tags","modification_id",string="Tags")

    @api.model
    def create(self,vals):
        vals['mod_name'] = self.env['ir.sequence'].next_by_code('carpoint.modification.task')
        return super(modificationTask,self).create(vals)
    
