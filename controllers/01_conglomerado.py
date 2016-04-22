# coding: utf8

import os

def index():

	## Controlador correspondiente a la pestaña "Conglomerado", de la sección
	## homónima.

	campos = [

		###########################################
		# Conglomerado
		###########################################

		# El campo "monitoreo_tipo" de la tabla "Conglomerado_muestra", se llena
		# a la hora de procesar los datos,

		INPUT(_name='nombre',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='fecha_visita',_type='date',requires=IS_NOT_EMPTY()),
		SELECT(_name='tipo',
			requires=IS_IN_DB(db,db.Cat_tipo_conglomerado.nombre,'%(nombre)s')),
		SELECT(_name='estado',
			requires=IS_IN_DB(db,db.Cat_estado_conglomerado.nombre,'%(nombre)s')),
		SELECT(_name='municipio',
			requires=IS_IN_DB(db,db.Cat_municipio_conglomerado.nombre,'%(nombre)s')),
		INPUT(_name='predio',_type='string',requires=IS_NOT_EMPTY()),
		SELECT(_name='tenencia',
			requires=IS_IN_DB(db,db.Cat_tenencia_conglomerado.nombre,'%(nombre)s')),
		SELECT(_name='uso_suelo_tipo',
			requires=IS_IN_DB(db,db.Cat_suelo_conglomerado.nombre,'%(nombre)s')),

		INPUT(_name='compania',_type='string',requires=IS_NOT_EMPTY()),

		# El campo de vegetación_tipo posiblemente se envíe vacío de la vista (si
		# vegetación no es el uso de suelo principal), por ello, conviene ponerlo
		# como un string, para que no lo rebote la forma en este caso.

		INPUT(_name='vegetacion_tipo',_type='string'),

		INPUT(_name='perturbado',_type='boolean'),
		INPUT(_name='comentario',_type='text'),

		###########################################
		# Formato de campo
		###########################################

		INPUT(_name='formato_campo',_type='file',requires=IS_NOT_EMPTY()),

		# En la información acerca de sitios, los campos de "sitio_numero" y
		# "conglomerado_muestra_id", que se encuentran en la tabla "Sitio_muestra",
		# se llenarán a la hora de procesar los datos enviados de la vista.

		###########################################
		# Sitio 1 (centro)
		###########################################

		INPUT(_name='existe_1',_type='boolean'),

		# Como el centro puede no existir, no se pueden pedir como obligatorios
		# los siguientes campos (sin embargo, el validador de la vista se encar-
		# gará de que los llenen en caso de que sí exista el sitio).
		INPUT(_name='lat_grado_1',_type='integer'),
		INPUT(_name='lat_min_1',_type='integer'),
		INPUT(_name='lat_seg_1',_type='double'),
		INPUT(_name='lon_grado_1',_type='integer'),
		INPUT(_name='lon_min_1',_type='integer'),
		INPUT(_name='lon_seg_1',_type='double'),
		INPUT(_name='altitud_1',_type='double'),
		INPUT(_name='gps_error_1',_type='double'),

		# El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
		# conviene ponerlo como un string, para que no requiera que esté en
		# el catálogo (y por ende, no vacío).
		INPUT(_name='elipsoide_1',_type='string'),
		INPUT(_name='hay_evidencia_1',_type='boolean'),
		
		###########################################
		# Imagen sitio 1
		###########################################

		INPUT(_name='imagen_1',_type='file'),
			
		###########################################
		# Sitio 2
		###########################################
			
		INPUT(_name='existe_2',_type='boolean'),

		# Como el sitio 2 puede no existir, no se pueden pedir como obligatorios
		# los siguientes campos (sin embargo, el validador de la vista se encar-
		# gará de que los llenen en caso de que sí exista el sitio).
		INPUT(_name='lat_grado_2',_type='integer'),
		INPUT(_name='lat_min_2',_type='integer'),
		INPUT(_name='lat_seg_2',_type='double'),
		INPUT(_name='lon_grado_2',_type='integer'),
		INPUT(_name='lon_min_2',_type='integer'),
		INPUT(_name='lon_seg_2',_type='double'),
		INPUT(_name='altitud_2',_type='double'),
		INPUT(_name='gps_error_2',_type='double'),

		# El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
		# conviene ponerlo como un string, para que no requiera que esté en
		# el catálogo (y por ende, no vacío).
		INPUT(_name='elipsoide_2',_type='string'),          
		INPUT(_name='hay_evidencia_2',_type='boolean'),
		
		###########################################
		# Imagen sitio 2
		###########################################

		INPUT(_name='imagen_2',_type='file'),
 
		###########################################
		# Sitio 3
		###########################################
	
		INPUT(_name='existe_3',_type='boolean'),

		# Como el campo 3 puede no existir, no se pueden pedir como obligatorios
		# los siguientes campos (sin embargo, el validador de la vista se encar-
		# gará de que los llenen)
		INPUT(_name='lat_grado_3',_type='integer'),
		INPUT(_name='lat_min_3',_type='integer'),
		INPUT(_name='lat_seg_3',_type='double'),
		INPUT(_name='lon_grado_3',_type='integer'),
		INPUT(_name='lon_min_3',_type='integer'),
		INPUT(_name='lon_seg_3',_type='double'),
		INPUT(_name='altitud_3',_type='double'),
		INPUT(_name='gps_error_3',_type='double'),

		# El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
		# conviene ponerlo como un string, para que no requiera que esté en
		# el catálogo (y por ende, no vacío).
		INPUT(_name='elipsoide_3',_type='string'),
		INPUT(_name='hay_evidencia_3',_type='boolean'),
		
		###########################################
		# Imagen sitio 3
		###########################################

		INPUT(_name='imagen_3',_type='file'),

		###########################################
		# Sitio 4
		###########################################
	
		INPUT(_name='existe_4',_type='boolean'),

		# Como el campo 4 puede no existir, no se pueden pedir como obligatorios
		# los siguientes campos (sin embargo, el validador de la vista se encar-
		# gará de que los llenen)
		INPUT(_name='lat_grado_4',_type='integer'),
		INPUT(_name='lat_min_4',_type='integer'),
		INPUT(_name='lat_seg_4',_type='double'),
		INPUT(_name='lon_grado_4',_type='integer'),
		INPUT(_name='lon_min_4',_type='integer'),
		INPUT(_name='lon_seg_4',_type='double'),
		INPUT(_name='altitud_4',_type='double'),
		INPUT(_name='gps_error_4',_type='double'),

		# El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
		# conviene ponerlo como un string, para que no requiera que esté en
		# el catálogo (y por ende, no vacío).
		INPUT(_name='elipsoide_4',_type='string'),
		INPUT(_name='hay_evidencia_4',_type='boolean'),
		
		###########################################
		# Imagen sitio 4
		###########################################

		INPUT(_name='imagen_4',_type='file'),

		###########################################
		# Punto de control
		###########################################

		# El punto de control siempre existe.
		
		INPUT(_name='lat_grado_c',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='lat_min_c',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='lat_seg_c',_type='double',requires=IS_NOT_EMPTY()),
		INPUT(_name='lon_grado_c',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='lon_min_c',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='lon_seg_c',_type='double',requires=IS_NOT_EMPTY()),
		INPUT(_name='altitud_c',_type='double',requires=IS_NOT_EMPTY()),
		INPUT(_name='gps_error_c',_type='double',requires=IS_NOT_EMPTY()),
		SELECT(_name='elipsoide_c',
		requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),          
		INPUT(_name='hay_evidencia_c',_type='boolean'),
		
		###########################################
		# Imagen punto de control
		###########################################

		# Notar que en Punto de Control se suben dos fotos
		INPUT(_name='imagen_c',_type='file',requires=IS_NOT_EMPTY(),_multiple=True)
			
	]

	# Ésta forma únicamente se utilizará para validar antes de ingresar a la base
	# de datos y así, evitar excepciones a nivel base de datos.

	forma = FORM(*campos)

	if forma.accepts(request.vars,formname='formaHTML'):

		###########################################
		# Procesando los datos del conglomerado
		###########################################
		
		datosConglomerado = db.Conglomerado_muestra._filter_fields(forma.vars)
		
		# Campo oculto SAC-MOD (Conafor), SAR-MOD (Conanp)
		datosConglomerado['monitoreo_tipo'] = 'SAC-MOD'

		# Si no escogieron "uso_suelo_tipo" como "Vegetación", entonces anulamos
		# (por consistencia en base de datos), los valores que se pudieran haber
		# ingresado en los datos dependientes de esta opción:

		# Casteando para asegurarnos que la comparación sea entre enteros.

		if str(datosConglomerado['uso_suelo_tipo']) != 'Vegetación':

			datosConglomerado['vegetacion_tipo'] = None
			datosConglomerado['perturbado'] = None

		# Si escogieron "uso_suelo_tipo" como "Vegetacion", entonces dejamos los
		# valores que introdujeron (la vista se encarga de validar que los campos
		# sean llenados). A excepción de:

		# Si escogieron "uso_suelo_tipo" como "Vegetación" y no marcaron la casilla
		# de perturbado, entonces hay que asignarle "False" a esta, para diferen-
		# ciarla de cuando no es requerida.

		elif not(bool(datosConglomerado['perturbado'])):
		
			datosConglomerado['perturbado'] = False
			
		# Insertando en la base de datos:
		conglomeradoInsertado = db.Conglomerado_muestra.insert(**datosConglomerado)

		###########################################
		# Procesando los datos del formato de campo
		###########################################

		# Guardando el formato en la carpeta adecuada
		formato_campo = db.Formato_campo.archivo.store(
			forma.vars.formato_campo.file, forma.vars.formato_campo.filename)
		
		# Creando los campos de la tabla Formato_campo:

		datosFormato = {}
		datosFormato['conglomerado_muestra_id'] = conglomeradoInsertado
		datosFormato['archivo'] = formato_campo
		datosFormato['archivo_nombre_original'] = forma.vars.formato_campo.filename

		db.Formato_campo.insert(**datosFormato)

		# En los campos correspondientes a los sitios declarados, si no
		# seleccionaron "inaccesible", entonces todo se guarda normalmente, de lo
		# contrario, sólo se llena el punto de control (los otros sitios se
		# registran como inexistentes en la base de datos)

		if (datosConglomerado['tipo'] == '3 Inaccesible terreno/clima' or\
			datosConglomerado['tipo'] == '4 Inaccesible social' or\
			datosConglomerado['tipo'] == '5 Inaccesible gabinete'):

			datosSitio = {}
			datosSitio['conglomerado_muestra_id'] = conglomeradoInsertado
			datosSitio['existe'] = False

			for sitio_numero in ['Centro', 'Sitio 2',  'Sitio 3', 'Sitio 4']:
				datosSitio['sitio_numero'] = sitio_numero
				db.Sitio_muestra.insert(**datosSitio)    

		else:  

			###########################################
			# Procesando los datos del sitio 1 (centro)
			###########################################

			datosSitio1 = {}

			# Agregando los datos que no se pidieron al usuario:  
			datosSitio1['conglomerado_muestra_id'] = conglomeradoInsertado
			datosSitio1['sitio_numero'] = 'Centro'

			# Si existe el sitio 1:
			if bool(forma.vars['existe_1']):

				# Agregando los datos extraídos de la forma:
				datosSitio1['existe'] = forma.vars['existe_1']
				datosSitio1['lat_grado'] = forma.vars['lat_grado_1']
				datosSitio1['lat_min'] = forma.vars['lat_min_1']
				datosSitio1['lat_seg'] = forma.vars['lat_seg_1']
				datosSitio1['lon_grado'] = forma.vars['lon_grado_1']
				datosSitio1['lon_min'] = forma.vars['lon_min_1']
				datosSitio1['lon_seg'] = forma.vars['lon_seg_1']
				datosSitio1['altitud'] = forma.vars['altitud_1']
				datosSitio1['gps_error'] = forma.vars['gps_error_1']
				datosSitio1['elipsoide'] = forma.vars['elipsoide_1']

				# Si hay evidencia, entonces True se guarda en la base de datos, en
				# caso contrario, se tiene que guardar manualmente False, pues si no,
				# Web2py guarda Null.

				if bool(forma.vars['hay_evidencia_1']):
					datosSitio1['hay_evidencia'] = forma.vars['hay_evidencia_1']
				else:
					datosSitio1['hay_evidencia'] = False
					
			else:
				datosSitio1['existe'] = False
			
			# Insertando en la base de datos:
			sitio1Insertado = db.Sitio_muestra.insert(**datosSitio1)      
			
			###########################################
			# Procesando los datos de la imagen del sitio 1
			###########################################

			if bool(forma.vars['existe_1']):

				# Guardando la imagen de referencia en la carpeta adecuada
				imagen1 = db.Imagen_referencia_sitio.archivo.store(
					forma.vars.imagen_1.file, forma.vars.imagen_1.filename)
			
				# Creando los campos de la tabla Imagen_referencia_sitio:

				datosImagen1 = {}
				datosImagen1['sitio_muestra_id'] = sitio1Insertado
				datosImagen1['archivo'] = imagen1
				datosImagen1['archivo_nombre_original'] = forma.vars.imagen_1.filename
			
				#Insertando el registro en la base de datos:
			
				db.Imagen_referencia_sitio.insert(**datosImagen1)
				
			###########################################
			# Procesando los datos del sitio 2
			###########################################

			datosSitio2 = {}

			#Agregando los datos que no se pidieron al usuario:
			datosSitio2['conglomerado_muestra_id'] = conglomeradoInsertado
			datosSitio2['sitio_numero'] = 'Sitio 2'
			
			#Si existe el sitio 2:
			if bool(forma.vars['existe_2']):

				#Agregando los datos extraídos de la forma:
				datosSitio2['existe'] = forma.vars['existe_2']
				datosSitio2['lat_grado'] = forma.vars['lat_grado_2']
				datosSitio2['lat_min'] = forma.vars['lat_min_2']
				datosSitio2['lat_seg'] = forma.vars['lat_seg_2']
				datosSitio2['lon_grado'] = forma.vars['lon_grado_2']
				datosSitio2['lon_min'] = forma.vars['lon_min_2']
				datosSitio2['lon_seg'] = forma.vars['lon_seg_2']
				datosSitio2['altitud'] = forma.vars['altitud_2']
				datosSitio2['gps_error'] = forma.vars['gps_error_2']
				datosSitio2['elipsoide'] = forma.vars['elipsoide_2']
				
				if bool(forma.vars['hay_evidencia_2']):
					datosSitio2['hay_evidencia'] = forma.vars['hay_evidencia_2']
				else:
					datosSitio2['hay_evidencia'] = False
					
			else:
				datosSitio2['existe'] = False
			
			#Insertando en la base de datos:
			sitio2Insertado = db.Sitio_muestra.insert(**datosSitio2)      

			###########################################
			# Procesando los datos de la imagen del sitio 2
			###########################################
			
			if bool(forma.vars['existe_2']):
							
				# Guardando la imagen de referencia en la carpeta adecuada
				imagen2 = db.Imagen_referencia_sitio.archivo.store(
					forma.vars.imagen_2.file, forma.vars.imagen_2.filename)
			
				# Creando los campos de la tabla Imagen_referencia_sitio:

				datosImagen2 = {}
				datosImagen2['sitio_muestra_id'] = sitio2Insertado
				datosImagen2['archivo'] = imagen2
				datosImagen2['archivo_nombre_original'] = forma.vars.imagen_2.filename
			
				# Insertando el registro en la base de datos:
			
				db.Imagen_referencia_sitio.insert(**datosImagen2)

			###########################################
			# Procesando los datos del sitio 3
			###########################################
			
			datosSitio3 = {}

			# Agregando los datos que no se pidieron al usuario:
			datosSitio3['conglomerado_muestra_id'] = conglomeradoInsertado
			datosSitio3['sitio_numero'] = 'Sitio 3'
			
			# Si existe el sitio 3:
			if bool(forma.vars['existe_3']):

				#Agregando los datos extraídos de la forma:
				datosSitio3['existe'] = forma.vars['existe_3']
				datosSitio3['lat_grado'] = forma.vars['lat_grado_3']
				datosSitio3['lat_min'] = forma.vars['lat_min_3']
				datosSitio3['lat_seg'] = forma.vars['lat_seg_3']
				datosSitio3['lon_grado'] = forma.vars['lon_grado_3']
				datosSitio3['lon_min'] = forma.vars['lon_min_3']
				datosSitio3['lon_seg'] = forma.vars['lon_seg_3']
				datosSitio3['altitud'] = forma.vars['altitud_3']
				datosSitio3['gps_error'] = forma.vars['gps_error_3']
				datosSitio3['elipsoide'] = forma.vars['elipsoide_3']
				
				if bool(forma.vars['hay_evidencia_3']):
					datosSitio3['hay_evidencia'] = forma.vars['hay_evidencia_3']
				else:
					datosSitio3['hay_evidencia'] = False
					
			else:
				datosSitio3['existe'] = False
			
			#Insertando en la base de datos:
			sitio3Insertado = db.Sitio_muestra.insert(**datosSitio3)
			
			###########################################
			# Procesando los datos de la imagen del sitio 3
			###########################################
			
			if bool(forma.vars['existe_3']):
							
				# Guardando la imagen de referencia en la carpeta adecuada
				imagen3 = db.Imagen_referencia_sitio.archivo.store(
					forma.vars.imagen_3.file, forma.vars.imagen_3.filename)
			
				# Creando los campos de la tabla Imagen_referencia_sitio:
			
				datosImagen3 = {}
				datosImagen3['sitio_muestra_id'] = sitio3Insertado
				datosImagen3['archivo'] = imagen3
				datosImagen3['archivo_nombre_original'] = forma.vars.imagen_3.filename
			
				#Insertando el registro en la base de datos:
			
				db.Imagen_referencia_sitio.insert(**datosImagen3)

			###########################################
			# Procesando los datos del sitio 4
			###########################################
			
			datosSitio4 = {}

			# Agregando los datos que no se pidieron al usuario:
			datosSitio4['conglomerado_muestra_id'] = conglomeradoInsertado
			datosSitio4['sitio_numero'] = 'Sitio 4'
			
			# Si existe el sitio 4:
			if bool(forma.vars['existe_4']):

				#Agregando los datos extraídos de la forma:
				datosSitio4['existe'] = forma.vars['existe_4']
				datosSitio4['lat_grado'] = forma.vars['lat_grado_4']
				datosSitio4['lat_min'] = forma.vars['lat_min_4']
				datosSitio4['lat_seg'] = forma.vars['lat_seg_4']
				datosSitio4['lon_grado'] = forma.vars['lon_grado_4']
				datosSitio4['lon_min'] = forma.vars['lon_min_4']
				datosSitio4['lon_seg'] = forma.vars['lon_seg_4']
				datosSitio4['altitud'] = forma.vars['altitud_4']
				datosSitio4['gps_error'] = forma.vars['gps_error_4']
				datosSitio4['elipsoide'] = forma.vars['elipsoide_4']
				
				if bool(forma.vars['hay_evidencia_4']):
					datosSitio4['hay_evidencia'] = forma.vars['hay_evidencia_4']
				else:
					datosSitio4['hay_evidencia'] = False
					
			else:
				datosSitio4['existe'] = False
			
			#Insertando en la base de datos:
			sitio4Insertado = db.Sitio_muestra.insert(**datosSitio4)
			
			###########################################
			# Procesando los datos de la imagen del sitio 4
			###########################################
			
			if bool(forma.vars['existe_4']):
							
				#Guardando la imagen de referencia en la carpeta adecuada
				imagen4 = db.Imagen_referencia_sitio.archivo.store(
					forma.vars.imagen_4.file, forma.vars.imagen_4.filename)
			
				#Creando los campos de la tabla Imagen_referencia_sitio:
			
				datosImagen4 = {}
				datosImagen4['sitio_muestra_id'] = sitio4Insertado
				datosImagen4['archivo'] = imagen4
				datosImagen4['archivo_nombre_original'] = forma.vars.imagen_4.filename
			
				#Insertando el registro en la base de datos:
			
				db.Imagen_referencia_sitio.insert(**datosImagen4)

		# El punto de control siempre existe

		###########################################
		# Procesando los datos del punto de control
		###########################################
		
		datosSitioC = {}

		# Agregando los datos que no se pidieron al usuario:

		datosSitioC['conglomerado_muestra_id'] = conglomeradoInsertado
		datosSitioC['sitio_numero'] = 'Punto de control'
		datosSitioC['existe'] = True
		
		# Leyendo los datos del formulario:
		datosSitioC['lat_grado'] = forma.vars['lat_grado_c']
		datosSitioC['lat_min'] = forma.vars['lat_min_c']
		datosSitioC['lat_seg'] = forma.vars['lat_seg_c']
		datosSitioC['lon_grado'] = forma.vars['lon_grado_c']
		datosSitioC['lon_min'] = forma.vars['lon_min_c']
		datosSitioC['lon_seg'] = forma.vars['lon_seg_c']
		datosSitioC['altitud'] = forma.vars['altitud_c']
		datosSitioC['gps_error'] = forma.vars['gps_error_c']
		datosSitioC['elipsoide'] = forma.vars['elipsoide_c']
		
		if bool(forma.vars['hay_evidencia_c']):
			datosSitioC['hay_evidencia'] = forma.vars['hay_evidencia_c']
		else:
			datosSitioC['hay_evidencia'] = False
			
		#Insertando en la base de datos:
		sitioCInsertado = db.Sitio_muestra.insert(**datosSitioC)
		
		###########################################
		# Procesando los datos de la imagen del punto de control
		###########################################

		# Notar que, a diferencia de los sitios, en punto de control se suben 2 fotografías

		archivos = forma.vars['imagen_c']

		if not isinstance(archivos, list):
		
			archivos = [archivos]

		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada
			archivoImagen = db.Imagen_referencia_sitio.archivo.store(aux,aux.filename)

			datosArchivoImagen = {}
			datosArchivoImagen['sitio_muestra_id'] = sitioCInsertado
			datosArchivoImagen['archivo'] = archivoImagen
			datosArchivoImagen['archivo_nombre_original'] = aux.filename

			# Guardando la imagen de referencia en la carpeta adecuada
			db.Imagen_referencia_sitio.insert(**datosArchivoImagen)

		##################################################
		# Creación de carpetas para alojar fotos y sonidos 
		##################################################

		# se crean las carpetas que van a alojar las fotos y videos de la trampa 
		# cámara así como los sonidos audibles y ultrasónicos. Ruta:
		# cliente_snmb_windows/mac_v5
		# ├───web2py
		# ├───conglomerados
		# |   ├───nombre_aaaa-mm-dd
		# |   |   ├───c
		# |   |   ├───ga
		# |   |   ├───gu

		thisPath = os.getcwd()


		########### Para Windows ###########
		#newPath = os.path.normpath(thisPath + os.sep + os.pardir)

		############ Para Mac ###########
		newPath = os.path.normpath(thisPath +\
			os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)

		idConglomerado = str(datosConglomerado['nombre'])
		fechaConglomerado = str(datosConglomerado['fecha_visita'])

		newFolder = idConglomerado + '_' + fechaConglomerado

		if not os.path.exists(os.path.join(newPath,'conglomerados',newFolder)):
			os.makedirs(os.path.join(newPath,'conglomerados',newFolder))
			os.makedirs(os.path.join(newPath,'conglomerados',newFolder,'c'))
			os.makedirs(os.path.join(newPath,'conglomerados',newFolder,'g_a'))
			os.makedirs(os.path.join(newPath,'conglomerados',newFolder,'g_u'))

		response.flash = 'Éxito'
		
	elif forma.errors:

		response.flash = 'Hubo un error al llenar la forma'
	   
	else:
		pass

	##############################################################
	# Enviando la información de las dropdowns
	##############################################################

	# Llenando las combobox de tipo de conglomerado, estado, tenencia, principal
	# uso de suelo, tipo de vegetación y elipsoide

	listaTipo = db(db.Cat_tipo_conglomerado).select(db.Cat_tipo_conglomerado.nombre)

	listaEstado = db(db.Cat_estado_conglomerado).select(db.Cat_estado_conglomerado.nombre)

	listaTenencia = db(db.Cat_tenencia_conglomerado).select(db.Cat_tenencia_conglomerado.nombre)

	listaUsoSuelo = db(db.Cat_suelo_conglomerado).select(db.Cat_suelo_conglomerado.nombre)

	listaVegetacion = db(db.Cat_vegetacion_conglomerado).select(db.Cat_vegetacion_conglomerado.nombre)

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	return dict(listaTipo = listaTipo,\
		listaEstado = listaEstado,\
		listaTenencia = listaTenencia,\
		listaUsoSuelo = listaUsoSuelo,\
		listaVegetacion = listaVegetacion,\
		listaElipsoide = listaElipsoide)

def asignarMunicipios():

	## Función invocada mediante AJAX para llenar la combobox de municipio
	## a partir del estado seleccionado.

	# Obteniendo la información del estado que seleccionó el usuario:
	estadoElegidoNombre = request.vars.estado

	# Obteniendo la clave de dicho estado:
	estadoElegidoClave = db(db.Cat_estado_conglomerado.nombre == estadoElegidoNombre
		).select().first().clave_ent

	# Obteniendo los municipios que existen en dicho estado a partir de la clave
	municipiosAsignados = db(
		db.Cat_municipio_conglomerado.clave_ent == estadoElegidoClave
		).select(db.Cat_municipio_conglomerado.nombre)

	# Creando la dropdown de municipios y enviándola a la vista para que sea desplegada:

	dropdownHTML = "<select class='generic-widget' name='municipio' id='municipio'>"

	dropdownHTML += "<option value=''/>"

	for municipio in municipiosAsignados:

		dropdownHTML += "<option value='" + str(municipio.nombre) + "'>" + municipio.nombre + "</option>"  
	
	dropdownHTML += "</select>"
	
	return XML(dropdownHTML)

def conglomeradoExistente():

	## Función convocada mediante AJAX para revisar que no se haya ingresado el
	## mismo conglomerado con anterioridad. El AJAX se activará cuando escriban
	## un caracter del nombre de conglomerado.

	# Obteniendo la información del conglomerado que ha ingresado el usuario.
	# Puede ser que no haya terminado de escribir, por ello, se revisa primero
	# la longitud del caracter:

	longitudNombres = 6

	# El resultado en el tercer caso será el número de registros en la base de
	# datos con el mismo nombre de conglomerado, que se regresará a JS para
	# su interpretación:

	if (len(request.vars.nombre) < longitudNombres):
		resultado = 0

	elif (len(request.vars.nombre) > longitudNombres):
		resultado = -1

	else:

		conglomeradoElegidoNombre = request.vars.nombre

	# Haciendo un query a la tabla de Conglomerado_muestra con la
	# información anterior:

		conglomeradoYaInsertado = db(
			db.Conglomerado_muestra.nombre == conglomeradoElegidoNombre).select()

	# Regresa la longitud de conglomeradoYaInsertado para que sea interpretada por JS

		resultado = len(conglomeradoYaInsertado)

	return resultado
