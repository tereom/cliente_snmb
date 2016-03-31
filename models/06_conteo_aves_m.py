# coding: utf8

## En esta sección se definen las tablas correspondientes a la sección de
## Conteo de aves.
## El campo de ID es automático en Web2py, por lo que no se incluye:

###########################################
# Punto_conteo_aves
###########################################

Campos_Punto_conteo_aves =[

	Field('sitio_muestra_id','reference Sitio_muestra',
		required=True),
	Field('tecnico','string',required=True),
	Field('fecha','date',required=True),
	Field('hora_inicio','time',required=True),
	Field('hora_termino','time',required=True),
	Field('condiciones_ambientales','string',required=True),
	Field('comentario','text')
]

db.define_table('Punto_conteo_aves', *Campos_Punto_conteo_aves, 
	singular='Punto de conteo de aves', plural='Puntos de conteo de aves')

###########################################
# Conteo_ave
###########################################

Campos_Conteo_ave =[

	Field('punto_conteo_aves_id','reference Punto_conteo_aves',required=True),

	#Los campos 'nombre_comun_en_lista' y 'nombre_cientifico_en_lista' no son
	#obligatorios, pues se dejan vacíos si no introdujeron alguno de los nombres.
	Field('nombre_comun_en_lista','boolean'),
	Field('nombre_comun','string'),
	Field('nombre_cientifico_en_lista','boolean'),
	Field('nombre_cientifico','string'),
	Field('es_visual','boolean',required=True),
	Field('es_sonora','boolean',required=True),
	Field('numero_individuos','integer',required=True),
	Field('distancia_aproximada','double',required=True)
]

db.define_table('Conteo_ave', *Campos_Conteo_ave,
	singular='Conteo de aves', plural='Conteos de aves')

###########################################
# Archivo_conteo_ave
###########################################

Campos_Archivo_conteo_ave = [

	Field('conteo_ave_id','reference Conteo_ave',required=True),
	Field('archivo_nombre_original','string',required=True),
	Field('archivo','upload',autodelete=True,required=True)
]

db.define_table('Archivo_conteo_ave', *Campos_Archivo_conteo_ave,
	singular='Archivo conteo de aves', plural='Archivos conteo de aves')
