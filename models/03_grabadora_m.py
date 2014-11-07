# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Grabadora, es decir: Grabadora, Imagen_referencia_grabadora, 
## Archivo_referencia_grabadora, Imagen_referencia_microfonos,
## Archivo_grabadora
## El campo de ID es automático en Web2py, por lo que no se incluye:

##########################################################################
## Grabadora
########################################################################

Campos_Grabadora = [

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

    Field('microfonos_mojados','boolean',required=True),
    Field('comentario', 'text')
    ]

db.define_table('Grabadora',*Campos_Grabadora)

########################
#Imagen_referencia_grabadora
########################

Campos_Imagen_referencia_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_grabadora',*Campos_Imagen_referencia_grabadora,
    singular='Imagen grabadora', plural='Imágenes gradadoras')

########################
#Imagen_referencia_microfonos
########################

Campos_Imagen_referencia_microfonos = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_microfonos',*Campos_Imagen_referencia_microfonos,
    singular='Imágen micrófonos', plural='Imágenes micrófonos')

########################
#Archivo_referencia_grabadora (metadatos)
########################

Campos_Archivo_referencia_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_referencia_grabadora',*Campos_Archivo_referencia_grabadora, 
    singular='Archivo metadatos', plural='Archivos metadatos')

########################
#Archivo_grabadora
########################

Campos_Archivo_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True),
    Field('es_audible','boolean',required=True)
    ]

db.define_table('Archivo_grabadora',*Campos_Archivo_grabadora, 
    singular='Archivo grabadora', plurals='Archivos grabadoras')