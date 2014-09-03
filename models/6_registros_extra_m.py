# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Registros Extras, es decir: Transecto_huellas_excretas_muestra, 
## Huella_excreta, Archivo_huella_excreta

# db.define_table('Transecto_huellas_excretas_muestra',
#                 Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
#                 Field('transecto_numero',\
#                         'reference Transecto_numero_opcion',\
#                 	label=T("Transecto")),  
#                 Field('fecha', 'date',label=T("Fecha"),\
#                         required='TRUE'),
#                 Field('hora_inicio', 'time',label=T("Hora inicio"),\
#                         required='TRUE'),
#                 Field('hora_termino', 'date',label=T("Hora término"),\
#                         required='TRUE'),
#                 Field('tecnico', 'string',label=T("Técnico"),required='TRUE'),
#                 Field('comment_', 'text',label=T("Observaciones"))
#                 )

# db.Transecto_huellas_excretas_muestra.transecto_numero.requires==\
#         IS_IN_DB(db,db.Transecto_numero_opcion.num_transecto,'%(nombre_transecto)s')
# db.Transecto_huellas_excretas_muestra.fecha.requires=IS_NOT_EMPTY()
# db.Transecto_huellas_excretas_muestra.hora_inicio.requires=IS_NOT_EMPTY()
# db.Transecto_huellas_excretas_muestra.hora_termino.requires=IS_NOT_EMPTY()
# db.Transecto_huellas_excretas_muestra.tecnico.requires=IS_NOT_EMPTY()

# db.define_table('Huella_excreta',
#                 Field('transecto_huellas_excretas_id',\
#                         'reference Transecto_huellas_excretas_muestra'),
#                 Field('es_huella','boolean', label="Huellas"),
#                 Field('hay_nombre_comun', 'boolean', label="Nombre común"),
#                 Field('nombre_comun','string'),
#                 Field('hay_nombre_cientifico', 'boolean', label="Nombre científico"),
#                 Field('nombre_cientifico','string'),
#                 Field('largo','double',label="Largo"),
#                 Field('ancho','double',label="Ancho")
# )
