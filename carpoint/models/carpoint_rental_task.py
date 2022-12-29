# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointUser(models.Model):
    _name = "carpoint.rental.task"
    _description = "Car Point Task Module"

    task_uid = fields.Integer(string="Task No:", default=lambda self: self.env['ir.sequence'].next_by_code('increment_task_field'))
    task_user = fields.Many2many('carpoint.users',required=True)  
    task_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today())
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done')],default='new')
