from odoo import models, fields

class Questionnarie(models.Model):
    _name= 'initial_questionnarie'
    _description = 'Cuestionario Inicial es lo mazimo para poder compartir '
    _rec_name = 'names'
    
    registration_code = fields.Char(string="Code History")
    
    registration_date = fields.Date(string='Date')
    
    # Datos Personales
    
    names = fields.Char(string='Names')
    
    lastname = fields.Char(string='Lastname')
    
    identification = fields.Integer(string="CI")
    
    nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string="Nationality", default='1')
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    place_of_birth = fields.Char(string='Plance of birthday')
    
    age = fields.Integer(string='Age')
    
    sex = fields.Selection( [('1', 'F'), ('2', 'M')], string="Sexo")
    
    schooling = fields.Selection([
        ('0', 'Inicial'),
        ('1', 'Primaria'),
        ('2', 'Media')], string="Schooling")
    
    institution = fields.Char(string='Institution')
    
    address = fields.Char(string='Address')
    
    phone = fields.Char(string="Phone")
    
    provider_by = fields.Char(string='Data Provider By')
    
    relationship = fields.Char(string='Kinship relationship with the evaluated')
    
    # Parte II Motivo Consulta
    
    evaluation_reason = fields.Text(string="evaluation_reason")
    
    age_difference = fields.Integer(string="Difference Age")
    
    difference_description = fields.Text(string="Difference Text")
    
    diagnosis_examination = fields.Text(string="Diagnosis or Examination")
    
    treatment_evolution = fields.Text(string="Treatment and evoluction")
    
    # Parte III Familiar
    
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
    
    family_dynamics = fields.Text(string="Family Dynamics")
    
    family_relationship = fields.Text(string="Family relationship")
    
    caragiver = fields.Selection([
        ("1" , "Mother"),
        ("2", "Father"),
        ("3", "Other")], 
        string="Caraviger"),
    
    name_caragiver = fields.Char(string="Full name caragiver")
    
    caragiver_age = fields.Integer(string="Caragiver age")
    
    caragiver_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string="Nationality", default='1')
    
    caragiver_id = fields.Integer(string="Caragiver ID")
    
    caragiver_educational = fields.Char(string="Educational")
    
    caragiver_occupation = fields.Char(string="Occupation Caragiver")
    
    caragiver_work_schedule = fields.Char(string="Work Schedule")
    
    caragiver_salary = fields.Integer(string="Salary")
    
    caragiver_support = fields.Text(string="Support Family")
    
    caragiver_status = fields.Char(string="Marital Status")
    
    caragiver_phone = fields.Integer(string="Phone")
    
    caragiver_relationship = fields.Char(string="Relationship")
    
    opinion_behavior_caragiver = fields.Text(string="opinion_behavior_father")
    
    # General Familia
    
    another_need_help = fields.Text(string="Another needs help")
    
    bioligical_condition = fields.Text(string="Bioligical parents condition")
    
    family_condition = fields.Text(string="Family Condition")
    
    adopted_child = fields.Boolean(string="Adopted")
    
    adoption_age = fields.Integer(string="Adoption process age")
    
    adoption_agreement = fields.Boolean(string="adoption agreement")
    
    knows_adopted = fields.Boolean(string="Knows he is adopted")
    
    reaction_adopted_family = fields.Char(string="Family reaction to adoption")
    
    # IV Datos Socioeconómicos
    
    type_housing = fields.Selection([
        ('0', 'house'),
        ('1','apartment'),
        ('2','farm'),
        ('3','ranch')], string="Type of Housing")
    
    describe_coexistence = fields.Text('Describe coexistence')
    
    # V Antecedentes
    
    planned_pregnancy = fields.Boolean(string="Planned Pregnancy")
    
    desired_child = fields.Boolean(string="Desired child")
        
    was_desired = fields.Text(string="Was desired")
    
    abortion_attempt = fields.Text(string="Abortion attempt")
    
    desired_child_sex = fields.Text(string="Sex of the child was desired")
    
    pregnancy_attitude = fields.Text(string="Pregnancy attirude parent")
    
    number_pregnancy = fields.Integer(string="Number of pregnancies")
    
    previous_abortion = fields.Boolean(string="Previous Abortion")
    
    type_abortion = fields.Selection(
        [('0', 'induce'),
        ('1', 'natural')], string="type abortion")
    
    # pregnancy_type_complication = fields.Many2many('complication_pregnancy')
    
    other_complication = fields.Text(string="Other")
    
    # habits_pregnancy = fields.Many2many('habits_pregnancy')
    
    habits_others = fields.Text(string="Habits Others")
    
    # VI Nacimiento 
    
    
    