# -*- coding: utf-8 -*-

from odoo import fields,models

class repairingtags(models.Model):
    _name = "carpoint.repairing.tags"
    _description = "Carpoint Repairing Tags Model"
    _order = "id desc"


    name = fields.Char(string="Name",required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_tag', 'unique (name)', "Tag name cannot be repeated!"),
   ]    
   