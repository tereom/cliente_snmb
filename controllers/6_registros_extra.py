# coding: utf8
# try something like
def index(): 
	Campos_pestana_6=[

    Field('esta_dentro_conglomerado','boolean',
        label=T("Dentro del conglomerado"),requires=IS_NOT_EMPTY()),
    Field('fecha','date',label=T("Fecha"),requires=IS_NOT_EMPTY()),
    Field('hora','time',label=T("Hora"),requires=IS_NOT_EMPTY()),
    Field('tecnico','string',label=T("Técnico"),requires=IS_NOT_EMPTY()),
    Field('lat_grado','integer',label=T("Grado")),
    Field('lat_min','integer',label=T("Minuto")),
    Field('lat_seg','double',label=T("Segundo")),
    Field('lon_grado','integer',label=T("Grado")),
    Field('lon_min','integer',label=T("Minuto")),
    Field('lon_seg','double',label=T("Segundo")),
    Field('altitud','double',label=T("Altitud(m)")),
    Field('gps_error','double',label=T("Error(m)")),
    Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum")), 
    Field('es_especimen','boolean',label=T("Especimen")),
    Field('hay_nombre_comun','boolean',label=T("Nombre común")),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico','boolean',label=T("Nombre científico")),
    Field('nombre_cientifico','string'),
    Field('numero_individuos',label="Número de individuos",
        requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')),    Field('comentario','text',label=T("Observaciones")),
    # campos huella
    Field('es_huella','boolean',label=T("Huellas")),       
    # campos archivo
    Field('archivo_nombre',requires=IS_NOT_EMPTY()),
    Field('archivo_nombre_original','upload',autodelete=True,
        label=T("Fotografías"),requires=IS_NOT_EMPTY())
    ]
    
	forma=SQLFORM.factory(*Campos_pestana_6,table_name='tabla')


	return dict(forma=forma)

