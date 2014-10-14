# coding: utf8
def index1():

    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.

    camposEspecie=[
    
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        #El siguiente campo va a leer de radio-botones, por eso admite un string
        #(lee el valor asociado al botón seleccionado)
        INPUT(_name='dentro_fuera_conglomerado',_type='string', 
            requires=IS_NOT_EMPTY()),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora',_type='time',requires=IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='elipsoide',
            requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),          
        
        #Catálogo CONABIO
        #Debido a la forma como se maneja la inserción de datos en la base
        #(no hay ningún campo que haga referencia a la lista conabio como tal),
        #es mejor si el formulario regresa los nombres en el catálogo (en lugar
        #de los ID's):
        INPUT(_name='conabio_lista',
            requires=IS_IN_DB(db,db.Cat_conabio_invasoras.nombre,'%(nombre)s')),

        #Campos de una especie invasora
        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        SELECT(_name='numero_individuos',
         requires=IS_IN_DB(db,db.Cat_numero_individuos.nombre, '%(nombre)s')),

        TEXTAREA(_name='comentario',_type='text'),
        
        ###########Imágenes############
        INPUT(_name='archivos_invasora_extra',_type='file', _multiple=True,
            requires=IS_NOT_EMPTY())
    ]
    
    formaEspecie=FORM(*camposEspecie)

    if formaEspecie.accepts(request.vars,formname='formaEspecieHTML'):
        
        #Filtrando los datos correspondientes a la tabla de la especie invasora:
        datosEspecie = db.Especie_invasora_extra._filter_fields(
            formaEspecie.vars)

        #Asociando el valor de la variable esta_dentro_conglomerado a partir del
        #valor del control dentro_fuera_conglomerado:
        
        if (formaEspecie.vars['dentro_fuera_conglomerado'])=='dentro':
            datosEspecie['esta_dentro_conglomerado']=True
        else:
            datosEspecie['esta_dentro_conglomerado']=False

        # Revisando la selección de lista CONABIO

        selListaConabio=formaEspecie.vars['conabio_lista']

        #Si se eligió una especie invasora de la lista CONABIO, entonces se marcan
        #las casillas de:
        #nombre_en_lista
        #hay_nombre_común
        #hay_nombre_científico
        #y utilizando el valor de seleccionado se llenan los campos de:
        #nombre_comun
        #nombre_cientifico.

        if selListaConabio!='Otros':

            datosEspecie['nombre_en_lista'] = True

            #Separando el valor obtenido en mombre común y científico:
            nombre = selListaConabio.split(' - ')
            datosEspecie['nombre_cientifico'] = nombre[0]
            datosEspecie['nombre_comun'] = nombre[1]

        else:

            datosEspecie['nombre_en_lista'] = False
        #Los otros valores se obtuvieron con anterioridad, al leerlos del formulario.

        #Insertando el registro en la base de datos:

        especieInsertada = db.Especie_invasora_extra.insert(**datosEspecie)

        ################Procesando los archivos múltiples#################################
        
        archivos = formaEspecie.vars['archivos_invasora_extra']
        if not isinstance(archivos, list):
        
            archivos = [archivos]
            
        for aux in archivos:

            #Guardando el archivo en la carpeta adecuada
            archivoInvasora = db.Archivo_especie_invasora_extra.archivo.store(aux, aux.filename)
            
            datosArchivoInvasora = {}
            datosArchivoInvasora['especie_invasora_extra_id'] = especieInsertada
            datosArchivoInvasora['archivo'] = archivoInvasora
            datosArchivoInvasora['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_especie_invasora_extra.insert(**datosArchivoInvasora)
        
        response.flash = 'Éxito'
        
    elif formaEspecie.errors:
    
       response.flash = 'Hubo un error al llenar la forma de especie invasora'
       
    else:
    
        response.flash = 'Por favor, llene los campos pedidos'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando la lista CONABIO (en este caso no requerimos
    #de los ID's, como se mencionó anteriormente), la lista de número de individuos
    #y la lista de elipsoides:

    listaConabio = db(db.Cat_conabio_invasoras).select(db.Cat_conabio_invasoras.nombre)

    listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)

    listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaConabio=listaConabio,\
        listaNumIndividuos=listaNumIndividuos,\
        listaElipsoide=listaElipsoide)

def index2():

    camposHuellaExcreta=[
    
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        #El siguiente campo va a leer de radio-botones, por eso admite un string
        #(lee el valor asociado al botón seleccionado)
        INPUT(_name='dentro_fuera_conglomerado',_type='string', 
            requires=IS_NOT_EMPTY()),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora',_type='time',requires=IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='elipsoide',
            requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),          
        
        #Campos de una huella o excreta
        #El siguiente campo va a leer de radio-botones, por eso admite un string
        #(lee el valor asociado al botón seleccionado)
        INPUT(_name='es_huella_excreta',_type='string',requires=IS_NOT_EMPTY()),

        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        INPUT(_name='largo',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='ancho',_type='double',requires=IS_NOT_EMPTY()),

        TEXTAREA(_name='comentario',_type='text'),

        ###########Imágenes############
        INPUT(_name='archivos_huella_excreta_extra',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())
    ]

    formaHuellaExcreta = FORM(*camposHuellaExcreta)

    if formaHuellaExcreta.accepts(request.vars,formname='formaHuellaExcretaHTML'):
        
        #Filtrando los datos correspondientes a la tabla de huellas/excretas:
        datosHuellaExcreta = db.Huella_excreta_extra._filter_fields(
            formaHuellaExcreta.vars)

        #Asociando el valor de la variable esta_dentro_conglomerado a partir del
        #valor del control dentro_fuera_conglomerado:
        
        if (formaHuellaExcreta.vars['dentro_fuera_conglomerado'])=='dentro':
            datosHuellaExcreta['esta_dentro_conglomerado']=True
        else:
            datosHuellaExcreta['esta_dentro_conglomerado']=False

        #Asociando el valor de la variable es_huella a partir del valor del control
        #es_huella_excreta
        
        if (formaHuellaExcreta.vars['es_huella_excreta'])=='huella':
            datosHuellaExcreta['es_huella']=True
        else:
            datosHuellaExcreta['es_huella']=False

        #Guardando el registro de la huella/excreta en la base de datos:
        
        huellaExcretaInsertada = db.Huella_excreta_extra.insert(**datosHuellaExcreta)

################Procesando los archivos múltiples#################################
        
        archivos = formaHuellaExcreta.vars['archivos_huella_excreta_extra']
        
        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:

        #Guardando el archivo en la carpeta adecuada
            archivoHuellaExcreta = db.Archivo_huella_excreta_extra.archivo.store(aux,aux.filename)
            
            datosArchivoHuellaExcreta = {}
            datosArchivoHuellaExcreta['huella_excreta_extra_id'] = huellaExcretaInsertada
            datosArchivoHuellaExcreta['archivo'] = archivoHuellaExcreta
            datosArchivoHuellaExcreta['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_huella_excreta_extra.insert(**datosArchivoHuellaExcreta)
        
        response.flash = 'Éxito'
        
    elif formaHuellaExcreta.errors:

       response.flash = 'Hubo un error al llenar la forma de huella/excreta'
       
    else:

        response.flash = 'Por favor, llene los campos solicitados'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #Haciendo lo mismo con los elipsoides:

    listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaElipsoide=listaElipsoide)

def index3():

    camposEspecimenRestos=[
    
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        #El siguiente campo va a leer de radio-botones, por eso admite un string
        #(lee el valor asociado al botón seleccionado)
        INPUT(_name='dentro_fuera_conglomerado',_type='string', 
            requires=IS_NOT_EMPTY()),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora',_type='time',requires=IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='elipsoide',
            requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),          
        
        #Campos de un especimen o restos
        #El siguiente campo va a leer de radio-botones, por eso admite un string
        #(lee el valor asociado al botón seleccionado)
        INPUT(_name='es_especimen_restos',_type='string',requires=IS_NOT_EMPTY()),

        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        SELECT(_name='numero_individuos',
            requires=IS_IN_DB(db,db.Cat_numero_individuos.nombre, '%(nombre)s')),

        TEXTAREA(_name='comentario',_type='text'),

        ###########Imágenes############
        INPUT(_name='archivos_especimen_restos_extra',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())
    ]

    formaEspecimenRestos = FORM(*camposEspecimenRestos)

    if formaEspecimenRestos.accepts(request.vars,formname='formaEspecimenRestosHTML'):
        
        #Filtrando los datos correspondientes a la tabla de especimenes/restos:
        datosEspecimenRestos = db.Especimen_restos_extra._filter_fields(
            formaEspecimenRestos.vars)

        #Asociando el valor de la variable esta_dentro_conglomerado a partir del
        #valor del control dentro_fuera_conglomerado:
        
        if (formaEspecimenRestos.vars['dentro_fuera_conglomerado'])=='dentro':
            datosEspecimenRestos['esta_dentro_conglomerado']=True
        else:
            datosEspecimenRestos['esta_dentro_conglomerado']=False

        #Asociando el valor de la variable es_especimen a partir del valor del
        #control es_especimen_restos
        
        if (formaEspecimenRestos.vars['es_especimen_restos'])=='especimen':
            datosEspecimenRestos['es_especimen']=True
        else:
            datosEspecimenRestos['es_especimen']=False

        #Guardando el registro del espécimen/restos en la base de datos:
        
        especimenRestosInsertado = db.Especimen_restos_extra.insert(
            **datosEspecimenRestos)

################Procesando los archivos múltiples#################################
        
        archivos = formaEspecimenRestos.vars['archivos_especimen_restos_extra']
        
        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:

        #Guardando el archivo en la carpeta adecuada
            archivoEspecimenRestos = db.Archivo_especimen_restos_extra.archivo.store(aux,aux.filename)
            
            datosArchivoEspecimenRestos = {}
            datosArchivoEspecimenRestos['especimen_restos_extra_id'] = especimenRestosInsertado
            datosArchivoEspecimenRestos['archivo'] = archivoEspecimenRestos
            datosArchivoEspecimenRestos['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_especimen_restos_extra.insert(**datosArchivoEspecimenRestos)
        
        response.flash = 'Éxito'
        
    elif formaEspecimenRestos.errors:

       response.flash = 'Hubo un error al llenar la forma de especímen/restos'
       
    else:

        response.flash = 'Por favor, llene los campos solicitados'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #Haciendo lo mismo con los elipsoides y categorías de número de individuos:

    listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

    listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)


    return dict(listaConglomerado=listaConglomerado,\
        listaNumIndividuos=listaNumIndividuos,\
        listaElipsoide=listaElipsoide)