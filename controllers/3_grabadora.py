# coding: utf8
# try something like
def index(): 
	Campos_pestana_3 = [
	# campos Grabadora
	    Field('nombre','reference Cat_nombre_grabadora',label=T("Código grabadora"),
	    	requires=IS_IN_DB(db,db.Cat_nombre_grabadora.id,'%(nombre)s')), 
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
    	Field('llovio','boolean',label=T("Llovió durante el muestreo")),
        Field('microfonos_mojados','boolean',
            label=T("Se mojaron los micrófonos")),
    	Field('comentario', 'text',label=T("Observaciones")),
	
	# campos magen_referencia_grabadora	
    	Field('archivo_nombre',requires=IS_NOT_EMPTY()),
    	Field('archivo_nombre_original','upload',autodelete=True,
    		label=T("Fotografía"),requires=IS_NOT_EMPTY())
	]

	forma=SQLFORM.factory(*Campos_pestana_3,table_name='tabla')

	if forma.validate():
		formaGrabadora=db.Grabadora._filter_fields(forma.vars)
		grabadoraInsertado = db.Grabadora.insert(**formaGrabadora)
		formaGrabadora['sitio_muestra_id']=grabadoraInsertado

		formaImagen = {}
		formaImage['grabadora_id']=grabadoraInsertado

	return dict(forma=forma)

# db.Grabadora.nombre.requires=IS_IN_DB(db,db.Grabadora_nombre_opcion.num_nombre,'%(nombre_nombre)s')
# db.Grabadora.fecha_inicio.requires=IS_NOT_EMPTY()
# db.Grabadora.fecha_termino.requires=IS_NOT_EMPTY()
# db.Grabadora.hora_inicio.requires=IS_NOT_EMPTY()
# db.Grabadora.hora_termino.requires=IS_NOT_EMPTY()
# db.Grabadora.lat_grado.requires=IS_NOT_EMPTY()
# db.Grabadora.lat_min.requires=IS_NOT_EMPTY()
# db.Grabadora.lat_seg.requires=IS_NOT_EMPTY()
# db.Grabadora.lon_grado.requires=IS_NOT_EMPTY()
# db.Grabadora.lon_min.requires=IS_NOT_EMPTY()
# db.Grabadora.lon_seg.requires=IS_NOT_EMPTY()
# db.Grabadora.altitud.requires=IS_NOT_EMPTY()
# db.Grabadora.gps_error.requires=IS_NOT_EMPTY()
# db.Grabadora.elipsoide.requires=IS_NOT_EMPTY()
# db.Grabadora.distancia_centro.requires=IS_NOT_EMPTY()
# db.Grabadora.resolucion.requires=IS_NOT_EMPTY()
# db.Grabadora.sensibilidad.requires=IS_NOT_EMPTY()