# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Especies Invasoras, es decir: Transecto_especies_invasoras_muestra, 
## Especie_invasora, Archivo_especie_invasora 

##########################################################################
## Transecto_especies_invasoras_muestra
########################################################################

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

db.define_table('Punto_conteo_aves',*Campos_Punto_conteo_aves, 
	singular='Punto de conteo de aves',plural='Puntos de conteo de aves')

##########################################################################
## Conteo_ave
########################################################################

Campos_Conteo_ave =[

	Field('punto_conteo_aves_id','reference Punto_conteo_aves',required=True),
	Field('nombre_en_lista','boolean', required=True),
	Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('es_visual','boolean',required=True),
    Field('es_sonora','boolean',required=True),
    Field('numero_individuos','integer',required=True),
    Field('distancia_aproximada','double',required=True)
]

db.define_table('Conteo_ave',*Campos_Conteo_ave,
	singular='Conteo de aves',plural='Conteos de aves')

##########################################################################
## Archivo_conteo_ave
########################################################################

Campos_Archivo_conteo_ave = [

	Field('conteo_ave_id','reference Conteo_ave',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
]

db.define_table('Archivo_conteo_ave',*Campos_Archivo_conteo_ave,
	singular='Archivo conteo de aves',plural='Archivos conteo de aves')
