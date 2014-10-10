# coding: utf8

def index1():

    Campos_Punto_conteo_aves = [

        #Datos para localizar un sitio único.
        #Estos datos deben conformar una llave del sitio.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        INPUT(_name='tecnico',_type='string',requires=IS_NOT_EMPTY()),
        INPUT(_name='fecha',_type='date',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_inicio',_type='time',requires=IS_NOT_EMPTY()),
        INPUT(_name='hora_termino',_type='time',requires=IS_NOT_EMPTY()),

        INPUT(_name='condiciones_ambientales',requires=
            IS_IN_DB(db,db.Cat_condiciones_ambientales.nombre,'%(nombre)s')),

        TEXTAREA(_name='comentario')
    ]

    #IS_DATE(format=T('%d-%m-%Y'))),
    
    formaPunto = FORM(*Campos_Punto_conteo_aves)
    
    if formaPunto.accepts(request.vars,formname='formaPuntoHTML'):
        db.Punto_conteo_aves.insert(**formaPunto.vars)
        response.flash = 'Éxito'
    elif formaPunto.errors:
        response.flash = 'Hubo un error al llenar la forma'
    else:
        response.flash ='Por favor, asegúrese de registrar cada punto de conteo sólo una vez'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    #De la misma manera, llenando la combobox de condiciones ambientales:

    listaCondicionesAmbientales = db(db.Cat_condiciones_ambientales).select(
        db.Cat_condiciones_ambientales.nombre)

    return dict(listaConglomerado=listaConglomerado,
        listaCondicionesAmbientales=listaCondicionesAmbientales)

# #AJAX para revisar que no se haya ingresado el mismo punto con anterioridad.
# #El AJAX se activará cuando seleccionen un conglomerado y un sitio.

# def sitioExistente():

#     #Obteniendo la información del conglomerado que seleccionó el usuario:
#     conglomeradoElegidoID = request.vars.conglomerado_muestra_id
#     numTransectoElegido = request.vars.transecto_numero

#     #Haciendo un query a la tabla de Transecto_huellas_excretas_muestra con la
#     #información anterior:

#     transectoYaInsertado=db(
#     (db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
#     (db.Transecto_huellas_excretas_muestra.transecto_numero==numTransectoElegido)
#     ).select()

#     #regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

#     return len(transectoYaInsertado)

# def index2():

#     Campos_huella_excreta = [

#         #Datos para localizar un transecto único y asociarle la observación a éste.
#         #Estos datos deben conformar una llave del transecto.

#         SELECT(_name='conglomerado_muestra_id',
#             requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
#         SELECT(_name='transecto_huellas_excretas_id',
#             requires=IS_IN_DB(db,db.Transecto_huellas_excretas_muestra.id,'%(nombre)s')),
#         #En estos campos se necesita AJAX (cascadas) para solucionar el problema de que un
#         #transecto asociado a un conglomerado existente no se haya declarado,

#         #Campos de una huella o excreta
#         #El siguiente campo va a leer de radio-botones, por eso admite un string
#         #(lee el valor asociado al botón seleccionado)
#         INPUT(_name='es_huella_excreta',_type='string',requires=IS_NOT_EMPTY()),

#         INPUT(_name='hay_nombre_comun',_type='boolean'),
#         INPUT(_name='nombre_comun',_type='string'),
#         INPUT(_name='hay_nombre_cientifico',_type='boolean'),
#         INPUT(_name='nombre_cientifico',_type='string'),
#         INPUT(_name='largo',_type='double',requires=IS_NOT_EMPTY()),
#         INPUT(_name='ancho',_type='double',requires=IS_NOT_EMPTY()),
        
#         ###########Imágenes############
#         INPUT(_name='archivos_huella_excreta',_type='file',_multiple=True,
#             requires=IS_NOT_EMPTY())
# 	]

#     formaHuellaExcreta = FORM(*Campos_huella_excreta)
    
#     if formaHuellaExcreta.accepts(request.vars,formname='formaHuellaExcretaHTML'):

#         #Filtrando los datos correspondientes a la tabla de huellas:

#         datosHuellaExcreta = db.Huella_excreta._filter_fields(formaHuellaExcreta.vars)
                
#         #Por medio de AJAX, estamos garantizando que cuando registran los
#         #transectos sólo se registre uno de cada número para cada muestreo del
#         #conglomerado.

#         #También garantizamos que los transectos en la dropdown de especie
#         #invasora sí estén registrados con anterioridad en el conglomerado.
        
        
#         #Asociando el valor de la variable es_huella a partir del valor del control
#         #es_huella_excreta
        
#         if (formaHuellaExcreta.vars['es_huella_excreta'])=='huella':
#             datosHuellaExcreta['es_huella']=True
#         else:
#             datosHuellaExcreta['es_huella']=False

#         #Guardando el registro de la especie invasora en la base de datos:
        
#         huellaExcretaInsertada = db.Huella_excreta.insert(**datosHuellaExcreta)

#         ################Procesando los archivos múltiples#################################
        
#         archivos = formaHuellaExcreta.vars['archivos_huella_excreta']
        
#         if not isinstance(archivos, list):
#             archivos = [archivos]
            
#         for aux in archivos:

#              #Guardando el archivo en la carpeta adecuada
#             archivoHuellaExcreta = db.Archivo_huella_excreta.archivo.store(aux,aux.filename)
            
#             datosArchivoHuellaExcreta = {}
#             datosArchivoHuellaExcreta['huella_excreta_id'] = huellaExcretaInsertada
#             datosArchivoHuellaExcreta['archivo'] = archivoHuellaExcreta
#             datosArchivoHuellaExcreta['archivo_nombre_original'] = aux.filename
        
#             #Insertando el registro en la base de datos:

#             db.Archivo_huella_excreta.insert(**datosArchivoHuellaExcreta)
        
#         response.flash = 'Éxito'
        
#     elif formaHuellaExcreta.errors:

#        response.flash = 'Hubo un error al llenar la forma de huellas/excretas'
       
#     else:

#         response.flash = 'Por favor, llene los campos solicitados'

#     ##########Enviando la información de las dropdowns##########################

#     #Regresando los nombres de todos los conglomerados insertados en la tabla de
#     #conglomerado junto con sus id's para llenar la combobox de conglomerado.

#     listaConglomerado = db(db.Conglomerado_muestra).select(
#         db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

#     # Tabla de revisión de registros ingresados
#     db.Huella_excreta.transecto_huellas_excretas_id.writable = False
#     db.Archivo_huella_excreta.huella_excreta_id.writable =False
#     grid = SQLFORM.smartgrid(db.Huella_excreta,csv=False,user_signature=False,
#         create=False,searchable=False,editable=False)

#     return dict(listaConglomerado=listaConglomerado,
#         grid=grid)

# #La siguiente función es invocada mediante AJAX para llenar la combobox de número
# #de transecto a partir de los transectos declarados en un conglomerado seleccionado.

# def asignarTransectos():

#     #Obteniendo la información del conglomerado que seleccionó el usuario:
#     conglomeradoElegidoID = request.vars.conglomerado_muestra_id

#     #Obteniendo los transectos declarados en dicho conglomerado
#     transectosDeclarados = db(
#         db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id==conglomeradoElegidoID
#         ).select(db.Transecto_huellas_excretas_muestra.transecto_numero,\
#         db.Transecto_huellas_excretas_muestra.id)

#     #Creando la dropdown de transectos y enviándola a la vista para que sea desplegada:

#     dropdownHTML = "<select class='generic-widget' name='transecto_huellas_excretas_id' id='tabla_transecto_huellas_excretas_id'>"

#     for transecto in transectosDeclarados:

#         dropdownHTML += "<option value='" + str(transecto.id) + "'>" + transecto.transecto_numero + "</option>"  
    
#     dropdownHTML += "</select>"
    
#     return XML(dropdownHTML)


def asignarSitios():

    # Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&
        (db.Sitio_muestra.existe==True)&
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='tabla_sitio_muestra_id'>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    return XML(dropdownHTML)