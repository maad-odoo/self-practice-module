# -*- coding: utf-8 -*-

from odoo import fields

class fuel(models.Model):
    _name="carpoint.fuel"
    _description="Carpoint Fules Model"

    disel = fields.Float(string="Disel:")
    petrol = fields.Flaot(string="Petrol:")
    cng = fields.Float(string="CNG:")