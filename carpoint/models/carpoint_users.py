# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointUser(models.Model):
    _name = "carpoint.users"
    _description = "Car Point User Module"
    _inherit = ['mail.thread','mail.activity.mixin']


    # user_uid = fields.Integer(string="User No:", default=lambda self: self.env['ir.sequence'].next_by_code('increment_user_field'))
    name = fields.Char('Name',required=True,tracking=True)
    user_purpose = fields.Selection(selection=[('rental','For Renting Car'),('repair','For Car Repairing'),('modify','For Modification')],tracking=True)
    user_contact = fields.Integer('Contact',required=True)  
    user_address = fields.Text('Address : ',required=True)
    user_DOS = fields.Date('Date of issue: ',default=lambda self:fields.Datetime.today(),tracking=True)
    active = fields.Boolean(default=True)
    state=fields.Selection(selection=[('new', 'New'), ('on_trip', 'On Trip'),('in_active','In Active')],default='new',tracking=True)

    def action_to_on_road(self):
        for record in self:
            record.state ='on_trip'
    
    def action_to_in_active(self):
        for record in self:
            record.state ='in_active'