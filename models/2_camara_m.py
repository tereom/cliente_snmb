#coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# Camara, es decir: Camara, File_camera, Reference_image_camera
# El campo de ID es automático en Web2py, por lo que no se incluye:

##########################################################################
## Cámara
########################################################################


Campos_Camara = [
	Field('nombre','reference Cat_nombre_camara',label=T("Código cámara"),required=True), 
	Field('fecha_inicio','date',label=T("Fecha de colocación"),required=True),
	Field('fecha_termino','date',label=T("Fecha de levantamiento"),required=True),
	Field('hora_inicio','time',label=T("Hora inicio"),required=True),
	Field('hora_termino', 'date',label=T("Hora término"),required=True),
	Field('lat_grado','integer',label=T("grado"),required=True),
	Field('lat_min','integer',label=T("minuto"),required=True),
	Field('lat_seg','double',label=T("segundo"),required=True),
	Field('lon_grado','integer',label=T("grado"),required=True),
	Field('lon_min','integer',label=T("minuto"),required=True),
	Field('lon_seg','double',label=T("segundo"),required=True),
	Field('altitud','double',label=T("Altitud(m)"),required=True),
	Field('gps_error','double',label=T("Error(m)"),required=True),
	Field('elipsoide', 'reference Cat_elipsoide_sitio',label=T("Datum"),
		required=True), 
    Field('sitio_muestra_id','reference Sitio_muestra',required=True),         
	Field('distancia_centro','double',
		label=T("Distancia al centro del sitio (m)"),required=True),
	Field('llovio','boolean',label=T("Llovió durante el muestreo"),required=True),
	Field('resolucion','reference Cat_resolucion_camara',label=T("Resolución"),required=True),
	Field('sensibilidad','reference Cat_sensibilidad_camara',label=T("Sensibilidad"),required=True),
    Field('comentario', 'text',label=T("Observaciones"))
    ]

db.define_table('Camara',*Campos_Camara)

########################
#Imagen_referencia_camara
########################

Campos_Imagen_referencia_camara = [
	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True, label=T("Fotografía"),required=True)
    ]

db.define_table('Imagen_referencia_camara',*Campos_Imagen_referencia_camara)

########################
#Archivo_camara
########################

Campos_Archivo_camara = [
	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True, label=T("Fotografía"),required=True)
    #Field('es_imagen', 'boolean', required=True)
    ]

db.define_table('Archivo_camara',*Campos_Archivo_camara)



