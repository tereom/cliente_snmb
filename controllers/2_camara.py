# coding: utf8
# try something like
def index(): 
	Campos_pestana_2 = [
	# campos Camara
	    Field('nombre','reference Cat_nombre_camara',label=T("Código cámara"),
	    	requires=IS_IN_DB(db,db.Cat_nombre_camara.id,'%(nombre)s')), 
    	Field('fecha_inicio', 'date',label=T("Fecha de colocación"),
    		requires=IS_NOT_EMPTY()),
    	Field('fecha_termino', 'date',label=T("Fecha de levantamiento"),
    		requires=IS_NOT_EMPTY()),	
    	Field('hora_inicio','time',label=T("Hora inicio"),
    		requires=IS_NOT_EMPTY()),
    	Field('hora_termino', 'time',label=T("Hora término"),
    		requires=IS_NOT_EMPTY()),
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
    	Field('sitio_muestra_id',label=T("Sitio"),
    		requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(sitio_numero)s')), 
    	Field('distancia_centro','double',
    		label=T("Distancia al centro del sitio (m)"),
    		requires=IS_NOT_EMPTY()),    		
    	Field('llovio', 'boolean',label=T("Llovió durante el muestreo")),
    	Field('resolucion','reference Camara_resolucion_opcion',
    		label=T("Resolución"),
    		requires=IS_IN_DB(db,db.Cat_resolucion_camara.id,'%(nombre)s')),
    	Field('sensibilidad','reference Camara_sensibilidad_opcion',
    		label=T("Sensibilidad"),
    		requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.id,'%(nombre)s')),
    	Field('comentario', 'text',label=T("Observaciones")),	
	# campos imagen_referencia_camara	
    	Field('archivo_nombre',requires=IS_NOT_EMPTY()),
    	Field('archivo_nombre_original','upload',autodelete=True,
    		label=T("Fotografía"),requires=IS_NOT_EMPTY())
	]

	forma=SQLFORM.factory(*Campos_pestana_2,table_name='tabla')

	if forma.validate():
		formaCamara=db.Camara._filter_fields(forma.vars)
		camaraInsertado = db.Camara.insert(**formaCamara)
		formaCamara['sitio_muestra_id']=camaraInsertado

		formaImagen = {}
		formaImage['camara_id']=camaraInsertado

	return dict(forma=forma)
# db.Camara.nombre.requires=IS_IN_DB(db,db.Camara_nombre_opcion.num_nombre,'%(nombre_nombre)s')
# db.Camara.fecha_inicio.requires=IS_NOT_EMPTY()
# db.Camara.fecha_termino.requires=IS_NOT_EMPTY()
# db.Camara.hora_inicio.requires=IS_NOT_EMPTY()
# db.Camara.hora_termino.requires=IS_NOT_EMPTY()
# db.Camara.lat_grado.requires=IS_NOT_EMPTY()
# db.Camara.lat_min.requires=IS_NOT_EMPTY()
# db.Camara.lat_seg.requires=IS_NOT_EMPTY()
# db.Camara.lon_grado.requires=IS_NOT_EMPTY()
# db.Camara.lon_min.requires=IS_NOT_EMPTY()
# db.Camara.lon_seg.requires=IS_NOT_EMPTY()
# db.Camara.altitud.requires=IS_NOT_EMPTY()
# db.Camara.gps_error.requires=IS_NOT_EMPTY()
# db.Camara.elipsoide.requires=IS_NOT_EMPTY()
# db.Camara.distancia_centro.requires=IS_NOT_EMPTY()
# db.Camara.resolucion.requires=IS_NOT_EMPTY()
# db.Camara.sensibilidad.requires=IS_NOT_EMPTY()