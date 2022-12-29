# -*- coding: utf-8 -*-

from odoo import api,models, fields

class seqtest(models.Model):
    _name="seq.test"

    reference_no = fields.Char(string='Order Reference', required=True,readonly=True, default=lambda self: ('100'))
    name = fields.Char('Name')


@api.model
def create(self, vals):
   if vals.get('reference_no', ('001')) == ('001'):
       vals['reference_no'] = self.env['ir.sequence'].next_by_code(
           'seq.test') or ('New')
   res = super(test_seq, self).create(vals)
   return res