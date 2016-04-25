# coding: utf8

# usados en "index2", "validarArchivos", "asignarInformacionArchivo"
import os 
import applications.init.modules.estructura_archivos_admin as eaa

import simplejson as json # usado en "validarArchivos"
import base64 # usado en "asignarInformacionArchivo"


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

		# Ahora ya no se envían los archivos a través de la forma, únicamente el
		# campo de "archivos_validados", y la información para construir la ruta
		# hacia la carpeta "nombre_aaa-mm-dd/c", donde se encuentran los archivos
		# a registrar en la base de datos.
		INPUT(_name='archivos_validados',_type='string',requires=IS_NOT_EMPTY()),
		INPUT(_name='conglomerado_muestra_nombre',_type='string',
			requires=IS_NOT_EMPTY()),
		INPUT(_name='conglomerado_muestra_fecha_visita',_type='string',
			requires=IS_NOT_EMPTY()),

		#INPUT(_name='archivos_camara',_type='file',requires=IS_NOT_EMPTY(),
		#	_multiple=True)
	]

	formaArchivosCamara = FORM(*camposArchivosCamara)

	if formaArchivosCamara.accepts(request.vars,formname='formaArchivosCamaraHTML'):

		###########################################
		# Procesando los archivos múltiples encontrados en la carpeta:
		# nombre_aaaa-mm-dd/c
		###########################################

		# Creando la ruta hacia la carpeta nombre_cgl_aaaa-mm-dd/c.

		rutaCarpetaCglMuestra = eaa.crearRutaCarpeta(
			str(formaArchivosCamara.vars['conglomerado_muestra_nombre']),
			str(formaArchivosCamara.vars['conglomerado_muestra_fecha_visita'])
		)

		rutaC = os.path.join(rutaCarpetaCglMuestra, 'c')

		# como ya se validó que la carpeta "nombre_aaaa-mm-dd/c" exista, la
		# siguiente instrucción no tiene por qué tronar.

		archivos = os.listdir(rutaC)
		
		#archivos = formaArchivosCamara.vars['archivos_camara']

		if not isinstance(archivos, list):
			archivos = [archivos]

		# como ya se validó que la carpeta "nombre_aaaa-mm-dd/c" sea no vacía, el
		# siguiente "for" no tiene por qué tronar.
			
		for aux in archivos:

			# Guardando el archivo en la carpeta adecuada

			# Descomentar ésto para que Web2py guarde el archivo en la carpeta
			# "uploads"
			#archivoCamara = db.Archivo_camara.archivo.store(aux, aux.filename)

			# Creando los campos de la tabla "Archivo_camara".
			
			datosArchivoCamara = {}
			datosArchivoCamara['camara_id'] = formaArchivosCamara.vars['camara_id']
			datosArchivoCamara['archivo'] = aux
			datosArchivoCamara['archivo_nombre_original'] = aux
		
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

def validarArchivos():

	## Función invocada mediante AJAX cuando se presiona el botón de "validar_archivos"
	## en la forma, y además se encuentra un valor para "camara_id" (por lo que
	## deben haberse seleccionado valores de "conglomerado_muestra_id" y
	## "sitio_muestra_id"). Esta función valida:
	##	1. Que la migración de los archivos no se haya realizado con anterioridad.
	##	2. Que la carpeta nombre_cgl_aaaa-mm-dd/c exista.
	##	3. Que dicha carpeta no esté vacía

	## Regresa un string con el mensaje apropiado en cada caso, para que la vista
	## lo alerte.

	# Bandera que indica si los archivos fueron validados correctamente

	flag = 0

	camaraElegidaID = request.vars.camara_id

	# Obteniendo los archivos correspondientes a la cámara seleccionada

	archivosCamara = db(db.Archivo_camara.camara_id == camaraElegidaID).select()

	datosConglomeradoNombre = ""
	datosConglomeradoFechaVisita = ""

	# Generando los distintos mensajes:

	if len(archivosCamara) > 0:

		mensaje = "Ya se han enviado los archivos de la cámara para el " +\
		"conglomerado seleccionado. Si lo necesita, borre el registro de la cámara " +\
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

		# Creando la ruta hacia la carpeta nombre_cgl_aaaa-mm-dd/c

		rutaCarpetaCglMuestra = eaa.crearRutaCarpeta(
			datosConglomeradoNombre,
			datosConglomeradoFechaVisita
		)

		rutaC = os.path.join(rutaCarpetaCglMuestra, 'c')

		#rutaCMensaje es la ruta C expresada para que el usuario la entienda

		rutaCMensaje = os.path.join(
			'conglomerados',
			datosConglomeradoNombre + '_' + datosConglomeradoFechaVisita,
			'c')

		# Verificando que dicha carpeta exista

		if not os.path.isdir(rutaC):

			mensaje = "No se encontró la carpeta " + rutaCMensaje +\
			". Favor de crearla."

		elif len(os.listdir(rutaC)) == 0:

			mensaje = "La carpeta " + rutaCMensaje + " está vacía, " +\
			"favor de agregarle los archivos de la cámara"

		else:

			mensaje = "Validación exitosa para " + str(len(os.listdir(rutaC))) +\
			" archivos en: " + rutaCMensaje + ". Ahora puede enviar la información."
			flag = 1

	# Enviando el diccionario como JSON para que JS lo pueda interpretar
	return json.dumps(dict(
		flag = flag,
		mensaje = mensaje,
		conglomerado_muestra_nombre = datosConglomeradoNombre,
		conglomerado_muestra_fecha_visita = datosConglomeradoFechaVisita
		))

def index3():

	## Controlador correspondiente a la pestaña "Selección de fauna", de
	## la sección "Trampa cámara". Esta función no incluye una forma, puesto que
	## cuando se presione el botón "enviar" en la vista correspondiente, la
	## información será procesada mediante AJAX, para no tener que recargar la
	## página entre información de cada fotografía.

	##############################################################
	# Procesando la información de la dropdown de conglomerado
	##############################################################

	# Regresando los nombres de todos los conglomerados insertados en la tabla de
	# conglomerado junto con sus id's para llenar la combobox de conglomerado.

	listaConglomerado = db(db.Conglomerado_muestra).select(
		db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

	return dict(listaConglomerado = listaConglomerado)

	# Obteniendo los registros en la tabla de Archivo_camara
	#fotosCamara = db(db.Archivo_camara).select()
	#return dict(fotosCamara=fotosCamara)

# Se usan la funciones: asignarSitios() y asignarCamara() definidas con anterioridad

def asignarArchivos():

	## Función invocada mediante AJAX para de la misma manera, enviar información 
	## de los archivos correspondientes a la cámara seleccionada. El AJAX se
	## activa al seleccionar un sitio asociado a un conglomerado, después de que
	## se asigna "camara_id" (también mediante AJAX).

	# El campo camara_id es únicamente auxiliar y se utiliza para buscar
	# los archivos asociados a una cámara (mediante AJAX).

	camaraElegidaID = request.vars.camara_id

	# Obteniendo los archivos correspondientes a la cámara seleccionada

	archivosCamara = db(db.Archivo_camara.camara_id == camaraElegidaID).select(
		db.Archivo_camara.id, db.Archivo_camara.archivo_nombre_original)


	if len(archivosCamara) == 0:

	# Si no encontraron archivos asociados a la cámara seleccionada:

		dropdownHTML = "<select class='generic-widget' name='archivo_camara_id' " +\
			"id='archivo_camara_id'>"

		dropdownHTML += "<option value=''/>"

		dropdownHTML += "</select>"

	else:

		# Creando la dropdown de archivos y enviándola a la vista para que sea
		# desplegada:

		dropdownHTML = "<select class='generic-widget' name='archivo_camara_id' " +\
			"id='archivo_camara_id'>"

		dropdownHTML += "<option value=''/>"

		for archivo in archivosCamara:

			dropdownHTML += "<option value='" + str(archivo.id) + "'>" +\
				archivo.archivo_nombre_original + "</option>"  
		
		dropdownHTML += "</select>"
		
	return XML(dropdownHTML)

def asignarInformacionArchivo():

	## Ésta funcion se invoca mediante AJAX, y genera una forma para
	## ingresar/modificar la información de la fotografía que seleccionó el
	## usuario en el menú desplegable. El AJAX se activa al seleccionar un
	## archivo de la lista desplegable.

	# Obteniendo la información del archivo que seleccionó el usuario:

	archivoElegidoID = request.vars.archivo_camara_id

	# Obteniendo la información del archivo

	datosArchivoAux = db(db.Archivo_camara.id == archivoElegidoID).select()

	datosArchivo = datosArchivoAux.first()

	# Creando la pantalla de revisión de archivos, considerando el caso en el
	# que datosArchivo esté vacía:

	if len(datosArchivoAux) == 0:

		revisionHTML = "<form id='forma_shadow'></form>"

	else:

		#HTML generado:

		# <form id='forma_shadow'>
		# 	<input type='hidden' name='id_archivo' value='str(datosArchivo.id)'/>

		# 	<center>
		# 		<img src='data:image/jpeg;base64,imagen_codificada'
		#		alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>
		# 	</center>
		# 	<hr/>

		# 	<div style='float:left;padding-right:60px;'>
		# 		<label for='con_fauna_evidente' style='float:left;padding-right:20px;'>
		# 			Con fauna evidente
		# 		</label>
		# 		<input type='radio' name='fauna_evidente' value='encontrada'
		#		id='con_fauna_evidente' checked='true'/>"
		# 	</div>
		# 	<div style='float:left;'>
		# 		<label for='sin_fauna_evidente' style='float:left;padding-right:20px;'>
		# 			Sin fauna evidente
		# 		</label>
		# 		<input type='radio' name='fauna_evidente' value='no_encontrada'
		#		id='sin_fauna_evidente' checked='true'/>
		# 	</div>
		# 	<div style='clear:both;'></div>
		# 	<br/>
		# 	<!--Para el fade-in/out:-->
		# 	<div id='info_fauna'>
		# 		<label for='nombre_comun' style='float:left;padding-right:49px;'>
		# 			Nombre común:
		# 		</label>
		# 		<input type='text' name='nombre_comun' class='string'
		# 		id='nombre_comun' value='datosArchivo.nombre_comun'/>
		# 		<br/>

		# 		<label for='nombre_cientifico' style='float:left;padding-right:37px;'>
		# 			Nombre científico:
		# 		</label>
		# 		<input type='text' name='nombre_cientifico' class='string'
		# 		id='nombre_cientifico' value='datosArchivo.nombre_cientifico'/>
		# 		<br/>

		# 		<label for='numero_individuos' style='float:left;padding-right:10px;'>
		# 			Número de individuos:
		# 		</label>
		# 		<input type='text' name='numero_individuos' class='integer'
		# 		id='numero_individuos' value='datosArchivo.numero_individuos'/>
		# 	</div>
		# 	<br/>
		#	<input type='button' accesskey='a' style='float:left;' value='Anterior' id='anterior'/>
		#	<input type='button' accesskey='s' style='float:right;' value='Siguiente' id='siguiente'/>
		#
		# 	<!--Se pone el center hasta el final, para que tome en cuenta el
		#	margen del elemento que flota a la derecha. -->
		#
		#	<center>
		#		<input type='button' value='Enviar' id='enviar'/>
		#	</center>
		# </form>

		# Obteniendo la información del conglomerado en el que se declararon los
		# archivos con el fin de reconstruir la ruta hacia ellos y poder visualizarlos.

		conglomeradoElegidoID = request.vars.conglomerado_muestra_id

		# Obteniendo la información del conglomerado

		datosConglomeradoAux = db(
			db.Conglomerado_muestra.id == conglomeradoElegidoID).select(
			db.Conglomerado_muestra.nombre, db.Conglomerado_muestra.fecha_visita)

		datosConglomerado = datosConglomeradoAux.first()

		datosConglomeradoNombre = str(datosConglomerado.nombre)
		datosConglomeradoFechaVisita = str(datosConglomerado.fecha_visita)

		# Creando el path hacia la imagen seleccionada (en caso de que se haya
		# seleccionado, recordar que el AJAX se activa para resetear la lista de
		# imágenes al cambiar cualquier combobox de la cascada).

		rutaCarpetaCglMuestra = eaa.crearRutaCarpeta(
			datosConglomeradoNombre,
			datosConglomeradoFechaVisita)

		pathImagen = os.path.join(rutaCarpetaCglMuestra,'c',datosArchivo.archivo)

		# Leyendo la imagen, pasándola a base 64 y guardándola en una variable
		# (hay que poner un try catch, por si no se puede leer la imagen).

		try:

			imagen = open(pathImagen, "rb")
			imagenCodificada = base64.b64encode(imagen.read())

		except:

			imagenCodificada = ""

		revisionHTML = "<form id='forma_shadow'><input type='hidden' " +\
			"name='id_archivo' value='" + str(datosArchivo.id) + "'/><center>"

		revisionHTML += "<img src='data:image/jpeg;base64," + imagenCodificada +\
			"' alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>"

		# Descomentar el código siguiente para utilizar la función download() de
		# Web2py para descargar la imagen en la vista (sólo funciona para imágenes
		# guardadas en "uploads" usando el método "store()" de Web2py.)

		#revisionHTML += "<img src='/init/02_camara/download/" + datosArchivo.archivo +\
		#    "' alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>"

		revisionHTML += "</center><hr/><div style='float:left;padding-right:60px;'>" +\
				"<label for='con_fauna_evidente' style='float:left;padding-right:20px;'>" +\
				"Con fauna evidente</label><input type='radio' name='fauna_evidente' " +\
				"value='encontrada' id='con_fauna_evidente'"

		# Si el campo de presencia de la foto elegida es True, entonces la
		# casilla "fauna evidente" aparece marcada.

		if datosArchivo.presencia:

			revisionHTML += " checked='true'/>"

		else:

			revisionHTML += "/>"

		revisionHTML += "</div><div style='float:left;'><label for='sin_fauna_evidente' " +\
			"style='float:left;padding-right:20px;'>Sin fauna evidente</label><input type='radio' " +\
			"name='fauna_evidente' value='no_encontrada' id='sin_fauna_evidente'"
		
		# Si el campo de presencia de la foto elegida es False, entonces la
		# casilla "Sin fauna evidente" aparece marcada.
		# Hay que revisar que sea igual a false, porque podría ser None.

		if datosArchivo.presencia == False:

			revisionHTML += " checked='true'/>"

		else:

			revisionHTML += "/>"

		revisionHTML += "</div><div style='clear:both;'></div><br/><div id='info_fauna'>" +\
			"<label for='nombre_comun' style='float:left;padding-right:49px;'>" +\
			"Nombre común:</label><input type='text' name='nombre_comun' class='string' " +\
			"id='nombre_comun' value='"

		#Si hay nombre común, éste aparece en la casilla para ingresar el texto.
		if datosArchivo.nombre_comun:

			revisionHTML += datosArchivo.nombre_comun

		revisionHTML += "'/><br/><label for='nombre_cientifico' " +\
			"style='float:left;padding-right:37px;'>Nombre científico:</label>" +\
			"<input type='text' name='nombre_cientifico' class='string' id='nombre_cientifico' value='"

		#Si hay nombre científico, éste aparece en la casilla para ingresar el texto.
		if datosArchivo.nombre_cientifico:

			revisionHTML += datosArchivo.nombre_cientifico

		revisionHTML += "'/><br/><label for='numero_individuos' " +\
			"style='float:left;padding-right:10px;'>Número de individuos:</label>" +\
			"<input type='text' name='numero_individuos' class='integer' id='numero_individuos' value='"

		if datosArchivo.numero_individuos:

			revisionHTML += str(datosArchivo.numero_individuos)

		revisionHTML += "'/></div><br/>" +\
			"<input type='button' accesskey='a' style='float:left;' value='Anterior' id='anterior'/>" +\
			"<input type='button' accesskey='s' style='float:right;' value='Siguiente' id='siguiente'/>" +\
			"<center><input type='button' value='Enviar' id='enviar'/></center>" +\
			"</form>"
	
	return XML(revisionHTML)

def actualizarArchivo():

	## Ésta funcion se invoca mediante AJAX, y guarda la información que se introdujo/
	## modificó en la forma generada para el archivo seleccionada. El AJAX se
	## activa al presionar el botón "Enviar" en la forma correspondiente

	# Utilizando los datos enviados de la forma_shadow, se actualiza el registro
	# de una foto en la base de datos.

	archivoElegidoID = request.vars.id_archivo
	faunaEvidente = request.vars.fauna_evidente
	nombreComun = request.vars.nombre_comun
	nombreCientifico = request.vars.nombre_cientifico
	numeroIndividuos = request.vars.numero_individuos

	# Viendo si se encontró fauna evidente, no se encontró o la foto simplemente
	# no fue revisada.
	if faunaEvidente == 'encontrada':

		db(db.Archivo_camara.id == archivoElegidoID).update(
			presencia = True,
			nombre_comun = nombreComun,
			nombre_cientifico = nombreCientifico,
			numero_individuos = numeroIndividuos
		)

	else:

		db(db.Archivo_camara.id == archivoElegidoID).update(
			presencia = False,
			nombre_comun = None,
			nombre_cientifico = None,
			numero_individuos = None)

# def download():

# 	## Esta función es de Web2py y se utiliza para visualizar las fotografías.
# 	## Hay que editarla para que funcione con la nueva política de archivos
# 	## (que no se suben a Web2py).

# 	return response.download(request, db)