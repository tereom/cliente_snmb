# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# Carbono, es decir: Carbono_mantillo, Ramas_transecto y Rama_caida_1000h

##########################################################################
## Transecto_ramas
##########################################################################

Campos_Transecto_ramas = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    Field('transecto_ramas_direccion','string',required=True),
    Field('pendiente','integer',required=True),
    Field('abundancia_1h','integer',required=True),
    Field('abundancia_10h','integer',required=True),
    Field('abundancia_100h','integer',required=True)
    ]

db.define_table('Transecto_ramas',*Campos_Transecto_ramas,
    singular='Ramas en transecto',plural='Ramas en transectos')


##########################################################################
## Rama_1000h
##########################################################################

Campos_Rama_1000h = [    
    Field('transecto_ramas_id','reference Transecto_ramas',required=True),
    Field('diametro','double',required=True),
    
    #Se insertará a partir de un catálogo
    Field('grado','integer',required=True)
]

db.define_table('Rama_1000h',*Campos_Rama_1000h,
    singular='Rama 1000h',plural='Ramas 1000h')


##########################################################################
## Punto_carbono
##########################################################################

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

db.define_table('Punto_carbono',*Campos_Punto_carbono,
    singular='Carbono en el mantillo',plural='Carbono en el mantillo')