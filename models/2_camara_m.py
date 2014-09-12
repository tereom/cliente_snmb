#coding: utf8

# En esta segción se definen las tablas correspondientes a la pestaña de 
# Camara, es decir: Camara, File_camera, Reference_image_camera
# El campo de ID es automático en Web2py, por lo que no se incluye:

Campos_Camara = [
    Field('nombre','reference Cat_nombre_camara',label=T("Código cámara")), 
    Field('fecha_inicio','date',label=T("Fecha de colocación"),required='TRUE'),
    Field('fecha_termino','date',label=T("Fecha de levantamiento"),
    	required='TRUE'),
    Field('hora_inicio','time',label=T("Hora inicio"),required='TRUE'),
    Field('hora_termino', 'date',label=T("Hora término"),required='TRUE'),
    Field('lat_grado','integer',label=T("grado"),required='TRUE'),
    Field('lat_min','integer',label=T("minuto"),required='TRUE'),
    Field('lat_seg','double',label=T("segundo"),required='TRUE'),
    Field('lon_grado','integer',label=T("grado"),required='TRUE'),
    Field('lon_min','integer',label=T("minuto"),required='TRUE'),
    Field('lon_seg','double',label=T("segundo"),required='TRUE'),
    Field('altitud','double',label=T("Altitud(m)"),required='TRUE'),
    Field('gps_error','double',label=T("Error(m)"),required='TRUE'),
    Field('elipsoide', 'reference Cat_elipsoide_sitio',label=T("Datum"),
    	required='TRUE'), 
    Field('sitio_muestra_id','reference Sitio_muestra'),         
    Field('distancia_centro','double',
    	label=T("Distancia al centro del sitio (m)"),required='TRUE'),
    Field('llovio','boolean',label=T("Llovió durante el muestreo")),
    Field('resolucion','reference Cat_resolucion_camara',label=T("Resolución")),
    Field('sensibilidad','reference Cat_sensibilidad_camara',
    	label=T("Sensibilidad")),
    Field('comentario', 'text',label=T("Observaciones"))]

db.define_table('Camara',*Campos_Camara)

Campos_Imagen_referencia_camara = [
	Field('camara_id','reference Camara', required='TRUE'),
    Field('archivo_nombre',required='TRUE'),
    Field('archivo_nombre_original', 'upload', autodelete=True, label=T("Fotografía"), required='TRUE')]

db.define_table('Imagen_referencia_camara',*Campos_Imagen_referencia_sitio)

