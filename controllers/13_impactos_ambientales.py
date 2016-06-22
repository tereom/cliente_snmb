#coding: utf8

def index1():

    ## Controlador correspondiente a la pestaña "Impactos actuales" de la sección:
    ## "Impactos ambientales"

    # Creando una lista con los tipos de impactos ambientales:

    listaTiposImpacto = db(db.Cat_tipo_impacto).select(db.Cat_tipo_impacto.nombre)
 
    n_impactos = len(listaTiposImpacto)

    camposImpactos = [

        ###########################################
        # Impactos actuales
        ###########################################

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s'))

    ]

    # Generando con un for los nombres de los campos relativos a cada impacto
    # ambiental

    for i in range(n_impactos):

        # Por la forma en como se diseñó la vista de esta pestaña, el tipo vendrá
        # de un input hidden (se mostrará en pantalla el contenido del mismo)

        tipo_i = 'tipo_' + str(i+1)

        hay_evidencia_i = 'hay_evidencia_' + str(i+1)
        en_vegetacion_i = 'en_vegetacion_' + str(i+1)
        en_suelo_i = 'en_suelo_' + str(i+1)
        comentario_i = 'comentario_' + str(i+1)

        camposImpactos.extend([

            INPUT(_name=tipo_i,_type='string'),

            #Campo para marcar si existe o no un evidencia de un impacto.
            INPUT(_name=hay_evidencia_i,_type='boolean'),

            SELECT(_name=en_vegetacion_i,
                requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
            SELECT(_name=en_suelo_i,
                requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
            TEXTAREA(_name=comentario_i)
        ])

    formaImpactos = FORM(*camposImpactos)

    if formaImpactos.accepts(request.vars,formname='formaImpactosHTML'):

        # Obteniendo el id del conglomerado asociado

        conglomeradoID = formaImpactos.vars['conglomerado_muestra_id']

        ###########################################
        # Procesando los datos de cada impacto ambiental
        ###########################################

        for i in range(n_impactos):

            # Creando de manera automatizada los nombres de los campos:

            tipo_i = 'tipo_' + str(i+1)
            hay_evidencia_i = 'hay_evidencia_' + str(i+1)
            en_vegetacion_i = 'en_vegetacion_' + str(i+1)
            en_suelo_i = 'en_suelo_' + str(i+1)
            comentario_i = 'comentario_' + str(i+1)

            datosImpacto_i = {}
            datosImpacto_i['conglomerado_muestra_id'] = conglomeradoID
            datosImpacto_i['tipo'] = formaImpactos.vars[tipo_i]

            # Si hay evidencia del i-ésimo tipo:

            if bool(formaImpactos.vars[hay_evidencia_i]):
                datosImpacto_i['hay_evidencia'] = True
            else:
                datosImpacto_i['hay_evidencia'] = False
        
            # Agregando los datos extraídos de la forma:

            datosImpacto_i['en_vegetacion'] = formaImpactos.vars[en_vegetacion_i]
            datosImpacto_i['en_suelo'] = formaImpactos.vars[en_suelo_i]
            datosImpacto_i['comentario'] = formaImpactos.vars[comentario_i]

            # Insertando los datos del impacto ambiental:

            db.Impacto_actual.insert(**datosImpacto_i)

        response.flash = 'Éxito'
        
    elif formaImpactos.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    # Regresando los nombres de todos los conglomerados insertados en la tabla de
    # conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    listaSeveridadImpacto = db(db.Cat_severidad_impactos).select(
        db.Cat_severidad_impactos.nombre)

    # Regresando la lista de tipos de impacto para crear la vista en HTML

    return dict(listaTiposImpacto = listaTiposImpacto,
        listaConglomerado = listaConglomerado,
        listaSeveridadImpacto = listaSeveridadImpacto,
        n_impactos = n_impactos)

def impactosExistentes():

    ## Función de AJAX para revisar que no se haya ingresado información de
    ## impactos actuales en el mismo conglomerado con anterioridad.
    ## El AJAX se activará cuando seleccionen un conglomerado.

    # Obteniendo la información del conglomerado que seleccionó el usuario:

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    # Haciendo un query a la tabla de Impacto_actual con la información anterior:

    impactosYaInsertados = db(db.Impacto_actual.conglomerado_muestra_id == conglomeradoElegidoID).select()

    # Regresa la longitud de impactosYaInsertados para que sea interpretada por JS

    return len(impactosYaInsertados)

def index2():

    ## Controlador correspondiente a la pestaña "Información de plagas", de la
    ## sección "Impactos ambientales".  

    camposPlaga = [

        ###########################################
        # Plaga
        ###########################################    

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        SELECT(_name='agente',
            requires=IS_IN_DB(db,db.Cat_agente_impactos.nombre,'%(nombre)s')),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='nombre_cientifico',_type='string'),
        SELECT(_name='prop_afectacion_arborea',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion.nombre,'%(nombre)s')),
        SELECT(_name='prop_afectacion_repoblado',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion.nombre,'%(nombre)s')),
        INPUT(_name='esta_activa_inactiva',_type='string'),

        ###########################################
        # Archivos plaga
        ###########################################    

        INPUT(_name='archivos_plaga',_type='file',_multiple=True)
    ]

    formaPlaga = FORM(*camposPlaga)

    if formaPlaga.accepts(request.vars, formname = 'formaPlagaHTML'):

		###########################################
		# Procesando los datos de una plaga
		###########################################

        # Filtrando los datos correspondientes a la tabla de plagas:

        datosPlaga = db.Plaga._filter_fields(formaPlaga.vars)

        # Si la plaga está activa, entonces True se guarda en la base de datos,
        # en caso contrario, se tiene que guardar manualmente False, pues si no,
        # Web2py guarda Null.

        if formaPlaga.vars['esta_activa_inactiva'] == 'activa':
            datosPlaga['esta_activa'] = True
        else:
            datosPlaga['esta_activa'] = False

        # Guardando el registro de la plaga en la base de datos:
        
        plagaInsertada = db.Plaga.insert(**datosPlaga)

		###########################################
		# Procesando los archivos de la plaga:
		###########################################

        # Como los archivos de plaga no son obligatorios, hay que poner
        # un try, except:

        try:
        
            archivos = formaPlaga.vars['archivos_plaga']
        
            if not isinstance(archivos, list):
                archivos = [archivos]
            
            for aux in archivos:

                # Guardando el archivo en la carpeta adecuada
                archivoPlaga = db.Archivo_plaga.archivo.store(aux,aux.filename)
            
                datosArchivoPlaga = {}
                datosArchivoPlaga['plaga_id'] = plagaInsertada
                datosArchivoPlaga['archivo'] = archivoPlaga
                datosArchivoPlaga['archivo_nombre_original'] = aux.filename
        
                # Insertando el registro en la base de datos:

                db.Archivo_plaga.insert(**datosArchivoPlaga)

        except:

            pass
        
        response.flash = 'Éxito'
        
    elif formaPlaga.errors:

       response.flash = 'Hubo un error al llenar los datos de la plaga'
       
    else:
        pass

	##############################################################
	# Procesando la información de las dropdowns
	##############################################################

    # Regresando los nombres de todos los conglomerados insertados en la tabla de
    # conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    listaAgente = db(db.Cat_agente_impactos).select(
        db.Cat_agente_impactos.nombre)
    
    listaPropAfectacion = db(db.Cat_prop_afectacion).select(
        db.Cat_prop_afectacion.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

    db.Archivo_plaga.plaga_id.writable = False
    grid = SQLFORM.grid(db.Plaga, orderby =~ db.Plaga.id,\
        csv = False, user_signature = False, details = False,
        create = False, searchable = False, editable = False)

    return dict(
    	listaConglomerado = listaConglomerado,
        listaAgente = listaAgente,
        listaPropAfectacion = listaPropAfectacion,
        grid = grid)

def index3():

    ## Controlador correspondiente a la pestaña "Información de incendios", de
    ## la sección: "Impactos ambientales"  

    camposIncendio = [

        ###########################################
        # Incendio
        ###########################################    

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        INPUT(_name='hay_evidencia',_type='boolean'),

        # Sólo si hay evidencia se llenan los campos siguientes.
        # Por eso mismo, aunque los campos de "tipo" y "prop_..." provengan de catálogo,
        # no se exigirá: requires=IS_IN_DB(...), pues pueden ser vacíos...

        # El siguiente campo va a leer de radio-botones, por eso admite un string
        # (lee el valor asociado al botón seleccionado)

        INPUT(_name='es_anio_actual_anterior', _type='string'),

        INPUT(_name='tipo', _type='string'),
        INPUT(_name='prop_afectacion_herbacea', _type='string'),
        INPUT(_name='prop_afectacion_arbustiva', _type='string'),
        INPUT(_name='prop_afectacion_arborea', _type='string'),
        INPUT(_name='prop_copa_quemada', _type='string'),
        INPUT(_name='hay_evidencia_recuperacion', _type='boolean'),

        ###########################################
        # Archivos incendio
        ###########################################

        INPUT(_name='archivos_incendio', _type='file', _multiple=True)

    ]

    formaIncendio = FORM(*camposIncendio)

    if formaIncendio.accepts(request.vars, formname = 'formaIncendioHTML'):

		###########################################
		# Procesando los datos de un incendio
		###########################################

        datosIncendio = {}
        datosIncendio['conglomerado_muestra_id'] = formaIncendio.vars['conglomerado_muestra_id']

        # Si los campos booleanos son verdaderos, entonces True se guarda en la
        # base de datos,en caso contrario, se tiene que guardar manualmente False,
        # pues si no, Web2py guarda Null.

        if bool(formaIncendio.vars['hay_evidencia']):

            datosIncendio['hay_evidencia'] = formaIncendio.vars['hay_evidencia']
            datosIncendio['tipo'] = formaIncendio.vars['tipo']
            datosIncendio['prop_afectacion_herbacea'] = formaIncendio.vars['prop_afectacion_herbacea']
            datosIncendio['prop_afectacion_arbustiva'] = formaIncendio.vars['prop_afectacion_arbustiva']
            datosIncendio['prop_afectacion_arborea'] = formaIncendio.vars['prop_afectacion_arborea']
            datosIncendio['prop_copa_quemada'] = formaIncendio.vars['prop_copa_quemada']

            if formaIncendio.vars['es_anio_actual_anterior'] == 'actual':
                datosIncendio['es_anio_actual'] = True

            else:
                datosIncendio['es_anio_actual'] = False

            if bool(formaIncendio.vars['hay_evidencia_recuperacion']):
                datosIncendio['hay_evidencia_recuperacion'] = True

            else:
                datosIncendio['hay_evidencia_recuperacion'] = False

        else:
            datosIncendio['hay_evidencia'] = False

        incendioInsertado = db.Incendio.insert(**datosIncendio)

		###########################################
		# Procesando los archivos de un incendio:
		###########################################

        # Como los archivos de incendio no son obligatorios, hay que poner
        # un try, except:

        try:
        
            archivos = formaIncendio.vars['archivos_incendio']
        
            if not isinstance(archivos, list):
                archivos = [archivos]
            
            for aux in archivos:

                #Guardando el archivo en la carpeta adecuada
                archivoIncendio = db.Archivo_incendio.archivo.store(aux,aux.filename)
            
                datosArchivoIncendio = {}
                datosArchivoIncendio['incendio_id'] = incendioInsertado
                datosArchivoIncendio['archivo'] = archivoIncendio
                datosArchivoIncendio['archivo_nombre_original'] = aux.filename
        
                #Insertando el registro en la base de datos:

                db.Archivo_incendio.insert(**datosArchivoIncendio)

        except:

            pass

        response.flash = 'Exito'

    elif formaIncendio.errors:

       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        pass
        #response.flash = 'Por favor, llene los campos solicitados'

	##############################################################
	# Procesando la información de las dropdowns
	##############################################################

    # Regresando los nombres de todos los conglomerados insertados en la tabla de
    # conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    # Listas para llenar los catálogos dropdown
    listaTipoIncendio = db(db.Cat_incendio).select(db.Cat_incendio.nombre)
    listaPropAfectacion = db(db.Cat_prop_afectacion).select(
        db.Cat_prop_afectacion.nombre)

    return dict(listaConglomerado = listaConglomerado,
        listaTipoIncendio = listaTipoIncendio,
        listaPropAfectacion = listaPropAfectacion)

def incendioExistente():

    ## Función de AJAX para revisar que no se haya ingresado información de incendios
    ## en el mismo conglomerado con anterioridad. El AJAX se activará cuando seleccionen 
    ## un conglomerado.

    # Obteniendo la información del conglomerado que seleccionó el usuario:

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    # Haciendo un query a la tabla de Incendios con la información anterior:

    incendioYaInsertado = db(db.Incendio.conglomerado_muestra_id == conglomeradoElegidoID).select()

    # Regresa la longitud de incendiosYaInsertados para que sea interpretada por JS:

    return len(incendioYaInsertado)



