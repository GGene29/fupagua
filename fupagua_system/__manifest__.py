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
        "security/ir_groups_views.xml",
        "security/ir.model.access.csv",
        # Access
        "security/receptionist/ir.model.access.csv",
        "security/specialist/ir.model.access.csv",
        # Data
        "data/specializations_views.xml",
        "data/pregnancy_complication_views.xml",
        "data/habits_pregnancy_data_views.xml",
        "data/birth_complications_data_views.xml",
        # Views
        "views/area_specialization_view.xml",
        "views/res_partner_views.xml",
        "views/patient_view.xml",
        "views/initial_questionnarie_view.xml",
        "views/sessions_views.xml",
        "views/services_views.xml",
        "views/complication_pregnancy_view.xml",
        "views/habits_pregnancy_view.xml",
        "views/birth_complications_view.xml",
        "views/illnesses_types_view.xml",
        "views/test_session_views.xml",
        "views/ir_menu_views.xml",
    ],
    'installable': True,
    
}