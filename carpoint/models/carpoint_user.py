# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointUser(models.Model):
    _name = "carpoint.user"
    _description = "Car Point User Module"

    name = fields.Char('Name',required=True)
    user_purpose = field.selection(selection=[('rental','For Renting Car'),('repair','For Car Repairing'),('modify','For Modification')])
    user_contact = field.Integer('Contact',required=True)  
    user_DOS = field.Date('Date of issue: ',default=lambda self:fields.Datetime.today())  
    user_DOC = field.Date('Date of completion:')