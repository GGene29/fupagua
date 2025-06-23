from odoo import models, fields, api
from datetime import date

class Patient(models.Model):
    _name='patient'
    _description='registro de pacientes'
    _rec_name ='name'
    
    create_patient = fields.Date(string="Date Registrion")
    
    name = fields.Char(string='Name')
    
    lastname = fields.Char(string='Lastname')
    
    date_of_birth = fields.Date(string="Date Birthday")
    
    age = fields.Integer(string='Age' , compute="_compute_age", store=True)
    
    month = fields.Integer(string='Month')
    
    phone = fields.Char(string="Phone")
    
    sex = fields.Selection( [('1', 'F'), ('2', 'M')], string="Sexo")


    current_area_specialization_id = fields.Many2one(
        'area_specialization',
        string='Current Area Specialization',
    )
    
    questionnarie = fields.One2many('initial_questionnarie', 'patient_id', string="Questionnarie")

    session_id = fields.One2many('session_fupagua', 'patient_id', string='Sesiones del paciente')
    
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        hoy = date.today()
        for record in self:
            if record.date_of_birth:
                fecha_nac = record.date_of_birth
                record.age = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            else:
                record.age = 0
    