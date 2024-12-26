from odoo import models, fields

class Services(models.Model):
    _name="services"
    _description="Model to store information about specialist services"
    _rec_name="name"

    name = fields.Char(
        string="Name",
        required=True
    )

    specialization_id = fields.Many2one(
        'area_specialization',
        string='specialization',
    )

