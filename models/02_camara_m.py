#coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# Camara, es decir: Camara, File_camera, Reference_image_camera
# El campo de ID es automático en Web2py, por lo que no se incluye:

##########################################################################
## Cámara
########################################################################


Campos_Camara = [

	Field('sitio_muestra_id','reference Sitio_muestra',required=True), 

 	#Se insertará a partir de un catálogo
	Field('nombre','string',required=True),

	Field('fecha_inicio','date',required=True),
	Field('fecha_termino','date',required=True),
	Field('hora_inicio','time',required=True),
	Field('hora_termino','time',required=True),

	Field('lat_grado','integer',required=True),
	Field('lat_min','integer',required=True),
	Field('lat_seg','double',required=True),
	Field('lon_grado','integer',required=True),
	Field('lon_min','integer',required=True),
	Field('lon_seg','double',required=True),
	Field('altitud','double',required=True),
	Field('gps_error','double',required=True),

	#Se insertarán a partir de un catálogo
	Field('elipsoide','string',required=True),
	Field('condiciones_ambientales','string',required=True),

	Field('distancia_centro','double'),
	Field('azimut','double'),

	#Se insertarán a partir de un catálogo
	Field('resolucion','string',required=True),
	Field('sensibilidad','string',required=True),

    Field('comentario', 'text')
    ]

db.define_table('Camara',*Campos_Camara,singular='Trampa cámara',plural=
	'Trampas cámara')

########################
#Imagen_referencia_camara
########################

Campos_Imagen_referencia_camara = [

	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_camara',*Campos_Imagen_referencia_camara, 
	singular='Imagen cámara',plural='Imágenes cámaras')

########################
#Archivo_camara
########################

Campos_Archivo_camara = [
	Field('camara_id','reference Camara',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True),
# uploadfolder='static/pictures'),      pensar estructura de carpetas
    Field('presencia','boolean'),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','integer')
    ]

db.define_table('Archivo_camara',*Campos_Archivo_camara, 
	singular='Archivo cámara',plural='Archivos cámara')
