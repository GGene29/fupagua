from odoo import fields, models, api , _

class ClinicalHistory(models.Model):
    _name="clinical_history"
    _description="model to save history pacient information"

    code_history = fields.Char(string="Código de Historia")
    
    patient_id = fields.Many2one(
        'patient',
        string="Historial del Paciente",

    )

    questionnarie_id = fields.Many2one(
        'initial_questionnarie',
        string='Cuestionario del Paciente',
    )

    session_ids = fields.One2many(
        'sessions.fupagua', 'history_ids',
        string='Sesiones del Paciente',
    )

    