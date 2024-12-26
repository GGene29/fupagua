from odoo import models, fields

class Questionnarie(models.Model):
    _name= 'initial_questionnarie'
    _description = 'Cuestionario Inicial es lo mazimo para poder compartir '
    _rec_name = 'names'
    
    registration_code = fields.Char(string="Code")
    
    registration_date = fields.Date(string='Date')
    
    names = fields.Char(string='Names')
    
    lastname = fields.Char(string='Lastname')
    
    identification = fields.Integer(string="CI")
    
    nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string="Nationality", default='1')
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    place_of_birth = fields.Char(string='Plance of birthday')
    
    age = fields.Integer(string='Age')
    
    # sex = fields.
    
    # schooling = fields.Select()
    
    institution = fields.Char(string='Institution')
    
    address = fields.Char(string='Address')
    
    phone = fields.Char(string="Phone")
    
    provider_by = fields.Char(string='Data Provider By')
    
    relationship = fields.Char(string='Kinship relationship with the evaluated')
    
    # Parte II
    
    evaluation_reason = fields.Text(string="evaluation_reason")
    
    age_difference = fields.Integer(string="Difference Age")
    
    difference_description = fields.Text(string="Difference Text")
    
    diagnosis_examination = fields.Text(string="Diagnosis or Examination")
    
    treatment_evolution = fields.Text(string="Treatment and evoluction")
    
    # Parte III
    
    mother_name = fields.Char(string="Mother Name")
    
    mother_age = fields.Integer(string="Mother age")
    
    mother_nationality = fields.Char(string="Mother Nationality")
    
    mother_nif = fields.Integer(string="Mother NIF")
    
    mother_educational = fields.Char(string="Mother Educational Level")
    
    mother_occupation = fields.Char(string="Mother Occupation")
    
    mother_work = fields.Char(string="Mother Work Schedule")
    
    mother_salary = fields.Integer(string="Mother Salary")
    
    mother_support = fields.Text(string="Support")
    
    mother_status = fields.Char(string="Marital Status")
    
    mother_phone = fields.Integer(string="Phone")
    
    mother_address = fields.Char(string="Addres Mother")
    
    mother_relationship = fields.Char(string="Relationship")
    
    opinion_behavior_mother = fields.Text(string="opinion_behavior_mother")
    
    father_name = fields.Char(string="father Name")
    
    father_age = fields.Integer(string="father age")
    
    father_nationality = fields.Char(string="father Nationality")
    
    father_nif = fields.Integer(string="father NIF")
    
    father_educational = fields.Char(string="father Educational Level")
    
    father_occupation = fields.Char(string="father Occupation")
    
    father_work = fields.Char(string="father Work Schedule")
    
    father_salary = fields.Integer(string="father Salary")
    
    father_support = fields.Text(string="Support")
    
    father_status = fields.Char(string="Marital Status")
    
    father_phone = fields.Integer(string="Phone")
    
    father_address = fields.Char(string="Addres father")
    
    father_relationship = fields.Char(string="Relationship")
    
    opinion_behavior_father = fields.Text(string="opinion_behavior_father")
    