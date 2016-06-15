# coding: utf8

def index1():

    ## Controlador correspondiente a la pestaña "Material leñoso caído" de la
    ## sección: "Vegetación y suelo"     

    camposTransectosRamas = [

        ###########################################
        # Transectos de ramas
        ###########################################

        # Datos para localizar un sitio único y asociarle los transectos
        # cardinales a éste.
        
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        ## Tabla de frecuencias de transecto por grosor de material

        # Transecto 1N
        INPUT(_name='pendiente_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_1N',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 2E
        INPUT(_name='pendiente_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_2E',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 3S
        INPUT(_name='pendiente_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_3S',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 4W
        INPUT(_name='pendiente_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_4W',_type='integer',requires=IS_NOT_EMPTY()),
    ]
    
    formaTransectosRamas = FORM(*camposTransectosRamas)  

    if formaTransectosRamas.accepts(request.vars,formname='formaTransectosRamasHTML'):

        ###########################################
        # Procesando los datos de cada transecto
        ###########################################

        ## Transecto Norte

        datosTransecto1 = {}

        datosTransecto1['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto1['direccion'] = 'Norte'

        datosTransecto1['pendiente'] = formaTransectosRamas.vars['pendiente_1N']
        datosTransecto1['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_1N']
        datosTransecto1['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_1N']
        datosTransecto1['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_1N']

        # Insertando en la base de datos

        db.Transecto_ramas.insert(**datosTransecto1)


        ## Transecto Este

        datosTransecto2 = {}

        datosTransecto2['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto2['direccion'] = 'Este'

        datosTransecto2['pendiente'] = formaTransectosRamas.vars['pendiente_2E']
        datosTransecto2['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_2E']
        datosTransecto2['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_2E']
        datosTransecto2['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_2E']

        # Insertando en la base de datos

        db.Transecto_ramas.insert(**datosTransecto2)


        ## Transecto Sur

        datosTransecto3 = {}

        datosTransecto3['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto3['direccion'] = 'Sur'

        datosTransecto3['pendiente'] = formaTransectosRamas.vars['pendiente_3S']
        datosTransecto3['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_3S']
        datosTransecto3['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_3S']
        datosTransecto3['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_3S']
    
        # Insertando en la base de datos

        db.Transecto_ramas.insert(**datosTransecto3)


        ## Transecto Oeste

        datosTransecto4 = {}

        datosTransecto4['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto4['direccion'] = 'Oeste'

        datosTransecto4['pendiente'] = formaTransectosRamas.vars['pendiente_4W']
        datosTransecto4['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_4W']
        datosTransecto4['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_4W']
        datosTransecto4['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_4W']

        # Insertando en la base de datos

        db.Transecto_ramas.insert(**datosTransecto4)

        response.flash = 'Éxito'
        
    elif formaTransectosRamas.errors:

        response.flash = 'Hubo un error al llenar la forma'
       
    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    # Regresando los nombres de todos los conglomerados insertados en la tabla de
    # conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

def asignarSitios():

    ## Función invocada mediante AJAX para llenar la combobox de número de sitio
    ## a partir de los sitios existentes de un conglomerado seleccionado.

    # Obteniendo la información del conglomerado que seleccionó el usuario:

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    # Obteniendo los sitios que existen en dicho conglomerado

    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&
        (db.Sitio_muestra.existe==True)&
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    # Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='tabla_sitio_muestra_id'>"

    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    return XML(dropdownHTML)

def transectosExistentes():
    
    ## Esta función se utiliza para evitar la declaración de transectos 
    ## cardinales en sitio, si ya fueron declarados éstos ahí con anterioridad.
    
    ## Se utiliza en:
    ##    - index1() para evitar declarar transectos duplicados en un mismo sitio. 
    ##    - index2() para evitar declarar ramas en sitios donde no se hayan 
    ##        declarado transectos.

    # Obteniendo la información del sitio que seleccionó el usuario:

    sitioElegidoID = request.vars.sitio_muestra_id

    # Haciendo un query a la tabla de Transecto_ramas con la información anterior:

    transectoYaInsertado = db(db.Transecto_ramas.sitio_muestra_id==\
        sitioElegidoID).select()

    # Regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(transectoYaInsertado)

def index2():

    ## Controlador correspondiente a la pestaña "Material 1000h" correspondiente
    ## a la sección: "Vegetación y suelo"  

    # Definiendo el número máximo de ramas que se podrán declarar al mismo tiempo:

    n_ramas = 10

    camposRama1000h = [

        ###########################################
        # Ramas 1000h
        ###########################################

        # Datos para localizar un sitio único, del cuál posteriormente se leerán
        # mediante AJAX los transectos cardinales declarados, para poder declarar
        # ramas en estos transectos.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto_ramas_id',
            requires=IS_IN_DB(db,db.Transecto_ramas.id,'%(nombre)s'))
    ]

    ##########################
    # Generando con un for los campos relativos a cada rama de 1000h:

    for i in range(n_ramas):

        # Creando de manera automatizada los nombres de los campos:

        existe_i = 'existe_' + str(i+1)
        transecto_ramas_i = 'transecto_ramas_' + str(i+1)
        diametro_i = 'diametro_' + str(i+1)
        grado_i = 'grado_' + str(i+1)

        camposRama1000h.extend([

            #Campo para marcar si existe o no una rama.

            INPUT(_name=existe_i,_type='boolean'),

            # El campo de transecto_ramas_i posiblemente se envíe vacío de la vista,
            # por ello, conviene ponerlo como un string, para que no requiera que
            # esté en la base de datos (y por ende, no vacío).

            INPUT(_name=transecto_ramas_i,_type='string'),
            INPUT(_name=diametro_i,_type='double'),
            INPUT(_name=grado_i,_type='integer')
        ])

    formaRamas = FORM(*camposRama1000h)

    if formaRamas.accepts(request.vars,formname='formaRamasHTML'):

        # Obteniendo el id del transecto en el cuál se encontraron las ramas.

        transectoRamasID = formaRamas.vars['transecto_ramas_id']

        ###########################################
        # Procesando los datos de cada rama
        ###########################################

        for i in range(n_ramas):

            # Creando de manera automatizada los nombres de los campos:
            existe_i = 'existe_' + str(i+1)
            # transecto_ramas_i = 'transecto_ramas_' + str(i+1)
            diametro_i = 'diametro_' + str(i+1)
            grado_i = 'grado_' + str(i+1)

            # Si existe la i-ésima rama:
            if bool(formaRamas.vars[existe_i]):

                datosRama_i = {}

                # Leyendo la dirección del transecto que seleccionó el usuario

                # transectoRamasDireccion_i = formaRamas.vars[transecto_ramas_i]

                # Obtenemos el id para transecto_ramas usando un query
        
                # Agregando los datos extraídos de la forma:
                datosRama_i['transecto_ramas_id']=transectoRamasID
                datosRama_i['diametro']=formaRamas.vars[diametro_i]
                datosRama_i['grado']=formaRamas.vars[grado_i]

                # Insertando los datos de la rama:
                db.Rama_1000h.insert(**datosRama_i)

        response.flash = 'Éxito'
        
    elif formaRamas.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    listaGrado = db(db.Cat_grado_carbono).select(db.Cat_grado_carbono.nombre)

    ##############################################################
    # Creando la tabla de revisión de los registros ingresados
    ##############################################################

    db.Rama_1000h.transecto_ramas_id.writable = False

    grid = SQLFORM.smartgrid(db.Rama_1000h, orderby=~db.Rama_1000h.id,
        csv=False, user_signature=False, details = False,
        create=False, searchable=False, editable=False)

    # Regresando el número de ramas para crear la vista en HTML
    return dict(
        n_ramas=n_ramas,
        listaConglomerado=listaConglomerado,
        listaGrado=listaGrado,
        grid=grid)

def asignarTransectos():

    ## Función invocada mediante AJAX para llenar la combobox de transectos a 
    ## partir de los transectos existentes de un conglomerado y sitio seleccionados.

    sitioElegidoID = request.vars.sitio_muestra_id

    # Obteniendo los transectos que han sido declarados en dicho sitio

    transectosAsignados = db(db.Transecto_ramas.sitio_muestra_id==sitioElegidoID).select(
        db.Transecto_ramas.id, db.Transecto_ramas.direccion)

    # Creando la dropdown de transectos y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='transecto_ramas_id' id='tabla_transecto_ramas_id'>"

    dropdownHTML += "<option value=''/>"

    for transecto in transectosAsignados:

        dropdownHTML += "<option value='" + str(transecto.id) + "'>" + transecto.direccion + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)


def index3():

    ## Controlador correspondiente a la pestaña "Carbono en el mantillo",
    ## correspondiente a la sección: "Vegetación y suelo"

    CamposPuntosCarbono = [

        ###########################################
        # Puntos de muestreo de Carbono en el mantillo
        ###########################################

        # Datos para localizar un sitio único y asociarle los puntos de carbono
        # a éste.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s'))
    ]

    ##########################
    # Generando con un for los campos relativos a cada punto de carbono:
    # Son 8 puntos de carbono:
    #   1. transecto norte 5m
    #   2. transecto norte 10m
    #   3. transecto este 5m
    #   4. transecto este 10m
    #   5. transecto sur 5m
    #   6. transecto sur 10m
    #   7. transecto oeste 5m
    #   8. transecto oeste 10m

    n_puntos = 8

    for i in range(n_puntos):

        material_tipo_i = 'material_tipo_' + str(i+1)
        grosor_i = 'grosor_' + str(i+1)
        peso_humedo_i = 'peso_humedo_' + str(i+1)
        peso_humedo_muestra_i = 'peso_humedo_muestra_' + str(i+1)
        peso_seco_muestra_i = 'peso_seco_muestra_' + str(i+1)

        CamposPuntosCarbono.extend([

            SELECT(_name=material_tipo_i,
                requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
            INPUT(_name=grosor_i,_type='integer',requires=IS_NOT_EMPTY()),
            INPUT(_name=peso_humedo_i,_type='double',requires=IS_NOT_EMPTY()),
            INPUT(_name=peso_humedo_muestra_i,_type='double',requires=IS_NOT_EMPTY()),
            INPUT(_name=peso_seco_muestra_i,_type='double',requires=IS_NOT_EMPTY())

        ])

    formaPuntosCarbono = FORM(*CamposPuntosCarbono)  

    if formaPuntosCarbono.accepts(request.vars,formname='formaPuntosCarbonoHTML'):

        ###########################################
        # Procesando los datos de cada punto
        ###########################################

        # Aunque se podría programar la inserción de los registros correspondientes
        # a cada punto muestreado con un for, se prefiere no hacer ésto. La razón
        # es que hay datos a insertar que no son obtenidos de la forma anterior
        # (es decir, datos que no se obtienen de los campos generados con un for).
        # Por ello, habría que generar una estructura que contuviera estos datos,
        # para que estos fueran extraídos de manera iterativo. Ésto complicaría
        # el código de manera innecesaria.

        datosPunto1 = {}

        datosPunto1['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']

        # Datos a insertar no contenidos en la forma generada iterativamente
        datosPunto1['transecto_direccion'] = 'Norte'
        datosPunto1['transecto_distancia'] = 5

        datosPunto1['material_tipo'] = formaPuntosCarbono.vars['material_tipo_1']
        datosPunto1['grosor'] = formaPuntosCarbono.vars['grosor_1']
        datosPunto1['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_1']
        datosPunto1['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_1']
        datosPunto1['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_1']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto1)

        ### Punto 2

        datosPunto2 = {}

        datosPunto2['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto2['transecto_direccion'] = 'Norte'
        datosPunto2['transecto_distancia'] = 10

        datosPunto2['material_tipo'] = formaPuntosCarbono.vars['material_tipo_2']
        datosPunto2['grosor'] = formaPuntosCarbono.vars['grosor_2']
        datosPunto2['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_2']
        datosPunto2['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_2']
        datosPunto2['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_2']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto2)

        ### Punto 3

        datosPunto3 = {}

        datosPunto3['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto3['transecto_direccion'] = 'Este'
        datosPunto3['transecto_distancia'] = 5

        datosPunto3['material_tipo'] = formaPuntosCarbono.vars['material_tipo_3']
        datosPunto3['grosor'] = formaPuntosCarbono.vars['grosor_3']
        datosPunto3['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_3']
        datosPunto3['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_3']
        datosPunto3['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_3']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto3)

        ### Punto 4

        datosPunto4 = {}

        datosPunto4['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto4['transecto_direccion'] = 'Este'
        datosPunto4['transecto_distancia'] = 10

        datosPunto4['material_tipo'] = formaPuntosCarbono.vars['material_tipo_4']
        datosPunto4['grosor'] = formaPuntosCarbono.vars['grosor_4']
        datosPunto4['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_4']
        datosPunto4['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_4']
        datosPunto4['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_4']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto4)

        ### Punto 5

        datosPunto5 = {}

        datosPunto5['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto5['transecto_direccion'] = 'Sur'
        datosPunto5['transecto_distancia'] = 5

        datosPunto5['material_tipo'] = formaPuntosCarbono.vars['material_tipo_5']
        datosPunto5['grosor'] = formaPuntosCarbono.vars['grosor_5']
        datosPunto5['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_5']
        datosPunto5['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_5']
        datosPunto5['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_5']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto5)

        ### Punto 6

        datosPunto6 = {}

        datosPunto6['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto6['transecto_direccion'] = 'Sur'
        datosPunto6['transecto_distancia'] = 10

        datosPunto6['material_tipo'] = formaPuntosCarbono.vars['material_tipo_6']
        datosPunto6['grosor'] = formaPuntosCarbono.vars['grosor_6']
        datosPunto6['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_6']
        datosPunto6['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_6']
        datosPunto6['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_6']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto6)

        ### Punto 7

        datosPunto7 = {}

        datosPunto7['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto7['transecto_direccion'] = 'Oeste'
        datosPunto7['transecto_distancia'] = 5

        datosPunto7['material_tipo'] = formaPuntosCarbono.vars['material_tipo_7']
        datosPunto7['grosor'] = formaPuntosCarbono.vars['grosor_7']
        datosPunto7['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_7']
        datosPunto7['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_7']
        datosPunto7['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_7']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto7)

        ### Punto 8

        datosPunto8 = {}

        datosPunto8['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
        datosPunto8['transecto_direccion'] = 'Oeste'
        datosPunto8['transecto_distancia'] = 10

        datosPunto8['material_tipo'] = formaPuntosCarbono.vars['material_tipo_8']
        datosPunto8['grosor'] = formaPuntosCarbono.vars['grosor_8']
        datosPunto8['peso_humedo'] = formaPuntosCarbono.vars['peso_humedo_8']
        datosPunto8['peso_humedo_muestra'] = formaPuntosCarbono.vars['peso_humedo_muestra_8']
        datosPunto8['peso_seco_muestra'] = formaPuntosCarbono.vars['peso_seco_muestra_8']

        # Insertando en la base de datos:
        db.Punto_carbono.insert(**datosPunto8)

        response.flash = 'Éxito'
    
    elif formaPuntosCarbono.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    # Regresando los nombres de todos los conglomerados insertados en la tabla de
    # conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    #Asimismo, llenando el catálogo de tipo de material

    listaTipo = db(db.Cat_material_carbono).select(db.Cat_material_carbono.nombre)

    return dict(
        listaTipo=listaTipo, 
        listaConglomerado=listaConglomerado)

def puntosExistentes():
    
    ## Función de AJAX para revisar que no se haya ingresado la forma 
    ## correspondiente a "Carbono en el mantillo" en el mismo sitio con anterioridad
    ##anterioridad. El AJAX se activará cuando seleccionen un 
    ## conglomerado y un número de sitio.

    #Obteniendo la información del sitio que seleccionó el usuario:

    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Punto_carbono con la información anterior:

    puntoYaInsertado =db(db.Punto_carbono.sitio_muestra_id==sitioElegidoID).select()

    #Regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(puntoYaInsertado)

def index4():
    
    ## Controlador correspondiente a la pestaña "Árboles pequeños y arbustos", de
    ## la sección "Vegetación y suelo"

    camposArbolTransecto = [

        ###########################################
        # Campos de los árboles pequeños y arbustos
        ###########################################

        # Datos para localizar un sitio único y asociarle un individuo a éste

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
        SELECT(_name='transecto',
            requires=IS_IN_DB(db,db.Cat_transecto_direccion.nombre,'%(nombre)s'))
        ]

    ##########################
    # Generando con un for los campos relativos a cada individuo:

    n_individuos = 10

    for i in range(n_individuos):

        existe_i = 'existe_' + str(i+1)
        individuo_numero_i = 'individuo_numero' + str(i+1)
        nombre_comun_i = 'nombre_comun_' + str(i+1)
        nombre_cientifico_i = 'nombre_cientifico_' + str(i+1)
        forma_vida_i = 'forma_vida_' + str(i+1)
        distancia_copa_i = 'distancia_copa_' + str(i+1)
        altura_i = 'altura_' + str(i+1)

        camposArbolTransecto.extend([
            #Campo para marcar si existe o no una rama.
            INPUT(_name=existe_i,_type='boolean'),

            INPUT(_name=individuo_numero_i,_type='integer'),
            INPUT(_name=nombre_comun_i,_type='string'),
            INPUT(_name=nombre_cientifico_i,_type='string'),
            INPUT(_name=forma_vida_i,_type='string'),
            INPUT(_name=distancia_copa_i,_type='double'),
            INPUT(_name=altura_i,_type='double')
        ])

    formaArbolTransecto = FORM(*camposArbolTransecto)

    if formaArbolTransecto.accepts(request.vars,formname='formaArbolTransectoHTML'):

        ###########################################
        # Procesando los datos de cada individuo
        ###########################################

        # Datos para localizar un sitio único y asociarle los puntos de carbono
        # a éste. El campo de TransectoID se asignará una vez por forma enviada,
        # y afectará a todos los individuos registrados en la misma.

        arbolSitioID = formaArbolTransecto.vars['sitio_muestra_id']
        arbolTransectoID = formaArbolTransecto.vars['transecto']

        # Generando los otros campos con un for:

        for i in range(n_individuos):

            # Creando de manera automatizada los nombres de los campos:

            existe_i = 'existe_' + str(i+1)
            individuo_numero_i = 'individuo_numero' + str(i+1)
            nombre_comun_i = 'nombre_comun_' + str(i+1)
            nombre_cientifico_i = 'nombre_cientifico_' + str(i+1)
            forma_vida_i = 'forma_vida_' + str(i+1)
            distancia_copa_i = 'distancia_copa_' + str(i+1)
            altura_i = 'altura_' + str(i+1)

            # Si existe el i-ésimo árbol:
            if bool(formaArbolTransecto.vars[existe_i]):

                datosArbolTransecto_i = {}
        
                # Agregando los datos extraídos de la forma:
                datosArbolTransecto_i['individuo_numero'] = formaArbolTransecto.vars[individuo_numero_i]
                datosArbolTransecto_i['nombre_comun'] = formaArbolTransecto.vars[nombre_comun_i]
                datosArbolTransecto_i['nombre_cientifico'] = formaArbolTransecto.vars[nombre_cientifico_i]
                datosArbolTransecto_i['forma_vida'] = formaArbolTransecto.vars[forma_vida_i]
                datosArbolTransecto_i['distancia_copa'] = formaArbolTransecto.vars[distancia_copa_i]
                datosArbolTransecto_i['altura'] = formaArbolTransecto.vars[altura_i]

                datosArbolTransecto_i['sitio_muestra_id'] = arbolSitioID
                datosArbolTransecto_i['transecto'] = arbolTransectoID

                # Insertando los datos de la rama:
                db.Arbol_transecto.insert(**datosArbolTransecto_i)

        response.flash = 'Éxito'
        
    elif formaArbolTransecto.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    listaTransecto = db(db.Cat_transecto_direccion).select(db.Cat_transecto_direccion.nombre)

    listaFormaVida = db(db.Cat_forma_vida).select(db.Cat_forma_vida.nombre)

    ##############################################################
    # Creando la tabla de revisión de los registros ingresados
    ##############################################################

    db.Arbol_transecto.sitio_muestra_id.writable = False
    grid = SQLFORM.smartgrid(db.Arbol_transecto, orderby =~ db.Arbol_transecto.id,\
        csv = False,user_signature = False, details = False,
        create = False, searchable = False, editable = False)

    # Regresando el número de ramas para crear la vista en HTML
    return dict(
        n_individuos = n_individuos,
        listaConglomerado = listaConglomerado,
        listaTransecto = listaTransecto,
        listaFormaVida = listaFormaVida,
        grid = grid)

def index5():
    
    ## Controlador correspondiente a la pestaña Árboles grandes, de la sección
    ## "Vegetación y suelo"

    camposArbolCuadrante = [

        # Datos para localizar un sitio único y asociarle los puntos de carbono a éste.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s'))
        ]

    ##########################
    # Generando con un for los campos relativos a cada individuo:

    n_individuos = 8

    for i in range(n_individuos):

        # Creando de manera automatizada los nombres de los campos:

        existe_i = 'existe_' + str(i+1)
        distancia_i = 'distancia_' + str(i+1)
        azimut_i = 'azimut_' + str(i+1)
        nombre_comun_i = 'nombre_comun_' + str(i+1)
        nombre_cientifico_i = 'nombre_cientifico_' + str(i+1)
        altura_i = 'altura_' + str(i+1)
        diametro_normal_i = 'diametro_normal_' + str(i+1)
        diametro_copa_i = 'diametro_copa_' + str(i+1)

        camposArbolCuadrante.extend([

            # Campo para marcar si existe o no un árbol.
            INPUT(_name=existe_i,_type='boolean'),

            INPUT(_name=distancia_i,_type='double'),
            INPUT(_name=azimut_i,_type='double'),
            INPUT(_name=nombre_comun_i,_type='string'),
            INPUT(_name=nombre_cientifico_i,_type='string'),
            INPUT(_name=altura_i,_type='double'),
            INPUT(_name=diametro_normal_i,_type='double'),
            INPUT(_name=diametro_copa_i,_type='double')
            ])

    formaArbol = FORM(*camposArbolCuadrante)

    if formaArbol.accepts(request.vars,formname='formaArbolHTML'):

        ###########################################
        # Procesando los datos de cada individuo
        ###########################################

        # Asignando el id del sitio al que pertenecen todos los individuos
        # enviados en la forma.

        arbolSitioID = formaArbol.vars['sitio_muestra_id']

        for i in range(n_individuos):

            #Creando de manera automatizada los nombres de los campos:
            existe_i = 'existe_' + str(i+1)
            distancia_i = 'distancia_' + str(i+1)
            azimut_i = 'azimut_' + str(i+1)
            nombre_comun_i = 'nombre_comun_' + str(i+1)
            nombre_cientifico_i = 'nombre_cientifico_' + str(i+1)
            altura_i = 'altura_' + str(i+1)
            diametro_normal_i = 'diametro_normal_' + str(i+1)
            diametro_copa_i = 'diametro_copa_' + str(i+1)

            # Datos que se guardarán para cualquier árbol, independientemente si
            # existe o no:

            datosArbol_i = {}

            datosArbol_i['sitio_muestra_id'] = arbolSitioID

            # Escribiendo el número de individuo
            datosArbol_i['individuo_numero'] = (i+1)

            
            # Si existe el i-ésimo árbol:
            if bool(formaArbol.vars[existe_i]):
        
                # Agregando los datos extraídos de la forma:
                datosArbol_i['existe'] = formaArbol.vars[existe_i]
                datosArbol_i['distancia'] = formaArbol.vars[distancia_i]
                datosArbol_i['azimut'] = formaArbol.vars[azimut_i]
                datosArbol_i['nombre_comun'] = formaArbol.vars[nombre_comun_i]
                datosArbol_i['nombre_cientifico'] = formaArbol.vars[nombre_cientifico_i]
                datosArbol_i['altura'] = formaArbol.vars[altura_i]
                datosArbol_i['diametro_normal'] = formaArbol.vars[diametro_normal_i]
                datosArbol_i['diametro_copa'] = formaArbol.vars[diametro_copa_i]

            else:

                datosArbol_i['existe'] = False                

            # Insertando los datos de la rama:

            db.Arbol_cuadrante.insert(**datosArbol_i)

        response.flash = 'Éxito'
        
    elif formaArbol.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    # Regresando el número de individuos para crear la vista en HTML
    return dict(
        n_individuos = n_individuos,
        listaConglomerado = listaConglomerado
        )

def sitiosArboladoExistentes():

    ## Función de AJAX para revisar que no se haya ingresado la forma 
    ## correspondiente a "Árboles grandes" en el mismo sitio con 
    ## anterioridad. El AJAX se activará cuando seleccionen un 
    ## conglomerado y un número de sitio.

    # Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    # Haciendo un query a la tabla de Arbol_cuadrante con la información anterior:
    arbolesYaInsertados = db(db.Arbol_cuadrante.sitio_muestra_id == sitioElegidoID).select()

    # Regresa la longitud de arbolesYaInsertados para que sea interpretada por la vista
    return len(arbolesYaInsertados)

def index6():

    ## Controlador correspondiente a la pestaña "Epífitas" de la sección:
    ## "Vegetación y suelo"

    camposEpifitas = [

    ###########################################
    # Información de epífitas
    ###########################################

    # Notar que se va a llenar un sólo registro de epífitas por muestra de
    # conglomerado.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        INPUT(_name='helechos_observados',_type='boolean'),
        INPUT(_name='orquideas_observadas',_type='boolean'),
        INPUT(_name='musgos_observados',_type='boolean'),
        INPUT(_name='liquenes_observados',_type='boolean'),
        INPUT(_name='cactaceas_observadas',_type='boolean'),
        INPUT(_name='bromeliaceas_observadas',_type='boolean'),
        INPUT(_name='otras_observadas',_type='boolean'),
        INPUT(_name='nombre_otras',_type='string')
    ]

    formaEpifitas = FORM(*camposEpifitas)

    if formaEpifitas.accepts(request.vars, formname='formaEpifitasHTML'):

        ###########################################
        # Procesando la información de epífitas
        ###########################################

        datosEpifitas = {}

        datosEpifitas['conglomerado_muestra_id'] = formaEpifitas.vars['conglomerado_muestra_id']

        # Insertando "False" cuando se recibe "None" del HTML:

        if bool(formaEpifitas.vars['helechos_observados']):
            datosEpifitas['helechos_observados'] = True
        else:
            datosEpifitas['helechos_observados'] = False

        if bool(formaEpifitas.vars['orquideas_observadas']):
            datosEpifitas['orquideas_observadas'] = True
        else:
            datosEpifitas['orquideas_observadas'] = False

        if bool(formaEpifitas.vars['musgos_observados']):
            datosEpifitas['musgos_observados'] = True
        else:
            datosEpifitas['musgos_observados'] = False

        if bool(formaEpifitas.vars['liquenes_observados']):
            datosEpifitas['liquenes_observados'] = True
        else:
            datosEpifitas['liquenes_observados'] = False

        if bool(formaEpifitas.vars['cactaceas_observadas']):
            datosEpifitas['cactaceas_observadas'] = True
        else:
            datosEpifitas['cactaceas_observadas'] = False

        if bool(formaEpifitas.vars['bromeliaceas_observadas']):
            datosEpifitas['bromeliaceas_observadas'] = True
        else:
            datosEpifitas['bromeliaceas_observadas'] = False

        if bool(formaEpifitas.vars['otras_observadas']):
            datosEpifitas['otras_observadas'] = True
            datosEpifitas['nombre_otras'] = formaEpifitas.vars['nombre_otras']
        else:
            datosEpifitas['otras_observadas'] = False

        # Insertando en la base de datos:

        db.Informacion_epifitas.insert(**datosEpifitas)

        response.flash = 'Éxito'
        
    elif formaEpifitas.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass

    ###########################################
    # Procesando la información de las dropdowns
    ###########################################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

def informacionEpifitasExistente():

    ## Función convocada mediante AJAX para revisar que no se haya ingresado
    ## información de epífitas en un conglomerado con anterioridad.
    ## El AJAX se activará cuando seleccionen un conglomerado.

    # Obteniendo la información del sitio que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    # Haciendo un query a la tabla de Informacion_epifitas con la información anterior:
    informacionYaInsertada = db(db.Informacion_epifitas.conglomerado_muestra_id == conglomeradoElegidoID).select()

    # Regresa la longitud de informacionYaInsertada para que sea interpretada por JS

    return len(informacionYaInsertada)