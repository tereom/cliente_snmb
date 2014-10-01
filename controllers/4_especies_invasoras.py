# coding: utf8
def index1():

    Campos_transecto_invasoras = [

    # campos transecto invasoras

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
    
    formaTransecto = FORM(*Campos_transecto_invasoras)
    
    if formaTransecto.accepts(request.vars,formname='formaTransectoHTML'):
        db.Transecto_especies_invasoras_muestra.insert(**formaTransecto.vars)
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

    #Haciendo un query a la tabla de Transecto_especies_invasoras_muestra con la
    #información anterior:

    transectoYaInsertado=(db(
    (db.Transecto_especies_invasoras_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
    (db.Transecto_especies_invasoras_muestra.transecto_numero==numTransectoElegido)
    )).select()

    #regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(transectoYaInsertado)

def index2():

    Campos_especie_invasora = [

		#Datos para localizar un transecto único y asociarle la observación a éste.
   		#Estos datos deben conformar una llave del transecto.

   		SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

    	SELECT(_name='transecto_especies_invasoras_id',
            requires=IS_IN_DB(db,db.Transecto_especies_invasoras_muestra.id,'%(nombre)s')),
    	#En estos campos se necesita AJAX (cascadas) para solucionar el problema
        #de que un transecto asociado a un conglomerado existente no se haya declarado.

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
		
		###########Imágenes############
		INPUT(_name='archivos_invasora',_type='file', _multiple=True,
            requires=IS_NOT_EMPTY())
	]
    
    formaEspecie = FORM(*Campos_especie_invasora)
    
    if formaEspecie.accepts(request.vars,formname='formaEspecieHTML'):

        #Filtrando los datos correspondientes a la tabla de la especie invasora:
        datosEspecie = db.Especie_invasora._filter_fields(formaEspecie.vars)
                
        #Por medio de AJAX, estamos garantizando que cuando registran los
        #transectos sólo se registre uno de cada número para cada muestreo del
        #conglomerado.

        #También garantizamos que los transectos en la dropdown de especie
        #invasora sí estén registrados con anterioridad en el conglomerado.

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

        especieInsertada = db.Especie_invasora.insert(**datosEspecie)

		################Procesando los archivos múltiples#################################
    	
    	archivos = formaEspecie.vars['archivos_invasora']
    	if not isinstance(archivos, list):
    	
    		archivos = [archivos]
    		
    	for aux in archivos:

            #Guardando el archivo en la carpeta adecuada
    		archivoInvasora = db.Archivo_especie_invasora.archivo.store(aux, aux.filename)
    		
    		datosArchivoInvasora = {}
    		datosArchivoInvasora['especie_invasora_id'] = especieInsertada
    		datosArchivoInvasora['archivo'] = archivoInvasora
    		datosArchivoInvasora['archivo_nombre_original'] = aux.filename
    	
    		#Insertando el registro en la base de datos:

    		db.Archivo_especie_invasora.insert(**datosArchivoInvasora)
        
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
    #de los ID's, como se mencionó anteriormente) y la lista de número de individuos

    listaConabio = db(db.Cat_conabio_invasoras).select(db.Cat_conabio_invasoras.nombre)

    listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)

    # Tabla de revisión de registros ingresados
    db.Especie_invasora.transecto_especies_invasoras_id.writable = False
    db.Archivo_especie_invasora.especie_invasora_id.writable =False
    grid = SQLFORM.smartgrid(db.Especie_invasora,csv=False,user_signature=False, 
        create=False,searchable=False,editable=False)

    return dict(listaConglomerado=listaConglomerado,\
        listaConabio=listaConabio,\
        listaNumIndividuos=listaNumIndividuos, 
        grid=grid)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de transecto a partir de los transectos declarados en un conglomerado seleccionado.

def asignarTransectos():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los transectos declarados en dicho conglomerado
    transectosDeclarados = db(
        db.Transecto_especies_invasoras_muestra.conglomerado_muestra_id==conglomeradoElegidoID
        ).select(db.Transecto_especies_invasoras_muestra.transecto_numero,\
        db.Transecto_especies_invasoras_muestra.id)

    #Creando la dropdown de transectos y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='transecto_especies_invasoras_id' id='tabla_transecto_especies_invasoras_id'>"

    for transecto in transectosDeclarados:

        dropdownHTML += "<option value='" + str(transecto.id) + "'>" + transecto.transecto_numero + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)


