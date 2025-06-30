from odoo import fields, models, api , _

class ClinicalHistory(models.Model):
    _name="clinical_history"
    _description="model to save history pacient information"

    patient_id = fields.Many2one(
        'patient',
        string="Historial del Paciente",

    )

    questionnarie_id = fields.Many2one(
        'initial_questionnarie',
        string='Cuestionario del Paciente',
    )

    session_id = fields.Many2one(
        'sessions.fupagua',
        string='Sessiones del Paciente',
    )
    