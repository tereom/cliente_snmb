# coding: utf8

def index():

    '''
    Controlador correspondiente a la pestaña *Epífitas*.  

    Funcionamiento: Genera los campos de la forma, con el fin de validar la 
    información ingresada en la vista (views/12_epifitas/index.html), antes de 
    ser agregada a la base de datos.

    '''

    camposForma = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        #Datos para localizar un sitio único y la información de epífitas a éste.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

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

    if forma.accepts(request.vars,formname='formaEpifitasHTML'):

        datosEpifitas = {}

        datosEpifitas['conglomerado_muestra_id']=forma.vars['conglomerado_muestra_id']

        #Insertando "False" cuando se recibe "None" del HTML:

        if bool(forma.vars['helechos_observados']):
            datosEpifitas['helechos_observados']=True
        else:
            datosEpifitas['helechos_observados']=False

        if bool(forma.vars['orquideas_observadas']):
            datosEpifitas['orquideas_observadas']=True
        else:
            datosEpifitas['orquideas_observadas']=False

        if bool(forma.vars['musgos_observados']):
            datosEpifitas['musgos_observados']=True
        else:
            datosEpifitas['musgos_observados']=False

        if bool(forma.vars['liquenes_observados']):
            datosEpifitas['liquenes_observados']=True
        else:
            datosEpifitas['liquenes_observados']=False

        if bool(forma.vars['cactaceas_observadas']):
            datosEpifitas['cactaceas_observadas']=True
        else:
            datosEpifitas['cactaceas_observadas']=False

        if bool(forma.vars['bromeliaceas_observadas']):
            datosEpifitas['bromeliaceas_observadas']=True
        else:
            datosEpifitas['bromeliaceas_observadas']=False

        if bool(forma.vars['otras_observadas']):
            datosEpifitas['otras_observadas']=True
            datosEpifitas['nombre_otras']=forma.vars['nombre_otras']
        else:
            datosEpifitas['otras_observadas']=False

        #insertando en la base de datos:
        db.Informacion_epifitas.insert(**datosEpifitas)

        response.flash = 'Éxito'
        
    elif forma.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        pass
        #response.flash ='Por favor, ingrese la información acerca de epífitas'

    ### Información de los menus dropdown

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

def informacionEpifitasExistente():

    '''
    Función convocada mediante AJAX para revisar que no se haya ingresado información
    de epífitas en el mismo conglomerado con anterioridad. El AJAX se activará cuando
    seleccionen un conglomerado.

    '''

    #Obteniendo la información del sitio que seleccionó el usuario:
    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Haciendo un query a la tabla de Informacion_epifitas con la información anterior:

    informacionYaInsertada=db(db.Informacion_epifitas.conglomerado_muestra_id==conglomeradoElegidoID).select()

    #regresa la longitud de informacionYaInsertada para que sea interpretada por JS

    return len(informacionYaInsertada)









