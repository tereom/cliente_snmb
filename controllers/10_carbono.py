# coding: utf8

def index1():

    camposTransectosRamas = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        # de datos y así, evitar excepciones.

        #Datos para localizar un sitio único y asociarle los transectos cardinales a éste.
        
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        ### Tabla de frecuencias de transecto por grosor de material

        # Transecto 1N
        INPUT(_name='pendiente_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_1N',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_1N',_type='integer',requires=IS_NOT_EMPTY()),
        #INPUT(_name='abundancia_1000h_1N',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 2E
        INPUT(_name='pendiente_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_2E',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_2E',_type='integer',requires=IS_NOT_EMPTY()),
        #INPUT(_name='abundancia_1000h_2E',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 3S
        INPUT(_name='pendiente_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_3S',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_3S',_type='integer',requires=IS_NOT_EMPTY()),
        #INPUT(_name='abundancia_1000h_3S',_type='integer',requires=IS_NOT_EMPTY()),

        # Transecto 4W
        INPUT(_name='pendiente_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_1h_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_10h_4W',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='abundancia_100h_4W',_type='integer',requires=IS_NOT_EMPTY()),
        #INPUT(_name='abundancia_1000h_4W',_type='integer',requires=IS_NOT_EMPTY())
    ]
    
    formaTransectosRamas = FORM(*camposTransectosRamas)  

    if formaTransectosRamas.accepts(request.vars,formname='formaTransectosRamasHTML'):

        ### Transecto Norte

        datosTransecto1 = {}

        datosTransecto1['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto1['direccion'] = 'Norte'

        datosTransecto1['pendiente'] = formaTransectosRamas.vars['pendiente_1N']
        datosTransecto1['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_1N']
        datosTransecto1['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_1N']
        datosTransecto1['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_1N']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**datosTransecto1)

        ### Transecto Este

        datosTransecto2 = {}

        datosTransecto2['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto2['direccion'] = 'Este'

        datosTransecto2['pendiente'] = formaTransectosRamas.vars['pendiente_2E']
        datosTransecto2['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_2E']
        datosTransecto2['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_2E']
        datosTransecto2['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_2E']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**datosTransecto2)


        ### Transecto Sur

        datosTransecto3 = {}

        datosTransecto3['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto3['direccion'] = 'Sur'

        datosTransecto3['pendiente'] = formaTransectosRamas.vars['pendiente_3S']
        datosTransecto3['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_3S']
        datosTransecto3['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_3S']
        datosTransecto3['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_3S']
    
        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**datosTransecto3)


        ### Transecto Oeste

        datosTransecto4 = {}

        datosTransecto4['sitio_muestra_id'] = formaTransectosRamas.vars['sitio_muestra_id']
        datosTransecto4['direccion'] = 'Oeste'

        datosTransecto4['pendiente'] = formaTransectosRamas.vars['pendiente_4W']
        datosTransecto4['abundancia_1h'] = formaTransectosRamas.vars['abundancia_1h_4W']
        datosTransecto4['abundancia_10h'] = formaTransectosRamas.vars['abundancia_10h_4W']
        datosTransecto4['abundancia_100h'] = formaTransectosRamas.vars['abundancia_100h_4W']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**datosTransecto4)

        response.flash = 'Éxito'
        
    elif formaTransectosRamas.errors:

        response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, llene esta pestaña sólo una vez para cada sitio'


    ### Información de los menus dropdown

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de sitio a partir de los sitios existentes de un conglomerado seleccionado.

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

    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    return XML(dropdownHTML)

#La siguiente función se utiliza para evitar la declaración de transectos cardinales
#en sitio, si ya fueron declarados éstos ahí con anterioridad.

#La siguiente función se utiliza tanto en index1() (para evitar declarar transectos
#duplicados en un mismo sitio), como en index2() (para evitar declarar ramas en
#sitios donde no se hayan declarado transectos.)

def transectosExistentes():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Transecto_ramas con la información anterior:

    transectoYaInsertado=db(db.Transecto_ramas.sitio_muestra_id==\
        sitioElegidoID).select()

    #Regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(transectoYaInsertado)

def index2():

    #Definiendo el número máximo de ramas que se podrán declarar al mismo tiempo:

    n_ramas = 10

    camposRama1000h = [

        #Datos para localizar un sitio único, del cuál posteriormente se leerán
        #mediante AJAX los transectos cardinales declarados, para poder declarar
        #ramas en estos transectos. Estos datos deben conformar una llave del sitio:
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),
    ]

    ##########################
    #Generando los otros campos con un for:

    for i in range(n_ramas):

        #Creando de manera automatizada los nombres de los campos:
        existe_i = 'existe_' + str(i+1)
        transecto_ramas_i = 'transecto_ramas_' + str(i+1)
        diametro_i = 'diametro_' + str(i+1)
        grado_i = 'grado_' + str(i+1)

        #Extendiendo la lista anterior:
        camposRama1000h.extend([
            #Campo para marcar si existe o no una rama.
            INPUT(_name=existe_i,_type='boolean'),

            #El campo de transecto_ramas_i posiblemente se envíe vacío de la vista,
            #por ello, conviene ponerlo como un string, para que no requiera que
            #esté en la base de datos (y por ende, no vacío).

            INPUT(_name=transecto_ramas_i,_type='string'),
            INPUT(_name=diametro_i,_type='double'),
            INPUT(_name=grado_i,_type='integer')])

    formaRamas = FORM(*camposRama1000h)

    if formaRamas.accepts(request.vars,formname='formaRamasHTML'):

        # Asignando el id del sitio para localizar el transecto al cual se
        # le asignará la rama
        transectoRamasSitioId = formaRamas.vars['sitio_muestra_id']

        for i in range(n_ramas):

            # Creando de manera automatizada los nombres de los campos:
            existe_i = 'existe_' + str(i+1)
            transecto_ramas_i = 'transecto_ramas_' + str(i+1)
            diametro_i = 'diametro_' + str(i+1)
            grado_i = 'grado_' + str(i+1)

            # Si existe la i-ésima rama:
            if bool(formaRamas.vars[existe_i]):

                datosRama_i = {}

                # Leyendo la dirección del transecto que seleccionó el usuario

                transectoRamasDireccion_i = formaRamas.vars[transecto_ramas_i]

                # Obtenemos el id para transecto_ramas usando un query

                transectoRamasId = db((
                    db.Transecto_ramas.direccion==transectoRamasDireccion_i)&
                    (db.Transecto_ramas.sitio_muestra_id==\
                        transectoRamasSitioId)).select(db.Transecto_ramas.id).first()
        
                # Agregando los datos extraídos de la forma:
                datosRama_i['transecto_ramas_id']=transectoRamasId
                datosRama_i['diametro']=formaRamas.vars[diametro_i]
                datosRama_i['grado']=formaRamas.vars[grado_i]

                # Insertando los datos de la rama:
                db.Rama_1000h.insert(**datosRama_i)

        response.flash = 'Éxito'
        
    elif formaRamas.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:

        response.flash ='Por favor, introduzca la información de una rama 1000h'

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    # opciones para el dropdown de transectos
    listaTransecto = db(db.Cat_transecto_ramas).select(db.Cat_transecto_ramas.nombre)

    #Regresando el número de ramas para crear la vista en HTML
    return dict(n_ramas=n_ramas,
        listaConglomerado=listaConglomerado,
        listaTransecto=listaTransecto)

def index3():

    CamposPuntosCarbono = [

        #Datos para localizar un sitio único y asociarle los puntos de carbono a éste.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        ### Tabla de información sobre puntos de carbono

        # Punto 1: transecto norte 5m
        SELECT(_name='material_tipo_1',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_1',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_1',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_1',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_1',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 2: transecto norte 10m

        SELECT(_name='material_tipo_2',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_2',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_2',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_2',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_2',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 3: transecto este 5m

        SELECT(_name='material_tipo_3',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_3',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_3',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_3',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_3',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 4: transecto este 10m

        SELECT(_name='material_tipo_4',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_4',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_4',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_4',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_4',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 5: transecto sur 5m

        SELECT(_name='material_tipo_5',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_5',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_5',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_5',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_5',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 6: transecto sur 10m

        SELECT(_name='material_tipo_6',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_6',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_6',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_6',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_6',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 7: transecto oeste 5m

        SELECT(_name='material_tipo_7',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_7',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_7',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_7',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_7',_type='double',requires=IS_NOT_EMPTY()),

        # Punto 8: transecto oeste 10m

        SELECT(_name='material_tipo_8',
            requires=IS_IN_DB(db,db.Cat_material_carbono.nombre,'%(nombre)s')),
        INPUT(_name='grosor_8',_type='integer',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_8',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_humedo_muestra_8',_type='double',requires=IS_NOT_EMPTY()),
        INPUT(_name='peso_seco_muestra_8',_type='double',requires=IS_NOT_EMPTY())
        ]

    formaPuntosCarbono = FORM(*CamposPuntosCarbono)  

    if formaPuntosCarbono.accepts(request.vars,formname='formaPuntosCarbonoHTML'):

        ### Punto 1

        datosPunto1 = {}

        datosPunto1['sitio_muestra_id'] = formaPuntosCarbono.vars['sitio_muestra_id']
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
    
        response.flash ='Por favor, ingrese los datos de los puntos de carbono'

def puntosExistentes():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Punto_carbono con la información anterior:

    puntoYaInsertado=db(db.Punto_carbono.sitio_muestra_id==sitioElegidoID).select()

    #Regresa la longitud de trasectoYaInsertado para que sea interpretada por JS

    return len(puntoYaInsertado)























