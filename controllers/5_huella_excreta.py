# coding: utf8

def index1():

    Campos_transecto_huellas_excretas = [

    # campos transecto huellas y excretas

    # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.
    
    # No se ingresarán los tres muestreos de transecto de especies invasoras al 
    # mismo tiempo porque puede ser que los hagan a distintos tiempos, y prefieran
    # llenar un transecto mientras descansan.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_numero',
            requires=IS_IN_DB(db,db.Cat_numero_transecto.id,'%(nombre)s')),
        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
        TEXTAREA(_name='comentario'),
    ]

    #IS_DATE(format=T('%d-%m-%Y'))),
    
    formaTransecto = FORM(*Campos_transecto_huellas_excretas)
    
    if formaTransecto.accepts(request.vars,formname='formaTransectoHTML'):
        db.Transecto_huellas_excretas_muestra.insert(**formaTransecto.vars)
        response.flash = 'Éxito'
    elif formaTransecto.errors:
        response.flash = 'Hubo un error al llenar la forma'
    else:
        response.flash ='Por favor, asegúrese que registra cada transecto sólo una vez'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando la combobox de números de transecto:

    listaNumeroTransecto = db(db.Cat_numero_transecto).select(
        db.Cat_numero_transecto.id, db.Cat_numero_transecto.nombre)

    return dict(listaConglomerado=listaConglomerado,\
        listaNumeroTransecto=listaNumeroTransecto)

#AJAX para revisar que no se haya ingresado el mismo transecto con anterioridad.
#El AJAX se activará cuando seleccionen un conglomerado y un número de transecto.

def transectoExistente():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id
    numTransectoElegido = request.vars.transecto_numero

    #Haciendo un query a la tabla de Transecto_huellas_excretas_muestra con la
    #información anterior:

    transectoYaInsertado=db(
    (db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
    (db.Transecto_huellas_excretas_muestra.transecto_numero==numTransectoElegido)
    ).select()

    #regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(transectoYaInsertado)

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