from odoo import models ,fields

class Specialist(models.Model):
    _name='specialist_user'
    _description='Usuarios especialistas'
    
    description_specialist = fields.Text(string="Description Specialist") 
    