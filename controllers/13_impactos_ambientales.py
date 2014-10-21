# coding: utf8

def index1():

    camposImpactoActual = [

        # Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
        # para incluir las dropdowns en cascada.
    
        #Ésta forma únicamente se utilizará para validar antes de ingresar a la base
        #de datos y así, evitar excepciones.

        # Campos Impacto_actual

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s'))

        ]

        for i in range(11):

            #Creando de manera automatizada los nombres de los campos:
            hay_evidencia_i = 'hay_evidencia_' + str(i+1)
            en_vegetacion_i = 'en_vegetacion_' + str(i+1)
            en_suelo_i = 'en_suelo_' + str(i+1)
            comentario_i = 'comentario_' + str(i+1)

            #Extendiendo la lista anterior:
            camposImpactoActual.extend([
                #Campo para marcar si existe o no un árbol.
                INPUT(_name=hay_evidencia_i,_type='boolean'),

                #Los siguientes campos sólo se lleban en el caso que haya evidencia

                SELECT(_name=en_vegetacion_i,
                    requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
                SELECT(_name=en_suelo_i,
                    requires=IS_IN_DB(db,db.Cat_severidad_impactos.nombre,'%(nombre)s')),
                TEXTAREA(_name=comentario_i)
            ])

        

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
            requires=IS_IN_DB(db,db.Cat_agente_impactos),'%(nombre)s'),
        INPUT(_name='nombre_comun',_type='string'),
        INPUT(_name='nombre_cientifico',_type='string'),
        SELECT(_name='prop_afectacion_arborea',
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
        SELECT(_name='prop_afectacion_repoblado',
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
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
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
        SELECT(_name='prop_afectacion_arbustiva',
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
        SELECT(_name='prop_afectacion_arborea',
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
        SELECT(_name='prop_copa_quemada',
            requires=IS_IN_DB(db,db.Cat_porp_afectacion),'%(nombre)s'),
        INPUT(_name='hay_evidencia_recuperacion',_type='boolean')



    ]