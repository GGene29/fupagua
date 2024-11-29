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
        "security/ir.model.access.csv",
        "views/area_specialization_view.xml",
        "views/specialist_user_view.xml",
    ],
    'installable': True,
    
}