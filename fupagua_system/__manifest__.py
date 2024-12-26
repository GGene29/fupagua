{
    #Nombre del Módulo
    'name' : "fupagua_system",
    # Descripción del Modulo
    'description' : """ Model administrative FUPAGUA""",
    # Creador
    'author' : 'Pasantes',
    # Versionado
    'version' : '1.0.0',
    # Dependencias del módulo para el funcionamiento
    'depends' : ['base', 'contacts', 'web'],
    # Cargas
    'data' : [
        # Security
        "security/ir.model.access.csv",
        # Data
        "data/specializations_views.xml",
        # Views
        "views/area_specialization_view.xml",
        "views/res_partner_views.xml",
        "views/patient_view.xml",
        "views/initial_questionnarie_view.xml",
        "views/sessions_views.xml",
    ],
    'installable': True,
    
}