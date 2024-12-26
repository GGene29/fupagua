from odoo import models,fields

class ResPartner(models.Model):
    # Heredamos el modelo partner
    _inherit = 'res.partner'
    
    # Descripcion
    description_specialist = fields.Text(string="Description Specialist")
    # Area de especializacion
    area_specialization_id = fields.Many2one(
        'area_specialization' , 
        'Area de Specialización'
    )

    service_ids = fields.Many2many('services', string="Services")