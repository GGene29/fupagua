from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Questionnarie(models.Model):
    _name= 'initial_questionnarie'
    _description = 'Cuestionario Inicial es lo mazimo para poder compartir '
    _rec_name = 'patient_id'
    _inherits = {'patient' : 'patient_id' }
    
    patient_id = fields.Many2one('patient', string='Patient')
    
    registration_code = fields.Char(string='Code History', required='1')
        
    # Datos Personales
    
    identification = fields.Integer(string='CI')
    
    nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    place_of_birth = fields.Char(string='Plance of birthday' , required='1')
        
    schooling = fields.Selection([
        ('0', 'Inicial'),
        ('1', 'Primaria'),
        ('2', 'Media')], string='Schooling')
    
    institution = fields.Char(string='Institution')
    
    origins = fields.Char(string='Origins')
    
    address = fields.Char(string='Address',required='1')
    
    provider_by = fields.Char(string='Data Provider By', required='1')
    
    relationship = fields.Char(string='Kinship relationship with the evaluated', required='1')
    
    # Parte II Motivo Consulta
    
    referred = fields.Char(string='Referred by') 
    
    evaluation_reason = fields.Text(string='evaluation_reason')
    
    age_difference = fields.Integer(string='Difference Age')
    
    difference_description = fields.Text(string='Difference Text')
    
    diagnosis_examination = fields.Text(string='Diagnosis or Examination')
    
    treatment_evolution = fields.Text(string='Treatment and evoluction')
    
    # Parte III Familiar
    
    biological_parents_charge = fields.Boolean(string='biological parents in charge', default=True)
    
    mother_name = fields.Char(string='Mother Name')
    
    mother_age = fields.Integer(string='Mother age')
    
    mother_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    mother_nif = fields.Integer(string='Mother NIF')
    
    mother_educational = fields.Char(string='Mother Educational Level')
    
    mother_occupation = fields.Char(string='Mother Occupation')
    
    mother_work = fields.Char(string='Mother Work Schedule')
    
    mother_salary = fields.Integer(string='Mother Salary')
    
    mother_support = fields.Text(string='Support')
    
    mother_status = fields.Char(string='Marital Status')
    
    mother_phone = fields.Integer(string='Phone')
    
    mother_address = fields.Char(string='Addres Mother')
    
    mother_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_mother = fields.Text(string='opinion_behavior_mother')
    
    father_name = fields.Char(string='father Name')
    
    father_age = fields.Integer(string='father age')
    
    father_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    father_nif = fields.Integer(string='father NIF')
    
    father_educational = fields.Char(string='father Educational Level')
    
    father_occupation = fields.Char(string='father Occupation')
    
    father_work = fields.Char(string='father Work Schedule')
    
    father_salary = fields.Integer(string='father Salary')
    
    father_support = fields.Text(string='Support')
    
    father_status = fields.Char(string='Marital Status')
    
    father_phone = fields.Integer(string='Phone')
    
    father_address = fields.Char(string='Addres father')
    
    father_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_father = fields.Text(string='opinion_behavior_father')
    
    family_dynamics = fields.Text(string='Family Dynamics')
    
    family_relationship = fields.Text(string='Family relationship')
    
    caragiver = fields.Selection([
        ('1' , 'Mother'),
        ('2', 'Father'),
        ('3', 'Other')], 
        string='Caraviger')
    
    name_caragiver = fields.Char(string='Full name caragiver')
    
    caragiver_age = fields.Integer(string='Caragiver age')
    
    caragiver_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    caragiver_id = fields.Integer(string='Caragiver ID')
    
    caragiver_educational = fields.Char(string='Educational')
    
    caragiver_occupation = fields.Char(string='Occupation Caragiver')
    
    caragiver_work_schedule = fields.Char(string='Work Schedule')
    
    caragiver_salary = fields.Integer(string='Salary')
    
    caragiver_support = fields.Text(string='Support Family')
    
    caragiver_status = fields.Char(string='Marital Status')
    
    caragiver_phone = fields.Integer(string='Phone')
    
    caragiver_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_caragiver = fields.Text(string='opinion_behavior_father')
    
    # General Familia
    
    another_need_help = fields.Text(string='Another needs help')
    
    bioligical_condition = fields.Text(string='Bioligical parents condition')
    
    family_condition = fields.Text(string='Family Condition')
    
    adopted_child = fields.Boolean(string='Adopted', default=False)
    
    adoption_age = fields.Integer(string='Adoption process age')
    
    adoption_agreement = fields.Boolean(string='adoption agreement')
    
    knows_adopted = fields.Boolean(string='Knows he is adopted')
    
    reaction_adopted_family = fields.Char(string='Family reaction to adoption')
    
    # IV Datos Socioeconómicos
    
    type_housing = fields.Selection([
        ('0', 'house'),
        ('1','apartment'),
        ('2','farm'),
        ('3','ranch')], string='Type of Housing')
    
    describe_coexistence = fields.Text('Describe coexistence')
    
    # V Antecedentes
    
    planned_pregnancy = fields.Boolean(string='Planned Pregnancy')
    
    desired_child = fields.Boolean(string='Desired child')
        
    was_desired = fields.Text(string='Was desired')
    
    abortion_attempt = fields.Text(string='Abortion attempt')
    
    desired_child_sex = fields.Text(string='Sex of the child was desired')
    
    pregnancy_attitude = fields.Text(string='Pregnancy attitude parent')
    
    number_pregnancy = fields.Integer(string='Number of pregnancies')
    
    previous_abortion = fields.Boolean(string='Previous Abortion')
    
    type_abortion = fields.Selection(
        [('0', 'induce'),
        ('1', 'natural')], string='type abortion')
    
    abortion_observation = fields.Char(string='Observation')
    
    monitor_pregnancy = fields.Char(string="Since when did you monitor your pregnancy?")
    
    kilos_gain_pregnancy = fields.Integer(string="Kilos gain pregnancy?")
    
    pregnancy_type_complication = fields.Many2many('complication_pregnancy')
    
    period_pregnancy = fields.Text(string="Pregnancy Period")
    
    other_complication = fields.Text(string='Other')
    
    type_habits_pregnancy = fields.Many2many('habits_pregnancy')
    
    habits_others = fields.Text(string='Habits Others')
    
    # VI Nacimiento 
    
    age_mother_delivery = fields.Integer(string='Age of mother ar delivery')
    
    weeks_gestation = fields.Integer(string='Weeks of gestation')
    
    type_delivery = fields.Selection([
        ('1','Cesarea'),
        ('2','Natural')], string='Type of labor', default='2')
    
    cause_cesarean = fields.Text(string='Cause of cesarean')
    
    length_labor = fields.Char(string='Length of labor')
    
    presentation_newborn = fields.Char(string='Presentation of newborn')    
    
    forceps_required = fields.Boolean(string='Required forceps')
    
    anesthesia_required = fields.Boolean(string='Required anesthesia')
    
    birth_weigth = fields.Char(string='Borth weigth')
    
    birth_heigth = fields.Char(string='heigth')
    
    normal_breathing = fields.Char(string='Normal breathing')
    
    spontaneous_crying = fields.Char(string='Spontaneous crying')
    
    birth_complications_type = fields.Many2many('birth_complications')
    
    another_birth_complication = fields.Char(string='Another birth complication')
    
    # VII Alimentación
    
    exclusive_breatfeeding = fields.Char(string='Did the child enjoy exclusive breastfeeding?')
    
    age_combine_formula = fields.Char(string='At what age did you begin to combine breastfeeding with milk formulas')
    
    specify_formulas = fields.Text(string='Specify milk formulas')
    
    breatfeeding_discontinued = fields.Char(string='When was breastfeeding discontinued?')
    
    semisolids_which = fields.Text(string='When did you initiate semisolids and which ones did you use?')
    
    solids_which = fields.Text(string='When did you initiate solids and which ones did you use?')
    
    current_diet = fields.Text(string='What is the current diet like?')
    
    selective_foods = fields.Boolean(string='Is he/she selective about foods')
    
    specify_like_dislike = fields.Text(string='Specify which ones he/she prefers and which one he/she dislikes:')
    
    intolerance = fields.Boolean(string='Does he/she have intolerance to any food')
    
    specify_intolerance = fields.Text(string='Specify intolerance food')
    
    eats_alone = fields.Boolean(string='Eats alone')
    
    down_eats = fields.Text(string='Sits down to eat and finishes his/her meal')
    
    # VIII Desarrollo Evolutivo 
    
    # IX Accidentes Enfermedades
    
    have_accident = fields.Boolean(string='Have you ever had an accident?')
    
    what_type = fields.Text(string='When and what type?')
    
    needed_operation = fields.Boolean(string='Have you ever needed an operation?')
    
    type_operation = fields.Text(string='When and what type?')
    
    receiving_medication = fields.Text(string='Are you receiving any medication:')
    
    treating_physician = fields.Char(string='Treating physician')
    
    pediatrician_monitors = fields.Char(string='Pediatrician who monitors you')
    
    vaccinations = fields.Char(string='Have you had all your vaccinations:')
    
    # type_have_illnesses = fields.Many2many('have_illnesses', string='Have you had any of the following illnesses, indicate if they are common')
    
    other_illnesses = fields.Char(string='Other illness:')
    
    concerns_health = fields.Text(string='Do you have any concerns about your son or daughters health?')
    
    # X Escolaridad Aprendizaje
    
    enter_school_age = fields.Integer(string='At what age did you enter school:')
    
    attitude_school = fields.Text(string='What was your initial attitude towards school:')
    
    repeated_school = fields.Boolean(string='Have you repeated boolean')
    
    what_grade = fields.Char(string='what grade')
    
    minimun_promoted = fields.Text(string='Have you achieved the minimum objectives to be promoted to the next level:')
    
    interrumped_school = fields.Boolean(string='Have you interrupted your attendance for a long time')
    
    was_cause = fields.Text(string='what was the cause')
    
    changes_school = fields.Boolean(string='Have you changed schools')
    
    when_which = fields.Text(string='when and to which ones')
    
    performance_writing = fields.Text(string='Writing')
    
    performance_reading = fields.Text(string='Reading')

    performance_calculus = fields.Text(string='Calculus')

    performance_social_interaction = fields.Text(string='Social Interaction')
    
    subjects_problems = fields.Text(string='In which subjects do you have problems:')
    
    difficult_subject = fields.Text(string='If you have difficulty in any subject, mention from which grade onwards these became more noticeable:')
    
    likes_subject = fields.Char(string='What are the subjects that you like the most:')
    
    learning_home = fields.Text(string='How do you face the teaching-learning processes at home:')
    
    face_homework = fields.Text(string='How do you face homework and what strategies do you have to do them:')
    
    time_homrework = fields.Text(string='At what time do you usually do homework and where:')
    
    what_motivate = fields.Text(string='What motivates you:')
    
    reaction_achievements = fields.Text(string='What is your reaction to achievements and failures (indicate Examples):')
    
    excited_share = fields.Text(string='When you get excited about something or do something you know is right, do you show it to other people? (a)')
    
    part_recreational = fields.Text(string='Does your child take part in recreational or sports activities on his/her own initiative (which ones):')
    
    activities_frequently = fields.Text(string='Does your child have any skills or do any activities frequently?')

    # XI Comportamiento General
    
    aggressive_family = fields.Text(string='Is he/she sometimes aggressive towards his/her caregivers or family members?')
    
    aggressive_outside_family = fields.Text(string='Is he/she aggressive towards people outside the family?')
    
    hurt_deliberately = fields.Text(string='Has he/she ever deliberately hurt himself/herself, for example by biting, hitting or pulling his/her hair?')
    
    other_comments_general = fields.Text(string='Any other comments:')
      