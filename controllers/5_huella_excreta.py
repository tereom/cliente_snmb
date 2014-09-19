# coding: utf8
# try something like
def index1():
    Campos_transecto_huellas = [
        SELECT(_name='conglomerado_muestra_id', 
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_numero',
            requires=IS_IN_DB(db,db.Cat_numero_transecto.id,'%(nombre)s')),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',
            requires=IS_DATE(format=T('%d-%m-%Y'))),
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
        TEXTAREA(_name='comentario'),
    ]
    
    formaTransecto = FORM(*Campos_transecto_huellas)

    if formaTransecto.accepts(request.vars,formname='formaTransectoHTML'):
        response.flash = 'qiubo'
        db.Transecto_huellas_excretas_muestra.insert(**formaTransecto.vars)
        response.flash = 'Éxito'
    elif formaTransecto.errors:
        response.flash = 'Hubo un error al llenar la forma de transecto'
    else:
        response.flash ='Por favor, primero envíe los datos del transecto y luego las huellas/excretas asociadas'

    return dict()

def index2():
    Campos_huellas = [
        #Datos para localizar un transecto único y asociarle la cámara a éste.
        #Estos datos deben conformar una llave del transecto.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_numero',
            requires=IS_IN_DB(db,db.Cat_numero_transecto.id,'%(nombre)s')),
        #En estos campos se necesita AJAX (cascadas) para solucionar el problema de que un
        #transecto asociado a un conglomerado existente no se haya declarado,

        #Campos de una especie invasora
        #INPUT(_name='nombre_en_lista',_type='boolean'),
        INPUT(_name='hay_nombre_comun',_type='boolean'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='hay_nombre_cientifico',_type='boolean'),
        INPUT(_name='nombre_cientifico',_type='string'),
        INPUT(_name='es_huella_excreta',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='largo',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='ancho',_type='double',requires=IS_NOT_EMPTY()),
        
        ###########Imágenes############
        INPUT(_name='archivos_huella',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())
	]

    formaHuella = FORM(*Campos_huellas)
    
    if formaHuella.accepts(request.vars,formname='formaHuellaHTML'):    
        #Filtrando los datos correspondientes a la tabla de huellas:
        formaHuellaExcreta = db.Huella_excreta._filter_fields(formaHuella.vars)
        
        #Utilizando la llave del transecto para encontrarlo:
        
        idConglomerado = formaHuella.vars['conglomerado_muestra_id']
        transectoNumero = formaHuella.vars['transecto_numero']
        
        #Falta poner un try catch porque todavía no usamos AJAX
        
        transectoHuella = db((db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==idConglomerado)&(db.Transecto_huellas_excretas_muestra.transecto_numero==transectoNumero)).select().first()
        
        formaHuellaExcreta['transecto_huellas_excretas_id'] = transectoHuella
        
        if (formaHuella.vars['es_huella_excreta'])=='huella':
            formaHuellaExcreta['es_huella']=True
        else:
            formaHuellaExcreta['es_huella']=False

        #Guardando el registro de la especie invasora en la base de datos:
        
        huellaInsertada = db.Huella_excreta.insert(**formaHuellaExcreta)


        ################Procesando los archivos múltiples#################################
        
        archivos = formaHuella.vars['archivos_huella']
        
        if not isinstance(archivos, list):
            archivos = [archivos]
            
        for aux in archivos:
            archivoHuella = db.Archivo_huella_excreta.archivo.store(aux,aux.filename)
            
            formaArchivoHuella = {}
            formaArchivoHuella['huella_excreta_id'] = huellaInsertada
            formaArchivoHuella['archivo'] = archivoHuella
            formaArchivoHuella['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_huella_excreta.insert(**formaArchivoHuella)
        
        response.flash = 'Éxito'
        
    elif formaHuella.errors:
       response.flash = 'Hubo un error al llenar la forma de huellas/excretas'
       
    else:
        response.flash = 'Por favor, llene los campos solicitados'

    return dict()