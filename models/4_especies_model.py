# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Especies Invasoras, es decir: Transect_sample_invaders, Invader, File_invader

db.define_table('Camera',
                Field('name','reference Camera_name_option',\
                	label=T("Código cámara")), 
                Field('start_date', 'date',label=T("Fecha de colocación"),\
                        required='TRUE'),
                Field('stop_date', 'date',label=T("Fecha de levantamiento"),\
                        required='TRUE'),
                Field('start_time', 'time',label=T("Hora inicio"),\
                        required='TRUE'),
                Field('stop_time', 'date',label=T("Hora término"),\
                        required='TRUE'),
                Field('loc_camera_lat_deg','integer',label=T("grado"),required='TRUE'),
                Field('loc_camera_lat_min','integer',label=T("minuto"),required='TRUE'),
                Field('loc_camera_lat_sec','double',label=T("segundo"),required='TRUE'),
                Field('loc_camera_lon_deg','integer',label=T("grado"),required='TRUE'),
                Field('loc_camera_lon_min','integer',label=T("minuto"),required='TRUE'),
                Field('loc_camera_lon_sec','double',label=T("segundo"),required='TRUE'),
                Field('loc_camera_altitude','double',label=T("Altitud(m)"),required='TRUE'),
                Field('loc_camera_gps_error','double',label=T("Error(m)"),required='TRUE'),
                Field('loc_camera_ellipsoid', 'reference Site_ellipsoid_option',\
                        label=T("Datum"),required='TRUE'), 
                Field('site_sample_id','reference Site_sample'),         
                Field('distance','double',label=T("Distancia al centro del sitio (m)"),required='TRUE'),
                Field('it_rained', 'boolean',label=T("Llovió durante el muestreo")),
                Field('resolution','reference Camera_resolution_option',\
                		label=T("Resolución")),
                Field('sensitivity','reference Camera_sensitivity_option',\
                		label=T("Sensibilidad")),
                Field('comment_', 'text',label=T("Observaciones"))
                )

db.Camera.name.requires=IS_IN_DB(db,db.Camera_name_option.num_name,'%(name_name)s')
db.Camera.start_date.requires=IS_NOT_EMPTY()
db.Camera.stop_date.requires=IS_NOT_EMPTY()
db.Camera.start_time.requires=IS_NOT_EMPTY()
db.Camera.stop_time.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lat_deg.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lat_min.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lat_sec.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lon_deg.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lon_min.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_lon_sec.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_altitude.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_gps_error.requires=IS_NOT_EMPTY()
db.Camera.loc_camera_ellipsoid.requires=IS_NOT_EMPTY()
db.Camera.distance.requires=IS_NOT_EMPTY()
db.Camera.resolution.requires=IS_NOT_EMPTY()
db.Camera.sensitivity.requires=IS_NOT_EMPTY()
