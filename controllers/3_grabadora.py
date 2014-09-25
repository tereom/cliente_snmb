# coding: utf8


def index(): 
    Campos_pestana_3 = [

    # campos Grabadora

    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.
    
    #Datos para localizar un sitio único y asociarle la cámara a éste.
    #Estos datos deben conformar una llave del sitio.

    SELECT(_name='conglomerado_muestra_id',
        requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
    SELECT(_name='sitio_numero',
        requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')),
    
    #Datos de la grabadora
    SELECT(_name='nombre',
        requires=IS_IN_DB(db,db.Cat_nombre_grabadora.id,'%(nombre)s')),
    INPUT(_name='fecha_inicio',_type='date',requires=IS_NOT_EMPTY()),
    INPUT(_name='fecha_termino',_type='date',requires=IS_NOT_EMPTY()),    
    INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
    INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
        
    INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
    SELECT(_name='elipsoide',
        requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')),

    INPUT(_name='distancia_centro',_type='double',requires=IS_NOT_EMPTY()),           
    INPUT(_name='llovio',_type='boolean'),
    INPUT(_name='microfonos_mojados',_type='boolean'),

    TEXTAREA(_name='comentario',_type='text'),

    ###########Imagen de referencia grabadora ############
    INPUT(_name='imagen_grabadora',_type='file',requires=IS_NOT_EMPTY()),

    ###########Imagen de referencia micrófonos ############
    INPUT(_name='imagen_microfonos',_type='file',requires=IS_NOT_EMPTY()),
    
    ###########Archivo referencia grabadora ############
    INPUT(_name='archivo_metadatos',_type='file',requires=IS_NOT_EMPTY()),
    
    ###########Archivos de la grabadora###########
    INPUT(_name='archivos_audibles',_type='file',_multiple=True,
        requires=IS_NOT_EMPTY()),

    INPUT(_name='archivos_ultrasonicos',_type='file',_multiple=True,
        requires=IS_NOT_EMPTY())
    ]

    forma = FORM(*Campos_pestana_3)

    if forma.accepts(request.vars,formname='formaHTML'):
    
        ################Procesando la grabadora#################################
    
        #Filtrando los datos correspondientes a la tabla de la grabadora:
        datosGrabadora = db.Grabadora._filter_fields(forma.vars)
        
        #Utilizando la llave del sitio para encontrarlo:
        
        idConglomerado = forma.vars['conglomerado_muestra_id']
        sitioNumero = forma.vars['sitio_numero']
        
        sitioGrabadora = db((db.Sitio_muestra.conglomerado_muestra_id==idConglomerado)&
            (db.Sitio_muestra.sitio_numero==sitioNumero)).select().first()
        
        datosGrabadora['sitio_muestra_id'] = sitioGrabadora
        
        #Guardando el registro de la cámara en la base de datos:
        
        grabadoraInsertada = db.Grabadora.insert(**datosGrabadora)
        
        ################Procesando la imagen de referencia grabadora#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRef = db.Imagen_referencia_grabadora.archivo.store(
            forma.vars.imagen_grabadora.file,forma.vars.imagen_grabadora.filename)
        
        #Creando los campos de la tabla Imagen_referencia_grabadora:
        
        datosImagenRef = {}
        datosImagenRef['grabadora_id'] = grabadoraInsertada
        datosImagenRef['archivo'] = imagenRef
        datosImagenRef['archivo_nombre_original'] = forma.vars.imagen_grabadora.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_grabadora.insert(**datosImagenRef)

        ################Procesando la imagen de referencia micrófonos#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRefMicro = db.Imagen_referencia_microfonos.archivo.store(
            forma.vars.imagen_microfonos.file,forma.vars.imagen_microfonos.filename)
        
        #Creando los campos de la tabla Archivo_referencia_grabadora:
        
        datosImagenRefMicro = {}
        datosImagenRefMicro['grabadora_id'] = grabadoraInsertada
        datosImagenRefMicro['archivo'] = imagenRefMicro
        datosImagenRefMicro['archivo_nombre_original'] = forma.vars.imagen_microfonos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_microfonos.insert(**datosImagenRefMicro)

        ################Procesando el archivo de metadatos#################################
        
        #Guardando el archivo de metadatos en la carpeta adecuada
        archivoMeta = db.Archivo_referencia_grabadora.archivo.store(
            forma.vars.archivo_metadatos.file,forma.vars.archivo_metadatos.filename)
        
        #Creando los campos de la tabla Imagen_referencia_microfonos:
        
        datosArchivoRef = {}
        datosArchivoRef['grabadora_id'] = grabadoraInsertada
        datosArchivoRef['archivo'] = archivoMeta
        datosArchivoRef['archivo_nombre_original'] = forma.vars.archivo_metadatos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Archivo_referencia_grabadora.insert(**datosArchivoRef)
        
        ################Procesando los archivos audibles########################
        
        archivosAudibles = forma.vars['archivos_audibles']
        if not isinstance(archivosAudibles, list):
        
            archivosAudibles = [archivosAudibles]
            
        for aux in archivosAudibles:

            #Guardando el archivo en la carpeta adecuada
            ArchivoAudible = db.Archivo_grabadora.archivo.store(aux, aux.filename)
            
            datosArchivoAudible = {}
            datosArchivoAudible['grabadora_id'] = grabadoraInsertada
            datosArchivoAudible['archivo'] = ArchivoAudible
            datosArchivoAudible['archivo_nombre_original'] = aux.filename
            datosArchivoAudible['es_audible'] = True
        
            #Insertando el registro en la base de datos:

            db.Archivo_grabadora.insert(**datosArchivoAudible)

            ################Procesando los archivos ultrasónicos####################
        
        archivosUltrasonicos = forma.vars['archivos_ultrasonicos']
        if not isinstance(archivosUltrasonicos, list):
        
            archivosUltrasonicos = [archivosUltrasonicos]
            
        for aux in archivosUltrasonicos:
            archivoUltrasonico = db.Archivo_grabadora.archivo.store(aux, aux.filename)
            
            datosArchivoUltrasonico = {}
            datosArchivoUltrasonico['grabadora_id'] = grabadoraInsertada
            datosArchivoUltrasonico['archivo'] = archivoUltrasonico
            datosArchivoUltrasonico['archivo_nombre_original'] = aux.filename
            datosArchivoUltrasonico['es_audible'] = False
        
            #Insertando el registro en la base de datos:

            db.Archivo_grabadora.insert(**datosArchivoUltrasonico)
    
        response.flash = 'Éxito'
        
    elif forma.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los datos de la grabadora'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando las combobox de nombre y elipsoide:

    listaNombreGrabadora = db(db.Cat_nombre_grabadora).select(
        db.Cat_nombre_grabadora.id, db.Cat_nombre_grabadora.nombre)

    listaElipsoide = db(db.Cat_elipsoide).select(
        db.Cat_elipsoide.id, db.Cat_elipsoide.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaNombreGrabadora=listaNombreGrabadora,\
        listaElipsoide=listaElipsoide)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de sitio a partir de los sitios existentes de un conglomerado seleccionado.

def asignarSitios():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id
    puntoControlId = db(db.Cat_numero_sitio.nombre=='Punto de control').select().first()

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!=puntoControlId)
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_numero' id='tabla_sitio_numero'>"

    for sitio in sitiosAsignados:

        #Obteniendo el nombre asociado al numero de sitio, del catálogo correspondiente:
        nombreSitio = db(db.Cat_numero_sitio.id==sitio.sitio_numero).select().first().nombre

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + nombreSitio + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)


