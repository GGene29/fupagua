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
        'specialist_user',
        string='specialist',
    )

    # TODO: Add many2one field about clinical history