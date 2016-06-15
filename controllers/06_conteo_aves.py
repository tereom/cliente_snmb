# coding: utf8

def index1():
	
	## Controlador correspondiente a la pestaña "Punto de conteo", de la sección:
	## "Conteo de aves".

	camposPuntoConteo = [

		###########################################
		# Punto de conteo de aves
		###########################################

		# Datos para localizar un sitio único y asociarle el punto de conteo de
		# aves a éste.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

		# Datos del punto de conteo de aves:

		INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
		INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
		INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
		INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),

		SELECT(_name='condiciones_ambientales',requires=
			IS_IN_DB(db,db.Cat_condiciones_ambientales.nombre,'%(nombre)s')),

		TEXTAREA(_name='comentario',_type='text')
	]
	
	formaPuntoConteo = FORM(*camposPuntoConteo)
	
	if formaPuntoConteo.accepts(request.vars, formname='formaPuntoConteoHTML'):

		###########################################
		# Procesando los datos del punto de conteo de aves
		###########################################

		# Filtrando los datos correspondientes a la tabla de Punto_conteo_aves:

		datosPuntoConteo = db.Punto_conteo_aves._filter_fields(formaPuntoConteo.vars)

		# Insertando el registro en la base de datos

		db.Punto_conteo_aves.insert(**datosPuntoConteo)

		response.flash = 'Éxito'

	elif formaPuntoConteo.errors:

		response.flash = 'Hubo un error al llenar la forma'

	else:
		pass

	##############################################################
	# Enviando la información de las dropdowns
	##############################################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	# De la misma manera, llenando la combobox de condiciones ambientales:

	listaCondicionesAmbientales = db(db.Cat_condiciones_ambientales).select(
		db.Cat_condiciones_ambientales.nombre)

	return dict(listaConglomerado = listaConglomerado,
		listaCondicionesAmbientales = listaCondicionesAmbientales)

def asignarSitios():

	## Función invocada mediante AJAX para llenar la combobox "sitio_muestra_id"
	## a partir de los sitios existentes de un conglomerado seleccionado.

	# Obteniendo la información del conglomerado que seleccionó el usuario:
	conglomeradoElegidoID = request.vars.conglomerado_muestra_id

	# Obteniendo los sitios que existen en dicho conglomerado
	sitiosAsignados = db(
		(db.Sitio_muestra.conglomerado_muestra_id == conglomeradoElegidoID) &\
		(db.Sitio_muestra.existe == True) &\
		(db.Sitio_muestra.sitio_numero != 'Punto de control')
		).select(db.Sitio_muestra.sitio_numero, db.Sitio_muestra.id)

	# Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

	dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='sitio_muestra_id'>"

	dropdownHTML += "<option value=''/>"

	for sitio in sitiosAsignados:

		dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  
	
	dropdownHTML += "</select>"
	
	return XML(dropdownHTML)

def puntoConteoExistente():

	## Función invocada mediante AJAX para revisar que no se haya ingresado un
	## punto de conteo en el mismo sitio con anterioridad. El AJAX se activará
	## cuando seleccionen un conglomerado y un número de sitio.

	# Obteniendo la información del sitio que seleccionó el usuario:
	sitioElegidoID = request.vars.sitio_muestra_id

	# Haciendo un query a la tabla de Punto_conteo_aves con la información anterior:

	puntoConteoYaInsertado = db(
		db.Punto_conteo_aves.sitio_muestra_id == sitioElegidoID).select()

	#regresa la longitud de puntoConteoYaInsertado para que sea interpretada por JS

	return len(puntoConteoYaInsertado)

def index2():

	## Controlador correspondiente a la pestaña "Avistamientos", de la
	## sección "Conteo de aves".

	# Funcionamiento de la vista:
	# Se debe marcar al menos una de las dos casillas, ya sea de nombre común o
	# nombre científico. Al hacer ésto, aparece la combo box para elegir el nombre
	# correspondiente. Finalmente, si se escoge la opción de "Otros" en la combobox,
	# aparece un campo para escribirlo manualmente.

	# Razonamiento detrás de la forma:
	# 1. Preferimos el nombre científico al nombre común, por ello, en la vista,
	# la casilla correspondiente al campo "hay_nombre_cientifico" estará marca-
	# da por default.
	# 2. Pensábamos que la lista de nombres científicos era exhaustiva, pero no
	# lo es si sólo conocen el género y no la especie, conviene permitirles
	# que escriban el nombre.
	# 3. Si conocen el nombre científico, nos interesa que también escriban/
	# seleccionen el nombre común, NO queremos ligar ambas listas (ie. que al
	# elegir un nombre científico, se llene el nombre común por default), ya
	# que como los nombres comunes cambian por región, esa información puede
	# resultar valiosa si en el futuro queremos imputar información de los
	# nombres científicos a partir de los comunes.
	# 4. Si no conocen el nombre científico, deben escribir el nombre común,
	# pero no se ligará al nombre científico, ya que puede ser que dos aves
	# de distintas regiones tengan el mismo nombre común pero diferentes
	# nombres científicos.

	camposAvistamiento = [

		###########################################
		# Avistamiento de aves
		###########################################

		# Datos para localizar un punto de conteo único y asociarle los
		# avistamientos a éste.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
		SELECT(_name='punto_conteo_aves_id',
			requires=IS_IN_DB(db,db.Punto_conteo_aves.id,'%(nombre)s')),

		# Campos de un avistamiento de aves:

		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='seleccion_nombre_cientifico',_type='string'),
		INPUT(_name='nombre_cientifico',_type='string'),

		INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='seleccion_nombre_comun',_type='string'),
		INPUT(_name='nombre_comun',_type='string'),

		INPUT(_name='es_visual',_type='boolean'),
		INPUT(_name='es_sonora',_type='boolean'),

		INPUT(_name='numero_individuos',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='distancia_aproximada',_type='double',requires=IS_NOT_EMPTY()),

		###########################################
		# Archivos avistamiento de aves
		###########################################

		INPUT(_name='archivos_avistamiento',_type='file',_multiple=True)

	]


	formaAvistamiento = FORM(*camposAvistamiento)

	if formaAvistamiento.accepts(request.vars, formname = 'formaAvistamientoHTML'):

		###########################################
		# Procesando los datos del avistamiento:
		###########################################

		datosAvistamiento = {}  
		
		datosAvistamiento['punto_conteo_aves_id'] = formaAvistamiento.vars['punto_conteo_aves_id']

		datosAvistamiento['numero_individuos'] = formaAvistamiento.vars['numero_individuos']
		datosAvistamiento['distancia_aproximada'] = formaAvistamiento.vars['distancia_aproximada']

		# La observación es visual/sonora, entonces True se guarda en la base de datos,
		# en caso contrario, se tiene que guardar manualmente False, pues si no,
		# Web2py guarda Null.

		if bool(formaAvistamiento.vars['es_visual']):
			datosAvistamiento['es_visual'] = True
		else:
			datosAvistamiento['es_visual'] = False

		if bool(formaAvistamiento.vars['es_sonora']):
			datosAvistamiento['es_sonora'] = True
		else:
			datosAvistamiento['es_sonora'] = False

		# Asignando nombres comunes y científicos
		
		if bool(formaAvistamiento.vars['hay_nombre_cientifico']):

			seleccionListaCientifico = formaAvistamiento.vars['seleccion_nombre_cientifico']

			if bool(seleccionListaCientifico != 'Otros'):

				datosAvistamiento['nombre_cientifico_en_lista'] = True
				datosAvistamiento['nombre_cientifico'] = seleccionListaCientifico

			else:

				datosAvistamiento['nombre_cientifico_en_lista'] = False
				datosAvistamiento['nombre_cientifico'] = formaAvistamiento.vars['nombre_cientifico']

		# Si no hay nombre científico, los dos campos anteriores se insertan vacíos.

		if bool(formaAvistamiento.vars['hay_nombre_comun']):

			seleccionListaComun = formaAvistamiento.vars['seleccion_nombre_comun']

			if bool(seleccionListaComun != 'Otros'):

				datosAvistamiento['nombre_comun_en_lista'] = True
				datosAvistamiento['nombre_comun'] = seleccionListaComun

			else:

				datosAvistamiento['nombre_comun_en_lista'] = False
				datosAvistamiento['nombre_comun'] = formaAvistamiento.vars['nombre_comun']

		# Si no hay nombre común, los dos campos anteriores se insertan vacíos.

		# Insertando el registro en la base de datos:
		
		avistamientoInsertado = db.Avistamiento_aves.insert(**datosAvistamiento)

		###########################################
		# Procesando los archivos del avistamiento:
		###########################################

		# Como los archivos de conteo de aves no son obligatorios, hay que poner
		# un try, except:

		try:
		
			archivos = formaAvistamiento.vars['archivos_avistamiento']
		
			if not isinstance(archivos, list):
				archivos = [archivos]
			
			for aux in archivos:

				# Guardando el archivo en la carpeta adecuada

				archivoAvistamiento = db.Archivo_avistamiento_aves.archivo.store(aux,aux.filename)
			
				datosArchivoAvistamiento = {}
				datosArchivoAvistamiento['avistamiento_aves_id'] = avistamientoInsertado
				datosArchivoAvistamiento['archivo'] = archivoAvistamiento
				datosArchivoAvistamiento['archivo_nombre_original'] = aux.filename
		
				# Insertando el registro en la base de datos:

				db.Archivo_avistamiento_aves.insert(**datosArchivoAvistamiento)

		except:

			pass
		
		response.flash = 'Éxito'
		
	elif formaAvistamiento.errors:

	   response.flash = 'Hubo un error al llenar la forma de conteo de aves'
	   
	else:
		pass

	###########################################
	# Procesando la información de las dropdowns
	###########################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	listaAvesNombreComun = db(db.Cat_conabio_aves).select(
		db.Cat_conabio_aves.nombre_comun).sort(lambda row: row.nombre_comun)

	listaAvesNombreCientifico = db(db.Cat_conabio_aves).select(
		db.Cat_conabio_aves.nombre_cientifico).sort(lambda row: row.nombre_cientifico)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Avistamiento_aves.punto_conteo_aves_id.writable = False
	db.Archivo_avistamiento_aves.avistamiento_aves_id.writable =False

	grid = SQLFORM.grid(db.Avistamiento_aves, orderby=~ db.Avistamiento_aves.id,\
		csv = False, user_signature = False, details = False,
		create = False, searchable = False, editable = False)

	return dict(listaConglomerado = listaConglomerado,\
		listaAvesNombreComun = listaAvesNombreComun,\
		listaAvesNombreCientifico = listaAvesNombreCientifico,\
		grid = grid)

def asignarPuntoConteo():

	## Función invocada mediante AJAX para verficar si se ha ingresado información 
	## de punto de control para el conglomerado y sitio seleccionados. En caso
	## de que no se haya ingresado un punto de control no se permite enviar la
	## forma. El AJAX se activa cuando se selecciona un número de sitio

	# El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
	# el punto de conteo asociado a un sitio (mediante AJAX).

	sitioElegidoID = request.vars.sitio_muestra_id

	# Obteniendo los puntos de conteo que han sido declarados en dicho sitio

	puntosConteoAsignados = db(db.Punto_conteo_aves.sitio_muestra_id == \
		sitioElegidoID).select(db.Punto_conteo_aves.id, db.Punto_conteo_aves.fecha)

	puntoConteo = puntosConteoAsignados.first()

	# Bajo el supuesto que sólo existe un punto de conteo de aves por fecha para
	# determinado sitio, no se requiere hacer dropdowns:

	if len(puntosConteoAsignados) == 0:

		respuestaHTML = "<p>No se encontró un punto de conteo de aves en el sitio elegido</p>"

		respuestaHTML += "<input type='hidden' name='punto_conteo_aves_id' "+\
			"id='punto_conteo_aves_id' value=''/>"

	else:

		respuestaHTML = "<p>Fecha de conteo de aves: " + str(puntoConteo.fecha) +"</p>"

		respuestaHTML += "<input type='hidden' name='punto_conteo_aves_id' "+\
			"id='punto_conteo_aves_id' value='" + str(puntoConteo.id)+ "'/>"

	return XML(respuestaHTML)