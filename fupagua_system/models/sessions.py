from odoo import fields, models, api

class Sessions(models.Model):
    _name="sessions.fupagua"
    _description="model to save session information"
    _rec_name="patient_id"

    date = fields.Date(
        string="Session Date"
    )

    patient_id = fields.Many2one('patient', string='Paciente')

    #initial_questionnarie_id = fields.Many2one('initial_questionnarie', string='Initial Questionnarie')

    specialist_id = fields.Many2one('res.users', string='specialist')

    test_ids = fields.One2many('test.session', 'session_ids', string="Preguntas")
    
    observaciones = fields.Text(string='Notas adicionales')

    history_ids = fields.Many2one('clinical_history', string='Relacion con Historia Clinica')
