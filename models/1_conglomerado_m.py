# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de Conglomerado, es decir: Conglomerado_muestra, Sitio_muestra y Reference_image_site:
## El campo de ID es automático en Web2py, por lo que no se incluye:

###FALTA REVISAR CUÁLES CAMPOS SON ÚNICOS (LLAVES NO PRIMARIAS)

########################
#Conglomerado_muestra
########################

Campos_Conglomerado_muestra = [
	Field('nombre','integer',label=T("Número de conglomerado"),required='TRUE'),
	Field('fecha_visita', 'date',label=T("Fecha visita"),required='TRUE'),
	Field('tipo','reference Cat_tipo_conglomerado',label=T("Tipo de conglomerado"),required='TRUE'),
    Field('estado','reference Cat_estado_conglomerado',label=T("Estado"),required='TRUE'),
    Field('municipio','reference Cat_municipio_conglomerado',label=T("Municipio"),required='TRUE'),
    Field('predio','string',label=T("Predio"),required='TRUE'),
    Field('tenencia','reference Cat_tenencia_conglomerado',label=T("Tenencia"), required='TRUE'),
    Field('uso_suelo_tipo', 'reference Cat_suelo_conglomerado',label=T("Tipo de uso de suelo"),required='TRUE'),
	Field('vegetacion_tipo','reference Cat_vegetacion_conglomerado',label=T("Tipo de vegetación")),
    Field('perturbado','boolean',label=T("Perturbado")),
	Field('comentario','text',label=T("Observaciones"))
	]

db.define_table('Conglomerado_muestra', *Campos_Conglomerado_muestra)

########################
#Sitio_muestra
########################

Campos_Sitio_muestra = [
	Field('conglomerado_muestra_id','reference Conglomerado_muestra',
		required='TRUE'),
	Field('sitio_numero','reference Cat_numero_sitio',
		label=T("Número de sitio"), required='TRUE'),
	Field('existe', 'boolean',label=T("Existe"),required='TRUE'),
	Field('lat_grado','integer',label=T("Grado")),
	Field('lat_min','integer',label=T("Minuto")),
	Field('lat_seg','double',label=T("Segundo")),
	Field('lon_grado','integer',label=T("Grado")),
	Field('lon_min','integer',label=T("Minuto")),
	Field('lon_seg','double',label=T("Segundo")),
    Field('altitud','double',label=T("Altitud(m)")),
    Field('gps_error','double',label=T("Error(m)")),
	Field('elipsoide', 'reference Cat_elipsoide',label=T("Datum")), 
    Field('evidencia', 'boolean',label=XML("Evidencia <br/> anterior"))
    ] 

db.define_table('Sitio_muestra',*Campos_Sitio_muestra)

########################
#Imagen_referencia_sitio
########################

Campos_Imagen_referencia_sitio = [
	Field('sitio_muestra_id','reference Sitio_muestra',required='TRUE'),
    Field('archivo_nombre_original',required='TRUE'),
    Field('archivo','upload',autodelete=True,label=T("Fotografía"), required='TRUE')]
    
    # La inclusión del siguiente campo no es segura, ya que hay que ver su utilidad. Si se
    #incluye, se necesitará un módulo que lea datos de la forma y los combine para formar
    #el nombre_CONAFOR. También hay que ver si es necesario que los archivos se guarden en
    #carpetas distintas, ya que todo se va a hacer de manera automatizada.
    # Field('archivo_nombre_CONAFOR',required='TRUE'),

db.define_table('Imagen_referencia_sitio',*Campos_Imagen_referencia_sitio)

########################################################################
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more opcions, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
