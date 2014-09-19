# coding: utf8
def index(): 

    Campos_pestana_2 = [
    
    # campos cámara
    
    # Posteriormente habrá dropdowns en cascada para los campos de conglomerado 
    # y sitio, para abordar el caso en el que los sitios de un conglomerado
    # puedan no existir.
    
    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.
    
    #Datos para localizar un sitio único y asociarle la cámara a éste.
    #Estos datos deben conformar una llave del sitio.

    SELECT(_name='conglomerado_muestra_id',
        requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
    SELECT(_name='sitio_numero',
        requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')),
    
	#Datos de la cámara
    SELECT(_name='nombre',
        requires=IS_IN_DB(db,db.Cat_nombre_camara.id,'%(nombre)s')),  
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
        requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),          

    INPUT(_name='distancia_centro',_type='double',requires=IS_NOT_EMPTY()),
    SELECT(_name='resolucion',
        requires=IS_IN_DB(db,db.Cat_resolucion_camara.id,'%(nombre)s')),
    SELECT(_name='sensibilidad',
        requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.id,'%(nombre)s')),
    INPUT(_name='llovio',_type='boolean'),

    TEXTAREA(_name='comentario',_type='text'),

    ###########Imagen de referencia############
    INPUT(_name='imagen_camara',_type='file',requires=IS_NOT_EMPTY()),
    
    ###########Archivos de la cámara###########
    INPUT(_name='archivos_camara',_type='file',requires=IS_NOT_EMPTY(),
        _multiple=True)

    ]

    forma = FORM(*Campos_pestana_2)

    if forma.accepts(request.vars,formname='formaHTML'):
    
    	################Procesando la cámara#################################
    
    	#Filtrando los datos correspondientes a la tabla de la cámara:
        datosCamara = db.Camara._filter_fields(forma.vars)
        
        #Utilizando la llave del sitio para encontrarlo:
        
        idConglomerado = forma.vars['conglomerado_muestra_id']
        sitioNumero = forma.vars['sitio_numero']
        
        sitioCamara = db((db.Sitio_muestra.conglomerado_muestra_id==idConglomerado)&
        (db.Sitio_muestra.sitio_numero==sitioNumero)).select().first()
        
        datosCamara['sitio_muestra_id'] = sitioCamara
        
        #Guardando el registro de la cámara en la base de datos:
        
        camaraInsertada = db.Camara.insert(**datosCamara)
        
		################Procesando la imagen de referencia#################################
		
		#Guardando la imagen de referencia en la carpeta adecuada
        imagenRef = db.Imagen_referencia_camara.archivo.store(
            forma.vars.imagen_camara.file, forma.vars.imagen_camara.filename)
        
		#Creando los campos de la tabla Imagen_referencia_camara:
		
        formaImagenRef = {}
        formaImagenRef['camara_id'] = camaraInsertada
        formaImagenRef['archivo'] = imagenRef
        formaImagenRef['archivo_nombre_original'] = forma.vars.imagen_camara.filename
		
		#Insertando el registro en la base de datos:
		
        db.Imagen_referencia_camara.insert(**formaImagenRef)
        
    	################Procesando los archivos múltiples#################################
    	
    	archivos = forma.vars['archivos_camara']
    	if not isinstance(archivos, list):
    	
    		archivos = [archivos]
    		
    	for aux in archivos:
    		archivoCamara = db.Archivo_camara.archivo.store(aux, aux.filename)
    		
    		formaArchivoCamara = {}
    		formaArchivoCamara['camara_id'] = camaraInsertada
    		formaArchivoCamara['archivo'] = archivoCamara
    		formaArchivoCamara['archivo_nombre_original'] = aux.filename
    	
    		#Insertando el registro en la base de datos:

    		db.Archivo_camara.insert(**formaArchivoCamara)
	
        response.flash = 'Éxito'
        
    elif forma.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
    	response.flash ='Por favor, introduzca los datos de la cámara'

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerados = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    return dict(listaConglomerados=listaConglomerados)

def asignarSitios():

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    dropdownHTML = "<select class='generic-widget' name='sitio_numero' id='tabla_sitio_numero'>"
    for sitio in sitiosAsignados:

        #Obteniendo el nombre asociado al numero de sitio, del catálogo correspondiente:
        nombreSitio = db(db.Cat_numero_sitio.id==sitio.sitio_numero).select().first().nombre
        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + nombreSitio + "</option>"  
    dropdownHTML += "</select>"
    return XML(dropdownHTML)

