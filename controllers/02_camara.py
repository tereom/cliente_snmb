# coding: utf8
def index1():

	## Controlador correspondiente a la pestaña "Información de la trampa cámara",
	## de la sección "Trampa cámara"

	camposCamara = [
	
		###########################################
		# Cámara
		###########################################

		# Datos para localizar un sitio único y asociarle la cámara a éste.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
		
		# Datos de la cámara

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

		INPUT(_name='distancia_centro',_type='double'),
		INPUT(_name='azimut',_type='double'),
		SELECT(_name='resolucion',
			requires=IS_IN_DB(db,db.Cat_resolucion_camara.nombre,'%(nombre)s')),
		SELECT(_name='sensibilidad',
			requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.nombre,'%(nombre)s')),
		SELECT(_name='condiciones_ambientales',requires=
			IS_IN_DB(db,db.Cat_condiciones_ambientales.nombre,'%(nombre)s')),

		TEXTAREA(_name='comentario',_type='text'),

		###########################################
		# Imagen de referencia de la cámara
		###########################################

		INPUT(_name='imagen_camara',_type='file',requires=IS_NOT_EMPTY()),

	]

	formaCamara = FORM(*camposCamara)

	if formaCamara.accepts(request.vars,formname='formaCamaraHTML'):
	
		###########################################
		# Procesando los datos de la cámara
		###########################################
	
		# Filtrando los datos correspondientes a la tabla de la cámara:
		datosCamara = db.Camara._filter_fields(formaCamara.vars)

		# Guardando el registro de la cámara en la base de datos:
		camaraInsertada = db.Camara.insert(**datosCamara)
		
		###########################################
		# Procesando la imagen de referencia de la cámara
		###########################################
		
		# Guardando la imagen de referencia en la carpeta adecuada

		imagenRef = db.Imagen_referencia_camara.archivo.store(
			formaCamara.vars.imagen_camara.file, formaCamara.vars.imagen_camara.filename)
		
		# Creando los campos de la tabla Imagen_referencia_camara:
		
		datosImagenRef = {}
		datosImagenRef['camara_id'] = camaraInsertada
		datosImagenRef['archivo'] = imagenRef
		datosImagenRef['archivo_nombre_original'] = formaCamara.vars.imagen_camara.filename
		
		# Insertando el registro en la base de datos:
		
		db.Imagen_referencia_camara.insert(**datosImagenRef)
			
		response.flash = 'Éxito'
		
	elif formaCamara.errors:
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

	listaResolucion = db(db.Cat_resolucion_camara).select(db.Cat_resolucion_camara.nombre)

	listaSensibilidad = db(db.Cat_sensibilidad_camara).select(db.Cat_sensibilidad_camara.nombre)

	listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)

	listaCondicionesAmbientales = db(db.Cat_condiciones_ambientales).select(
		db.Cat_condiciones_ambientales.nombre)

	return dict(listaConglomerado = listaConglomerado,\
		listaResolucion = listaResolucion,\
		listaSensibilidad = listaSensibilidad,\
		listaElipsoide = listaElipsoide,\
		listaCondicionesAmbientales = listaCondicionesAmbientales)

def asignarSitios():

	## Función invocada mediante AJAX para llenar la combobox "sitio_muestra_id"
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

def camaraExistente():

	## Función de AJAX para revisar que no se haya ingresado una cámara en el
	## mismo sitio con anterioridad. El AJAX se activará cuando seleccionen un 
	## conglomerado y un número de sitio.
	
	# Obteniendo la información del sitio que seleccionó el usuario:

	sitioElegidoID = request.vars.sitio_muestra_id

	# Haciendo un query a la tabla de Camara con la información anterior:

	camaraYaInsertada = db(db.Camara.sitio_muestra_id == sitioElegidoID).select()

	# Regresa la longitud de camaraYaInsertada para que sea interpretada por JS

	return len(camaraYaInsertada)

def index2():

	## Controlador correspondiente a la pestaña "Archivos trampa cámara", de
	## la sección "Trampa cámara"

	camposArchivosCamara = [

		###########################################
		# Archivos de la cámara
		###########################################

		# Localización de la cámara. Por medio del conglomerado y sitio debe ser
		# posible localizar a lo más una cámara.

		SELECT(_name='conglomerado_muestra_id',
			requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		SELECT(_name='sitio_muestra_id',
			requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
		SELECT(_name='camara_id',
			requires=IS_IN_DB(db,db.Camara.id,'%(nombre)s')),

		INPUT(_name='archivos_camara',_type='file',requires=IS_NOT_EMPTY(),
			_multiple=True)
	]

	formaArchivosCamara = FORM(*camposArchivosCamara)

	if formaArchivosCamara.accepts(request.vars,formname='formaArchivosCamaraHTML'):

		###########################################
		# Procesando los archivos múltiples capturados con una cámara
		###########################################
		
		archivos = formaArchivosCamara.vars['archivos_camara']

		if not isinstance(archivos, list):
			archivos = [archivos]
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			archivoCamara = db.Archivo_camara.archivo.store(aux, aux.filename)

			# Creando los campos de la tabla "Archivo_camara".
			
			datosArchivoCamara = {}
			datosArchivoCamara['camara_id'] = formaArchivosCamara.vars['camara_id']
			datosArchivoCamara['archivo'] = archivoCamara
			datosArchivoCamara['archivo_nombre_original'] = aux.filename
		
			# Insertando el registro en la base de datos:

			db.Archivo_camara.insert(**datosArchivoCamara)

		response.flash = 'Éxito'
		
	elif formaArchivosCamara.errors:
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

	db.Archivo_camara.camara_id.writable = False
	grid = SQLFORM.smartgrid(db.Archivo_camara, orderby =~ db.Archivo_camara.id,\
		csv = False, user_signature = False, 
		create = False, searchable = False, editable = False,
		maxtextlengths = {'Archivo_camara.archivo_nombre_original' : 50})

	return dict(listaConglomerado = listaConglomerado, grid = grid)

# La siguiente función es para generar una combobox de cámaras por sitio, es decir,
# sirve mejor para cuando hay más de una cámara declarada en un sitio.

# def asignarCamaras():

#     # El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
#     # la cámara asociada a un sitio (mediante AJAX).

#     sitioElegidoID = request.vars.sitio_muestra_id

#     # Obteniendo las cámaras que han sido declaradas en dicho sitio

#     camarasAsignadas = db(db.Camara.sitio_muestra_id == sitioElegidoID).select(
#         db.Camara.id, db.Camara.nombre)

#     #Creando la dropdown de cámaras y enviándola a la vista para que sea desplegada:

#     dropdownHTML = "<select class='generic-widget' name='camara_id' id='camara_id'>"

#     dropdownHTML += "<option value=''/>"

#     for camara in camarasAsignadas:

#         dropdownHTML += "<option value='" + str(camara.id) + "'>" + camara.nombre + "</option>"  
	
#     dropdownHTML += "</select>"
	
#     return XML(dropdownHTML)

def asignarCamara():
	
	## Función invocada mediante AJAX para de la misma manera, enviar información 
	## de la trampa cámara para el conglomerado y sitio seleccionados. El AJAX se
	## activará al seleccionar un sitio asociado a un conglomerado.

	# El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
	# la cámara asociada a un sitio (mediante AJAX).

	sitioElegidoID = request.vars.sitio_muestra_id

	# Obteniendo las cámaras que han sido declaradas en dicho sitio

	camarasAsignadas = db(db.Camara.sitio_muestra_id ==\
		sitioElegidoID).select(db.Camara.id, db.Camara.nombre)

	camara = camarasAsignadas.first()

	# Bajo el supuesto que sólo existe una cámara por sitio, no se requiere
	# hacer dropdowns:

	respuestaHTML = "<p>Cámara localizada: </p>"

	if len(camarasAsignadas) == 0:

		respuestaHTML += "<p>No se encontró ninguna cámara declarada en el sitio elegido</p>"

		# La vista no permitirá enviar la forma si "camara_id" está vacío.
		respuestaHTML += "<input type='hidden' name='camara_id' "+\
			"id='camara_id' value=''/>"

	else:

		respuestaHTML += "<p>" + str(camara.nombre) +"</p>"

		respuestaHTML += "<input type='hidden' name='camara_id' "+\
			"id='camara_id' value='" + str(camara.id)+ "'/>"

	return XML(respuestaHTML)

