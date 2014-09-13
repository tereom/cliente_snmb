# coding: utf8
# try something like

def index():
    
    Campos_transecto_invasoras = [
        SELECT(_name='conglomerado_muestra_id', requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_numero', requires=IS_IN_DB(db,db.Cat_numero_transecto.id,'%(nombre)s')),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),    
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
        TEXTAREA(_name='comentario'),
	]
    
    Campos_especie_invasora = [
		#Datos para localizar un transecto único y asociarle la cámara a éste.
   		#Estos datos deben conformar una llave del transecto.
   		SELECT(_name='conglomerado_muestra_id', requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
    	SELECT(_name='transecto _numero',requires=IS_IN_DB(db,db.Cat_numero_transecto.id,'%(nombre)s')),
    	#En estos campos se necesita AJAX (cascadas) para solucionar el problema de que un
    	#transecto asociado a un conglomerado existente no se haya declarado,

		#Campos de una especie invasora
		#INPUT(_name='nombre_en_lista',_type='boolean'),
		INPUT(_name='hay_nombre_comun',_type='boolean'),
		INPUT(_name='nombre_comun',_type='string'),
		INPUT(_name='hay_nombre_cientifico',_type='boolean'),
		INPUT(_name='nombre_cientifico',_type='string'),
		INPUT(_name='numero_individuos', _type='integer', requires=IS_NOT_EMPTY()),
		
		###########Imágenes############
		INPUT(_name='archivos_invasora',_type='file', _multiple=True, requires=IS_NOT_EMPTY())
	]
    
    formaTransecto = FORM(*Campos_transecto_invasoras)
    formaEspecie = FORM(*Campos_especie_invasora)
    
    if formaTransecto.accepts(request.vars,formname='formaTransectoHTML'):
        db.Transecto_especies_invasoras_muestra.insert(**formaTransecto.vars)
    elif formaTransecto.errors:
        response.flash = 'Hubo un error al llenar la forma de transecto'
    else:
    	response.flash ='Por favor, primero envíe los datos del transecto y luego los de las especies asociadas'

    if formaEspecie.accepts(request.vars,formname='formaEspecieHTML'):
        '''
		#Filtrando los datos correspondientes a la tabla de la especie invasora:
        formaEspecieInvasora = db.Especie_invasora._filter_fields(formaEspecie.vars)
        
        #Utilizando la llave del transecto para encontrarlo:
        
        idConglomerado = formaEspecie.vars['conglomerado_muestra_id']
        transectoNumero = formaEspecie.vars['transecto_numero']
        
        #Falta poner un try catch porque todavía no usamos AJAX
        
        transectoEspecie = db((db.Transecto_especies_invasoras_muestra.conglomerado_muestra_id==idConglomerado)&
        (db.Transecto_especies_invasoras_muestra.transecto_numero==transectoNumero)).select().first()
        
        formaEspecieInvasora['transecto_especies_invasoras_id'] = transectoEspecie
        
        #Guardando el registro de la especie invasora en la base de datos:
        
        especieInsertada = db.Transecto_especies_invasoras_muestra.insert(**formaEspecieInvasora)

		################Procesando los archivos múltiples#################################
    	
    	archivos = forma.vars['archivos_invasora']
    	if not isinstance(archivos, list):
    	
    		archivos = [archivos]
    		
    	for aux in archivos:
    		archivoInvasora = db.Archivo_especie_invasora.archivo.store(aux, aux.filename)
    		
    		formaArchivoInvasora = {}
    		formaArchivoInvasora['especie_invasora_id'] = especieInsertada
    		formaArchivoInvasora['archivo'] = archivoInvasora
    		formaArchivoInvasora['archivo_nombre_original'] = aux.filename
    	
    		#Insertando el registro en la base de datos:

    		db.Archivo_especie_invasora.insert(**formaArchivoInvasora)
        '''
        response.flash = 'Éxito'
        
    elif formaEspecie.errors:
    
       response.flash = 'Hubo un error al llenar la forma de especie invasora'
       
    else:
    
    	response.flash = 'Gato'

	return dict()
