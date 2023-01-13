# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class settings(models.TransientModel):
    _inherit= 'res.config.settings'

    name=fields.Char(string="Name:")
