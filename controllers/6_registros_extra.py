# coding: utf8

def index1():

	Campos_especie_invasora_extra=[
	
		SELECT(_name='conglomerado_muestra_id', requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		INPUT(_name='esta_dentro_conglomerado',_type='string', requires=IS_NOT_EMPTY()),
		INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires = IS_DATE(format=T('%d-%m-%Y'))),
        INPUT(_name='hora',_type='time',requires = IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
    	SELECT(_name='elipsoide', requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),
    	
    	INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),
		INPUT(_name='numero_individuos', _type='integer', requires=IS_NOT_EMPTY()),
		INPUT(_name='archivos_invasora',_type='file', _multiple=True, requires=IS_NOT_EMPTY())
    ]
    
	formaEspecie=SQLFORM.factory(*Campos_especie_invasora_extra,table_name='tabla')

def index2():

	Campos_huella_excreta_extra=[
	
		SELECT(_name='conglomerado_muestra_id', requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
		INPUT(_name='esta_dentro_conglomerado',_type='string', requires=IS_NOT_EMPTY()),
		INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires = IS_DATE(format=T('%d-%m-%Y'))),
        INPUT(_name='hora',_type='time',requires = IS_NOT_EMPTY()),
        
        INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
    	INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
    	INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
    	SELECT(_name='elipsoide', requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),
    	
    	INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),
		INPUT(_name='numero_individuos', _type='integer', requires=IS_NOT_EMPTY()),
		INPUT(_name='archivos_invasora',_type='file', _multiple=True, requires=IS_NOT_EMPTY())

	return dict(forma=forma)

