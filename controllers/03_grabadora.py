# coding: utf8
def index1(): 
    
    camposGrabadora = [

    # campos Grabadora

    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.
    
    #Datos para localizar un sitio único y asociarle la grabadora a éste.

    SELECT(_name='conglomerado_muestra_id',
        requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
    SELECT(_name='sitio_muestra_id',
        requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
    
    #Datos de la grabadora
    SELECT(_name='nombre',
        requires=IS_IN_DB(db,db.Cat_nombre_grabadora.nombre,'%(nombre)s')),
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

    #Datos de la grabadora
    SELECT(_name='elipsoide',
        requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),

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
    
    ]

    formaGrabadora = FORM(*camposGrabadora)

    if formaGrabadora.accepts(request.vars,formname='formaGrabadoraHTML'):
    
        ################Procesando la grabadora#################################
    
        #Filtrando los datos correspondientes a la tabla de la grabadora:
        datosGrabadora = db.Grabadora._filter_fields(formaGrabadora.vars)
                
        #Guardando el registro de la grabadora en la base de datos:
        
        grabadoraInsertada = db.Grabadora.insert(**datosGrabadora)
        
        ################Procesando la imagen de referencia grabadora#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRef = db.Imagen_referencia_grabadora.archivo.store(
            formaGrabadora.vars.imagen_grabadora.file,formaGrabadora.vars.imagen_grabadora.filename)
        
        #Creando los campos de la tabla Imagen_referencia_grabadora:
        
        datosImagenRef = {}
        datosImagenRef['grabadora_id'] = grabadoraInsertada
        datosImagenRef['archivo'] = imagenRef
        datosImagenRef['archivo_nombre_original'] = formaGrabadora.vars.imagen_grabadora.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_grabadora.insert(**datosImagenRef)

        ################Procesando la imagen de referencia micrófonos#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRefMicro = db.Imagen_referencia_microfonos.archivo.store(
            formaGrabadora.vars.imagen_microfonos.file,formaGrabadora.vars.imagen_microfonos.filename)
        
        #Creando los campos de la tabla Archivo_referencia_grabadora:
        
        datosImagenRefMicro = {}
        datosImagenRefMicro['grabadora_id'] = grabadoraInsertada
        datosImagenRefMicro['archivo'] = imagenRefMicro
        datosImagenRefMicro['archivo_nombre_original'] = formaGrabadora.vars.imagen_microfonos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_microfonos.insert(**datosImagenRefMicro)

        ################Procesando el archivo de metadatos#################################
        
        #Guardando el archivo de metadatos en la carpeta adecuada
        archivoMeta = db.Archivo_referencia_grabadora.archivo.store(
            formaGrabadora.vars.archivo_metadatos.file,formaGrabadora.vars.archivo_metadatos.filename)
        
        #Creando los campos de la tabla Imagen_referencia_microfonos:
        
        datosArchivoRef = {}
        datosArchivoRef['grabadora_id'] = grabadoraInsertada
        datosArchivoRef['archivo'] = archivoMeta
        datosArchivoRef['archivo_nombre_original'] = formaGrabadora.vars.archivo_metadatos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Archivo_referencia_grabadora.insert(**datosArchivoRef)
            
        response.flash = 'Éxito'
        
    elif formaGrabadora.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los datos de la grabadora'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando las combobox de nombre y elipsoide:

    listaNombreGrabadora = db(db.Cat_nombre_grabadora).select(db.Cat_nombre_grabadora.nombre)

    listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaNombreGrabadora=listaNombreGrabadora,\
        listaElipsoide=listaElipsoide)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de sitio a partir de los sitios existentes de un conglomerado seleccionado.

def asignarSitios():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='tabla_sitio_muestra_id'>"

    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)

def grabadoraExistente():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Grabadora con la información anterior:

    grabadoraYaInsertada=db(db.Grabadora.sitio_muestra_id==sitioElegidoID).select()

    #regresa la longitud de grabadoraYaInsertada para que sea interpretada por JS

    return len(grabadoraYaInsertada)

# AQUÍ SURGE UNA CUESTIÓN: PARA PODER VALIDAR LA UNICIDAD DE LA CÁMARA,
# NECESITAMOS UN TRIGGER "ON CHANGE". SIN EMBARGO, PARA PODER HACER ESTO BIEN
# REQUERIMOS INCLUIR UN ESPACIO EN BLANCO POR DEFAULT EN LAS COMBOBOX GENERADAS
# MEDIANTE AJAX, CON LO QUE SURGE LA CUESTIÓN DE VALIDARLAS, Y NECESITAMOS UNA
# FUNCIÓN DE JQUERY DISTINTA PARA PODER PEGARLES A LOS ELEMENTOS QUE NO EXISTEN
# DESDE UN PRINCIPIO.

def index2():

    camposArchivosGrabadora = [

        #Localización de la grabadora. Por medio del conglomerado y sitio debe ser
        #posible localizar a lo más una grabadora.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='grabadora_id',
            requires=IS_IN_DB(db,db.grabadora.id,'%(nombre)s')),

        #Elegir si se están introduciendo archivos audiblles o ultrasónicos

        INPUT(_name='es_audible_ultrasonico',_type='string',requires=IS_NOT_EMPTY()),

        ###########Archivos de la grabadora###########
        INPUT(_name='archivos_grabadora',_type='file',requires=IS_NOT_EMPTY(),
            _multiple=True)

    ]

    formaArchivosGrabadora = FORM(*camposArchivosGrabadora)

    if formaArchivosGrabadora.accepts(request.vars,formname='formaArchivosGrabadoraHTML'):

        #Revisando si los archivos subidos son audibles/ultrasónicos, mediante la
        #selección del usuario:

        if (formaArchivosGrabadora.vars['es_audible_ultrasonico']=='audible'):

            esAudible=True

        else:

            esAudible=False

    ################Procesando los archivos múltiples###########################
        
        archivos = formaArchivosGrabadora.vars['archivos_grabadora']

        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:

            #Guardando el archivo en la carpeta adecuada
            archivoGrabadora = db.Archivo_grabadora.archivo.store(aux, aux.filename)
            
            datosArchivoGrabadora = {}
            datosGrabadora['es_audible']= esAudible
            datosArchivoGrabadora['grabadora_id'] = formaArchivosGrabadora.vars['grabadora_id']
            datosArchivoGrabadora['archivo'] = archivoGrabadora
            datosArchivoGrabadora['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_grabadora.insert(**datosArchivoGrabadora)

        response.flash = 'Éxito'
        
    elif formaGrabadora.errors:

       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los archivos asociados a una grabadora'

    ##########Enviando la información de la dropdown de conglomerado############

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

def asignarGrabadora():

    # El campo conglomerado_muestra_id es únicamente auxiliar y se utiliza para:
    # 1. Mediante AJAX, buscar los sitios asociados a un conglomerado.
    # 2. Utilizando dichos sitios, buscar en la lista de grabadora,
    # para ver en cuáles de dichos sitios existe una grabadora declarada. Mostrar
    # en la vista los sitios, pero enviar al controlador los id's de las grabadoras
    # asociadas a cada sitio.

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Bandera que indica si se encontró alguna grabadora declarada en alguno de
    #los sitios del conglomerado elegido:

    flag = False

    #Creando la dropdown de sitios/grabadoras y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='grabadora_id' id='tabla_grabadora_id'>"
    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        #Buscando, de entre los sitios de un conglomerado, en cuáles ha sido
        #declarada una grabadora. En caso de que no ocurra para ningún sitio,
        #se enviará un mensaje (para ello se utiliza la bandera).

        grabadoraSitio = db(db.Grabadora.sitio_muestra_id==sitio.id).select(
            db.Grabadora.id).first()

        if len(grabadoraSitio)>1:

            flag = True

            #Como cuidamos que exista a lo más una grabadora por sitio de un conglome-
            #rado, al elegir el conglomerado y el número de sitio, automática-
            #mente sabemos la grabadora a la que corresponde, sin embargo, para el
            #usuario mandamos el número de sitio del conglomerado elegido,
            #mientras que para el controlador enviamos el id de dicha grabadora.

            dropdownHTML += "<option value='" + str(grabadoraSitio.id) + "'>"+\
            sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    #Finalmente, si flag=false, en lugar de enviar la dropdown, enviamos un mensaje
    #de que no hay grabadoras declaradas en dicho conglomerado:

    if not flag:

        dropdownHTML = "<p id='tabla_grabadora_id'> Favor de registrar una grabadora para este conglomerado.</p>"
    
    return XML(dropdownHTML)



