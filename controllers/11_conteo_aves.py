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
        db.Punto_conteo_aves.insert(**formaPuntoConteo.vars)
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

    camposAve = [

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

        INPUT(_name='numero_individuos',_type='integer',requires=IS_NOT_EMPTY),


    ]

    formaArchivosCamara = FORM(*camposArchivosCamara)

    if formaArchivosCamara.accepts(request.vars,formname='formaArchivosCamaraHTML'):

        INPUT(_name='largo',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='ancho',_type='double',requires=IS_NOT_EMPTY()),
        
        ###########Imágenes############
        INPUT(_name='archivos_huella_excreta',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())
	]

    formaHuellaExcreta = FORM(*Campos_huella_excreta)
    
    if formaHuellaExcreta.accepts(request.vars,formname='formaHuellaExcretaHTML'):

        #Filtrando los datos correspondientes a la tabla de huellas:

        datosHuellaExcreta = db.Huella_excreta._filter_fields(formaHuellaExcreta.vars)
                
        #Por medio de AJAX, estamos garantizando que cuando registran los
        #transectos sólo se registre uno de cada número para cada muestreo del
        #conglomerado.

        #También garantizamos que los transectos en la dropdown de especie
        #invasora sí estén registrados con anterioridad en el conglomerado.
        
        
        #Asociando el valor de la variable es_huella a partir del valor del control
        #es_huella_excreta
        
        if (formaHuellaExcreta.vars['es_huella_excreta'])=='huella':
            datosHuellaExcreta['es_huella']=True
        else:
            datosHuellaExcreta['es_huella']=False

        #Guardando el registro de la especie invasora en la base de datos:
        
        huellaExcretaInsertada = db.Huella_excreta.insert(**datosHuellaExcreta)

        ################Procesando los archivos múltiples#################################
        
        archivos = formaHuellaExcreta.vars['archivos_huella_excreta']
        
        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:

             #Guardando el archivo en la carpeta adecuada
            archivoHuellaExcreta = db.Archivo_huella_excreta.archivo.store(aux,aux.filename)
            
            datosArchivoHuellaExcreta = {}
            datosArchivoHuellaExcreta['huella_excreta_id'] = huellaExcretaInsertada
            datosArchivoHuellaExcreta['archivo'] = archivoHuellaExcreta
            datosArchivoHuellaExcreta['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_huella_excreta.insert(**datosArchivoHuellaExcreta)
        
        response.flash = 'Éxito'
        
    elif formaHuellaExcreta.errors:

       response.flash = 'Hubo un error al llenar la forma de huellas/excretas'
       
    else:

        response.flash = 'Por favor, llene los campos solicitados'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    # Tabla de revisión de registros ingresados
    db.Huella_excreta.transecto_huellas_excretas_id.writable = False
    db.Archivo_huella_excreta.huella_excreta_id.writable =False
    grid = SQLFORM.smartgrid(db.Huella_excreta,csv=False,user_signature=False,
        create=False,searchable=False,editable=False)

    return dict(listaConglomerado=listaConglomerado,
        grid=grid)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de transecto a partir de los transectos declarados en un conglomerado seleccionado.

def asignarTransectos():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los transectos declarados en dicho conglomerado
    transectosDeclarados = db(
        db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==conglomeradoElegidoID
        ).select(db.Transecto_huellas_excretas_muestra.transecto_numero,\
        db.Transecto_huellas_excretas_muestra.id)

    #Creando la dropdown de transectos y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='transecto_huellas_excretas_id' id='tabla_transecto_huellas_excretas_id'>"

    for transecto in transectosDeclarados:

        dropdownHTML += "<option value='" + str(transecto.id) + "'>" + transecto.transecto_numero + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)