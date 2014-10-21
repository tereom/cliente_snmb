# coding: utf8

def index1():

    #Creando una lista con los tipos de impactos ambientales:

    tipos = ['incendios','huracanes','inundaciones','apertura de caminos',\
            'aprovechamientos forestales','uso de suelo diferente al forestal',\
            'pastoreo','plagas y enfermedades','lineas eléctricas',\
            'actividades mineras','asentamientos humanos']
            ]

    n_impactos = len(tipos)

    camposImpactos = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        # Campos Impacto_actual

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s'))

        ]

        for i in range(n_impactos):

            #Creando de manera automatizada los nombres de los campos:
            hay_evidencia_i = 'hay_evidencia_' + str(i+1)
            en_vegetacion_i = 'en_vegetacion_' + str(i+1)
            en_suelo_i = 'en_suelo_' + str(i+1)
            comentario_i = 'comentario_' + str(i+1)

            #Extendiendo la lista anterior:
            camposImpactoActual.extend([
                #Campo para marcar si existe o no un árbol.
                INPUT(_name=hay_evidencia_i,_type='boolean'),

                #Los siguientes campos sólo se llenan en el caso que haya evidencia

                SELECT(_name=en_vegetacion_i,
                    requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
                SELECT(_name=en_suelo_i,
                    requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
                TEXTAREA(_name=comentario_i)
            ])

        formaImpactos = FORM(*camposImpactos)

        if formaImpactos.accepts(request.vars,formname='formaImpactosHTML'):

            #Obteniendo el id del conglomerado asociado
            conglomeradoID = formaImpactos.vars['conglomerado_muestra_id']

        for i in range(n_impactos):

            #Creando de manera automatizada los nombres de los campos:
            hay_evidencia_i = 'hay_evidencia_' + str(i+1)
            en_vegetacion_i = 'en_vegetacion_' + str(i+1)
            en_suelo_i = 'en_suelo_' + str(i+1)
            comentario_i = 'comentario_' + str(i+1)

            datosImpacto_i = {}
            datosImpacto_i['conglomerado_muestra_id'] = conglomeradoID
            datosImpacto_i['tipo'] = tipos[i]

            # Si hay evidencia del i-ésimo tipo:
            if bool(formaImpactos.vars[hay_evidencia_i]):
        
                # Agregando los datos extraídos de la forma:
                datosImpacto_i['hay_evidencia']=formaImpactos.vars[hay_evidencia_i]
                datosImpacto_i['en_vegetacion']=formaImpactos.vars[en_vegetacion_i]
                datosImpacto_i['en_suelo']=formaImpactos.vars[en_suelo_i]
                datosImpacto_i['comentario']=formaImpactos.vars[comentario_i]

            else:

                datosImpacto_i['hay_evidencia']=False

            # Insertando los datos del impacto ambiental:
            db.Impacto_actual.insert(**datosImpacto_i)

        response.flash = 'Éxito'
        
    elif formaImpactos.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:

        response.flash ='Por favor, introduzca la información de los impactos ambientales actuales'

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id,db.Conglomerado_muestra.nombre)

    #Regresando el número de impactos para crear la vista en HTML
    return dict(n_impactos=n_impactos,
        listaConglomerado=listaConglomerado)

def index2():

    camposPlaga = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        # Campos Plaga
        SELECT(_name='agente',
            requires=IS_IN_DB(db,db.Cat_agente_impactos,'%(nombre)s')),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='nombre_cientifico',_type='string'),
        SELECT(_name='prop_afectacion_arborea',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        SELECT(_name='prop_afectacion_repoblado',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        INPUT(_name='esta_activa',_type='boolean'),

        # Campos Archivo_plaga
        INPUT(_name='archivos_huella_excreta',_type='file',_multiple=True,
            requires=IS_NOT_EMPTY())

    ]



def index3():

    camposIncendio = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.
        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),

        # Campos Incendio
        INPUT(_name='es_anio_actual',_type='boolean'),
        INPUT(_name='hay_evidencia',_type='boolean'),
        SELECT(_name='tipo',requires=IS_IN_DB(db,db.Cat_incendio,'%(nombre)s')),
        SELECT(_name='prop_afectacion_herbacea',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        SELECT(_name='prop_afectacion_arbustiva',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        SELECT(_name='prop_afectacion_arborea',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        SELECT(_name='prop_copa_quemada',
            requires=IS_IN_DB(db,db.Cat_prop_afectacion,'%(nombre)s')),
        INPUT(_name='hay_evidencia_recuperacion',_type='boolean')

    ]

    forma = FORM(*camposIncendio)

    if forma.accepts(request.vars,formname='formaIncendioHTML'):

        datosIncendio =db.Incendio._filter_fields(formaIncendioHTML.vars) 

    elif forma.errors:

       response.flash = 'Hubo un error al llenar la forma'
       
    else:

        response.flash = 'Por favor, llene los campos solicitados'

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    # Listas para llenar los catálogos dropdown
    listaTipoIncendio = db(db.Cat_incendio).select(db.Cat_incendio.nombre)
    listaPropAfectacion = db(db.Cat_prop_afectacion).select(db.Cat_prop_afectacion.nombre)

    return dict(listaConglomerado=listaConglomerado,
        listaTipoIncendio=listaTipoIncendio,
        listaPropAfectacion=listaPropAfectacion)




