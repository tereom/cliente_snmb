# coding: utf8

def index1():

    Campos_transecto_huellas_excretas = [

    # campos transecto huellas y excretas

    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.
    
    # No se ingresarán los tres muestreos de transecto de especies invasoras al 
    # mismo tiempo porque puede ser que los hagan a distintos tiempos, y prefieran
    # llenar un transecto mientras descansan.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_numero',
            requires=IS_IN_DB(db,db.Cat_numero_transecto.nombre,'%(nombre)s')),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
        TEXTAREA(_name='comentario'),
    ]

    #IS_DATE(format=T('%d-%m-%Y'))),
    
    formaTransecto = FORM(*Campos_transecto_huellas_excretas)
    
    if formaTransecto.accepts(request.vars,formname='formaTransectoHTML'):
        db.Transecto_huellas_excretas_muestra.insert(**formaTransecto.vars)
        response.flash = 'Éxito'
    elif formaTransecto.errors:
        response.flash = 'Hubo un error al llenar la forma'
    else:
        response.flash ='Por favor, asegúrese que registra cada transecto sólo una vez'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando la combobox de números de transecto:

    listaNumeroTransecto = db(db.Cat_numero_transecto).select(db.Cat_numero_transecto.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaNumeroTransecto=listaNumeroTransecto)

#AJAX para revisar que no se haya ingresado el mismo transecto con anterioridad.
#El AJAX se activará cuando seleccionen un conglomerado y un número de transecto.

def transectoExistente():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id
    numTransectoElegido = request.vars.transecto_numero

    #Haciendo un query a la tabla de Transecto_huellas_excretas_muestra con la
    #información anterior:

    transectoYaInsertado=db(
    (db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
    (db.Transecto_huellas_excretas_muestra.transecto_numero==numTransectoElegido)
    ).select()

    #regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(transectoYaInsertado)

def index2():

    Campos_huella_excreta = [

        #Datos para localizar un transecto único y asociarle la observación a éste.
        #Estos datos deben conformar una llave del transecto.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_huellas_excretas_id',
            requires=IS_IN_DB(db,db.Transecto_huellas_excretas_muestra.id,'%(nombre)s')),
        #En estos campos se necesita AJAX (cascadas) para solucionar el problema de que un
        #transecto asociado a un conglomerado existente no se haya declarado,

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

    grid = SQLFORM.smartgrid(db.Especie_invasora,csv=False,user_signature=False,
        create=False)

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

        #Obteniendo el nombre asociado al numero de transecto, del catálogo correspondiente:
        nombreTransecto = db(db.Cat_numero_transecto.id==transecto.transecto_numero).select().first().nombre

        dropdownHTML += "<option value='" + str(transecto.id) + "'>" + nombreTransecto + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)