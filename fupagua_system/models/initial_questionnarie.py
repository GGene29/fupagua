from odoo import models, fields, api
from datetime import date
# from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Questionnarie(models.Model):
    _name= 'initial_questionnarie'
    _description = 'Cuestionario Inicial realizado al paciente'
    _rec_name = 'patient_id'
    _inherits = {'patient' : 'patient_id'}
    
    patient_id = fields.Many2one('patient', string='Patient')
    
    registration_code = fields.Char(string='Code History', required='1')
        
    # Datos Personales
    
    identification = fields.Integer(string='CI')
    
    nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='')
    
    place_of_birth = fields.Char(string='Plance of birthday')
        
    schooling = fields.Selection([
        ('0', 'Inicial'),
        ('1', 'Primaria'),
        ('2', 'Media')], string='Schooling')
    
    institution = fields.Char(string='Institution')
    
    origins = fields.Char(string='Origins')
    
    address = fields.Char(string='Address')
    
    provider_by = fields.Char(string='Data Provider By')
    
    relationship = fields.Char(string='Kinship relationship with the evaluated')
    
    # Parte II Motivo Consulta
    
    referred = fields.Char(string='Referred by') 
    
    interview_date = fields.Date(string='Fecha de la entrevista')
    
    evaluation_reason = fields.Text(string='evaluation_reason')
    
    age_difference = fields.Integer(string='Difference Age')
    
    difference_description = fields.Text(string='Difference Text')
    
    diagnosis_examination = fields.Text(string='Diagnosis or Examination')
    
    treatment_evolution = fields.Text(string='Treatment and evoluction')
    
    # Parte III Familiar
    
    biological_parents_charge = fields.Boolean(string='biological parents in charge', default=True)
    
    mother_name = fields.Char(string='Mother Name')
    
    mother_age = fields.Integer(string='Mother age')
    
    mother_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    mother_nif = fields.Integer(string='Mother NIF')
    
    mother_educational = fields.Char(string='Mother Educational Level')
    
    mother_occupation = fields.Char(string='Mother Occupation')
    
    mother_work = fields.Char(string='Mother Work Schedule')
    
    mother_salary = fields.Integer(string='Mother Salary')
    
    mother_support = fields.Text(string='Support')
    
    mother_status = fields.Char(string='Marital Status')
    
    mother_phone = fields.Integer(string='Phone')
    
    mother_address = fields.Char(string='Addres Mother')
    
    mother_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_mother = fields.Text(string='opinion_behavior_mother')
    
    father_name = fields.Char(string='father Name')
    
    father_age = fields.Integer(string='father age')
    
    father_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    father_nif = fields.Integer(string='father NIF')
    
    father_educational = fields.Char(string='father Educational Level')
    
    father_occupation = fields.Char(string='father Occupation')
    
    father_work = fields.Char(string='father Work Schedule')
    
    father_salary = fields.Integer(string='father Salary')
    
    father_support = fields.Text(string='Support')
    
    father_status = fields.Char(string='Marital Status')
    
    father_phone = fields.Integer(string='Phone')
    
    father_address = fields.Char(string='Addres father')
    
    father_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_father = fields.Text(string='opinion_behavior_father')
    
    family_dynamics = fields.Text(string='Family Dynamics')
    
    family_relationship = fields.Text(string='Family relationship')
    
    caragiver = fields.Selection([
        ('1' , 'Mother'),
        ('2', 'Father'),
        ('3', 'Other')], 
        string='Caraviger')
    
    name_caragiver = fields.Char(string='Full name caragiver')
    
    caragiver_age = fields.Integer(string='Caragiver age')
    
    caragiver_nationality = fields.Selection([
        ('1', 'Venezolano'),
        ('2', 'Extranjero')], string='Nationality', default='1', required='1')
    
    caragiver_id = fields.Integer(string='Caragiver ID')
    
    caragiver_educational = fields.Char(string='Educational')
    
    caragiver_occupation = fields.Char(string='Occupation Caragiver')
    
    caragiver_work_schedule = fields.Char(string='Work Schedule')
    
    caragiver_salary = fields.Integer(string='Salary')
    
    caragiver_support = fields.Text(string='Support Family')
    
    caragiver_status = fields.Char(string='Marital Status')
    
    caragiver_phone = fields.Integer(string='Phone')
    
    caragiver_relationship = fields.Char(string='Relationship')
    
    opinion_behavior_caragiver = fields.Text(string='opinion_behavior_father')
    
    # General Familia
    
    another_need_help = fields.Text(string='Another needs help')
    
    bioligical_condition = fields.Text(string='Bioligical parents condition')
    
    family_condition = fields.Text(string='Family Condition')
    
    adopted_child = fields.Boolean(string='Adopted', default=False)
    
    adoption_age = fields.Integer(string='Adoption process age')
    
    adoption_agreement = fields.Boolean(string='adoption agreement')
    
    knows_adopted = fields.Boolean(string='Knows he is adopted')
    
    reaction_adopted_family = fields.Char(string='Family reaction to adoption')
    
    # IV Datos Socioeconómicos
    
    type_housing = fields.Selection([
        ('0', 'house'),
        ('1','apartment'),
        ('2','farm'),
        ('3','ranch')], string='Type of Housing')
    
    describe_coexistence = fields.Text('Describe coexistence')
    
    # V Antecedentes
    
    planned_pregnancy = fields.Boolean(string='Planned Pregnancy')
    
    desired_child = fields.Boolean(string='Desired child')
        
    was_desired = fields.Text(string='Was desired')
    
    abortion_attempt = fields.Text(string='Abortion attempt')
    
    desired_child_sex = fields.Text(string='Sex of the child was desired')
    
    pregnancy_attitude = fields.Text(string='Pregnancy attitude parent')
    
    number_pregnancy = fields.Integer(string='Number of pregnancies')
    
    previous_abortion = fields.Boolean(string='Previous Abortion')
    
    type_abortion = fields.Selection(
        [('0', 'induce'),
        ('1', 'natural')], string='type abortion')
    
    abortion_observation = fields.Char(string='Observation')
    
    monitor_pregnancy = fields.Char(string="Since when did you monitor your pregnancy?")
    
    kilos_gain_pregnancy = fields.Integer(string="Kilos gain pregnancy?")
    
    pregnancy_type_complication = fields.Many2many('complication_pregnancy')
    
    period_pregnancy = fields.Text(string="Pregnancy Period")
    
    other_complication = fields.Text(string='Other')
    
    type_habits_pregnancy = fields.Many2many('habits_pregnancy')
    
    habits_others = fields.Text(string='Habits Others')
    
    # VI Nacimiento 
    
    age_mother_delivery = fields.Integer(string='Age of mother ar delivery')
    
    weeks_gestation = fields.Integer(string='Weeks of gestation')
    
    type_delivery = fields.Selection([
        ('1','Cesarea'),
        ('2','Natural')], string='Type of labor', default='2')
    
    cause_cesarean = fields.Text(string='Cause of cesarean')
    
    length_labor = fields.Char(string='Length of labor')
    
    presentation_newborn = fields.Char(string='Presentation of newborn')    
    
    forceps_required = fields.Boolean(string='Required forceps')
    
    anesthesia_required = fields.Boolean(string='Required anesthesia')
    
    birth_weigth = fields.Char(string='Borth weigth')
    
    birth_heigth = fields.Char(string='heigth')
    
    normal_breathing = fields.Char(string='Normal breathing')
    
    spontaneous_crying = fields.Char(string='Spontaneous crying')
    
    birth_complications_type = fields.Many2many('birth_complications')
    
    another_birth_complication = fields.Char(string='Another birth complication')
    
    # VII Alimentación
    
    exclusive_breatfeeding = fields.Char(string='Did the child enjoy exclusive breastfeeding?')
    
    age_combine_formula = fields.Char(string='At what age did you begin to combine breastfeeding with milk formulas')
    
    specify_formulas = fields.Text(string='Specify milk formulas')
    
    breatfeeding_discontinued = fields.Char(string='When was breastfeeding discontinued?')
    
    semisolids_which = fields.Text(string='When did you initiate semisolids and which ones did you use?')
    
    solids_which = fields.Text(string='When did you initiate solids and which ones did you use?')
    
    current_diet = fields.Text(string='What is the current diet like?')
    
    selective_foods = fields.Boolean(string='Is he/she selective about foods')
    
    specify_like_dislike = fields.Text(string='Specify which ones he/she prefers and which one he/she dislikes:')
    
    intolerance = fields.Boolean(string='Does he/she have intolerance to any food')
    
    specify_intolerance = fields.Text(string='Specify intolerance food')
    
    eats_alone = fields.Boolean(string='Eats alone')
    
    down_eats = fields.Text(string='Sits down to eat and finishes his/her meal')
    
    # VIII Desarrollo Evolutivo 
    
    # MOTOR
    
    holding_head = fields.Char(string='¿Cuándo logró el Control cefálico? - sostener la cabeza')
    
    turning_bed = fields.Char(string='¿Cuándo inició el Rolado? - voltearse en la cama ')
    
    when_did_crawling = fields.Char(string='¿Cuándo inició Gateo y cómo lo hizo?')
    
    sit_up_himself = fields.Char(string='¿Cuándo logró sentarse sólo?:')
    
    up_by_himself = fields.Char(string='A qué edad se paro solo:')
    
    walk_himself = fields.Char(string='A que edad cominó solo')
    
    defend_fall = fields.Char(string='¿Se defendió al caer? ¿Metía las manos o se pegaba en la cara?')
    
    unusually_walking = fields.Char(string='¿Hay algo raro en su manera de caminar?')
    
    grab_hability = fields.Char(string='¿Tiene habilidad para agarrar las cosas?')
    
    pick_objects = fields.Char(string='A qué edad pudo tomar objetos con ambas manos')
    
    passing_object = fields.Char(string='A qué edad comenzó a pasarse los objetos de una mano a otra')
    
    development_normal = fields.Char(string='¿Usted considera que el desarrollo motor de su hijo se dio de una manera normal o algo retrasado?')
    
    movements_persistent = fields.Char(string='¿Presenta algún movimiento persistente, tales como dar vueltas, brincar repetidamente o carreras de un lado a otro?')
    
    disorders_motor = fields.Char(string='¿Usted cree que tiene trastornos motores?')
    
    been_evaluated = fields.Char(string='¿Ha sido evaluado?')
    
    development_difficulties = fields.Char(string='¿Cuándo piensa usted que mostró por primera vez dificultades en su desarrollo motor? ')
        
# LENGUAJE
    
    start_babbling = fields.Char(string='Cuando inició el Balbuceo:')
    
    syllabifications = fields.Char(string='Cuando inició las Silabaciones:')
    
    first_words = fields.Char(string='Cuando dijo las primeras Palabras sin significado (cuales):')
    
    significant_words = fields.Char(string='Cuando dijo las primeras Palabras con significado')
    
    pronoun = fields.Char(string='Cuando inició el Uso del pronombre "YO"')
    
    simple_commands = fields.Text(string='¿Comprende órdenes simples?')
    
    sequential_commands_two = fields.Text(string='¿Comprende órdenes en secuencias de 2?')
    
    sequential_commands_three = fields.Text(string='¿Comprende órdenes en secuencias de 3?')
    
    simple_answer = fields.Text(string='¿Responde preguntas simples con un sí o un no? Explique')
    
    personal_question = fields.Text(string='¿Responde preguntas personales? Explique')
    
    complex_questions = fields.Text(string='¿Responde preguntas complejas? Explique')
    
    recognizes = fields.Text(string='Cosas que RECONOCE:')
    
    names_without_help = fields.Text(string='NOMBRA SIN AYUDA a través de señas, gestos, Claves Visuales o palabras - indique cuál utiliza y ejemplos:')
    
    communication_skills = fields.Text(string='En su COMUNICACIÓN es capaz de: - señale si lo hace con palabras, gestos o claves visuales:')
    
    pronounces_correctly = fields.Char(string='Pronuncia Corecctamente')
    
    pronounces_poorly = fields.Char(string='Con pocos errores:')
    
    pronounces_very_poorly = fields.Char(string='Con muchos errores')
    
    does_not_understand = fields.Char(string='No se entiende')
    
    omission_of_syllables = fields.Char(string='Uso de sílabas')
    
    strange_understands = fields.Char(string='¿Las personas fuera de la familia entienden perfectamente lo que pronuncia?')
    
    invented_words = fields.Text(string='¿Alguna vez ha utilizado palabras o frases que pareciera haber inventado él mismo? (b) De algún ejemplo: ')
    
    sentence_without_context = fields.Text(string='Tendencia de frases raras o repetir frase fuera de contexto')
    
    includes_verbs = fields.Text(string='¿Diariamente emplea frases que por lo menos incluyan un verbo y que sean comprendidas por otras personas?')
    
    expression = fields.Text(string='¿Existe alguna expresión que diga una y otra vez exactamente igual o insiste en que usted lo diga?(c) Si es así, que sucede si lo interrumpen o se niega a contestar.')
    
    social_participation = fields.Text(string='Cuando la gente habla, ¿él o ella participa en la conversación para ser amistoso o sociable o sólo interviene para obtener o saber algo? ')
    
    continues_conversation = fields.Text(string='¿Es capaz de continuar el hilo de la conversación? (b) ¿Sus conversaciones tienen intereses variados o las utiliza en diferentes contextos? ')
    
    interests = fields.Text(string='¿En algún momento le muestra cosas que a ella o a él le interesan, sin ningún motivo aparte de compartir sus intereses?')
    
    expresses_tastes = fields.Text(string='¿Él o ella muestra intenciones de hacerle partícipe de lo que le gusta, sin más interés que expresar su placer?')
    
    inappropriate_questions = fields.Text(string='¿En ocasiones hace preguntas o dice cosas socialmente inadecuadas? ')
    
    normal_speech = fields.Text(string='¿Su habla tiene un volumen, ritmo y velocidad normal?')
    
    repeats_tone = fields.Text(string='¿Alguna vez repite palabras, frases u oraciones enteras en el mismo tono de voz que lo escuchó la primera vez?')
    
    spontaneous_gestures = fields.Text(string='¿Utiliza espontáneamente y de manera apropiada gestos comunes?')
    
    facial_expression = fields.Text(string='¿Muestra expresiones faciales en la interacción con otras personas?¿según la situación?')
    
    body_as_extension = fields.Text(string='¿Lo lleva de la mano, muñeca o alguna parte del cuerpo hacia un objeto que desee? (a) ¿lo hace como si la parte de su cuerpo fuese una herramienta o extensión de su propio brazo?')
    
    index_finger = fields.Text(string='Señala con el dedo índice lo que quiere o lo hace con la mano extendida:')
    
    eye_contact = fields.Text(string='Cuando señala lo que quiere ¿usa el contacto visual hacia lo que desea?')
    
    isolated_words = fields.Text(string=' Usa solo palabras aisladas:')
    
    holophrases = fields.Text(string='Usa holofrases (palabras que significan una frase completa):')
    
    phrases_meaning_verb = fields.Text(string='Cuando comenzó a utilizar frases de 2-3 palabras con sentido que incluyan un verbo')
    
    sentences = fields.Text(string='Usa oraciones:')
    
    adjectives = fields.Text(string='Usa adjetivos:')
    
    articles = fields.Text(string='Usa artículos')
    
    articles_and_nouns = fields.Text(string='Concordancia entre artículos y sustantivos:')
    
    verb_tenses = fields.Text(string='Conjuga bien los tiempos verbales')
    
    doubt_of_development = fields.Text(string='¿Qué edad tenía él o ella cuando usted se preguntó por primera vez si algo no estaba bien en el desarrollo del lenguaje, relaciones o comportamiento?')
    
    language_loss = fields.Text(string='¿Alguna vez le preocupó que su hijo o hija pudiera haber perdido el lenguaje después de haber aprendido a hablar? ¿Cuánto lenguaje había adquirido antes de perderlo? (Descríbalo)')
    
    language_impairment = fields.Text(string='¿Tuvo alguna enfermedad física en el momento en que empezó a perder el lenguaje?')
    
    lost_ability = fields.Text(string='¿Hubo alguna otra habilidad que haya perdido al mismo tiempo que sus habilidades en el lenguaje? ¿Cuáles?')
    
    recovery_time = fields.Text(string='¿Cuánto tiempo pasó hasta que empezó a recuperarlas?')
   
    #  AUDICION

    listens_well = fields.Char(string='Oye bien')
    
    noisy_toys = fields.Char(string='Juguetes sonoros')
    
    hears_airplanes = fields.Char(string='Oye aviones')
    
    hearing_assessment = fields.Char(string='Evaluaciones auditivas')
    
    hears_trucks = fields.Char(string='Oye camiones')
    
    telephone_conversation = fields.Char(string='Oye conversaciones')
    
    voices_in_other_room = fields.Char(string='Oye conversaciones telefónicas')
    
    whispered_voices = fields.Char(string='Oye voces cuchicheadas')
    
    locates_noises = fields.Char(string='Ubica los ruidos que oye')
    
    has_tinnitus = fields.Char(string='Presenta tinitus')
    
    earaches = fields.Char(string='Presenta frecuentemente dolor de oído')
    
    suppuration = fields.Char(string='Presenta frecuentemente supuración')
    
    tolerates_noise = fields.Char(string='Tolera el ruido')
    
    speech_behavior = fields.Text(string='Si usted entra en una habitación y empieza hablar sin llamarle por su nombre, ¿qué hace?')
    
    responds_to_name = fields.Char(string='Responde a su nombre')

# VISION
    
    sees_well = fields.Char(string='Ve bien:')
    
    visual_assessment = fields.Char(string='Evaluaciones de la vista')
    
    turns_head = fields.Char(string='Gira la cabeza para enfocar')
    
    looks_at_objects = fields.Char(string='Se acerca o leja para mirar')
    
    blinks_frequently = fields.Char(string='Parpadea con frecuencia')
    
    eyes_stuck_together = fields.Char(string='Amanece con los ojos pegados')
    
    shadow_play = fields.Char(string='Juega con sombras')
    
    rotating_objects = fields.Char(string='Tiene un interés particular por mirar los objetos que giran:')
    
    looks_at_it = fields.Text(string='¿Le mira directamente a la cara cuando le habla?')
    
    # HABITOS ACTIVIDADES
    
    void_control = fields.Char(string='A qué edad controló los efínteres')
    
    daytime_bladder = fields.Char(string='Vesical diurno')
    
    daytime_rectal = fields.Char(string='Rectal diurno')
    
    nighttime_bladder = fields.Char(string='Vesical nocturno')
    
    nighttime_rectal = fields.Char(string='Rectal nocturno')
    
    takes_a_nap = fields.Char(string='Duerme siesta')
    
    hours_of_nighttime_sleep = fields.Char(string='Cuantas horas duerme de noche')
    
    how_is_his_her_sleep = fields.Char(string='Cómo es su sueño')
    
    undresses = fields.Char(string='Se desarropa en la noche')
    
    grinds_teeth = fields.Char(string='Habla o cruje los dientes al dormir')
    
    insists_on_bath = fields.Char(string='Hay que insistir para que se bañe')
    
    bath_alone = fields.Char(string='Se baña solo')
    
    indicates_how_to_bathe = fields.Char(string='Requiere que le digan cómo bañarse')
    
    water_temperature = fields.Char(string='Le molesta o prefiere alguna temperatura del agua')
    
    dresses_alone = fields.Char(string='Se viste solo')
    
    chooses_clothes = fields.Char(string='Escoge su ropa')
    
    difficulty_with_clothes = fields.Char(string='Dificultad al usar alguna prenda de vestir')
    
    discomfort_with_clothes = fields.Char(string='Le molesta alguna prenda en particular')
    
    bites_nails = fields.Char(string='Se come las uñas')
    
    sucks_thumb = fields.Char(string='Chupa su dedo')
    
    uses_pacifier = fields.Char(string='Utiliza chupon')
    
    plays_with_unusual_object = fields.Char(string='Juega con algún objeto inusual')
    
    calming_blanket = fields.Char(string='Tiene alguna cobija o almohada como tranquilizante')
    
    helps_at_home = fields.Char(string='Colabora con labores del hogar voluntariamente o como parte de sus obligaciones (cuales):')
    
    peer_interaction = fields.Char(string='¿Interactúa en el juego con iguales?')
    
    active_play = fields.Char(string='¿Juega activamente con ellos o sólo a su lado?')
    
    role_exchange = fields.Char(string='¿Puede intercambiar los roles en el juego?')
    
    curiosity_with_other_children = fields.Char(string='¿Le llama la atención lo que hacen otros niños de su edad?')
    
    approaching_child = fields.Char(string='¿Qué hace si otro niño se le acerca?')
    
    initiates_interaction = fields.Char(string='¿Inicia él la interacción?')
    
    chooses_friends = fields.Char(string='¿Escoge a sus amigos?')
    
    game_of_clues = fields.Char(string='¿Participa o participaba con adultos conocidos en juegos, de pistas, topitos o esconderse detrás de la cobija?')
    
    imitation_of_others = fields.Char(string='¿Participa en juegos de imitación con otros niños que no sean sus hermanos? ')
    
    particular_object_preference = fields.Char(string='¿Cuándo juega prefiere algún objeto o parte de un objeto en particular o lo hacen de una manera rutinaria?')
    
    interest_in_senses = fields.Char(string='¿Tiene algún interés particular en el tacto, olfato, gusto, hacia las comidas, objetos o juguetes?')
    
    imaginary_games = fields.Text(string='¿Realiza Juegos simbólicos o de imaginación? explique frecuencia')
    
    competitiveness = fields.Char(string='¿Participa en Juegos competitivos?')
    
    likes_video_games = fields.Char(string='¿Les gustan los videos juegos?')
    
    spontaneous_sharing = fields.Text(string='¿Es capaz de compartir de manera espontánea su juguete o comida? (a) ¿lo hace si se lo piden?')
    
    free_behavior = fields.Text(string='Si lo dejas hacer lo que quiere, ¿qué tipo de cosas hace?')
    
    reciprocal_act = fields.Text(string='¿Devuelve la sonrisa cuando alguien le sonríe o sonríe cuando alguien conocido se le acerca de manera recíproca?')
    
    spontaneous_when_greeting = fields.Text(string='¿Puede sonreír espontáneamente para saludar?')
    
    reaction_in_approach = fields.Text(string='¿Cómo reacciona cuando un adulto familiar o amistades se le acerca y le habla o trata de atraer su atención?')
    
    can_comfort_you = fields.Text(string='¿Trata de consolarle si usted está triste, herido o enfermo?')
    
    interest_in_body_part = fields.Text(string='Interés peculiar, raro e inusual en su intensidad. Movimiento de mano u otra parte del cuerpo ¿Qué pasa si lo detienen?')
    
    interferes_with_movement_interest = fields.Text(string='¿Estos movimientos o este interés interfieren en las generales del día?')
    
    imitates_relatives = fields.Text(string='¿Es capaz de imitarlo imitar a otros miembros de la familia?')
    
    imitates_similar_exact = fields.Text(string='¿Lo imita de manera inmediata o lo puede hacer en otro momento?')
    
    # IX Accidentes Enfermedades
    
    have_accident = fields.Boolean(string='Have you ever had an accident?')
    
    what_type = fields.Text(string='When and what type?')
    
    needed_operation = fields.Boolean(string='Have you ever needed an operation?')
    
    type_operation = fields.Text(string='When and what type?')
    
    receiving_medication = fields.Text(string='Are you receiving any medication:')
    
    treating_physician = fields.Char(string='Treating physician')
    
    pediatrician_monitors = fields.Char(string='Pediatrician who monitors you')
    
    vaccinations = fields.Char(string='Have you had all your vaccinations:')
    
    type_have_illnesses = fields.Many2many('illnesses', string='Ha tenido alguna de las siguientes enfermedades')
    
    illnesses_specify = fields.Text(string='Indique que tan comunes son:')
    
    other_illnesses = fields.Char(string='Other illness:')
    
    concerns_health = fields.Text(string='Do you have any concerns about your son or daughters health?')
    
    # X Escolaridad Aprendizaje
    
    enter_school_age = fields.Integer(string='At what age did you enter school:')
    
    attitude_school = fields.Text(string='What was your initial attitude towards school:')
    
    repeated_school = fields.Boolean(string='Have you repeated boolean')
    
    what_grade = fields.Char(string='what grade')
    
    minimun_promoted = fields.Text(string='Have you achieved the minimum objectives to be promoted to the next level:')
    
    interrumped_school = fields.Boolean(string='Have you interrupted your attendance for a long time')
    
    was_cause = fields.Text(string='what was the cause')
    
    changes_school = fields.Boolean(string='Have you changed schools')
    
    when_which = fields.Text(string='when and to which ones')
    
    performance_writing = fields.Text(string='Writing')
    
    performance_reading = fields.Text(string='Reading')

    performance_calculus = fields.Text(string='Calculus')

    performance_social_interaction = fields.Text(string='Social Interaction')

    subjects_problems = fields.Text(string='En qué materias presenta problemas:')
    
    difficult_subject = fields.Text(string='De tener dificultad en alguna asignatura, mencione a partir de que grado éstas se hicieron más notorias:')
    
    likes_subject = fields.Char(string='Cuáles son las materias que más le gusta:')
    
    learning_home = fields.Text(string='Cómo se enfrenta a los procesos de enseñanza-aprendizaje en casa:')
    
    face_homework = fields.Text(string='Cómo se enfrenta a las tareas y que estrategias tiene para realizarlas:')
    
    time_homrework = fields.Text(string='A qué horas acostumbra realizar las tareas y en donde:')
    
    what_motivate = fields.Text(string='Qué lo motiva')
    
    reaction_achievements = fields.Text(string='Cuál es su reacción ante los logros y fracasos (señale ejemplos):')
    
    excited_share = fields.Text(string='¿Cuándo algo le emociona o realiza algo que sabe que está bien, lo muestra a otras personas? (a)')
    
    part_recreational = fields.Text(string='Asiste a actividades recreativa o deportiva por iniciativa propia (cuales):')
    
    activities_frequently = fields.Text(string='¿Tiene su hijo alguna habilidad o realiza alguna actividad con frecuencia?')

    # XI Comportamiento General
    
    aggressive_family = fields.Text(string='¿En ocasiones es agresivo con sus cuidadores o miembros de la familia?')
    
    aggressive_outside_family = fields.Text(string='¿Es agresivo con personas fuera de la familia?')
    
    hurt_deliberately = fields.Text(string='¿Alguna vez se lastimó deliberadamente, por ejemplo morderse, golpearse o tirarse el cabello?')
    
    other_comments_general = fields.Text(string='Algún otro comentario:')

    @api.model
    def create(self, vals):
        code_registro = super(Questionnarie, self).create(vals)

        if code_registro.registration_code:    
            self.env['clinical_history'].create({
                'code_history': code_registro.registration_code,
                'questionnarie_id': code_registro.id
                })
        return code_registro
        