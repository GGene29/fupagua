from odoo import models, fields

class Patient(models.Model):
    _name='patient'
    _description='registro de pacientes'
    
    create_patient = fields.Date(string="Date Registrion")
    
    name = fields.Char(string='Name')
    
    lastname = fields.Char(string='Lastname')
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    age = fields.Integer(string='Age')
    
    phone = fields.Char(string="Phone")
    
    sex = fields.Selection( [('1', 'F'), ('2', 'M')], string="Sexo")


    current_area_specialization_id = fields.Many2one(
        'area_specialization',
        string='Current Area Specialization',
    )
    
    # questionnarie = fields.One2many('initial_questionnarie', 'patient_id', string="Questionnarie")