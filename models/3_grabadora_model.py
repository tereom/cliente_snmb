# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Grabadora, es decir: Recorder, Reference_image_recorder, 
## Reference_file_recorder, Reference_image_all_microphones
## Microphone_group, File_microphone_group
## El campo de ID es automático en Web2py, por lo que no se incluye:

db.define_table('Recorder',
                Field('name','reference Recorder_name_option',\
                	label=T("Código grabadora")),  
                Field('start_date', 'date',label=T("Fecha de colocación"),\
                        required='TRUE'),
                Field('stop_date', 'date',label=T("Fecha de levantamiento"),\
                        required='TRUE'),
                Field('start_time', 'time',label=T("Hora inicio"),\
                        required='TRUE'),
                Field('stop_time', 'date',label=T("Hora término"),\
                        required='TRUE'),
                Field('loc_recorder_lat_deg','integer',label=T("grado"),required='TRUE'),
                Field('loc_recorder_lat_min','integer',label=T("minuto"),required='TRUE'),
                Field('loc_recorder_lat_sec','double',label=T("segundo"),required='TRUE'),
                Field('loc_recorder_lon_deg','integer',label=T("grado"),required='TRUE'),
                Field('loc_recorder_lon_min','integer',label=T("minuto"),required='TRUE'),
                Field('loc_recorder_lon_sec','double',label=T("segundo"),required='TRUE'),
                Field('loc_recorder_altitude','double',label=T("Altitud(m)"),required='TRUE'),                
                Field('loc_recorder_gps_error','double',label=T("Error(m)"),required='TRUE'),
                Field('loc_recorder_ellipsoid', 'reference Site_ellipsoid_option',\
                        label=T("Datum"),required='TRUE'), 
                Field('site_sample_id','reference Site_sample'),         
                Field('distance','double',label=T("Distancia al centro del sitio (m)"),required='TRUE'),
                Field('it_rained', 'boolean',label=T("Llovió durante el muestreo")),
                Field('microphones_got_wet', 'boolean',\
                		label=T("Se mojaron los micrófonos")),
                Field('comment_', 'text',label=T("Observaciones"))
                )

db.Recorder.name.requires=IS_IN_DB(db,db.Recorder_name_option.num_name,'%(name_name)s')
db.Recorder.start_date.requires=IS_NOT_EMPTY()
db.Recorder.stop_date.requires=IS_NOT_EMPTY()
db.Recorder.start_time.requires=IS_NOT_EMPTY()
db.Recorder.stop_time.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lat_deg.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lat_min.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lat_sec.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lon_deg.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lon_min.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_lon_sec.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_altitude.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_gps_error.requires=IS_NOT_EMPTY()
db.Recorder.loc_recorder_ellipsoid.requires=IS_NOT_EMPTY()
db.Recorder.distance.requires=IS_NOT_EMPTY()
