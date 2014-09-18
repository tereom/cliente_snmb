# coding: utf8

def index1():

    Campos_especie_invasora_extra=[
    
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        INPUT(_name='dentro_fuera_conglomerado',_type='string', 
            requires=IS_NOT_EMPTY()),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',
            requires = IS_DATE(format=T('%d-%m-%Y'))),
        INPUT(_name='hora',_type='time',requires = IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='elipsoide',
            requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),
        
        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        INPUT(_name='numero_individuos', _type='integer', requires=IS_NOT_EMPTY()),
        INPUT(_name='archivos_invasora',_type='file', _multiple=True, requires=IS_NOT_EMPTY())
    ]
    
    formaEspecie=FORM(*Campos_especie_invasora_extra)

    if formaEspecie.accepts(request.vars,formname='formaEspecieHTML'):
        
        #Filtrando los datos correspondientes a la tabla de la especie invasora:
        formaEspecieInvasora = db.Especie_invasora_extra._filter_fields(
            formaEspecie.vars)        
    
        formaEspecieInvasora['nombre_en_lista'] = True                
        if (formaEspecie.vars['dentro_fuera_conglomerado'])=='dentro':
            formaEspecieInvasora['esta_dentro_conglomerado']=True
        else:
            formaEspecieInvasora['esta_dentro_conglomerado']=False
        
        especieInsertada = db.Especie_invasora_extra.insert(
            **formaEspecieInvasora)

        # Añadiendo las imágenes        
        archivos = formaEspecie.vars['archivos_invasora']
        if not isinstance(archivos, list):        
            archivos = [archivos]
            
        for aux in archivos:
            archivoInvasora = db.Archivo_especie_invasora_extra.archivo.store(
                aux,aux.filename)
            
            formaArchivoInvasora = {}
            formaArchivoInvasora['especie_invasora_extra_id'] = especieInsertada
            formaArchivoInvasora['archivo'] = archivoInvasora
            formaArchivoInvasora['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_especie_invasora_extra.insert(**formaArchivoInvasora)
        
        response.flash = 'Éxito'
        
    elif formaEspecie.errors:
        response.flash = 'Hubo un error al llenar la forma'
    else:
        response.flash = 'Hubo un error al llenar la forma'
    return dict()

def index2():

    Campos_huella_excreta_extra=[
    
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        INPUT(_name='esta_dentro_conglomerado',_type='string',
            requires=IS_NOT_EMPTY()),
        INPUT(_name='tecnico',_type='string',
            requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',
            requires=IS_DATE(format=T('%d-%m-%Y'))),
        INPUT(_name='hora',_type='time',requires=IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='elipsoide', requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),
        
        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        INPUT(_name='numero_individuos',_type='integer',
            requires=IS_NOT_EMPTY()),
        INPUT(_name='archivos_invasora',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())
        ]

    formaHuella=FORM(*Campos_huella_excreta_extra)

