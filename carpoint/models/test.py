# -*- coding: utf-8 -*-

from odoo import models,fields,api

class sequenceTest(models.Model):
    _name = "sequence.model"


    seq_name = fields.Char(string='Task Reference', required=True,readonly=True, default=lambda self: ('New'))

    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('sequence.model')
        return super(modificationTask,self).create(vals)
    
