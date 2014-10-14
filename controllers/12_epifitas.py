# coding: utf8

def index():

    camposForma = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        #Datos para localizar un sitio único y la información de epífitas a éste.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        #Datos de epífitas:

        INPUT(_name='helechos_observados',_type='boolean'),
        INPUT(_name='orquideas_observadas',_type='boolean'),
        INPUT(_name='musgos_observados',_type='boolean'),
        INPUT(_name='liquenes_observados',_type='boolean'),
        INPUT(_name='cactaceas_observadas',_type='boolean'),
        INPUT(_name='bromeliaceas_observadas',_type='boolean'),
        INPUT(_name='otras_observadas',_type='boolean'),
        INPUT(_name='nombre_otras',_type='string')

    ]

    forma = FORM(*camposForma)

    if forma.accepts(request.vars,formname='formaEpifitaHTML'):

        datosEpifitas = {}

        datosEpifitas['sitio_muestra_id']=forma.vars['sitio_muestra_id']

        #Insertando "False" cuando se recibe "None" del HTML:

        if bool(forma.vars['helechos_observados']):
            datosEpifitas['helechos_observados']=forma.vars['helechos_observados']
        else:
            datosEpifitas['helechos_observados']=False

        if bool(forma.vars['orquideas_observadas']):
            datosEpifitas['orquideas_observadas']=forma.vars['orquideas_observadas']
        else:
            datosEpifitas['orquideas_observadas']=False

        if bool(forma.vars['musgos_observados']):
            datosEpifitas['musgos_observados']=forma.vars['musgos_observados']
        else:
            datosEpifitas['musgos_observados']=False

        if bool(forma.vars['liquenes_observados']):
            datosEpifitas['liquenes_observados']=forma.vars['liquenes_observados']
        else:
            datosEpifitas['liquenes_observados']=False

        if bool(forma.vars['cactaceas_observadas']):
            datosEpifitas['cactaceas_observadas']=forma.vars['cactaceas_observadas']
        else:
            datosEpifitas['cactaceas_observadas']=False

        if bool(forma.vars['bromeliaceas_observadas']):
            datosEpifitas['bromeliaceas_observadas']=forma.vars['bromeliaceas_observadas']
        else:
            datosEpifitas['bromeliaceas_observadas']=False

        if bool(forma.vars['otras_observadas']):
            datosEpifitas['otras_observadas']=forma.vars['otras_observadas']
            datosEpifitas['nombre_otras']=forma.vars['nombre_otras']
        else:
            datosEpifitas['otras_observadas']=False

        #insertando en la base de datos:
        db.Informacion_epifitas.insert(**datosEpifitas)

        response.flash = 'Éxito'
        
    elif forma.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        
        response.flash ='Por favor, ingrese la información acerca de epífitas'

    ### Información de los menus dropdown

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

#La siguiente función es invocada mediante AJAX para llenar la combobox de número
#de sitio a partir de los sitios existentes de un conglomerado seleccionado.

def asignarSitios():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    #Creando la dropdown de sitios y enviándola a la vista para que sea desplegada:

    dropdownHTML = "<select class='generic-widget' name='sitio_muestra_id' id='tabla_sitio_muestra_id'>"

    dropdownHTML += "<option value=''/>"

    for sitio in sitiosAsignados:

        dropdownHTML += "<option value='" + str(sitio.id) + "'>" + sitio.sitio_numero + "</option>"  
    
    dropdownHTML += "</select>"
    
    return XML(dropdownHTML)

#AJAX para revisar que no se haya ingresado información de epífitas en el mismo
#sitio con anterioridad.
#El AJAX se activará cuando seleccionen un conglomerado y un número de sitio.

def informacionEpifitasExistente():

    #Obteniendo la información del sitio que seleccionó el usuario:
    sitioElegidoID = request.vars.sitio_muestra_id

    #Haciendo un query a la tabla de Informacion_epifitas con la información anterior:

    informacionYaInsertada=db(db.Informacion_epifitas.sitio_muestra_id==sitioElegidoID).select()

    #regresa la longitud de informacionYaInsertada para que sea interpretada por JS

    return len(informacionYaInsertada)

# AQUÍ SURGE UNA CUESTIÓN: PARA PODER VALIDAR LA UNICIDAD DE LA INFORMACION,
# NECESITAMOS UN TRIGGER "ON CHANGE". SIN EMBARGO, PARA PODER HACER ESTO BIEN
# REQUERIMOS INCLUIR UN ESPACIO EN BLANCO POR DEFAULT EN LAS COMBOBOX GENERADAS
# MEDIANTE AJAX, CON LO QUE SURGE LA CUESTIÓN DE VALIDARLAS, Y NECESITAMOS UNA
# FUNCIÓN DE JQUERY DISTINTA PARA PODER PEGARLES A LOS ELEMENTOS QUE NO EXISTEN
# DESDE UN PRINCIPIO.









