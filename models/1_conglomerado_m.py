# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de Conglomerado, es decir: Conglomerado_muestra, Sitio_muestra y Reference_image_site:
## El campo de ID es automático en Web2py, por lo que no se incluye:

db.define_table('Conglomerado_muestra',
                Field('nombre','integer',label=T("Num. conglomerado"),\
                        required='TRUE'),
                Field('fecha_visita', 'date',label=T("Fecha de visita"),\
                        required='TRUE'),
                Field('tipo', 'reference Conglomerado_tipo_opcion',\
                        label=T("Tipo de conglomerado"),required='TRUE'),
                Field('estado', 'reference Conglomerado_estado_opcion',\
                        label=T("Estado"),required='TRUE'),
                Field('municipio', 'integer',label=T("Municipio"),required='TRUE'),
                Field('predio','string',label=T("Predio"),required='TRUE'),
                Field('tenencia', 'reference Conglomerado_tenencia_opcion',\
                        label=T("Tenencia"), required='TRUE'),
                Field('uso_suelo_tipo', 'reference Conglomerado_suelo_opcion',
                        label=T("Tipo de uso de suelo"),required='TRUE'),
                Field('vegetacion_tipo',\
                        'reference Conglomerado_vegetacion_opcion',\
                        label=T("Tipo de vegetación")),
                Field('perturbado', 'boolean',label=T("Perturbado")),
                Field('comentario', 'text',label=T("Observaciones")))

db.Conglomerado_muestra.nombre.requires=IS_NOT_EMPTY()
db.Conglomerado_muestra.fecha_visita.requires=IS_NOT_EMPTY()
db.Conglomerado_muestra.tipo.requires=IS_IN_DB(db,db.Conglomerado_tipo_opcion.num_tipo,'%(nombre_tipo)s')
db.Conglomerado_muestra.estado.requires=IS_IN_DB(db,db.Conglomerado_estado_opcion.num_estado,'%(nombre_estado)s')
db.Conglomerado_muestra.municipio.requires=IS_NOT_EMPTY()
db.Conglomerado_muestra.predio.requires=IS_NOT_EMPTY()
db.Conglomerado_muestra.tenencia.requires=IS_IN_DB(db,db.Conglomerado_tenencia_opcion.num_tenencia,'%(nombre_tenencia)s')
db.Conglomerado_muestra.uso_suelo_tipo.requires=IS_IN_DB(db,db.Conglomerado_suelo_opcion.num_suelo,'%(nombre_suelo)s')
db.Conglomerado_muestra.vegetacion_tipo.requires=IS_IN_DB(db,db.Conglomerado_vegetacion_opcion.num_vegetacion,'%(nombre_vegetacion)s')

db.define_table('Sitio_muestra',
                Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
                Field('sitio_numero', 'reference Sitio_numero_opcion',\
                        label=T("Número de sitio")),
                Field('lat_grado','integer',label=T("grado"),required='TRUE'),
                Field('lat_min','integer',label=T("minuto"),required='TRUE'),
                Field('lat_seg','double',label=T("segundo"),required='TRUE'),
                Field('lon_grado','integer',label=T("grado"),required='TRUE'),
                Field('lon_min','integer',label=T("minuto"),required='TRUE'),
                Field('lon_seg','double',label=T("segundo"),required='TRUE'),
                Field('altitud','double',label=T("Altitud(m)"),required='TRUE'),
                Field('gps_error','double',label=T("Error(m)"),required='TRUE'),
                Field('elipsoide', 'reference Sitio_elipsoide_opcion',\
                        label=T("Datum"),required='TRUE'), 
                Field('evidencia', 'boolean',label=XML("Evidencia <br/> anterior")), 
                Field('existe', 'boolean',label=T("Existe")))



#db.Sitio_muestra.sitio_numero.requires=IS_IN_DB(db,db.Sitio_numero_opcion.num_numero,'%(nombre_numero)s')
#db.Sitio_muestra.lat_grado.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.lat_min.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.lat_seg.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.lon_grado.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.lon_min.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.lon_seg.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.altitud.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.gps_error.requires=IS_NOT_EMPTY()
#db.Sitio_muestra.elipsoide.requires=IS_IN_DB(db,db.Sitio_elipsoide_opcion.num_elipsoide,'%(nombre_elipsoide)s')


db.define_table('Imagen_referencia_sitio',
                Field('sitio_muestra_id','reference Sitio_muestra'),
                Field('archivo_nombre'),
                Field('archivo_nombre_original', 'upload', label=T("Imagen"))
                )
########################################################################
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more opcions, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
