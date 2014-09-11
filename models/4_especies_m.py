# coding: utf8

## En esta segción se definen las tablas correspondientes a la pestaña de 
## Especies Invasoras, es decir: Transecto_especies_invasoras_muestra, 
## Especie_Invasora, Archivo_especie_invasora 
'''
db.define_table('Transecto_especies_invasoras_muestra',
                Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
                Field('transecto_numero',\
                        'reference Transecto_numero_opcion',\
                	label=T("Transecto")),  
                Field('fecha', 'date',label=T("Fecha"),\
                        required='TRUE'),
                Field('hora_inicio', 'time',label=T("Hora inicio"),\
                        required='TRUE'),
                Field('hora_termino', 'time',label=T("Hora término"),\
                        required='TRUE'),
                Field('tecnico','string',label=T("Técnico")),
                Field('comentario','text',label=T("Observaciones"))
                )

db.Transecto_especies_invasoras_muestra.transecto_numero.requires=\
        IS_IN_DB(db,db.Transecto_numero_opcion.num_transecto,'%(nombre_transecto)s')
db.Transecto_especies_invasoras_muestra.fecha.requires=IS_NOT_EMPTY()
db.Transecto_especies_invasoras_muestra.hora_inicio.requires=IS_NOT_EMPTY()
db.Transecto_especies_invasoras_muestra.hora_termino.requires=IS_NOT_EMPTY()
db.Transecto_especies_invasoras_muestra.tecnico.requires=IS_NOT_EMPTY()

db.define_table('Especie_invasora',
                Field('transecto_especies_invasoras_id',\
                        'reference Transecto_especies_invasoras_muestra'),
                Field('nombre_en_lista','boolean',\
                        label="Lista CONABIO de especies invasoras"),
                Field('hay_nombre_comun', 'boolean', label="Nombre común"),
                Field('nombre_comun','string'),
                Field('hay_nombre_cientifico', 'boolean', label="Nombre científico"),
                Field('nombre_cientifico','string'),
                Field('numero_individuos', \
                        'reference Especie_individuos_opcion',\
                         label = "Número de individuos")
)

db.Especie_invasora.numero_individuos.requires=\
        IS_IN_DB(db,db.Especie_individuos_opcion.num_individuos,'%(nombre_individuos)s')

  '''      
