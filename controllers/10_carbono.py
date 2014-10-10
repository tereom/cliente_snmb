# coding: utf8

def index1():

    Campos_pestana_transectos_ramas = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada y la subida de múltiples archivos.
    
    #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    # de datos y así, evitar excepciones.

        #Datos para localizar un sitio único.
        #Estos datos deben conformar una llave del sitio.
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
    
    forma = FORM(*Campos_pestana_transectos_ramas)  

    if forma.accepts(request.vars,formname='formaHTML'):

        ### Transecto Norte

        formaTransecto1 = {}

        formaTransecto1['sitio_muestra_id'] = forma.vars['sitio_muestra_id']
        formaTransecto1['transecto_ramas_direccion'] = 'Norte'

        formaTransecto1['pendiente'] = forma.vars['pendiente_1N']
        formaTransecto1['abundancia_1h'] = forma.vars['abundancia_1h_1N']
        formaTransecto1['abundancia_10h'] = forma.vars['abundancia_10h_1N']
        formaTransecto1['abundancia_100h'] = forma.vars['abundancia_100h_1N']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**formaTransecto1)

        ### Transecto Este

        formaTransecto2 = {}

        formaTransecto2['sitio_muestra_id'] = forma.vars['sitio_muestra_id']
        formaTransecto2['transecto_ramas_direccion'] = 'Este'

        formaTransecto2['pendiente'] = forma.vars['pendiente_2E']
        formaTransecto2['abundancia_1h'] = forma.vars['abundancia_1h_2E']
        formaTransecto2['abundancia_10h'] = forma.vars['abundancia_10h_2E']
        formaTransecto2['abundancia_100h'] = forma.vars['abundancia_100h_2E']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**formaTransecto2)


        ### Transecto Sur

        formaTransecto3 = {}

        formaTransecto3['sitio_muestra_id'] = forma.vars['sitio_muestra_id']
        formaTransecto3['transecto_ramas_direccion'] = 'Sur'

        formaTransecto3['pendiente'] = forma.vars['pendiente_3S']
        formaTransecto3['abundancia_1h'] = forma.vars['abundancia_1h_3S']
        formaTransecto3['abundancia_10h'] = forma.vars['abundancia_10h_3S']
        formaTransecto3['abundancia_100h'] = forma.vars['abundancia_100h_3S']
    
        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**formaTransecto3)


        ### Transecto Oeste

        formaTransecto4 = {}

        formaTransecto4['sitio_muestra_id'] = forma.vars['sitio_muestra_id']
        formaTransecto4['transecto_ramas_direccion'] = 'Oeste'

        formaTransecto4['pendiente'] = forma.vars['pendiente_4W']
        formaTransecto4['abundancia_1h'] = forma.vars['abundancia_1h_4W']
        formaTransecto4['abundancia_10h'] = forma.vars['abundancia_10h_4W']
        formaTransecto4['abundancia_100h'] = forma.vars['abundancia_100h_4W']

        # Insertando en la base de datos:
        db.Transecto_ramas.insert(**formaTransecto4)

        response.flash = 'Éxito'
        
    elif forma.errors:

        response.flash = 'Hubo un error al llenar la forma'
       
    else:
        response.flash ='Por favor, introduzca los campos obligatorios'


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

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  

    dropdownHTML += "</select>"

    return XML(dropdownHTML)





