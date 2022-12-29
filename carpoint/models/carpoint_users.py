# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointUser(models.Model):
    _name = "carpoint.users"
    _description = "Car Point User Module"

    user_uid = fields.Integer(string="User No:", default=lambda self: self.env['ir.sequence'].next_by_code('increment_user_field'))
    name = fields.Char('Name',required=True)
    user_purpose = fields.Selection(selection=[('rental','For Renting Car'),('repair','For Car Repairing'),('modify','For Modification')])
    user_contact = fields.Integer('Contact',required=True)  
    user_address = fields.Text('Address : ',required=True)
    user_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today())
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done')],default='new')
