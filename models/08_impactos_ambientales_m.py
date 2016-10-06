# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## impactos ambientales.
## El campo de ID es automático en Web2py, por lo que no se incluye:

###########################################
# Impacto_actual
###########################################

Campos_Impacto_actual = [

	Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
	Field('tipo','string',required=True),
	Field('hay_evidencia','boolean',required=True),
	
	# los campos en_vegetacion y en_suelo se insertarán de un catálogo
	Field('en_vegetacion','string',required=True),
	Field('en_suelo','string',required=True),
	Field('comentario','text')

	]

db.define_table('Impacto_actual', *Campos_Impacto_actual,
	singular='Impactos ambientales', plural='Impactos ambientales')

##########################################################################
## Plaga
##########################################################################

Campos_Plaga = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),

    # Se insertará a partir de un catálogo
    Field('agente','string',required=True),

    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),

    # Estas las dejamos como requeridas, aunque nuestro proceso contemple la 
    # inclusión de plagas fantasma, debido a que queremos hacer los menores cambios
    # a la base de datos.
    
    Field('prop_afectacion_arborea','string',required=True),
    Field('prop_afectacion_repoblado','string',required=True),
    Field('esta_activa','boolean',required=True)

    ]

db.define_table('Plaga',*Campos_Plaga,singular='Plaga',plural='Plagas')

###########################################
# Archivo_plaga
###########################################

Campos_Archivo_plaga = [
	Field('plaga_id','reference Plaga',required=True),
	Field('archivo_nombre_original','string',required=True),
	Field('archivo','upload',required=True)
	]

db.define_table('Archivo_plaga', *Campos_Archivo_plaga, 
	singular='Archivo plaga', plural='Archivos plagas')


###########################################
# Incendio
###########################################

Campos_Incendio = [
	Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
	Field('hay_evidencia','boolean',required=True),
	Field('es_anio_actual','boolean'),
	Field('hay_evidencia_recuperacion','boolean'),

	# Se insertarán a partir de un catálogo
	Field('tipo','string'),
	Field('prop_afectacion_herbacea','string'),
	Field('prop_afectacion_arbustiva','string'),
	Field('prop_afectacion_arborea','string'),
	Field('prop_copa_quemada','string'),
	]

db.define_table('Incendio', *Campos_Incendio, 
	singular='Incendio', plural='Incendios')

###########################################
# Archivo_incendio
###########################################

Campos_Archivo_incendio = [
	Field('incendio_id','reference Incendio',required=True),
	Field('archivo_nombre_original','string',required=True),
	Field('archivo','upload',required=True)
	]

db.define_table('Archivo_incendio', *Campos_Archivo_incendio, 
	singular='Archivo incendio', plural='Archivos incendios')
