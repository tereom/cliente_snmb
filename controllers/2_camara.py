

# coding: utf8
def index(): 

    Campos_pestana_2 = [
        # campos Camara
    # Posteriormente habrá dropdowns en cascada para los campos de conglomerado y sitio,
    # para abordar el caso en el que los sitios de un conglomerado puedan no existir.
    
    #Datos para localizar un sitio único y asociarle la cámara a éste.
    #Estos datos deben ser una llave del sitio.
        #SELECT(_name='conglomerado_muestra_id',
        #    requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_numero',
            requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')),
    
    # #Datos de la cámara
    #     INPUT(_name='distancia_centro',_type='double', 
    #         requires=IS_NOT_EMPTY()),           
    #     INPUT(_name='fecha_inicio',_type='date',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='fecha_termino',_type='date',requires=IS_NOT_EMPTY()),    
    #     INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='llovio',_type='boolean'),
        
    #     INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
    #     INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
    #     SELECT(_name='elipsoide',
    #         requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),          

    #     SELECT(_name='nombre',
    #         requires=IS_IN_DB(db,db.Cat_nombre_camara.id,'%(nombre)s')),
    #     SELECT(_name='resolucion',
    #         requires=IS_IN_DB(db,db.Cat_resolucion_camara.id,'%(nombre)s')),
    #     SELECT(_name='sensibilidad',
    #         requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.id,'%(nombre)s')),

        TEXTAREA(_name='comentario',_type='text')    

        ###########Imagen############
        #INPUT(_name='imagen_camara',_type='file',requires=IS_NOT_EMPTY())
    ]

    forma = FORM(*Campos_pestana_2)

    if forma.accepts(request.vars,formname='prueba'):
        response.flash = 'Thanks! The form has been submitted.'
        formaCamara = db.Camara._filter_fields(request.vars)
        camaraInsertada = db.Camara.insert(**formaCamara)
        
    elif forma.errors:
       response.flash = 'Please correct the error(s).'

    return dict()
>>>>>>> 7b565abddbea63a416bbed339a02a75bb7be0f73
