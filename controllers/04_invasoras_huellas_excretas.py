# coding: utf8
def index1():

	## Controlador correspondiente a la pestaña "Transecto muestra", de la sección
	## "Especies invasoras y huellas/excretas".

	camposTransectos = [

		# Dato para localizar una muestra de conglomerado y asociarle los tres
		# transectos a ésta:

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

		###########################################
		# Transecto 2
		###########################################

		INPUT(_name='existe_2',_type='boolean'),

		# Como los transectos pueden o no existir, los siguientes campos ya no
		# son obligatorios a nivel de controlador. A nivel de vista sí lo son,
		# cuando se marca la casilla "existe".

		# El campo "transecto_numero_2" se llenará a la hora de procesar la forma
		INPUT(_name='tecnico_2',_type='string'),
		INPUT(_name='fecha_2',_type='date'),
		INPUT(_name='hora_inicio_2',_type='time'),
		INPUT(_name='hora_termino_2',_type='time'),
		TEXTAREA(_name='comentario_2'),

		###########################################
		# Transecto 3
		###########################################

		INPUT(_name='existe_3',_type='boolean'),

		# Como los transectos pueden o no existir, los siguientes campos ya no
		# son obligatorios a nivel de controlador. A nivel de vista sí lo son,
		# cuando se marca la casilla "existe".

		# El campo "transecto_numero_3" se llenará a la hora de procesar la forma
		INPUT(_name='tecnico_3',_type='string'),
		INPUT(_name='fecha_3',_type='date'),
		INPUT(_name='hora_inicio_3',_type='time'),
		INPUT(_name='hora_termino_3',_type='time'),
		TEXTAREA(_name='comentario_3'),

		###########################################
		# Transecto 4
		###########################################

		INPUT(_name='existe_4',_type='boolean'),

		# Como los transectos pueden o no existir, los siguientes campos ya no
		# son obligatorios a nivel de controlador. A nivel de vista sí lo son,
		# cuando se marca la casilla "existe".

		# El campo "transecto_numero_4" se llenará a la hora de procesar la forma
		INPUT(_name='tecnico_4',_type='string'),
		INPUT(_name='fecha_4',_type='date'),
		INPUT(_name='hora_inicio_4',_type='time'),
		INPUT(_name='hora_termino_4',_type='time'),
		TEXTAREA(_name='comentario_4'),
	]
	
	formaTransectos = FORM(*camposTransectos)
	
	if formaTransectos.accepts(request.vars,formname='formaTransectosHTML'):

		###########################################
		# Procesando los datos del transecto 2
		###########################################

		datosTransecto2 = {}

		datosTransecto2['conglomerado_muestra_id'] =\
			formaTransectos.vars['conglomerado_muestra_id']

		# Agregando el dato que no se pidió al usuario
		datosTransecto2['transecto_numero'] = 'Transecto 2'
		
		#Si existe el transecto 2:
		if bool(formaTransectos.vars['existe_2']):

			#Agregando los datos extraídos de la forma:
			datosTransecto2['existe'] = formaTransectos.vars['existe_2']
			datosTransecto2['fecha'] = formaTransectos.vars['fecha_2']
			datosTransecto2['hora_inicio'] = formaTransectos.vars['hora_inicio_2']
			datosTransecto2['hora_termino'] = formaTransectos.vars['hora_termino_2']
			datosTransecto2['tecnico'] = formaTransectos.vars['tecnico_2']
			datosTransecto2['comentario'] = formaTransectos.vars['comentario_2']

		else:

			datosTransecto2['existe'] = False
		
		#Insertando en la base de datos:
		db.Transecto_muestra.insert(**datosTransecto2)      

		###########################################
		# Procesando los datos del transecto 3
		###########################################

		datosTransecto3 = {}

		datosTransecto3['conglomerado_muestra_id'] =\
			formaTransectos.vars['conglomerado_muestra_id']

		# Agregando el dato que no se pidió al usuario
		datosTransecto3['transecto_numero'] = 'Transecto 3'
		
		#Si existe el transecto 3:
		if bool(formaTransectos.vars['existe_3']):

			#Agregando los datos extraídos de la forma:
			datosTransecto3['existe'] = formaTransectos.vars['existe_3']
			datosTransecto3['fecha'] = formaTransectos.vars['fecha_3']
			datosTransecto3['hora_inicio'] = formaTransectos.vars['hora_inicio_3']
			datosTransecto3['hora_termino'] = formaTransectos.vars['hora_termino_3']
			datosTransecto3['tecnico'] = formaTransectos.vars['tecnico_3']
			datosTransecto3['comentario'] = formaTransectos.vars['comentario_3']

		else:

			datosTransecto3['existe'] = False
		
		#Insertando en la base de datos:
		db.Transecto_muestra.insert(**datosTransecto3)      

		###########################################
		# Procesando los datos del transecto 4
		###########################################

		datosTransecto4 = {}

		datosTransecto4['conglomerado_muestra_id'] = \
			formaTransectos.vars['conglomerado_muestra_id']

		# Agregando el dato que no se pidió al usuario
		datosTransecto4['transecto_numero'] = 'Transecto 4'
		
		#Si existe el transecto 4:
		if bool(formaTransectos.vars['existe_4']):

			#Agregando los datos extraídos de la forma:
			datosTransecto4['existe'] = formaTransectos.vars['existe_4']
			datosTransecto4['fecha'] = formaTransectos.vars['fecha_4']
			datosTransecto4['hora_inicio'] = formaTransectos.vars['hora_inicio_4']
			datosTransecto4['hora_termino'] = formaTransectos.vars['hora_termino_4']
			datosTransecto4['tecnico'] = formaTransectos.vars['tecnico_4']
			datosTransecto4['comentario'] = formaTransectos.vars['comentario_4']

		else:

			datosTransecto4['existe'] = False
		
		#Insertando en la base de datos:
		db.Transecto_muestra.insert(**datosTransecto4)      

		response.flash = 'Éxito'

	elif formaTransectos.errors:
		response.flash = 'Hubo un error al llenar la forma'

	else:
		pass

	##############################################################
	# Procesando la información de las dropdowns
	##############################################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	return dict(listaConglomerado=listaConglomerado)

def transectosExistentes():

	## Función invocada mediante AJAX para revisar que no se haya datos de
	## transectos ingresados para un conglomerado elegido. El AJAX se activará
	## cuando se seleccione un conglomerado de la dropdown.

	# Obteniendo la información del conglomerado que seleccionó el usuario:
	conglomeradoElegidoID = request.vars.conglomerado_muestra_id

	#Haciendo un query a la tabla de "Transecto_muestra" con lainformación anterior:

	transectosYaInsertados = db(
		db.Transecto_muestra.conglomerado_muestra_id ==\
		conglomeradoElegidoID).select()

	# Regresa la longitud de trasectosYaInsertados para que sea interpretada por JS

	return len(transectosYaInsertados)

def index2():

	## Controlador correspondiente a la pestaña "Registros especies invasoras",
	## de la sección "Especies invasoras y huellas/excretas".

	camposEspecie = [

		# Datos para localizar un transecto único y asociarle la observación a
		# éste. Estos datos deben conformar una llave del transecto.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='transecto_muestra_id',
			requires=IS_IN_DB(db,db.Transecto_muestra.id,'%(nombre)s')),

		###########################################
		# Especie invasora
		###########################################

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
		
		###########################################
		# Archivos especie invasora
		###########################################

		INPUT(_name='archivos_invasora',_type='file', _multiple=True,
			requires=IS_NOT_EMPTY())
	]
	
	formaEspecie = FORM(*camposEspecie)
	
	if formaEspecie.accepts(request.vars,formname='formaEspecieHTML'):

		###########################################
		# Procesando los datos de la especie invasora
		###########################################

		datosEspecie = {}
		datosEspecie['transecto_muestra_id'] = formaEspecie.vars['transecto_muestra_id']
		datosEspecie['numero_individuos'] = formaEspecie.vars['numero_individuos']

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
		# Procesando los archivos múltiples asociados a la especie invasora
		###########################################
		
		archivos = formaEspecie.vars['archivos_invasora']

		if not isinstance(archivos, list):
		
			archivos = [archivos]
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada
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
		pass

	###########################################
	# Procesando la información de las dropdowns
	###########################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	# De la misma manera, llenando la lista de invasoras (en este caso no requerimos
	# de los ID's, pues se guardará el nombre) y la lista de número de individuos

	listaInvasoras = db(db.Cat_conabio_invasoras).select(db.Cat_conabio_invasoras.nombre)

	listaNumIndividuos = db(db.Cat_numero_individuos).select(db.Cat_numero_individuos.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Especie_invasora.transecto_muestra_id.writable = False
	db.Archivo_especie_invasora.especie_invasora_id.writable =False

	grid = SQLFORM.grid(db.Especie_invasora,orderby=~db.Especie_invasora.id,\
		csv=False,user_signature=False,
		create=False,searchable=False,editable=False)

	return dict(listaConglomerado = listaConglomerado,\
		listaInvasoras = listaInvasoras,\
		listaNumIndividuos = listaNumIndividuos,\
		grid = grid)

def asignarTransectos():

	## Función invocada mediante AJAX para llenar la combobox de número
	## de transecto a partir de los transectos declarados como existentes en un
	## conglomerado seleccionado. El AJAX se activa cuando seleccionan un número
	## de conglomerado.
	
	# Obteniendo la información del conglomerado que seleccionó el usuario:

	conglomeradoElegidoID = request.vars.conglomerado_muestra_id

	# Obteniendo los transectos declarados en dicho conglomerado

	transectosDeclarados = db(
		(db.Transecto_muestra.conglomerado_muestra_id == conglomeradoElegidoID) &\
		(db.Transecto_muestra.existe == True)
		).select(db.Transecto_muestra.transecto_numero,\
		db.Transecto_muestra.id)

	# Creando la dropdown de transectos y enviándola a la vista para que sea desplegada:

	dropdownHTML = "<select class='generic-widget' name='transecto_muestra_id' id='transecto_muestra_id'>"

	for transecto in transectosDeclarados:

		dropdownHTML += "<option value='" + str(transecto.id) + "'>" + transecto.transecto_numero + "</option>"  
	
	dropdownHTML += "</select>"
	
	return XML(dropdownHTML)

def index3():

	## Controlador correspondiente a la pestaña "Registros huellas/excretas",
	## de la sección "Especies invasoras y huellas/excretas".

	camposHuellaExcreta = [

		# Datos para localizar un transecto único y asociarle la observación a
		# éste. Estos datos deben conformar una llave del transecto.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='transecto_muestra_id',
			requires=IS_IN_DB(db,db.Transecto_muestra.id,'%(nombre)s')),

		###########################################
		# Huella/excreta
		###########################################

		#El siguiente campo va a leer de radio-botones, por eso admite un string
		#(lee el valor asociado al botón seleccionado)
		INPUT(_name='es_huella_excreta',_type='string',requires=IS_NOT_EMPTY()),

		INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),
		INPUT(_name='largo',_type='double',requires=IS_NOT_EMPTY()),
		INPUT(_name='ancho',_type='double',requires=IS_NOT_EMPTY()),
		
		###########################################
		# Archivos huella/excreta
		###########################################

		INPUT(_name='archivos_huella_excreta',_type='file',_multiple=True,
			requires=IS_NOT_EMPTY())
	]

	formaHuellaExcreta = FORM(*camposHuellaExcreta)
	
	if formaHuellaExcreta.accepts(request.vars, formname='formaHuellaExcretaHTML'):

		###########################################
		# Procesando los datos de la huella/excreta
		###########################################

		#Filtrando los datos correspondientes a la tabla de huellas:

		datosHuellaExcreta = {}
		datosHuellaExcreta['transecto_muestra_id'] = formaHuellaExcreta.vars['transecto_muestra_id']
		datosHuellaExcreta['largo'] = formaHuellaExcreta.vars['largo']
		datosHuellaExcreta['ancho'] = formaHuellaExcreta.vars['ancho']        
		
		# Obteniendo el valor del campo "es_huella" a partir del valor del
		# control "es_huella_excreta
		
		if (formaHuellaExcreta.vars['es_huella_excreta']) == 'huella':
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

		#Guardando el registro de la huella/excreta en la base de datos:
		
		huellaExcretaInsertada = db.Huella_excreta.insert(**datosHuellaExcreta)

		###########################################
		# Procesando los archivos múltiples asociados a la huella/excreta
		###########################################
		
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

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Huella_excreta.transecto_muestra_id.writable = False
	db.Archivo_huella_excreta.huella_excreta_id.writable =False
	
	grid = SQLFORM.grid(db.Huella_excreta, orderby =~ db.Huella_excreta.id,\
		csv = False, user_signature = False,
		create = False, searchable = False, editable = False)

	return dict(listaConglomerado = listaConglomerado,
		grid = grid)
