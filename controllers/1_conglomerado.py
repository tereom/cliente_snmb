# coding: utf8

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)

def index():

	Campos_pestana_1= [

    # Utilizamos una FORM porque nos brinda mayor flexibilidad que una SQLFORM.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.

		###############################
		#Campos del conglomerado
		###############################

		INPUT(_name='nombre',_type='integer',requires=IS_NOT_EMPTY()),
		INPUT(_name='fecha_visita',_type='date',requires=IS_NOT_EMPTY()),
		SELECT(_name='tipo',
			requires=IS_IN_DB(db,db.Cat_tipo_conglomerado.id,'%(nombre)s')),
    	SELECT(_name='estado',
    		requires=IS_IN_DB(db,db.Cat_estado_conglomerado.id,'%(nombre)s')),
    	SELECT(_name='municipio',
    		requires=IS_IN_DB(db,db.Cat_municipio_conglomerado.id,'%(nombre)s')),
    	INPUT(_name='predio',_type='string',requires=IS_NOT_EMPTY()),
    	SELECT(_name='tenencia',
    		requires=IS_IN_DB(db,db.Cat_tenencia_conglomerado.id,'%(nombre)s')),
    	SELECT(_name='uso_suelo_tipo',
    		requires=IS_IN_DB(db,db.Cat_suelo_conglomerado.id,'%(nombre)s')),

    	#El campo de vegetación_tipo posiblemente se envíe vacío de la vista (si
    	#vegetación no es el uso de suelo principal), por ello, conviene ponerlo
    	#como un entero, para que no requiera que esté en la base de datos (y
    	#por ende, no vacío).
		INPUT(_name='vegetacion_tipo',_type='integer'),

    	INPUT(_name='perturbado',_type='boolean'),
		INPUT(_name='comentario',_type='text'),

		################################
		#Campos del sitio 1 (centro)
		###############################

		# El centro del conglomerado y el punto de control siempre existen.
		
    	INPUT(_name='lat_grado_1',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_min_1',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_seg_1',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_grado_1',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_min_1',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_seg_1',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='altitud_1',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='gps_error_1',_type='double',requires=IS_NOT_EMPTY()),
    	SELECT(_name='elipsoide_1',
		requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')),
    	INPUT(_name='hay_evidencia_1',_type='boolean'),
    	
     	###########Imagen############
		INPUT(_name='imagen_1',_type='file',requires=IS_NOT_EMPTY()),
		 	
		###############################
		#Campos del sitio 2
		###############################
			
		INPUT(_name='existe_2',_type='boolean'),

		#Como el campo 2 puede no existir, no se pueden pedir como obligatorios
		#los siguientes campos (sin embargo, el validador de la vista se encar-
		#gará de que los llenen en caso de que sí)
    	INPUT(_name='lat_grado_2',_type='integer'),
    	INPUT(_name='lat_min_2',_type='integer'),
    	INPUT(_name='lat_seg_2',_type='double'),
    	INPUT(_name='lon_grado_2',_type='integer'),
    	INPUT(_name='lon_min_2',_type='integer'),
    	INPUT(_name='lon_seg_2',_type='double'),
    	INPUT(_name='altitud_2',_type='double'),
    	INPUT(_name='gps_error_2',_type='double'),

    	#El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
    	#conviene ponerlo como un entero, para que no requiera que esté en la
    	#base de datos (y por ende, no vacío).
    	INPUT(_name='elipsoide_2',_type='integer'),          
    	INPUT(_name='hay_evidencia_2',_type='boolean'),
    	
     	###########Imagen############
		INPUT(_name='imagen_2',_type='file'),
 
		###############################
		#Campos del sitio 3
		###############################
	
		INPUT(_name='existe_3',_type='boolean'),

		#Como el campo 3 puede no existir, no se pueden pedir como obligatorios
		#los siguientes campos (sin embargo, el validador de la vista se encar-
		#gará de que los llenen)
    	INPUT(_name='lat_grado_3',_type='integer'),
    	INPUT(_name='lat_min_3',_type='integer'),
    	INPUT(_name='lat_seg_3',_type='double'),
    	INPUT(_name='lon_grado_3',_type='integer'),
    	INPUT(_name='lon_min_3',_type='integer'),
    	INPUT(_name='lon_seg_3',_type='double'),
    	INPUT(_name='altitud_3',_type='double'),
    	INPUT(_name='gps_error_3',_type='double'),

    	#El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
    	#conviene ponerlo como un entero, para que no requiera que esté en la
    	#base de datos (y por ende, no vacío).
    	INPUT(_name='elipsoide_3',_type='integer'),
    	INPUT(_name='hay_evidencia_3',_type='boolean'),
    	
     	###########Imagen############
		INPUT(_name='imagen_3',_type='file'),

		###############################
		#Campos del sitio 4
		###############################
	
		INPUT(_name='existe_4',_type='boolean'),

		#Como el campo 4 puede no existir, no se pueden pedir como obligatorios
		#los siguientes campos (sin embargo, el validador de la vista se encar-
		#gará de que los llenen)
    	INPUT(_name='lat_grado_4',_type='integer'),
    	INPUT(_name='lat_min_4',_type='integer'),
    	INPUT(_name='lat_seg_4',_type='double'),
    	INPUT(_name='lon_grado_4',_type='integer'),
    	INPUT(_name='lon_min_4',_type='integer'),
    	INPUT(_name='lon_seg_4',_type='double'),
    	INPUT(_name='altitud_4',_type='double'),
    	INPUT(_name='gps_error_4',_type='double'),

    	#El campo de elipsoide posiblemente se envíe vacío de la vista, por ello,
    	#conviene ponerlo como un entero, para que no requiera que esté en la
    	#base de datos (y por ende, no vacío).
    	INPUT(_name='elipsoide_4',_type='integer'),
    	INPUT(_name='hay_evidencia_4',_type='boolean'),
    	
     	###########Imagen############
		INPUT(_name='imagen_4',_type='file'),

		###############################
		#Campos del punto de control
		###############################

		# El centro del conglomerado y el punto de control siempre existen.
		
    	INPUT(_name='lat_grado_c',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_min_c',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_seg_c',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_grado_c',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_min_c',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_seg_c',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='altitud_c',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='gps_error_c',_type='double',requires=IS_NOT_EMPTY()),
    	SELECT(_name='elipsoide_c',
		requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')),          
    	INPUT(_name='hay_evidencia_c',_type='boolean'),
    	
     	###########Imagen############
		INPUT(_name='imagen_c',_type='file',requires=IS_NOT_EMPTY()),
		 	
	##Cerrando la lista de campos para el formulario
	]

	forma = FORM(*Campos_pestana_1)

	if forma.accepts(request.vars,formname='formaHTML'):

	##################Procesando los datos del conglomerado######################
		
		datosConglomerado=db.Conglomerado_muestra._filter_fields(forma.vars)

		ID_suelo_vegetacion = db(db.Cat_suelo_conglomerado.nombre=='Vegetación'
			).select().first().id
  		
        #Casteando para asegurarnos que la comparación sea entre enteros.

        #Si no escogieron "uso_suelo_tipo" como "Vegetación", entonces anulamos
        #(por consistencia en base de datos), los valores que se pudieran haber
        #ingresado en los datos dependientes de esta opción:

		if int(datosConglomerado['uso_suelo_tipo'])!=int(ID_suelo_vegetacion):

			datosConglomerado['vegetacion_tipo']=None
			datosConglomerado['perturbado']=None

		#Si escogieron "uso_suelo_tipo" como "Vegetación" y no marcaron la casilla
        #de perturbado, entonces hay que asignarle "False" a esta, para diferen-
        #ciarla de cuando no es requerida.

		elif not(bool(datosConglomerado['perturbado'])):
		
			datosConglomerado['perturbado']=False
			
		#Insertando en la base de datos:
		conglomeradoInsertado = db.Conglomerado_muestra.insert(**datosConglomerado)
		
		################Procesando los datos del sitio 1##############################

		#Agregando los datos que no se pidieron al usuario:
		
		formaSitio1 = {}
		
		formaSitio1['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitio1['sitio_numero']=1
		formaSitio1['existe']=True
		
		#Leyendo los datos del formulario:
		formaSitio1['lat_grado']=forma.vars['lat_grado_1']
		formaSitio1['lat_min']=forma.vars['lat_min_1']
		formaSitio1['lat_seg']=forma.vars['lat_seg_1']
		formaSitio1['lon_grado']=forma.vars['lon_grado_1']
		formaSitio1['lon_min']=forma.vars['lon_min_1']
		formaSitio1['lon_seg']=forma.vars['lon_seg_1']
		formaSitio1['altitud']=forma.vars['altitud_1']
		formaSitio1['gps_error']=forma.vars['gps_error_1']
		formaSitio1['elipsoide']=forma.vars['elipsoide_1']
		
		#Si hay evidencia, entonces True se guarda en la base de datos, en caso contrario,
		#se tiene que guardar manualmente False, pues si no, Web2py guarda Null.
		if bool(forma.vars['hay_evidencia_1']):
			formaSitio1['hay_evidencia']=forma.vars['hay_evidencia_1']
		else:
			formaSitio1['hay_evidencia']=False
			
		#Insertando en la base de datos:
		sitio1Insertado = db.Sitio_muestra.insert(**formaSitio1)

		################Procesando la imagen 1##########################################
		
		#Guardando la imagen de referencia en la carpeta adecuada
		imagen1 = db.Imagen_referencia_sitio.archivo.store(
            forma.vars.imagen_1.file, forma.vars.imagen_1.filename)
        
		#Creando los campos de la tabla Imagen_referencia_sitio:

		datosImagen1 = {}
		datosImagen1['sitio_muestra_id'] = sitio1Insertado
		datosImagen1['archivo'] = imagen1
		datosImagen1['archivo_nombre_original'] = forma.vars.imagen_1.filename
		
		#Insertando el registro en la base de datos:
		
		db.Imagen_referencia_sitio.insert(**datosImagen1)
			
		################Procesando los datos del sitio 2##############################

		#Agregando los datos que no se pidieron al usuario:
		
		formaSitio2 = {}
		formaSitio2['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitio2['sitio_numero']=2
		
		#Si existe el sitio 2:
		if bool(forma.vars['existe_2']):

			#Agregando los datos extraídos de la forma:
			formaSitio2['existe']=forma.vars['existe_2']
			formaSitio2['lat_grado']=forma.vars['lat_grado_2']
			formaSitio2['lat_min']=forma.vars['lat_min_2']
			formaSitio2['lat_seg']=forma.vars['lat_seg_2']
			formaSitio2['lon_grado']=forma.vars['lon_grado_2']
			formaSitio2['lon_min']=forma.vars['lon_min_2']
			formaSitio2['lon_seg']=forma.vars['lon_seg_2']
			formaSitio2['altitud']=forma.vars['altitud_2']
			formaSitio2['gps_error']=forma.vars['gps_error_2']
			formaSitio2['elipsoide']=forma.vars['elipsoide_2']
			
			if bool(forma.vars['hay_evidencia_2']):
				formaSitio2['hay_evidencia']=forma.vars['hay_evidencia_2']
			else:
				formaSitio2['hay_evidencia']=False
				
		else:
			formaSitio2['existe']=False
		
		#Insertando en la base de datos:
		sitio2Insertado=db.Sitio_muestra.insert(**formaSitio2)		

		################Procesando la imagen 2##########################################
		
		if bool(forma.vars['existe_2']):
						
			#Guardando la imagen de referencia en la carpeta adecuada
			imagen2 = db.Imagen_referencia_sitio.archivo.store(
            	forma.vars.imagen_2.file, forma.vars.imagen_2.filename)
		
			#Creando los campos de la tabla Imagen_referencia_sitio:

			datosImagen2 = {}
			datosImagen2['sitio_muestra_id'] = sitio2Insertado
			datosImagen2['archivo'] = imagen2
			datosImagen2['archivo_nombre_original'] = forma.vars.imagen_2.filename
		
			#Insertando el registro en la base de datos:
		
			db.Imagen_referencia_sitio.insert(**datosImagen2)

		################Procesando los datos del sitio 3##############################

		#Agregando los datos que no se pidieron al usuario:
		
		formaSitio3 = {}
		formaSitio3['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitio3['sitio_numero']=3
		
		#Si existe el sitio 3:
		if bool(forma.vars['existe_3']):

			#Agregando los datos extraídos de la forma:
			formaSitio3['existe']=forma.vars['existe_3']
			formaSitio3['lat_grado']=forma.vars['lat_grado_3']
			formaSitio3['lat_min']=forma.vars['lat_min_3']
			formaSitio3['lat_seg']=forma.vars['lat_seg_3']
			formaSitio3['lon_grado']=forma.vars['lon_grado_3']
			formaSitio3['lon_min']=forma.vars['lon_min_3']
			formaSitio3['lon_seg']=forma.vars['lon_seg_3']
			formaSitio3['altitud']=forma.vars['altitud_3']
			formaSitio3['gps_error']=forma.vars['gps_error_3']
			formaSitio3['elipsoide']=forma.vars['elipsoide_3']
			
			if bool(forma.vars['hay_evidencia_3']):
				formaSitio3['hay_evidencia']=forma.vars['hay_evidencia_3']
			else:
				formaSitio3['hay_evidencia']=False
				
		else:
			formaSitio3['existe']=False
		
		#Insertando en la base de datos:
		sitio3Insertado=db.Sitio_muestra.insert(**formaSitio3)
		
		################Procesando la imagen 3##########################################
		
		if bool(forma.vars['existe_3']):
						
			#Guardando la imagen de referencia en la carpeta adecuada
			imagen3 = db.Imagen_referencia_sitio.archivo.store(
            	forma.vars.imagen_3.file, forma.vars.imagen_3.filename)
        
			#Creando los campos de la tabla Imagen_referencia_sitio:
		
			datosImagen3 = {}
			datosImagen3['sitio_muestra_id'] = sitio3Insertado
			datosImagen3['archivo'] = imagen3
			datosImagen3['archivo_nombre_original'] = forma.vars.imagen_3.filename
		
			#Insertando el registro en la base de datos:
		
			db.Imagen_referencia_sitio.insert(**datosImagen3)

		################Procesando los datos del sitio 4##############################

		#Agregando los datos que no se pidieron al usuario:
		
		formaSitio4 = {}
		formaSitio4['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitio4['sitio_numero']=4
		
		#Si existe el sitio 4:
		if bool(forma.vars['existe_4']):

			#Agregando los datos extraídos de la forma:
			formaSitio4['existe']=forma.vars['existe_4']
			formaSitio4['lat_grado']=forma.vars['lat_grado_4']
			formaSitio4['lat_min']=forma.vars['lat_min_4']
			formaSitio4['lat_seg']=forma.vars['lat_seg_4']
			formaSitio4['lon_grado']=forma.vars['lon_grado_4']
			formaSitio4['lon_min']=forma.vars['lon_min_4']
			formaSitio4['lon_seg']=forma.vars['lon_seg_4']
			formaSitio4['altitud']=forma.vars['altitud_4']
			formaSitio4['gps_error']=forma.vars['gps_error_4']
			formaSitio4['elipsoide']=forma.vars['elipsoide_4']
			
			if bool(forma.vars['hay_evidencia_4']):
				formaSitio4['hay_evidencia']=forma.vars['hay_evidencia_4']
			else:
				formaSitio4['hay_evidencia']=False
				
		else:
			formaSitio4['existe']=False
		
		#Insertando en la base de datos:
		sitio4Insertado=db.Sitio_muestra.insert(**formaSitio4)
		
		################Procesando la imagen 4##########################################
		
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


		################Procesando los datos del punto de control#########################

		#Agregando los datos que no se pidieron al usuario:
		
		formaSitioC = {}
		formaSitioC['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitioC['sitio_numero']=5
		formaSitioC['existe']=True
		
		#Leyendo los datos del formulario:
		formaSitioC['lat_grado']=forma.vars['lat_grado_c']
		formaSitioC['lat_min']=forma.vars['lat_min_c']
		formaSitioC['lat_seg']=forma.vars['lat_seg_c']
		formaSitioC['lon_grado']=forma.vars['lon_grado_c']
		formaSitioC['lon_min']=forma.vars['lon_min_c']
		formaSitioC['lon_seg']=forma.vars['lon_seg_c']
		formaSitioC['altitud']=forma.vars['altitud_c']
		formaSitioC['gps_error']=forma.vars['gps_error_c']
		formaSitioC['elipsoide']=forma.vars['elipsoide_c']
		
		if bool(forma.vars['hay_evidencia_c']):
			formaSitioC['hay_evidencia']=forma.vars['hay_evidencia_c']
		else:
			formaSitioC['hay_evidencia']=False
			
		#Insertando en la base de datos:
		sitioCInsertado=db.Sitio_muestra.insert(**formaSitioC)
		
		################Procesando la imagen del control##########################################
		
		#Guardando la imagen de referencia en la carpeta adecuada
		imagenC = db.Imagen_referencia_sitio.archivo.store(
            forma.vars.imagen_c.file, forma.vars.imagen_c.filename)
        
		#Creando los campos de la tabla Imagen_referencia_sitio:
		
		datosImagenC = {}
		datosImagenC['sitio_muestra_id'] = sitioCInsertado
		datosImagenC['archivo'] = imagenC
		datosImagenC['archivo_nombre_original'] = forma.vars.imagen_c.filename
		
		#Insertando el registro en la base de datos:
		
		db.Imagen_referencia_sitio.insert(**datosImagenC)

		response.flash = 'Éxito'
        
	elif forma.errors:

		response.flash = 'Hubo un error al llenar la forma'
       
	else:
		response.flash ='Por favor, introduzca los datos del conglomerado y sitios'

    ##########Enviando la información de las dropdowns##########################

    #Llenando las combobox de tipo de conglomerado, estado, tenencia, principal
    #uso de suelo, tipo de vegetación y datum

	listaTipo = db(db.Cat_tipo_conglomerado).select(
        db.Cat_tipo_conglomerado.id, db.Cat_tipo_conglomerado.nombre)

	listaEstado = db(db.Cat_estado_conglomerado).select(
        db.Cat_estado_conglomerado.id, db.Cat_estado_conglomerado.nombre)

	listaTenencia = db(db.Cat_tenencia_conglomerado).select(
        db.Cat_tenencia_conglomerado.id, db.Cat_tenencia_conglomerado.nombre)

	listaUsoSuelo = db(db.Cat_suelo_conglomerado).select(
    	db.Cat_suelo_conglomerado.id, db.Cat_suelo_conglomerado.nombre)

	listaVegetacion = db(db.Cat_vegetacion_conglomerado).select(
    	db.Cat_vegetacion_conglomerado.id, db.Cat_vegetacion_conglomerado.nombre)

	listaElipsoide = db(db.Cat_elipsoide).select(
        db.Cat_elipsoide.id, db.Cat_elipsoide.nombre)

	return dict(listaTipo=listaTipo,\
        listaEstado=listaEstado,\
        listaTenencia=listaTenencia,\
        listaUsoSuelo=listaUsoSuelo,\
        listaVegetacion=listaVegetacion,\
        listaElipsoide=listaElipsoide)

#La siguiente función es invocada mediante AJAX para llenar la combobox de municipio
# a partir del estado seleccionado.

def asignarMunicipios():

	#Obteniendo la información del estado que seleccionó el usuario:
    estadoElegidoID = request.vars.estado

    #Obteniendo la clave de dicho estado:
    estadoElegidoClave = db(db.Cat_estado_conglomerado.id==estadoElegidoID
    	).select().first().clave_ent

    #Obteniendo los municipios que existen en dicho estado a partir de la clave
    municipiosAsignados = db(
    	db.Cat_municipio_conglomerado.clave_ent==estadoElegidoClave
        ).select(db.Cat_municipio_conglomerado.nombre,db.Cat_municipio_conglomerado.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='municipio' id='tabla_municipio'>"

    for municipio in municipiosAsignados:

		dropdownHTML += "<option value='" + str(municipio.id) + "'>" + municipio.nombre + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)

#AJAX para revisar que no se haya ingresado el mismo conglomerado con anterioridad.
#El AJAX se activará cuando escriban un caracter del nombre de conglomerado.

def conglomeradoExistente():

    #Obteniendo la información del conglomerado que ha ingresado el usuario.
    #Puede ser que no haya terminado de escribir, por ello, se revisa primero
    #la longitud del caracter:

    longitudNombres = 5

    #El resultado en el tercer caso será el número de registros en la base de
    #datos con el mismo nombre de conglomerado, que se regresará a JS para
    #su interpretación:

    if (len(request.vars.nombre) < longitudNombres):
    	resultado = 0

    elif (len(request.vars.nombre) > longitudNombres):
    	resultado = -1

    else:

    	conglomeradoElegidoNombre = request.vars.nombre

    #Haciendo un query a la tabla de Conglomerado_muestra con la
    #información anterior:

    	conglomeradoYaInsertado=db(
    		db.Conglomerado_muestra.nombre==conglomeradoElegidoNombre).select()

    #regresa la longitud de conglomeradoYaInsertado para que sea interpretada por JS

    	resultado = len(conglomeradoYaInsertado)

    return resultado
