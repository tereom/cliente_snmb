# coding: utf8
def index1():

	## Controlador correspondiente a la pestaña "Especies invasoras", de la sección
	## "Registros extra".

	camposEspecie=[

		# Datos para asociarle la observación a un conglomerado.
	
		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

		###########################################
		# Especie invasora extra
		###########################################

		# El siguiente campo va a leer de radio-botones, por eso admite un string
		# (lee el valor asociado al botón seleccionado)

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
		
		# Si se selecciona el nombre de una especie invasora en
		# "seleccion_conabio_lista". entonces los campos "hay_nombre_comun",
		# "nombre_comun", "hay_nombre_cientifico" y "nombre_cientifico" no se
		# llenan.

		# Por otro lado, si seleccionan "Otros", la vista se encarga que se llenen
		# los campos correspondientes, dependiendo del valor de "hay_nombre_comun"
		# y "hay_nombre_cientifico" (se debe seleccionar al menos una de estas dos).

		INPUT(_name='seleccion_conabio_lista',
			requires=IS_IN_DB(db,db.Cat_conabio_invasoras.nombre,'%(nombre)s')),

		INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),

		SELECT(_name='numero_individuos',
		 requires=IS_IN_DB(db,db.Cat_numero_individuos.nombre, '%(nombre)s')),

		TEXTAREA(_name='comentario',_type='text'),
		
		###########################################
		# Archivos especie invasora extra
		###########################################

		INPUT(_name='archivos_invasora_extra',_type='file', _multiple=True,
			requires=IS_NOT_EMPTY())
	]
	
	formaEspecie = FORM(*camposEspecie)

	if formaEspecie.accepts(request.vars, formname='formaEspecieHTML'):

		###########################################
		# Procesando los datos de la especie invasora extra
		###########################################
		
		datosEspecie = {}

		datosEspecie['conglomerado_muestra_id'] = formaEspecie.vars['conglomerado_muestra_id']
		datosEspecie['tecnico'] = formaEspecie.vars['tecnico']

		datosEspecie['fecha'] = formaEspecie.vars['fecha']
		datosEspecie['hora'] = formaEspecie.vars['hora']

		datosEspecie['lat_grado'] = formaEspecie.vars['lat_grado']
		datosEspecie['lat_min'] = formaEspecie.vars['lat_min']
		datosEspecie['lat_seg'] = formaEspecie.vars['lat_seg']

		datosEspecie['lon_grado'] = formaEspecie.vars['lon_grado']
		datosEspecie['lon_min'] = formaEspecie.vars['lon_min']
		datosEspecie['lon_seg'] = formaEspecie.vars['lon_seg']

		datosEspecie['altitud'] = formaEspecie.vars['altitud']
		datosEspecie['gps_error'] = formaEspecie.vars['gps_error']
		datosEspecie['elipsoide'] = formaEspecie.vars['elipsoide']

		datosEspecie['numero_individuos'] = formaEspecie.vars['numero_individuos']
		datosEspecie['comentario'] = formaEspecie.vars['comentario']


		# Obteniendo el valor de la variable "esta_dentro_conglomerado" a partir del
		# valor del control "dentro_fuera_conglomerado":
		
		if formaEspecie.vars['dentro_fuera_conglomerado'] == 'dentro':
			datosEspecie['esta_dentro_conglomerado'] = True
		else:
			datosEspecie['esta_dentro_conglomerado'] = False

		# Revisando la selección de lista CONABIO

		seleccionConabioLista = formaEspecie.vars['seleccion_conabio_lista']

		if seleccionConabioLista != 'Otros':

			# Si se eligió una especie invasora de la lista CONABIO, entonces se
			# guarda True en el campo "nombre_en_lista", y se llenan con la información
			# seleccionada los campos de "nombre_comun" y "nombre_cientifico".

			datosEspecie['nombre_en_lista'] = True

			#Separando el valor obtenido en mombre común y científico:
			nombre = seleccionConabioLista.split(' - ')
			datosEspecie['nombre_cientifico'] = nombre[0]
			datosEspecie['nombre_comun'] = nombre[1]

		else:

			# En caso contrario, se guarda False en el campo "nombre_en_lista",
			# y se llenan con la información ingresada los campos de "nombre_comun"
			# y "nombre_cientifico" (la vista se encarga de que al menos un campo
			# de estos sea llenado)

			datosEspecie['nombre_en_lista'] = False

			if bool(formaEspecie.vars['hay_nombre_cientifico']):
				datosEspecie['nombre_cientifico'] = formaEspecie.vars['nombre_cientifico']

			if bool(formaEspecie.vars['hay_nombre_comun']):
				datosEspecie['nombre_comun'] = formaEspecie.vars['nombre_comun']

		# Insertando el registro en la base de datos:

		especieInsertada = db.Especie_invasora.insert(**datosEspecie)

		###########################################
		# Procesando los archivos múltiples asociados a la especie invasora extra
		###########################################
		
		archivos = formaEspecie.vars['archivos_invasora_extra']

		if not isinstance(archivos, list):
		
			archivos = [archivos]
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			archivoInvasora = db.Archivo_especie_invasora_extra.archivo.store(aux, aux.filename)
			
			datosArchivoInvasora = {}
			datosArchivoInvasora['especie_invasora_extra_id'] = especieInsertada
			datosArchivoInvasora['archivo'] = archivoInvasora
			datosArchivoInvasora['archivo_nombre_original'] = aux.filename
		
			# Insertando el registro en la base de datos:

			db.Archivo_especie_invasora_extra.insert(**datosArchivoInvasora)
		
		response.flash = 'Éxito'
		
	elif formaEspecie.errors:
	
		response.flash = 'Hubo un error al llenar la forma de especie invasora'
	
	else:

		pass

	###########################################
	# Procesando la información de las dropdowns
	###########################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	#De la misma manera, llenando la lista de invasoras (en este caso no requerimos
	#de los ID's, pues se guardará el nombre) y la lista de número de individuos

	listaInvasoras = db(db.Cat_conabio_invasoras).select(db.Cat_conabio_invasoras.nombre)

	listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Especie_invasora_extra.conglomerado_muestra_id.writable = False
	db.Archivo_especie_invasora_extra.especie_invasora_extra_id.writable =False

	grid = SQLFORM.grid(db.Especie_invasora_extra,orderby=~db.Especie_invasora_extra.id,\
		csv=False,user_signature=False, \
		create=False,searchable=False,editable=False)

	return dict(listaConglomerado = listaConglomerado,\
		listaInvasoras = listaInvasoras,\
		listaNumIndividuos = listaNumIndividuos,\
		listaElipsoide = listaElipsoide,\
		grid = grid)

def index2():

	## Controlador correspondiente a la pestaña "Huellas/excretas", de la sección
	## "Registros extra".

	camposHuellaExcreta=[
	
		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

		###########################################
		# Huella/excreta extra
		###########################################

		# El siguiente campo va a leer de radio-botones, por eso admite un string
		# (lee el valor asociado al botón seleccionado)

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

		###########################################
		# Archivos huella/excreta extra
		###########################################

		INPUT(_name='archivos_huella_excreta_extra',_type='file',_multiple=True,
			requires=IS_NOT_EMPTY())
	]

	formaHuellaExcreta = FORM(*camposHuellaExcreta)

	if formaHuellaExcreta.accepts(request.vars, formname='formaHuellaExcretaHTML'):
		
		datosHuellaExcreta = {}

		datosHuellaExcreta['conglomerado_muestra_id'] = formaHuellaExcreta.vars['conglomerado_muestra_id']
		datosHuellaExcreta['tecnico'] = formaHuellaExcreta.vars['tecnico']

		datosHuellaExcreta['fecha'] = formaHuellaExcreta.vars['fecha']
		datosHuellaExcreta['hora'] = formaHuellaExcreta.vars['hora']

		datosHuellaExcreta['lat_grado'] = formaHuellaExcreta.vars['lat_grado']
		datosHuellaExcreta['lat_min'] = formaHuellaExcreta.vars['lat_min']
		datosHuellaExcreta['lat_seg'] = formaHuellaExcreta.vars['lat_seg']

		datosHuellaExcreta['lon_grado'] = formaHuellaExcreta.vars['lon_grado']
		datosHuellaExcreta['lon_min'] = formaHuellaExcreta.vars['lon_min']
		datosHuellaExcreta['lon_seg'] = formaHuellaExcreta.vars['lon_seg']

		datosHuellaExcreta['altitud'] = formaHuellaExcreta.vars['altitud']
		datosHuellaExcreta['gps_error'] = formaHuellaExcreta.vars['gps_error']
		datosHuellaExcreta['elipsoide'] = formaHuellaExcreta.vars['elipsoide']

		datosHuellaExcreta['largo'] = formaHuellaExcreta.vars['largo']
		datosHuellaExcreta['ancho'] = formaHuellaExcreta.vars['ancho']
		datosHuellaExcreta['comentario'] = formaHuellaExcreta.vars['comentario']

		# Asociando el valor de la variable esta_dentro_conglomerado a partir del
		# valor del control dentro_fuera_conglomerado:
		
		if formaHuellaExcreta.vars['dentro_fuera_conglomerado'] == 'dentro':
			datosHuellaExcreta['esta_dentro_conglomerado'] = True
		else:
			datosHuellaExcreta['esta_dentro_conglomerado'] = False

		# Asociando el valor de la variable es_huella a partir del valor del control
		# es_huella_excreta
		
		if formaHuellaExcreta.vars['es_huella_excreta'] == 'huella':
			datosHuellaExcreta['es_huella'] = True
		else:
			datosHuellaExcreta['es_huella'] = False

		# Llenando con la información ingresada los campos de "nombre_comun"
		# y "nombre_cientifico" (la vista se encarga de que al menos un campo
		# de estos contenga información)

		if bool(formaHuellaExcreta.vars['hay_nombre_cientifico']):
			datosHuellaExcreta['nombre_cientifico'] = formaHuellaExcreta.vars['nombre_cientifico']

		if bool(formaHuellaExcreta.vars['hay_nombre_comun']):
			datosHuellaExcreta['nombre_comun'] = formaHuellaExcreta.vars['nombre_comun']

		# Guardando el registro de la huella/excreta en la base de datos:
		
		huellaExcretaInsertada = db.Huella_excreta_extra.insert(**datosHuellaExcreta)

		###########################################
		# Procesando los archivos múltiples asociados a la huella/excreta extra
		###########################################
		
		archivos = formaHuellaExcreta.vars['archivos_huella_excreta_extra']
		
		if not isinstance(archivos, list):
			archivos = [archivos]
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			archivoHuellaExcreta = db.Archivo_huella_excreta_extra.archivo.store(aux,aux.filename)
			
			datosArchivoHuellaExcreta = {}
			datosArchivoHuellaExcreta['huella_excreta_extra_id'] = huellaExcretaInsertada
			datosArchivoHuellaExcreta['archivo'] = archivoHuellaExcreta
			datosArchivoHuellaExcreta['archivo_nombre_original'] = aux.filename
		
			# Insertando el registro en la base de datos:

			db.Archivo_huella_excreta_extra.insert(**datosArchivoHuellaExcreta)
		
		response.flash = 'Éxito'
		
	elif formaHuellaExcreta.errors:

		response.flash = 'Hubo un error al llenar la forma de huella/excreta'
	
	else:
		pass

	###########################################
	# Procesando la información de las dropdowns
	###########################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	# Haciendo lo mismo con los elipsoides:

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Huella_excreta_extra.conglomerado_muestra_id.writable = False
	db.Archivo_huella_excreta_extra.huella_excreta_extra_id.writable =False

	grid = SQLFORM.grid(db.Huella_excreta_extra,orderby=~db.Huella_excreta_extra.id,\
		csv=False,user_signature=False, \
		create=False,searchable=False,editable=False)

	return dict(listaConglomerado = listaConglomerado,\
		listaElipsoide = listaElipsoide,\
		grid = grid)

def index3():

	## Controlador correspondiente a la pestaña "Especímentes/restos", de la sección
	## "Registros extra".

	camposEspecimenRestos=[
	
		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

		###########################################
		# Espécimen/restos (extra)
		###########################################

		# El siguiente campo va a leer de radio-botones, por eso admite un string
		# (lee el valor asociado al botón seleccionado)

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
		
		# El siguiente campo va a leer de radio-botones, por eso admite un string
		# (lee el valor asociado al botón seleccionado)

		INPUT(_name='es_especimen_restos',_type='string',requires=IS_NOT_EMPTY()),

		INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),
		SELECT(_name='numero_individuos',
			requires=IS_IN_DB(db,db.Cat_numero_individuos.nombre, '%(nombre)s')),

		TEXTAREA(_name='comentario',_type='text'),

		###########################################
		# Archivos espécimen/retos extra
		###########################################

		INPUT(_name='archivos_especimen_restos_extra',_type='file',_multiple=True,
			requires=IS_NOT_EMPTY())
	]

	formaEspecimenRestos = FORM(*camposEspecimenRestos)

	if formaEspecimenRestos.accepts(request.vars, formname='formaEspecimenRestosHTML'):
		
		datosEspecimenRestos = {}

		datosEspecimenRestos['conglomerado_muestra_id'] = formaEspecimenRestos.vars['conglomerado_muestra_id']
		datosEspecimenRestos['tecnico'] = formaEspecimenRestos.vars['tecnico']

		datosEspecimenRestos['fecha'] = formaEspecimenRestos.vars['fecha']
		datosEspecimenRestos['hora'] = formaEspecimenRestos.vars['hora']

		datosEspecimenRestos['lat_grado'] = formaEspecimenRestos.vars['lat_grado']
		datosEspecimenRestos['lat_min'] = formaEspecimenRestos.vars['lat_min']
		datosEspecimenRestos['lat_seg'] = formaEspecimenRestos.vars['lat_seg']

		datosEspecimenRestos['lon_grado'] = formaEspecimenRestos.vars['lon_grado']
		datosEspecimenRestos['lon_min'] = formaEspecimenRestos.vars['lon_min']
		datosEspecimenRestos['lon_seg'] = formaEspecimenRestos.vars['lon_seg']

		datosEspecimenRestos['altitud'] = formaEspecimenRestos.vars['altitud']
		datosEspecimenRestos['gps_error'] = formaEspecimenRestos.vars['gps_error']
		datosEspecimenRestos['elipsoide'] = formaEspecimenRestos.vars['elipsoide']

		datosEspecimenRestos['numero_individuos'] = formaEspecimenRestos.vars['numero_individuos']
		datosEspecimenRestos['comentario'] = formaEspecimenRestos.vars['comentario']

		# Asociando el valor de la variable esta_dentro_conglomerado a partir del
		# valor del control dentro_fuera_conglomerado:
		
		if formaEspecimenRestos.vars['dentro_fuera_conglomerado'] == 'dentro':
			datosEspecimenRestos['esta_dentro_conglomerado'] = True
		else:
			datosEspecimenRestos['esta_dentro_conglomerado'] = False

		# Asociando el valor de la variable es_especimen a partir del valor del
		# control es_especimen_restos
		
		if formaEspecimenRestos.vars['es_especimen_restos'] == 'especimen':
			datosEspecimenRestos['es_especimen'] = True
		else:
			datosEspecimenRestos['es_especimen'] = False

		# Llenando con la información ingresada los campos de "nombre_comun"
		# y "nombre_cientifico" (la vista se encarga de que al menos un campo
		# de estos contenga información)

		if bool(formaEspecimenRestos.vars['hay_nombre_cientifico']):
			datosEspecimenRestos['nombre_cientifico'] = formaEspecimenRestos.vars['nombre_cientifico']

		if bool(formaEspecimenRestos.vars['hay_nombre_comun']):
			datosEspecimenRestos['nombre_comun'] = formaEspecimenRestos.vars['nombre_comun']

		# Guardando el registro del espécimen/restos en la base de datos:
		
		especimenRestosInsertado = db.Especimen_restos_extra.insert(
			**datosEspecimenRestos)

		###########################################
		# Procesando los archivos múltiples asociados al espécimen/restos extra
		###########################################
		
		archivos = formaEspecimenRestos.vars['archivos_especimen_restos_extra']
		
		if not isinstance(archivos, list):
			archivos = [archivos]
			
		for aux in archivos:

		# Guardando el archivo en la carpeta adecuada

			archivoEspecimenRestos = db.Archivo_especimen_restos_extra.archivo.store(aux,aux.filename)
			
			datosArchivoEspecimenRestos = {}
			datosArchivoEspecimenRestos['especimen_restos_extra_id'] = especimenRestosInsertado
			datosArchivoEspecimenRestos['archivo'] = archivoEspecimenRestos
			datosArchivoEspecimenRestos['archivo_nombre_original'] = aux.filename
		
			# Insertando el registro en la base de datos:

			db.Archivo_especimen_restos_extra.insert(**datosArchivoEspecimenRestos)
		
		response.flash = 'Éxito'
		
	elif formaEspecimenRestos.errors:

		response.flash = 'Hubo un error al llenar la forma de especímen/restos'
	
	else:
		pass

	###########################################
	# Procesando la información de las dropdowns
	###########################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	#H aciendo lo mismo con los elipsoides y categorías de número de individuos:

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Especimen_restos_extra.conglomerado_muestra_id.writable = False
	db.Archivo_especimen_restos_extra.especimen_restos_extra_id.writable = False

	grid = SQLFORM.grid(db.Especimen_restos_extra,orderby=~db.Especimen_restos_extra.id,\
		csv=False,user_signature=False, \
		create=False,searchable=False,editable=False)

	return dict(listaConglomerado = listaConglomerado,\
		listaNumIndividuos = listaNumIndividuos,\
		listaElipsoide = listaElipsoide,\
		grid = grid)
