# -*- coding: utf-8 -*-

from odoo import fields,models

class tags(models.Model):
    _name = "carpoint.tags"
    _description = "Carpoint Tags Model"
    _order = "id desc"


    name = fields.Char(string="Name",required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_tag', 'unique (name)', "Tag name cannot be repeated!"),
   ]    
   