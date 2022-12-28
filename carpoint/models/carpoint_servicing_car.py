# -*- coding: utf-8 -*-

from odoo import models, fields

class carpointService(models.Model):
    _name = "carpoint.servicing.car"
    _description = "Car Point Services Module"

    car_name = fields.Text('Service Name',copy=False,required=True)
    car_service_type = fields.Selection(selection=[('repair', 'Reparing'), ('modify', 'Modification'),('other','Other')],required=True,default='repair')
    car_service_desc = fields.Text('Car Service Description',required=True)
    car_user = fields.Text('Car Owner',copy=False,required=True)
    car_service_DOS = fields.Date('Date of Starting',default=lambda self:fields.Datetime.today())
    car_service_DOC = fields.Date('Date of Completion',default=lambda self:fields.Datetime.today())
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('new', 'New'), ('inprogress', 'In Progress'),('done','Done')],default='new')



    
