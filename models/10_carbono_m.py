# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# Carbono, es decir: Carbono_mantillo, Ramas_transecto y Rama_caida_1000h

##########################################################################
## Punto_carbono
##########################################################################

Campos_Punto_carbono = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True), 
    Field('transecto_ramas_numero','reference Cat_numero_transecto_carbono',
        required=True),
    Field('transecto_distancia','integer',required=True),
    Field('material_tipo','reference Cat_material_carbono',required=True),
    Field('grosor','integer',required=True),
    Field('peso_humedo','double',required=True),
    Field('peso_humedo_muestra','double',required=True)
    ]

db.define_table('Punto_carbono',*Campos_Punto_carbono,
    singular='Carbono en el mantillo',plural='Carbono en el mantillo')

##########################################################################
## Transecto_ramas
##########################################################################

Campos_Transecto_ramas = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    Field('transecto_ramas_numero','reference Cat_numero_transecto_carbono',
        required=True),
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
    Field('grado','reference Cat_grado_carbono',required=True)
]