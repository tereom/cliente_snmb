# coding: utf8
# try something like
def index(): 
    Campos_pestana_3 = [
    # campos Grabadora
    SELECT(_name='conglomerado_muestra_id',
        requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
    SELECT(_name='sitio_numero',
        requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')),
    
    #Datos de la grabadora
    INPUT(_name='distancia_centro',_type='double',requires=IS_NOT_EMPTY()),           
    INPUT(_name='fecha_inicio',_type='date',requires=IS_NOT_EMPTY()),
    INPUT(_name='fecha_termino',_type='date',requires=IS_NOT_EMPTY()),    
    INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
    INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),
    INPUT(_name='llovio',_type='boolean'),
        
    INPUT(_name='lat_grado',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lat_min',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lat_seg',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_grado',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_min',_type='integer',requires=IS_NOT_EMPTY()),
    INPUT(_name='lon_seg',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='altitud',_type='double',requires=IS_NOT_EMPTY()),
    INPUT(_name='gps_error',_type='double',requires=IS_NOT_EMPTY()),
    SELECT(_name='elipsoide',
        requires=IS_IN_DB(db,db.Cat_elipsoide_sitio.id,'%(nombre)s')),          
    SELECT(_name='nombre',
        requires=IS_IN_DB(db,db.Cat_nombre_grabadora.id,'%(nombre)s')),
    INPUT(_name='microfonos_mojados',_type='boolean'),

    TEXTAREA(_name='comentario',_type='text'),

    ###########Imagen de referencia grabadora ############
    INPUT(_name='imagen_grabadora',_type='file',requires=IS_NOT_EMPTY()),

    ###########Imagen de referencia micrófonos ############
    INPUT(_name='imagen_microfonos',_type='file',requires=IS_NOT_EMPTY()),
    
    ###########Archivo referencia grabadora ############
    INPUT(_name='archivo_metadatos',_type='file',requires=IS_NOT_EMPTY()),
    
    ###########Archivos de la grabadora###########
    INPUT(_name='archivos_grabadora',_type='file',_multiple=True,
        requires=IS_NOT_EMPTY())
    ]

    forma = FORM(*Campos_pestana_3)

    if forma.accepts(request.vars,formname='formaHTML'):
    
        ################Procesando la grabadora#################################
    
        #Filtrando los datos correspondientes a la tabla de la grabadora:
        formaGrabadora = db.Grabadora._filter_fields(forma.vars)
        
        #Utilizando la llave del sitio para encontrarlo:
        
        idConglomerado = forma.vars['conglomerado_muestra_id']
        sitioNumero = forma.vars['sitio_numero']
        
        sitioGrabadora = db((db.Sitio_muestra.conglomerado_muestra_id==idConglomerado)&
            (db.Sitio_muestra.sitio_numero==sitioNumero)).select().first()
        
        formaGrabadora['sitio_muestra_id'] = sitioGrabadora
        
        #Guardando el registro de la cámara en la base de datos:
        
        grabadoraInsertada = db.Grabadora.insert(**formaGrabadora)
        
        ################Procesando la imagen de referencia grabadora#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRef = db.Imagen_referencia_grabadora.archivo.store(
            forma.vars.imagen_grabadora.file,
            forma.vars.imagen_grabadora.filename)
        
        #Creando los campos de la tabla Imagen_referencia_grabadora:
        
        formaImagenRef = {}
        formaImagenRef['grabadora_id'] = grabadoraInsertada
        formaImagenRef['archivo'] = imagenRef
        formaImagenRef['archivo_nombre_original'] = forma.vars.imagen_grabadora.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_grabadora.insert(**formaImagenRef)

        ################Procesando la imagen de referencia micrófonos#################################
        
        #Guardando la imagen de referencia en la carpeta adecuada
        imagenRefMicro = db.Imagen_referencia_microfonos.archivo.store(forma.vars.imagen_microfonos.file,forma.vars.imagen_microfonos.filename)
        
        #Creando los campos de la tabla Archivo_referencia_grabadora:
        
        formaImagenRefMicro = {}
        formaImagenRefMicro['grabadora_id'] = grabadoraInsertada
        formaImagenRefMicro['archivo'] = imagenRefMicro
        formaImagenRefMicro['archivo_nombre_original'] = forma.vars.imagen_microfonos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Imagen_referencia_microfonos.insert(**formaImagenRefMicro)

        ################Procesando el archivo de metadatos#################################
        
        #Guardando el archivo de metadatos en la carpeta adecuada
        archivoMeta = db.Archivo_referencia_grabadora.archivo.store(forma.vars.archivo_metadatos.file,forma.vars.archivo_metadatos.filename)
        
        #Creando los campos de la tabla Imagen_referencia_microfonos:
        
        formaArchivoRef = {}
        formaArchivoRef['grabadora_id'] = grabadoraInsertada
        formaArchivoRef['archivo'] = archivoMeta
        formaArchivoRef['archivo_nombre_original'] = forma.vars.archivo_metadatos.filename
        
        #Insertando el registro en la base de datos:
        
        db.Archivo_referencia_grabadora.insert(**formaArchivoRef)
        
        ################Procesando los archivos múltiples#################################
        
        archivos = forma.vars['archivos_grabadora']
        if not isinstance(archivos, list):
        
            archivos = [archivos]
            
        for aux in archivos:
            archivoGrabadora = db.Archivo_grabadora.archivo.store(aux, aux.filename)
            
            formaArchivoGrabadora = {}
            formaArchivoGrabadora['grabadora_id'] = grabadoraInsertada
            formaArchivoGrabadora['archivo'] = archivoGrabadora
            formaArchivoGrabadora['archivo_nombre_original'] = aux.filename
        
            #Insertando el registro en la base de datos:

            db.Archivo_grabadora.insert(**formaArchivoGrabadora)
    
        response.flash = 'Éxito'
        
    elif forma.errors:
       response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los datos de la grabadora'

    return dict()
