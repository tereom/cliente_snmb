# coding: utf8

## En esta sección se definen las tablas correspondientes a la sección de 
## Vegetación y suelo
## El campo de ID es automático en Web2py, por lo que no se incluye:

###########################################
## Transecto_ramas
###########################################

Campos_Transecto_ramas = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    Field('direccion','string',required=True),
    Field('pendiente','integer',required=True),
    Field('abundancia_1h','integer',required=True),
    Field('abundancia_10h','integer',required=True),
    Field('abundancia_100h','integer',required=True)
]

db.define_table('Transecto_ramas', *Campos_Transecto_ramas,
    singular='Ramas en transecto', plural='Ramas en transectos')


###########################################
## Rama_1000h
###########################################

Campos_Rama_1000h = [    

    Field('transecto_ramas_id','reference Transecto_ramas',required=True),
    Field('diametro','double',required=True),
    
    #Se insertará a partir de un catálogo
    Field('grado','integer',required=True)
]

db.define_table('Rama_1000h', *Campos_Rama_1000h,
    singular='Rama 1000h', plural='Ramas 1000h')


###########################################
## Punto_carbono
###########################################

Campos_Punto_carbono = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    Field('transecto_direccion','string',required=True),
    Field('transecto_distancia','integer',required=True),

    #Se insertará a partir de un catálogo
    Field('material_tipo','string',required=True),

    Field('grosor','integer',required=True),

    Field('peso_humedo','double',required=True),
    Field('peso_humedo_muestra','double',required=True),
    Field('peso_seco_muestra','double',required=True)
]

db.define_table('Punto_carbono', *Campos_Punto_carbono,
    singular='Carbono en el mantillo', plural='Carbono en el mantillo')


###########################################
##  Transecto_arboles (pequeños y arbustos)
###########################################

Campos_Transecto_arboles = [
    
    Field('sitio_muestra_id','reference Sitio_muestra',required=True),

    #Se insertará a partir de campos ocultos:
    Field('direccion','string',required=True)
]

db.define_table('Transecto_arboles', *Campos_Transecto_arboles,
    singular='Transecto árboles', plural='Transectos árboles')


###########################################
## Arbol_transecto (pequeños y arbustos)
###########################################

Campos_Arbol_transecto = [

    Field('transecto_arboles_id','reference Transecto_arboles',required=True),
    Field('individuo_numero','integer',required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('distancia_copa','double',required=True),
    Field('altura','double',required=True),

    # Se insertará a partir de un catálogo
    Field('forma_vida','string',required=True)
    
    ]

db.define_table('Arbol_transecto', *Campos_Arbol_transecto,
    singular='Árbol transecto', plural='Árboles transectos')


###########################################
## Arbol_cuadrante: árboles grandes
###########################################

Campos_Arbol_cuadrante = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    #Se insertará a partir de un catálogo
    # Field('cuadrante','string',required=True),
    Field('individuo_numero','integer',required=True),
    Field('existe', 'boolean',required=True),

    Field('distancia','double'),
    Field('azimut','double'),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('altura','double'),
    Field('diametro_normal','double'),
    Field('diametro_copa','double')
    ]

db.define_table('Arbol_cuadrante', *Campos_Arbol_cuadrante,
    singular='Árbol cuadrante', plural='Árboles cuadrantes')

########################
## Informacion_epifitas
########################

Campos_Informacion_epifitas = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
    Field('helechos_observados','boolean',required=True),
    Field('orquideas_observadas','boolean',required=True),
    Field('musgos_observados','boolean',required=True),
    Field('liquenes_observados','boolean',required=True),
    Field('cactaceas_observadas','boolean',required=True),
    Field('bromeliaceas_observadas','boolean',required=True),
    Field('otras_observadas','boolean',required=True),
    Field('nombre_otras','string')
    ]

db.define_table('Informacion_epifitas', *Campos_Informacion_epifitas,
    singular='Epífita', plural='Epífitas')