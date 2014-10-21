# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# impactos ambientales

##########################################################################
## Impacto actual
##########################################################################

Campos_Impacto_actual = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
    Field('tipo','string',required=True),
    Field('hay_evidencia','boolean',required=True),
    
    # los campos en_vegetacion y en_suelo se insertarán de un catálogo
    Field('en_vegetacion','string'),
    Field('en_suelo','string'),
    Field('comentario','text')

    ]

db.define_table('Impacto_actual',*Campos_Impacto_actual,
    singular='Impactos ambientales',plural='Impactos ambientales')


##########################################################################
## Plaga
##########################################################################

Campos_Plaga = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
    # agente se insertará a partir de un catálogo
    Field('agente','string',required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('prop_afectacion_arborea','string',required=True),
    Field('prop_afectacion_repoblado','string',required=True),
    Field('esta_activa','boolean',required=True)

    ]

db.define_table('Plaga',*Campos_Plaga,singular='Plaga',plural='Plagas')


##########################################################################
## Archivo plaga
##########################################################################

Campos_Archivo_plaga = [
    Field('plaga_id','reference Plaga',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',required=True)
    ]

db.define_table('Archivo_plaga',*Campos_Archivo_plaga, 
    singular='Archivo plaga',plural='Archivos plagas')


##########################################################################
## Incendio
##########################################################################

Campos_Incendio = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra',required=True),
    Field('es_anio_actual','boolean',required=True),
    Field('hay_evidencia','boolean',required=True),
    Field('tipo','string',required=True),
    Field('prop_afectacion_herbacea','string',required=True),
    Field('prop_afectacion_arbustiva','string',required=True),
    Field('prop_afectacion_arborea','string',required=True),
    Field('prop_copa_quemada','string',required=True),
    Field('hay_evidencia_recuperacion','boolean',required=True)
    ]

db.define_table('Incendio',*Campos_Incendio, 
    singular='Incendio',plural='Incendios')

##########################################################################
## Archivo incendio
##########################################################################

Campos_Archivo_incendio = [
    Field('incendio_id','reference Incendio',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',required=True)
    ]

db.define_table('Archivo_incendio',*Campos_Archivo_incendio, 
    singular='Archivo incendio',plural='Archivos incendios')
