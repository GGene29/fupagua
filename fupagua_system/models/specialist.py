from odoo import models ,fields

class Specialist(models.Model):
    _name='specialist_user'
    _description='Usuarios especialistas'
    
    name = fields.Char(string="Name")
    
    phone = fields.Integer(string="Phone")
    
    description_specialist = fields.Text(string="Description Specialist") 
    
    # service = fields.Char = fields.Select(string="Select Service")
    
    email = fields.Char(string="email")
    
    photo = fields.Binary(string="Photo")
    
    area_specialization_id = fields.Many2one('area_specialization' , 'Area de Specialización')
    
    