from odoo import models, fields

class Questionnarie(models.Model):
    _name= 'initial_questionnarie'
    _description = 'Cuestionario Inicial es lo mazimo para poder compartir '
    
    registration_code = fields.Char(string="Code")
    
    registration_date = fields.Date(string='Date')
    
    names = fields.Char(string='Names')
    
    lastname = fields.Char(string='Lastname')
    
    identification = fields.Integer(string="CI")
    
    # nationality = fields.Select()
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    place_of_birth = fields.Char(string='Plance of birthday')
    
    age = fields.Integer(string='Age')
    
    # sex = fields.Select()
    
    # schooling = fields.Select()
    
    institution = fields.Char(string='Institution')
    
    address = fields.Char(string='Address')
    
    phone = fields.Char(string="Phone")
    
    provider_by = fields.Char(string='Data Provider By')
    
    relationship = fields.Char(string='Kinship relationship with the evaluated')
    