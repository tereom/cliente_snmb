# coding: utf8
# try something like
def index(): 
	Campos_pestana_5=[
	# campos  transecto
    Field('transecto_numero',label=T("Transecto"),
        requires=IS_IN_DB(db,db.Cat_numero_transecto)),  
    Field('fecha','date',label=T("Fecha"),requires=IS_NOT_EMPTY()),
    Field('hora_inicio','time',label=T("Hora inicio"),requires=IS_NOT_EMPTY()),
    Field('hora_termino','time',label=T("Hora término"),requires=IS_NOT_EMPTY()),
    Field('tecnico','string',label=T("Técnico"),requires=IS_NOT_EMPTY()),
    Field('comentario','text',label=T("Observaciones")),
    # campos huella_excreta
    Field('es_huella','boolean',label=T("Huellas")),
    Field('hay_nombre_comun','boolean',label="Nombre común"),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico','boolean',label="Nombre científico"),
    Field('nombre_cientifico','string'),
    Field('largo','double',label="Largo(cm)"),
	Field('ancho','double',label="Ancho(cm)"),
    
    # campos archivo_huella_excreta	
    Field('archivo_nombre',requires=IS_NOT_EMPTY()),
    Field('archivo_nombre_original','upload',autodelete=True,
    	label=T("Fotografía"),requires=IS_NOT_EMPTY())
	]

	forma=SQLFORM.factory(*Campos_pestana_5,table_name='tabla')


	return dict(forma=forma)