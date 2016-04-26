# coding: utf8

# usados en "index2", "validarArchivos"
import os 
import applications.init.modules.estructura_archivos_admin as eaa

import simplejson as json # usado en "validarArchivos"

def index1(): 

	## Controlador correspondiente a la pestaña "Información de grabadora",
	## de la sección "Grabadora"
	
	camposGrabadora = [

		###########################################
		# Grabadora
		###########################################
		
		# Datos para localizar un sitio único y asociarle la grabadora a éste.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
	
		# Datos de la grabadora
		INPUT(_name='nombre',_type='string',requires=IS_NOT_EMPTY()),
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
		SELECT(_name='elipsoide',
			requires=IS_IN_DB(db,db.Cat_elipsoide.nombre,'%(nombre)s')),

		SELECT(_name='condiciones_ambientales',requires=
			IS_IN_DB(db,db.Cat_condiciones_ambientales.nombre,'%(nombre)s')),
		INPUT(_name='microfonos_mojados',_type='boolean'),

		TEXTAREA(_name='comentario',_type='text'),

		###########################################
		# Imagen de referencia de la grabadora
		###########################################

		INPUT(_name='imagen_grabadora',_type='file',requires=IS_NOT_EMPTY()),

		###########################################
		# Imágenes de referencia de los micrófonos
		###########################################

		INPUT(_name='imagen_microfonos',_type='file',_multiple=True,
			requires=IS_NOT_EMPTY()),
	
		###########################################
		# Archivo de referencia de la grabadora (metadatos)
		###########################################

		INPUT(_name='archivo_metadatos',_type='file',requires=IS_NOT_EMPTY()),
	
		]

	formaGrabadora = FORM(*camposGrabadora)

	if formaGrabadora.accepts(request.vars,formname='formaGrabadoraHTML'):
	
		###########################################
		# Procesando los datos de la grabadora
		###########################################
	
		# Filtrando los datos correspondientes a la tabla de la grabadora:

		datosGrabadora = db.Grabadora._filter_fields(formaGrabadora.vars)

		# Si los micrófonos se mojaron, entonces True se guarda en la base de
		# datos, en caso contrario, se tiene que guardar manualmente False, pues
		# si no, Web2py guarda Null.

		if bool(formaGrabadora.vars['microfonos_mojados']):
			datosGrabadora['microfonos_mojados'] = True
		else:
			datosGrabadora['microfonos_mojados'] = False
				
		#Guardando el registro de la grabadora en la base de datos:
		
		grabadoraInsertada = db.Grabadora.insert(**datosGrabadora)
		
		###########################################
		# Procesando la imagen de referencia de la grabadora
		###########################################
		
		# Guardando la imagen de referencia en la carpeta adecuada

		imagenRef = db.Imagen_referencia_grabadora.archivo.store(
			formaGrabadora.vars.imagen_grabadora.file,formaGrabadora.vars.imagen_grabadora.filename)
		
		# Creando los campos de la tabla Imagen_referencia_grabadora:
		
		datosImagenRef = {}

		datosImagenRef['grabadora_id'] = grabadoraInsertada
		datosImagenRef['archivo'] = imagenRef
		datosImagenRef['archivo_nombre_original'] = formaGrabadora.vars.imagen_grabadora.filename
		
		# Insertando el registro en la base de datos:
		
		db.Imagen_referencia_grabadora.insert(**datosImagenRef)

		###########################################
		# Procesando las imágenes de referencia de los micrófonos
		###########################################

		archivos = formaGrabadora.vars['imagen_microfonos']

		if not isinstance(archivos, list):
		
			archivos = [archivos]

		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			imagenRefMicro = db.Imagen_referencia_microfonos.archivo.store(
				aux,aux.filename)

			# Creando los campos de la tabla Imagen_referencia_microfonos:

			datosImagenRefMicro = {}
			datosImagenRefMicro['grabadora_id'] = grabadoraInsertada
			datosImagenRefMicro['archivo'] = imagenRefMicro
			datosImagenRefMicro['archivo_nombre_original'] = aux.filename

			# Insertando el registro en la base de datos:

			db.Imagen_referencia_microfonos.insert(**datosImagenRefMicro)

		###########################################
		# Procesando el archivo de metadatos de la grabadora
		###########################################
		
		# Guardando el archivo de metadatos en la carpeta adecuada
		archivoMeta = db.Archivo_referencia_grabadora.archivo.store(
			formaGrabadora.vars.archivo_metadatos.file,formaGrabadora.vars.archivo_metadatos.filename)
		
		# Creando los campos de la tabla Imagen_referencia_microfonos:
		
		datosArchivoRef = {}
		datosArchivoRef['grabadora_id'] = grabadoraInsertada
		datosArchivoRef['archivo'] = archivoMeta
		datosArchivoRef['archivo_nombre_original'] = formaGrabadora.vars.archivo_metadatos.filename
		
		# Insertando el registro en la base de datos:
		
		db.Archivo_referencia_grabadora.insert(**datosArchivoRef)
			
		response.flash = 'Éxito'
		
	elif formaGrabadora.errors:
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

	# De la misma manera, llenando las otras combobox:

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	listaCondicionesAmbientales = db(db.Cat_condiciones_ambientales).select(
		db.Cat_condiciones_ambientales.nombre)

	return dict(listaConglomerado=listaConglomerado,\
		listaElipsoide=listaElipsoide,\
		listaCondicionesAmbientales=listaCondicionesAmbientales)


def asignarSitios():
	
	## Función invocada mediante AJAX para llenar la combobox de número de sitio
	## a partir de los sitios existentes de un conglomerado seleccionado.

	# Obteniendo la información del conglomerado que seleccionó el usuario:
	conglomeradoElegidoID = request.vars.conglomerado_muestra_id

	# Obteniendo los sitios que existen en dicho conglomerado
	sitiosAsignados = db(
		(db.Sitio_muestra.conglomerado_muestra_id == conglomeradoElegidoID) &\
		(db.Sitio_muestra.existe == True)&\
		(db.Sitio_muestra.sitio_numero != 'Punto de control')
		).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

	#Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

	dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='sitio_muestra_id'>"

	dropdownHTML += "<option value=''/>"

	for sitio in sitiosAsignados:

		dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  
	
	dropdownHTML += "</select>"
	
	return XML(dropdownHTML)

def grabadoraExistente():

	## Función de AJAX para revisar que no se haya ingresado una grabadora en el
	## mismo sitio con anterioridad. El AJAX se activará cuando seleccionen un 
	## conglomerado y un número de sitio.

	# Obteniendo la información del sitio que seleccionó el usuario:

	sitioElegidoID = request.vars.sitio_muestra_id

	# Haciendo un query a la tabla de Grabadora con la información anterior:

	grabadoraYaInsertada=db(db.Grabadora.sitio_muestra_id==sitioElegidoID).select()

	# Regresa la longitud de grabadoraYaInsertada para que sea interpretada por JS

	return len(grabadoraYaInsertada)

def index2():

	# Controlador correspondiente a la pestaña "Archivos de audio", de la sección
	## "Grabadora":  

	camposArchivosGrabadora = [

		###########################################
		# Archivos de la grabadora
		###########################################

		#Localización de la grabadora. Por medio del conglomerado y sitio debe ser
		#posible localizar a lo más una grabadora.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
		SELECT(_name='grabadora_id',
			requires=IS_IN_DB(db,db.Grabadora.id,'%(nombre)s')),

		#Elegir si se quieren registrar archivos audiblles o ultrasónicos

		INPUT(_name='es_audible_ultrasonico',_type='string',requires=IS_NOT_EMPTY()),

		# Ahora ya no se envían los archivos a través de la forma, únicamente el
		# campo de "archivos_validados", y la información para construir la ruta
		# hacia la carpeta "nombre_aaa-mm-dd/t", donde se encuentran los archivos
		# a registrar en la base de datos.

		INPUT(_name='archivos_validados',_type='string',requires=IS_NOT_EMPTY()),
		INPUT(_name='conglomerado_muestra_nombre',_type='string',
			requires=IS_NOT_EMPTY()),
		INPUT(_name='conglomerado_muestra_fecha_visita',_type='string',
			requires=IS_NOT_EMPTY()),

		# INPUT(_name='archivos_grabadora',_type='file',requires=IS_NOT_EMPTY(),
		# 	_multiple=True)

	]

	formaArchivosGrabadora = FORM(*camposArchivosGrabadora)

	if formaArchivosGrabadora.accepts(request.vars,formname='formaArchivosGrabadoraHTML'):



		###########################################
		# Procesando los archivos múltiples capturados con una grabadora
		###########################################

		# Revisando si los archivos subidos son audibles/ultrasónicos, mediante la
		# selección del usuario:

		if (formaArchivosGrabadora.vars['es_audible_ultrasonico'] == 'audible'):

			esAudible = True

		else:

			esAudible = False
		
		#archivos = formaArchivosGrabadora.vars['archivos_grabadora']

		if not isinstance(archivos, list):
			archivos = [archivos]
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			# Descomentar ésto para que Web2py guarde el archivo en la carpeta
			# "uploads"
			#archivoGrabadora = db.Archivo_grabadora.archivo.store(aux, aux.filename)
			
			# Creando los campos de la tabla "Archivo_grabadora".

			datosArchivoGrabadora = {}
			datosArchivoGrabadora['es_audible'] = esAudible
			datosArchivoGrabadora['grabadora_id'] = formaArchivosGrabadora.vars['grabadora_id']
			datosArchivoGrabadora['archivo'] = aux.filename
			datosArchivoGrabadora['archivo_nombre_original'] = aux.filename
		
			#Insertando el registro en la base de datos:

			db.Archivo_grabadora.insert(**datosArchivoGrabadora)

		response.flash = 'Éxito'
		
	elif formaArchivosGrabadora.errors:

		response.flash = 'Hubo un error al llenar la forma'
		
	else:
		pass

	##############################################################
	# Procesando la información de la dropdown de conglomerado
	##############################################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	##############################################################
	# Creando la tabla de revisión de los registros ingresados
	##############################################################

	db.Archivo_grabadora.grabadora_id.writable = False
	grid = SQLFORM.smartgrid(db.Archivo_grabadora, orderby=~db.Archivo_grabadora.id,\
		csv = False, user_signature = False, 
		create = False, searchable = False, editable = False,
		maxtextlengths = {'Archivo_grabadora.archivo_nombre_original' : 50})

	return dict(listaConglomerado = listaConglomerado, grid = grid)

# def asignarGrabadoras():

#     # El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
#     # la grabadora asociada a un sitio (mediante AJAX).

#     sitioElegidoID = request.vars.sitio_muestra_id

#     #Obteniendo las grabadoras que han sido declaradas en dicho sitio

#     grabadorasAsignadas = db(db.Grabadora.sitio_muestra_id==sitioElegidoID).select(
#         db.Grabadora.id, db.Grabadora.nombre)

#     #Creando la dropdown de grabadoras y enviándola a la vista para que sea desplegada:

#     dropdownHTML = "<select class='generic-widget' name='grabadora_id' id='grabadora_id'>"

#     dropdownHTML += "<option value=''/>"

#     for grabadora in grabadorasAsignadas:

#         dropdownHTML += "<option value='" + str(grabadora.id) + "'>" + grabadora.nombre + "</option>"  
	
#     dropdownHTML += "</select>"
	
#     return XML(dropdownHTML)

def asignarGrabadora():

	## Función invocada mediante AJAX para de la misma manera, enviar información 
	## de la grabadora para el conglomerado y sitio seleccionados. El AJAX se
	## activará al seleccionar un sitio asociado a un conglomerado.

	# El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
	# la cámara asociada a un sitio (mediante AJAX).

	sitioElegidoID = request.vars.sitio_muestra_id

	# Obteniendo las grabadoras que han sido declaradas en dicho sitio

	grabadorasAsignadas = db(db.Grabadora.sitio_muestra_id==\
		sitioElegidoID).select(db.Grabadora.id, db.Grabadora.nombre)

	grabadora = grabadorasAsignadas.first()

	# Bajo el supuesto que sólo existe una grabadora por sitio, no se requiere
	# hacer dropdowns:

	respuestaHTML = "<p>Grabadora localizada: </p>"

	if len(grabadorasAsignadas)==0:

		respuestaHTML += "<p>No se encontró ninguna grabadora declarada en el sitio elegido</p>"

		# La vista no permitirá enviar la forma si "camara_id" está vacío.
		respuestaHTML += "<input type='hidden' name='grabadora_id' "+\
			"id='grabadora_id' value=''/>"

	else:

		respuestaHTML += "<p>" + str(grabadora.nombre) +"</p>"

		respuestaHTML += "<input type='hidden' name='grabadora_id' "+\
			"id='grabadora_id' value='" + str(grabadora.id)+ "'/>"

	return XML(respuestaHTML)

def validarArchivos():

	## Función invocada mediante AJAX cuando se presiona el botón de "validar_archivos"
	## en la forma, y se encontró un valor t para los campos: "es_audible_ultrasonico"
	## y grabadora_id" (debido a este último, deben haberse seleccionado valores
	## de "conglomerado_muestra_id" y "sitio_muestra_id"). Esta función valida:
	##	1. Que el registro de los archivos no se haya realizado con anterioridad.
	##	2. Que la carpeta nombre_cgl_aaaa-mm-dd/t exista.
	##	3. Que dicha carpeta no esté vacía

	## Regresa un JSON con:
	## 1. El mensaje apropiado en cada caso, para que la vista
	## lo alerte
	## 2. Una bandera que indica si la validación fue exitosa o no
	## 3. El "nombre" y la "fecha_visita" del conglomerado cuyo id fue recibido
	## mediante AJAX, para no tener que recalcularlos en index2().

	# Bandera que indica si los archivos fueron validados correctamente

	flag = 0

	grabadoraElegidaID = request.vars.grabadora_id

	tipoArchivo = request.vars.es_audible_ultrasonico

	# Obteniendo los archivos correspondientes a la grabadora y tipo seleccionados.
	# ésto código no puede tronar porque, gracias a la validación en la vista,
	# los valores de "grabadoraElegidaID" y "tipoArchivo" son no vacíos.

	if tipoArchivo == "audible":

		archivosGrabadora = db(
			(db.Archivo_grabadora.grabadora_id == grabadoraElegidaID) &\
			(db.Archivo_grabadora.es_audible == True)
			).select()

	else:

		archivosGrabadora = db(
			(db.Archivo_grabadora.grabadora_id == grabadoraElegidaID) &\
			(db.Archivo_grabadora.es_audible == False)
			).select()

	datosConglomeradoNombre = ""
	datosConglomeradoFechaVisita = ""

	# Generando los distintos mensajes:

	if len(archivosGrabadora) > 0:

		mensaje = "Ya se han enviado los archivos " + tipoArchivo + "s para el " +\
		"conglomerado seleccionado. Si lo necesita, borre el registro de la grabadora " +\
		"en la sección de 'Revisar registros', y vuelva a declararla"

	else:

		# Obteniendo los datos del conglomerado seleccionado, con el fin de crear
		# el path hacia la carpeta apropiada:

		conglomeradoElegidoID = request.vars.conglomerado_muestra_id

		# Obteniendo la información del conglomerado

		datosConglomeradoAux = db(
			db.Conglomerado_muestra.id == conglomeradoElegidoID).select(
			db.Conglomerado_muestra.nombre, db.Conglomerado_muestra.fecha_visita)

		datosConglomerado = datosConglomeradoAux.first()

		datosConglomeradoNombre = str(datosConglomerado['nombre'])
		datosConglomeradoFechaVisita = str(datosConglomerado['fecha_visita'])

		# Creando la ruta hacia la carpeta nombre_cgl_aaaa-mm-dd/t

		rutaCarpetaCglMuestra = eaa.crearRutaCarpeta(
			datosConglomeradoNombre,
			datosConglomeradoFechaVisita
		)

		if tipoArchivo == "audible":
			subcarpeta = "g_a"

		else:
			subcarpeta = "g_u"

		rutaT = os.path.join(rutaCarpetaCglMuestra, subcarpeta)

		#rutaTMensaje es la rutaT expresada para que el usuario la entienda

		rutaTMensaje = os.path.join(
			'conglomerados',
			datosConglomeradoNombre + '_' + datosConglomeradoFechaVisita,
			subcarpeta)

		# Verificando que dicha carpeta exista

		if not os.path.isdir(rutaT):

			mensaje = "No se encontró la carpeta " + rutaTMensaje +\
			". Favor de crearla."

		elif len(os.listdir(rutaT)) == 0:

			mensaje = "La carpeta " + rutaTMensaje + " está vacía, " +\
			"favor de agregarle los archivos " + tipoArchivo + "s"

		else:

			mensaje = "Validación exitosa para " + str(len(os.listdir(rutaT))) +\
			" archivos " + tipoArchivo + "s en: " + rutaTMensaje +\
			". Ahora puede enviar la información."
			flag = 1

	# Enviando el diccionario como JSON para que JS lo pueda interpretar
	return json.dumps(dict(
		flag = flag,
		mensaje = mensaje,
		conglomerado_muestra_nombre = datosConglomeradoNombre,
		conglomerado_muestra_fecha_visita = datosConglomeradoFechaVisita
		))



