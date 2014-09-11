# coding: utf8

## En esta segción se definen las tablas correspondientes a la pestaña de 
## Grabadora, es decir: Grabadora, Imagen_referencia_grabadora, 
## Archivo_referencia_grabadora, Imagen_referencia_microfonos
## Microphone_group, File_microphone_group
## El campo de ID es automático en Web2py, por lo que no se incluye:
'''
Campos_Grabadoora = ['Grabadora',
                Field('nombre','',\
                	label=T("Código grabadora")),  
                Field('fecha_inicio', 'date',label=T("Fecha de colocación"),\
                        required='TRUE'),
                Field('fecha_termino', 'date',label=T("Fecha de levantamiento"),\
                        required='TRUE'),
                Field('hora_inicio', 'time',label=T("Hora inicio"),\
                        required='TRUE'),
                Field('hora_termino', 'date',label=T("Hora término"),\
                        required='TRUE'),
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
                Field('sitio_muestra_id','reference Sitio_muestra'),         
                Field('distancia_centro','double',label=T("Distancia al centro del sitio (m)"),required='TRUE'),
                Field('llovio', 'boolean',label=T("Llovió durante el muestreo")),
                Field('microfonos_mojados', 'boolean',\
                		label=T("Se mojaron los micrófonos")),
                Field('comment_', 'text',label=T("Observaciones"))
                ]

'''