from odoo import models,fields,api

class TestSession(models.Model):
    _name = 'test.session'
    _description = 'Item de preguntas para las sesiones'

    # consulta_id = fields.Many2one('patient', string='Consulta', ondelete='cascade')
    paso = fields.Char(string='Paso')
    secuencia = fields.Char(string='Orden')
    pregunta = fields.Text(string='Pregunta')
    respuesta = fields.Boolean(string='Respuesta (Sí/No)')
    session_ids = fields.Many2one('sessions.fupagua', string='Sesion')
    
    area_id = fields.Many2one(
        'area_specialization', 
        string='Área/Sección', 
        help="Área temática a la que pertenece esta pregunta"
    )
    
