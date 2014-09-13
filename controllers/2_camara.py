# coding: utf8
def index(): 

	Campos_pestana_2 = [
	
	# campos Camara
	# Posteriormente habrá dropdowns en cascada para los campos de conglomerado y sitio,
	# para abordar el caso en el que los sitios de un conglomerado puedan no existir.
	
	#Datos para localizar un sitio único y asociarle la cámara a éste.
	#Estos datos deben ser una llave del sitio.
	    Field('conglomerado_muestra_id', label=T("Conglomerado"),
	    	requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
	    Field('sitio_numero',label=T("Sitio"),
    		requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')),
    
    #Datos de la cámara
        Field('distancia_centro','double', label=T("Distancia al centro del sitio (m)"),
    		requires=IS_NOT_EMPTY()),    		
    	Field('fecha_inicio', 'date',label=T("Fecha de colocación"),requires=IS_NOT_EMPTY()),
    	Field('fecha_termino', 'date',label=T("Fecha de levantamiento"),requires=IS_NOT_EMPTY()),	
    	Field('hora_inicio','time',label=T("Hora inicio"),requires=IS_NOT_EMPTY()),
    	Field('hora_termino', 'time',label=T("Hora término"),requires=IS_NOT_EMPTY()),
    	Field('llovio', 'boolean',label=T("Llovió durante el muestreo")),
    	
    	Field('lat_grado','integer',label=T("grado"),requires=IS_NOT_EMPTY()),
    	Field('lat_min','integer',label=T("minuto"),requires=IS_NOT_EMPTY()),
    	Field('lat_seg','double',label=T("segundo"),requires=IS_NOT_EMPTY()),
    	Field('lon_grado','integer',label=T("grado"),requires=IS_NOT_EMPTY()),
    	Field('lon_min','integer',label=T("minuto"),requires=IS_NOT_EMPTY()),
    	Field('lon_seg','double',label=T("segundo"),requires=IS_NOT_EMPTY()),
    	Field('altitud','double',label=T("Altitud(m)"),requires=IS_NOT_EMPTY()),
    	Field('gps_error','double',label=T("Error(m)"),requires=IS_NOT_EMPTY()),
    	Field('elipsoide',label=T("Datum"),
    		requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),    		

    	Field('nombre', label=T("Código cámara"),
	    	requires=IS_IN_DB(db,db.Cat_nombre_camara.id,'%(nombre)s')),
	    Field('resolucion', label=T("Resolución"),
    		requires=IS_IN_DB(db,db.Cat_resolucion_camara.id,'%(nombre)s')),
    	Field('sensibilidad', label=T("Sensibilidad"),
    		requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.id,'%(nombre)s')),
    	Field('comentario', 'text',label=T("Observaciones")),	

     	###########Imagen############
 		Field('imagen_camara', 'upload', label=T("Fotografía"), uploadfolder="naruto",
 		requires=IS_NOT_EMPTY())
	]

	forma=SQLFORM.factory(*Campos_pestana_2,table_name='tabla')

	if forma.validate():
	'''
		formaCamara=db.Camara._filter_fields(forma.vars)
		camaraInsertado = db.Camara.insert(**formaCamara)
		formaCamara['sitio_muestra_id']=camaraInsertado

		formaImagen = {}
		formaImage['camara_id']=camaraInsertado
	'''
	return dict()