# coding: utf8

def index1():

    camposPuntoConteo = [

        #Datos para localizar un sitio único.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),

        INPUT(_name='condiciones_ambientales',requires=
            IS_IN_DB(db,db.Cat_condiciones_ambientales.nombre,'%(nombre)s')),

        TEXTAREA(_name='comentario')
    ]
    
    formaPuntoConteo = FORM(*camposPuntoConteo)
    
    if formaPuntoConteo.accepts(request.vars,formname='formaPuntoConteoHTML'):

        #Filtrando los datos correspondientes a la tabla de Punto_conteo_aves:

        datosPuntoConteo = db.Punto_conteo_aves._filter_fields(formaPuntoConteo.vars)

        #Insertando el registro en la base de datos

        db.Punto_conteo_aves.insert(**datosPuntoConteo)

        response.flash = 'Éxito'

    elif formaPuntoConteo.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        
        response.flash ='Por favor, asegúrese de registrar cada punto de conteo sólo una vez'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando la combobox de condiciones ambientales:

    listaCondicionesAmbientales = db(db.Cat_condiciones_ambientales).select(
        db.Cat_condiciones_ambientales.nombre)

    return dict(listaConglomerado=listaConglomerado,
        listaCondicionesAmbientales=listaCondicionesAmbientales)

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

#AJAX para revisar que no se haya ingresado un punto de conteo en el mismo sitio con
#anterioridad.
#El AJAX se activará cuando seleccionen un conglomerado y un número de sitio.

def puntoConteoExistente():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Punto_conteo_aves con la información anterior:

    puntoConteoYaInsertado=db(db.Punto_conteo_aves.sitio_muestra_id==sitioElegidoID).select()

    #regresa la longitud de puntoConteoYaInsertado para que sea interpretada por JS

    return len(puntoConteoYaInsertado)

# AQUÍ SURGE UNA CUESTIÓN: PARA PODER VALIDAR LA UNICIDAD DE LA CÁMARA,
# NECESITAMOS UN TRIGGER "ON CHANGE". SIN EMBARGO, PARA PODER HACER ESTO BIEN
# REQUERIMOS INCLUIR UN ESPACIO EN BLANCO POR DEFAULT EN LAS COMBOBOX GENERADAS
# MEDIANTE AJAX, CON LO QUE SURGE LA CUESTIÓN DE VALIDARLAS, Y NECESITAMOS UNA
# FUNCIÓN DE JQUERY DISTINTA PARA PODER PEGARLES A LOS ELEMENTOS QUE NO EXISTEN
# DESDE UN PRINCIPIO.

def index2():

    camposConteoAve = [

        #Localización de un punto de conteo de aves. Por medio de estos datos debe
        #ser posible localizar un único punto de conteo de aves:

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='punto_conteo_aves_id',
            requires=IS_IN_DB(db,db.punto_conteo_aves.id,'%(nombre)s')),

        #Campos de una observación de aves:

        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),

        INPUT(_name='es_visual',_type='boolean'),
        INPUT(_name='es_sonora',_type='boolean'),

        INPUT(_name='numero_individuos',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='distancia_aproximada',_type='double',requires=IS_NOT_EMPTY()),

        ###########Imágenes############
        INPUT(_name='archivos_conteo_ave',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())

    ]

    formaConteoAve = FORM(*camposConteoAve)

    if formaConteoAve.accepts(request.vars,formname='formaConteoAveHTML'):    
        #Filtrando los datos correspondientes a la tabla de huellas:

        datosConteoAve = db.Conteo_ave._filter_fields(formaConteoAve.vars)        
        
        #Guardando el registro de la observación en la base de datos:
        
        conteoAveInsertado = db.Conteo_ave.insert(**datosConteoAve)

        ################Procesando los archivos múltiples#################################
        
        archivos = formaConteoAve.vars['archivos_conteo_ave']
        
        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:

            #Guardando el archivo en la carpeta adecuada
            archivoConteoAve = db.Archivo_conteo_ave.archivo.store(aux,aux.filename)
            
            datosArchivoConteoAve = {}
            datosArchivoConteoAve['conteo_ave_id'] = conteoAveInsertado
            datosArchivoConteoAve['archivo'] = archivoConteoAve
            datosArchivoConteoAve['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_conteo_ave.insert(**datosArchivoConteoAve)
        
        response.flash = 'Éxito'
        
    elif formaHuellaExcreta.errors:

       response.flash = 'Hubo un error al llenar la forma de conteo de aves'
       
    else:

        response.flash = 'Por favor, llene los campos solicitados'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    # Tabla de revisión de registros ingresados
    db.Conteo_ave.punto_conteo_aves_id.writable = False
    db.Archivo_conteo_ave.conteo_ave_id.writable =False
    grid = SQLFORM.smartgrid(db.Conteo_ave,csv=False,user_signature=False,
        create=False,searchable=False,editable=False)

    return dict(listaConglomerado=listaConglomerado,
        grid=grid)

def asignarPuntoConteo():

    # El campo conglomerado_muestra_id es únicamente auxiliar y se utiliza para:
    # 1. Mediante AJAX, buscar los sitios asociados a un conglomerado.
    # 2. Utilizando dichos sitios, buscar en la tabla de Punto_conteo_aves,
    # para ver en cuáles de dichos sitios existe una punto declarado. Mostrar
    # en la vista los sitios, pero enviar al controlador los id's de los puntos
    # de conteo asociados a cada sitio.

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Bandera que indica si se encontró algún punto de conteo declarado en alguno
    #de los sitios del conglomerado elegido:

    flag = False

    #Creando la dropdown de sitios/puntos y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='Punto_conteo_aves_id'"+\
        " id='tabla_punto_conteo_aves_id'>"
    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        #Buscando, de entre los sitios de un conglomerado, en cuáles ha sido
        #declarado un punto de conteo. En caso de que no ocurra para ningún sitio,
        #se enviará un mensaje (para ello se utiliza la bandera).

        puntoConteoSitio = db(db.Punto_conteo_aves.sitio_muestra_id==sitio.id).select(
            db.Punto_conteo_aves.id).first()

        if len(puntoConteoSitio)>1:

            flag = True

            #Como cuidamos que exista a lo más un punto por sitio de un conglome-
            #rado, al elegir el conglomerado y el número de sitio, automática-
            #mente sabemos el punto al que corresponde, sin embargo, para el
            #usuario mandamos el número de sitio del conglomerado elegido,
            #mientras que para el controlador enviamos el id de dicho punto.

            dropdownHTML += "<option value='" + str(puntoConteoSitio.id) + "'>"+\
            sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    #Finalmente, si flag=false, en lugar de enviar la dropdown, enviamos un mensaje
    #de que no hay cámaras declaradas en dicho conglomerado:

    if not flag:

        dropdownHTML = "<p id='tabla_camara_id'> Favor de registrar un punto de conteo de aves para este conglomerado.</p>"
    
    return XML(dropdownHTML)