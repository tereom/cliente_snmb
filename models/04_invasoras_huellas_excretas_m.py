# coding: utf8

## En esta sección se definen las tablas correspondientes a la sección de 
## Especies Invasoras/Huellas y excretas. 
## El campo de ID es automático en Web2py, por lo que no se incluye:

###########################################
# Transecto_muestra
###########################################

Campos_Transecto_muestra =[

	Field('conglomerado_muestra_id','reference Conglomerado_muestra',
		required=True),
	Field('fecha','date',required=True),

    #Se insertará a partir de un catálogo
	Field('transecto_numero','string', required=True),

	Field('tecnico','string',required=True),
    Field('hora_inicio','time',required=True),
	Field('hora_termino','time',required=True),
    Field('comentario','text')
]

db.define_table('Transecto_muestra', *Campos_Transecto_muestra, 
	singular='Transecto', plural='Transectos')

#db.Transecto_especies_invasoras_muestra.fecha.requires=IS_DATE('%d-%m-%Y')

###########################################
# Especie_invasora
###########################################

Campos_Especie_invasora =[

	Field('transecto_muestra_id','reference Transecto_muestra', required=True),
	Field('nombre_en_lista','boolean', required=True),
	Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),

    #Se insertará a partir de un catálogo
    Field('numero_individuos', 'string', required=True)
]

db.define_table('Especie_invasora', *Campos_Especie_invasora,
	singular='Especie invasora', plural='Especies invasoras')

###########################################
# Archivo_especie_invasora
###########################################

Campos_Archivo_especie_invasora =[

	Field('especie_invasora_id','reference Especie_invasora',required=True),
    Field('archivo_nombre_original','string',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
]

db.define_table('Archivo_especie_invasora', *Campos_Archivo_especie_invasora,
	singular='Archivo especie invasora', plural='Archivos especies invasoras')

###########################################
# Huella_excreta
###########################################


Campos_Huella_excreta = [

    Field('transecto_muestra_id','reference Transecto_muestra', required=True),
    Field('es_huella','boolean', required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('largo','double',required=True),
    Field('ancho','double',required=True)
    ]

db.define_table('Huella_excreta', *Campos_Huella_excreta,
    singular='Huella/excreta', plural='Huellas/excretas')

###########################################
# Archivo_huella_excreta
###########################################

Campos_Archivo_huella_excreta = [

    Field('huella_excreta_id','reference Huella_excreta',required=True),
    Field('archivo_nombre_original','string',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_huella_excreta', *Campos_Archivo_huella_excreta,
    singular='Archivo huella/excreta', plural='Archivos huellas/excretas')

