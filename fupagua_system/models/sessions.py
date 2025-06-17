from odoo import fields, models

class Sessions(models.Model):
    _name="sessions.fupagua"
    _description="model to save session information"
    _rec_name="initial_questionnarie_id"

    date = fields.Date(
        string="Session Date"
    )

    initial_questionnarie_id = fields.Many2one(
        'initial_questionnarie',
        string='Initial Questionnarie',
        required=True
    )

    specialist_id = fields.Many2one(
        'res.users',
        string='specialist',
    )

    # test_id = fields.Many2one('test.session' , string="Preguntas")
    # TODO: Add many2one field about clinical history
    test_ids = fields.One2many('test.session', 'session_ids' , string="Preguntas")