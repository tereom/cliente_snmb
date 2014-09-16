# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Grabadora, es decir: Grabadora, Imagen_referencia_grabadora, 
## Archivo_referencia_grabadora, Imagen_referencia_microfonos
## Microphone_group, File_microphone_group
## El campo de ID es automático en Web2py, por lo que no se incluye:

Campos_Grabadoora = [
    Field('nombre','reference Cat_nombre_grabadora',required=True), 
    Field('fecha_inicio','date',required=True),
    Field('fecha_termino','date',required=True),
    Field('hora_inicio','time',required=True),
    Field('hora_termino', 'date',required=True),
    Field('lat_grado','integer',required=True),
    Field('lat_min','integer',required=True),
    Field('lat_seg','double',required=True),
    Field('lon_grado','integer',required=True),
    Field('lon_min','integer',required=True),
    Field('lon_seg','double',required=True),
    Field('altitud','double',required=True),
    Field('gps_error','double',required=True),
    Field('elipsoide', 'reference Cat_elipsoide_sitio',required=True),
    Field('sitio_muestra_id','reference Sitio_muestra',required=True),         
    Field('distancia_centro','double',required=True),
    Field('llovio','boolean',required=True),
    Field('comentario','text'),
    Field('microfonos_mojados','boolean',label=T("Se mojaron los micrófonos")),
    Field('comentario', 'text',label=T("Observaciones"))
    ]

db.define_table('Grabadora',*Campos_Grabadoora)

########################
#Imagen_referencia_grabadora
########################

Campos_Imagen_referencia_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_grabadora',*Campos_Imagen_referencia_grabadora)

########################
#Imagen_referencia_microfonos
########################

Campos_Imagen_referencia_microfonos = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Imagen_referencia_microfonos',*Campos_Imagen_referencia_microfonos)

########################
#Archivo_referencia_grabadora (metadatos)
########################

Campos_Archivo_referencia_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_referencia_grabadora',
    *Campos_Archivo_referencia_grabadora)


########################
#Archivo_referencia_grabadora
########################

Campos_Archivo_grabadora = [
    Field('grabadora_id','reference Grabadora',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_grabadora',*Campos_Archivo_grabadora)