# coding: utf8

def index1():

    camposImpactoActual = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        # Campos Impacto_actual

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
#        SELECT(_name='tipo',
#            requires=IS_IN_DB(db,db.Cat_tipo_impacto.nombre,'%(nombre)s')),
        INPUT(_name='hay_evidencia',_type='boolean'),
        SELECT(_name='en_vegetacion',
            requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
        SELECT(_name='en_suelo',
            requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
        TEXTAREA(_name='comentario')

    ]


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




