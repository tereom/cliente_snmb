# coding: utf8
# try something like
def index(): 
	Campos_pestana_4= [
	# campos  transecto
    Field('transecto_numero',label=T("Transecto"),
        requires=IS_IN_DB(db,db.Cat_numero_transecto)),  
    Field('fecha','date',label=T("Fecha"),requires=IS_NOT_EMPTY()),
    Field('hora_inicio','time',label=T("Hora inicio"),requires=IS_NOT_EMPTY()),
    Field('hora_termino','date',label=T("Hora término"),requires=IS_NOT_EMPTY()),
    Field('tecnico','string',label=T("Técnico"),requires=IS_NOT_EMPTY()),
    Field('comentario','text',label=T("Observaciones")),
    # campos especie
    Field('nombre_en_lista','boolean',
        label=T("Lista CONABIO de especies invasoras")),
    Field('hay_nombre_comun', 'boolean', label="Nombre común"),
    Field('nombre_comun','string',requires=IS_NOT_EMPTY()),
    Field('hay_nombre_cientifico', 'boolean', label="Nombre científico"),
    Field('nombre_cientifico','string'),
    Field('numero_individuos',label = "Número de individuos",
        requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')),
	
    # campos imagen_referencia_grabadora	
    Field('archivo_nombre',requires=IS_NOT_EMPTY()),
    Field('archivo_nombre_original','upload',autodelete=True,
    	label=T("Fotografía"),requires=IS_NOT_EMPTY())
	]

	forma=SQLFORM.factory(*Campos_pestana_4,table_name='tabla')


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