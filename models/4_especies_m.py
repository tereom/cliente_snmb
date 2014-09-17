# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Especies Invasoras, es decir: Transecto_especies_invasoras_muestra, 
## Especie_Invasora, Archivo_especie_invasora 

##########################################################################
## Transecto_especies_invasoras_muestra
########################################################################

Campos_Transecto_especies_invasoras_muestra =[
	    Field('conglomerado_muestra_id','reference Conglomerado_muestra', required=True),
	    Field('fecha','date',required=True),
	    Field('transecto_numero','reference Cat_numero_transecto', required=True),
	    Field('tecnico','string',required=True),
    	Field('hora_inicio','time',required=True),
	    Field('hora_termino','time',required=True),
        Field('comentario','text')
]

db.define_table('Transecto_especies_invasoras_muestra', *Campos_Transecto_especies_invasoras_muestra)

##########################################################################
## Especie_invasora
########################################################################

Campos_Especie_invasora =[
	Field('transecto_especies_invasoras_id','reference Transecto_especies_invasoras_muestra', required=True),
	#Field('nombre_en_lista','boolean', required=True),
	Field('hay_nombre_comun', 'boolean', required=True),
	Field('nombre_comun','string'),
	Field('hay_nombre_cientifico', 'boolean', required=True),
    Field('nombre_cientifico','string'),
    Field('numero_individuos', 'integer', required=True)
]

db.define_table('Especie_invasora', *Campos_Especie_invasora)

##########################################################################
## Archivo_especie_invasora
########################################################################

Campos_Archivo_especie_invasora =[
	Field('especie_invasora_id','reference Especie_invasora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
    #Field('es_imagen', 'boolean', required=True)
]

db.define_table('Archivo_especie_invasora',*Campos_Archivo_especie_invasora)
