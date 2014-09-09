# # coding: utf8

# ## En esta segción se definen las tablas correspondientes a la pestaña de 
# ## Camara, es decir: Camara, File_camera, Reference_image_camera
# ## El campo de ID es automático en Web2py, por lo que no se incluye:

# db.define_table('Camara',
#                 Field('nombre','reference Camara_nombre_opcion',\
#                 		label=T("Código cámara")), 
#                 Field('fecha_inicio', 'date',label=T("Fecha de colocación"),\
#                         required='TRUE'),
#                 Field('fecha_termino', 'date',label=T("Fecha de levantamiento"),\
#                         required='TRUE'),
#                 Field('hora_inicio', 'time',label=T("Hora inicio"),\
#                         required='TRUE'),
#                 Field('hora_termino', 'time',label=T("Hora término"),\
#                         required='TRUE'),
#                 Field('lat_grado','integer',label=T("grado"),required='TRUE'),
#                 Field('lat_min','integer',label=T("minuto"),required='TRUE'),
#                 Field('lat_seg','double',label=T("segundo"),required='TRUE'),
#                 Field('lon_grado','integer',label=T("grado"),required='TRUE'),
#                 Field('lon_min','integer',label=T("minuto"),required='TRUE'),
#                 Field('lon_seg','double',label=T("segundo"),required='TRUE'),
#                 Field('altitud','double',label=T("Altitud(m)"),required='TRUE'),
#                 Field('gps_error','double',label=T("Error(m)"),required='TRUE'),
#                 Field('elipsoide', 'reference Sitio_elipsoide_opcion',\
#                         label=T("Datum"),required='TRUE'), 
#                 Field('sitio_muestra_id','reference Sitio_muestra'),         
#                 Field('distancia_centro','double',label=T("Distancia al centro del sitio (m)"),required='TRUE'),
#                 Field('llovio', 'boolean',label=T("Llovió durante el muestreo")),
#                 Field('resolucion','reference Camara_resolucion_opcion',\
#                 		label=T("Resolución")),
#                 Field('sensibilidad','reference Camara_sensibilidad_opcion',\
#                 		label=T("Sensibilidad")),
#                 Field('comentario', 'text',label=T("Observaciones"))
#                 )

# db.Camara.nombre.requires=IS_IN_DB(db,db.Camara_nombre_opcion.num_nombre,'%(nombre_nombre)s')
# db.Camara.fecha_inicio.requires=IS_NOT_EMPTY()
# db.Camara.fecha_termino.requires=IS_NOT_EMPTY()
# db.Camara.hora_inicio.requires=IS_NOT_EMPTY()
# db.Camara.hora_termino.requires=IS_NOT_EMPTY()
# db.Camara.lat_grado.requires=IS_NOT_EMPTY()
# db.Camara.lat_min.requires=IS_NOT_EMPTY()
# db.Camara.lat_seg.requires=IS_NOT_EMPTY()
# db.Camara.lon_grado.requires=IS_NOT_EMPTY()
# db.Camara.lon_min.requires=IS_NOT_EMPTY()
# db.Camara.lon_seg.requires=IS_NOT_EMPTY()
# db.Camara.altitud.requires=IS_NOT_EMPTY()
# db.Camara.gps_error.requires=IS_NOT_EMPTY()
# db.Camara.elipsoide.requires=IS_NOT_EMPTY()
# db.Camara.distancia_centro.requires=IS_NOT_EMPTY()
# db.Camara.resolucion.requires=IS_NOT_EMPTY()
# db.Camara.sensibilidad.requires=IS_NOT_EMPTY()

