# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de Registros Extras,
# es decir: Especie_invasora_extra, Archivo_especie_invasora_extra,
# Huella_excreta_extra, Archivo_huella_excreta_extra,
# Especimen_restos_extra, Archivo_especimen_restos_extra.

##########################################################################
## Especie_invasora_extra
##########################################################################

Campos_Especie_invasora_extra = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
        required=True),
    Field('esta_dentro_conglomerado','boolean',required=True),
    Field('tecnico','string',required=True),
    Field('fecha','date',required=True),
    Field('hora','time',required=True),

    Field('lat_grado','integer',required=True),
    Field('lat_min','integer',required=True),
    Field('lat_seg','double',required=True),
    Field('lon_grado','integer',required=True),
    Field('lon_min','integer',required=True),
    Field('lon_seg','double',required=True),
    Field('altitud','double',required=True),
    Field('gps_error','double',required=True),
    Field('elipsoide','reference Cat_elipsoide',required=True),

    Field('nombre_en_lista','boolean', required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('numero_individuos', 'reference Cat_numero_individuos', required=True),
    Field('comentario', 'text')
    ]

db.define_table('Especie_invasora_extra',*Campos_Especie_invasora_extra)

##########################################################################
## Archivo_especie_invasora_extra
########################################################################

Campos_Archivo_especie_invasora_extra =[

    Field('especie_invasora_extra_id','reference Especie_invasora_extra',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
]

db.define_table('Archivo_especie_invasora_extra',
    *Campos_Archivo_especie_invasora_extra)

##########################################################################
## Huella_excreta_extra
##########################################################################

Campos_Huella_excreta_extra = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
        required=True),
    Field('esta_dentro_conglomerado','boolean',required=True),
    Field('tecnico','string',required=True),
    Field('fecha','date',required=True),
    Field('hora','time',required=True),

    Field('lat_grado','integer',required=True),
    Field('lat_min','integer',required=True),
    Field('lat_seg','double',required=True),
    Field('lon_grado','integer',required=True),
    Field('lon_min','integer',required=True),
    Field('lon_seg','double',required=True),
    Field('altitud','double',required=True),
    Field('gps_error','double',required=True),
    Field('elipsoide','reference Cat_elipsoide',required=True),

    Field('es_huella','boolean', required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('largo','double',required=True),
    Field('ancho','double',required=True),
    Field('comentario','text')
    ]

db.define_table('Huella_excreta_extra', *Campos_Huella_excreta_extra)

##########################################################################
## Archivo_huella_excreta_extra
########################################################################

Campos_Archivo_huella_excreta_extra = [

    Field('huella_excreta_extra_id','reference Huella_excreta_extra',
        required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Archivo_huella_excreta_extra',
    *Campos_Archivo_huella_excreta_extra)

##########################################################################
## Especimen_restos_extra
##########################################################################

Campos_Especimen_restos_extra = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
        required=True),
    Field('esta_dentro_conglomerado','boolean',required=True),
    Field('tecnico','string',required=True),
    Field('fecha','date',required=True),
    Field('hora','time',required=True),

    Field('lat_grado','integer',required=True),
    Field('lat_min','integer',required=True),
    Field('lat_seg','double',required=True),
    Field('lon_grado','integer',required=True),
    Field('lon_min','integer',required=True),
    Field('lon_seg','double',required=True),
    Field('altitud','double',required=True),
    Field('gps_error','double',required=True),
    Field('elipsoide','reference Cat_elipsoide',required=True),

	Field('es_especimen','boolean',required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Cat_numero_individuos',required=True),
    Field('comentario','text')
    ]

db.define_table('Especimen_restos_extra',*Campos_Especimen_restos_extra)

##########################################################################
## Archivo_Especimen_restos_extra
########################################################################

Campos_Archivo_especimen_restos_extra = [

    Field('especimen_restos_extra_id','reference Especimen_restos_extra',
    	required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_especimen_restos_extra',
	*Campos_Archivo_especimen_restos_extra)

