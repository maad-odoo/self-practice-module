# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointService(models.Model):
    _name = "carpoint.service"
    _description = "Car Point Services Module"

    service_name = fields.Text('Service Name',copy=False,required=True)
    service_no = fields.Char('Service No.',required=True)
    service_type = fields.Char('Service Type',copy=False,required=True)
    service_desc = fields.Text('Service Description',required=True)
    service_DOS = fields.Date('Date of Starting',default=lambda self:fields.Datetime.today())
    service_DOC = fields.Date('Date of Completion',default=lambda self:fields.Datetime.today())
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done')],default='new')



    
