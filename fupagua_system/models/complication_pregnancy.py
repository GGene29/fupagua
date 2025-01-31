from odoo import models, fields

class ComplicationPregnancy(models.Model):
    _name = 'complication_pregnancy'
    _description = 'Complications presented during the pregnancy process'
    _rec_name = 'name'
    
    name = fields.Char(string="Complication Pregnancy", required="1")
    
    pregnancy_period = fields.Integer(string="Pregnancy Period")