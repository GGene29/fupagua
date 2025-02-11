from odoo import models, fields

class BirthComplications(models.Model):
    _name='birth_complications'
    _description = 'complications presented at birth'
    _rec_name = 'name'

    name = fields.Char(string="Type birth complication", required="1")