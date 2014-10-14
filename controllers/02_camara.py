# coding: utf8
def index1(): 

    camposCamara = [
    
        # campos cámara
            
        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada y la subida de múltiples archivos.
        
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        # de datos y así, evitar excepciones.
        
        #Datos para localizar un sitio único y asociarle la cámara a éste.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
        
    	#Datos de la cámara
        SELECT(_name='nombre',
            requires=IS_IN_DB(db,db.Cat_nombre_camara.nombre,'%(nombre)s')),  
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

        INPUT(_name='distancia_centro',_type='double',requires=IS_NOT_EMPTY()),
        SELECT(_name='resolucion',
            requires=IS_IN_DB(db,db.Cat_resolucion_camara.nombre,'%(nombre)s')),
        SELECT(_name='sensibilidad',
            requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.nombre,'%(nombre)s')),
        INPUT(_name='llovio',_type='boolean'),

        TEXTAREA(_name='comentario',_type='text'),

        ###########Imagen de referencia############
        INPUT(_name='imagen_camara',_type='file',requires=IS_NOT_EMPTY()),

    ]

    formaCamara = FORM(*camposCamara)

    if formaCamara.accepts(request.vars,formname='formaCamaraHTML'):
    
    	################Procesando la cámara#################################
    
    	#Filtrando los datos correspondientes a la tabla de la cámara:
        datosCamara = db.Camara._filter_fields(formaCamara.vars)
                
        #Guardando el registro de la cámara en la base de datos:
        
        camaraInsertada = db.Camara.insert(**datosCamara)
        
		################Procesando la imagen de referencia#################################
		
		#Guardando la imagen de referencia en la carpeta adecuada
        imagenRef = db.Imagen_referencia_camara.archivo.store(
            formaCamara.vars.imagen_camara.file, formaCamara.vars.imagen_camara.filename)
        
		#Creando los campos de la tabla Imagen_referencia_camara:
		
        datosImagenRef = {}
        datosImagenRef['camara_id'] = camaraInsertada
        datosImagenRef['archivo'] = imagenRef
        datosImagenRef['archivo_nombre_original'] = formaCamara.vars.imagen_camara.filename
		
		#Insertando el registro en la base de datos:
		
        db.Imagen_referencia_camara.insert(**datosImagenRef)
        	
        response.flash = 'Éxito'
        
    elif formaCamara.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
    	response.flash ='Por favor, introduzca los datos de la cámara'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando las combobox de nombre y elipsoide:

    listaNombreCamara = db(db.Cat_nombre_camara).select(db.Cat_nombre_camara.nombre)

    listaResolucion = db(db.Cat_resolucion_camara).select(db.Cat_resolucion_camara.nombre)

    listaSensibilidad = db(db.Cat_sensibilidad_camara).select(db.Cat_sensibilidad_camara.nombre)

    listaElipsoide = db(db.Cat_elipsoide).select(db.Cat_elipsoide.nombre)


    return dict(listaConglomerado=listaConglomerado,\
        listaNombreCamara=listaNombreCamara,\
        listaResolucion=listaResolucion,\
        listaSensibilidad=listaSensibilidad,\
        listaElipsoide=listaElipsoide)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de sitio a partir de los sitios existentes de un conglomerado seleccionado.

def asignarSitios():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='tabla_sitio_muestra_id'>"

    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)

#AJAX para revisar que no se haya ingresado una cámara en el mismo sitio con
#anterioridad.
#El AJAX se activará cuando seleccionen un conglomerado y un número de sitio.

def camaraExistente():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Camara con la información anterior:

    camaraYaInsertada=db(db.Camara.sitio_muestra_id==sitioElegidoID).select()

    #regresa la longitud de camaraYaInsertada para que sea interpretada por JS

    return len(camaraYaInsertada)

# AQUÍ SURGE UNA CUESTIÓN: PARA PODER VALIDAR LA UNICIDAD DE LA CÁMARA,
# NECESITAMOS UN TRIGGER "ON CHANGE". SIN EMBARGO, PARA PODER HACER ESTO BIEN
# REQUERIMOS INCLUIR UN ESPACIO EN BLANCO POR DEFAULT EN LAS COMBOBOX GENERADAS
# MEDIANTE AJAX, CON LO QUE SURGE LA CUESTIÓN DE VALIDARLAS, Y NECESITAMOS UNA
# FUNCIÓN DE JQUERY DISTINTA PARA PODER PEGARLES A LOS ELEMENTOS QUE NO EXISTEN
# DESDE UN PRINCIPIO.

def index2():

    camposArchivosCamara = [

        #Localización de la cámara. Por medio de estos datos debe ser posible
        #localizar una única cámara:

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='camara_id',
            requires=IS_IN_DB(db,db.camara.id,'%(nombre)s')),

        ###########Archivos de la cámara###########
        INPUT(_name='archivos_camara',_type='file',requires=IS_NOT_EMPTY(),
            _multiple=True)

    ]

    formaArchivosCamara = FORM(*camposArchivosCamara)

    if formaArchivosCamara.accepts(request.vars,formname='formaArchivosCamaraHTML'):

    ################Procesando los archivos múltiples###########################
        
        archivos = formaArchivosCamara.vars['archivos_camara']

        if not isinstance(archivos, list):
        
          archivos = [archivos]
            
        for aux in archivos:

            #Guardando el archivo en la carpeta adecuada
          archivoCamara = db.Archivo_camara.archivo.store(aux, aux.filename)
            
          datosArchivoCamara = {}
          datosArchivoCamara['camara_id'] = formaArchivosCamara.vars['camara_id']
          datosArchivoCamara['archivo'] = archivoCamara
          datosArchivoCamara['archivo_nombre_original'] = aux.filename
        
          #Insertando el registro en la base de datos:

          db.Archivo_camara.insert(**datosArchivoCamara)

        response.flash = 'Éxito'
        
    elif formaCamara.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los archivos asociados a una cámara'

    ##########Enviando la información de la dropdown de conglomerado############

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

def asignarCamara():

    # El campo conglomerado_muestra_id es únicamente auxiliar y se utiliza para:
    # 1. Mediante AJAX, buscar los sitios asociados a un conglomerado.
    # 2. Utilizando dichos sitios, buscar en la lista de cámara,
    # para ver en cuáles de dichos sitios existe una cámara declarada. Mostrar
    # en la vista los sitios, pero enviar al controlador los id's de las cámaras
    # asociadas a cada sitio.

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Bandera que indica si se encontró alguna cámara declarada en alguno de
    #los sitios del conglomerado elegido:

    flag = False

    #Creando la dropdown de sitios/cámaras y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='camara_id' id='tabla_camara_id'>"
    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        #Buscando, de entre los sitios de un conglomerado, en cuáles ha sido
        #declarada una cámara. En caso de que no ocurra para ningún sitio,
        #se enviará un mensaje (para ello se utiliza la bandera).

        camaraSitio = db(db.Camara.sitio_muestra_id==sitio.id).select(
            db.Camara.id).first()

        if len(camaraSitio)>1:

            flag = True

            #Como cuidamos que exista a lo más una cámara por sitio de un conglome-
            #rado, al elegir el conglomerado y el número de sitio, automática-
            #mente sabemos la cámara a la que corresponde, sin embargo, para el
            #usuario mandamos el número de sitio del conglomerado elegido,
            #mientras que para el controlador enviamos el id de dicha cámara.

            dropdownHTML += "<option value='" + str(camaraSitio.id) + "'>"+\
            sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    #Finalmente, si flag=false, en lugar de enviar la dropdown, enviamos un mensaje
    #de que no hay cámaras declaradas en dicho conglomerado:

    if not flag:

        dropdownHTML = "<p id='tabla_camara_id'> Favor de registrar una cámara para este conglomerado.</p>"
    
    return XML(dropdownHTML)