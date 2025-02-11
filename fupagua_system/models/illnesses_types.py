from odoo import models, fields

class Illnesses(models.Model):
    _name='illnesses'
    _description = 'illnesses types'
    _rec_name = 'name'

    name = fields.Char(string="Ha tenido alguna de las siguientes enfermedades", required="1")