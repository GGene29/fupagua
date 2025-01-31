from odoo import models ,fields

class Specialization(models.Model):
    _name= 'area_specialization'
    _description='Para cargar las areas de especialización'
    _rec_name="area_name"
    
    stage_area = fields.Char(string='Stage', required="1")
    
    area_name = fields.Char(string='Area of Specialization', required="1")