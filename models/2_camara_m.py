#coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# Camara, es decir: Camara, File_camera, Reference_image_camera
# El campo de ID es automático en Web2py, por lo que no se incluye:

##########################################################################
## Cámara
########################################################################


Campos_Camara = [

	Field('sitio_muestra_id','reference Sitio_muestra',required=True),         

	Field('nombre','reference Cat_nombre_camara',required=True),
	Field('fecha_inicio','date',required=True),
	Field('fecha_termino','date',required=True),
	Field('hora_inicio','time',required=True),
	Field('hora_termino','date',required=True),

	Field('lat_grado','integer',required=True),
	Field('lat_min','integer',required=True),
	Field('lat_seg','double',required=True),
	Field('lon_grado','integer',required=True),
	Field('lon_min','integer',required=True),
	Field('lon_seg','double',required=True),
	Field('altitud','double',required=True),
	Field('gps_error','double',required=True),
	Field('elipsoide','reference Cat_elipsoide',required=True),

	Field('distancia_centro','double',required=True),
	Field('llovio','boolean',required=True),
	Field('resolucion','reference Cat_resolucion_camara',required=True),
	Field('sensibilidad','reference Cat_sensibilidad_camara',required=True),
    Field('comentario', 'text')
    ]

db.define_table('Camara',*Campos_Camara)

########################
#Imagen_referencia_camara
########################

Campos_Imagen_referencia_camara = [

	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_camara',*Campos_Imagen_referencia_camara)

########################
#Archivo_camara
########################

Campos_Archivo_camara = [
	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',required=True)
    #Field('es_imagen', 'boolean', required=True)
    ]

db.define_table('Archivo_camara',*Campos_Archivo_camara)



