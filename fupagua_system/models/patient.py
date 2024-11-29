from odoo import models, fields

class Patient(models.Model):
    _name='patient'
    _description='registro de pacientes'
    
    # registration_code = fields.Char(string="Registration")
    create_patient = fields.Date(string="Date Registrion")
    
    name = fields.Char(string='Names')
    
    lastname = fields.Char(string='Lastname')
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    age = fields.Integer(string='Age')
    
    phone = fields.Char(string="Phone")
    
    
    
    
    
    