# -*- coding: utf-8 -*-

from odoo import fields,models

class fuel(models.Model):
    _name="carpoint.fuel"
    _description="Carpoint Fules Model"

    date = fields.Date(string="Todays Date:",default=lambda self: fields.datetime.today(),readonly="True")
    disel = fields.Float(string="Disel:")
    petrol = fields.Float(string="Petrol:")
    cng = fields.Float(string="CNG:")