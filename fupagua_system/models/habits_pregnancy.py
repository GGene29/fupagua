from odoo import models, fields

class HabitsPregnancy(models.Model):
    _name = 'habits_pregnancy'
    _description = 'Bad habits during pregnancy'
    _rec_name = 'name'
    
    name = fields.Char(string="She had bad habits during pregnancy", required="1")