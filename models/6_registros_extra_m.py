# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 

# Registros Extras, es decir: Especimen_restos_extra, 
# Huella_excreta, Archivo_huella_excreta

##########################################################################
## Especimen_restos_extra
##########################################################################

Campos_Especimen_restos_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required=True),
    Field('fecha','date',label=T("Fecha"),required=True),
    Field('hora', 'time',label=T("Hora"),required=True),
    Field('tecnico','string',label=T("Técnico"),required=True),

	Field('lat_grado','integer',label=T("Grado"),required=True),
	Field('lat_min','integer',label=T("Minuto"),required=True),
	Field('lat_seg','double',label=T("Segundo"),required=True),
	Field('lon_grado','integer',label=T("Grado"),required=True),
	Field('lon_min','integer',label=T("Minuto"),required=True),
	Field('lon_seg','double',label=T("Segundo"),required=True),
    Field('altitud','double',label=T("Altitud(m)"),required=True),
    Field('gps_error','double',label=T("Error(m)"),required=True),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum"),
		required=True),

	Field('es_especimen','boolean',label=T("Especimen"),required=True),
	Field('hay_nombre_comun','boolean',label=T("Nombre común"),required=True),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico', 'boolean',label=T("Nombre científico"),
    	required=True),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Cat_numero_individuos',
		label=T("Número de individuos"),required=True),
    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Especimen_restos_extra',*Campos_Especimen_restos_extra)

##########################################################################
## Archivo_Especimen_restos_extra
########################################################################

Campos_Archivo_especimen_restos_extra = [
    Field('especimen_restos_extra_id','reference Especimen_restos_extra',
    	required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_especimen_restos_extra',
	*Campos_Archivo_especimen_restos_extra)

##########################################################################
## Especie_invasora_extra
##########################################################################

Campos_Especie_invasora_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
    	required=True),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required=True),
    Field('fecha','date',label=T("Fecha"),required=True),
    Field('hora','time',label=T("Hora"),required=True),
    Field('tecnico','string',label=T("Técnico"),required=True),

	Field('lat_grado','integer',label=T("Grado"),required=True),
	Field('lat_min','integer',label=T("Minuto"),required=True),
	Field('lat_seg','double',label=T("Segundo"),required=True),
	Field('lon_grado','integer',label=T("Grado"),required=True),
	Field('lon_min','integer',label=T("Minuto"),required=True),
	Field('lon_seg','double',label=T("Segundo"),required=True),
    Field('altitud','double',label=T("Altitud(m)"),required=True),
    Field('gps_error','double',label=T("Error(m)"),required=True),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum"),
		required=True), 	

	Field('nombre_en_lista','boolean',label=T("Lista CONABIO de especies"),
		required=True),
	Field('hay_nombre_comun','boolean',label=T("Nombre común"),
		required=True),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico','boolean',label=T("Nombre científico"),
    	required=True),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Cat_numero_individuos',
		label=T("Número de individuos"),required=True),

    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Especie_invasora_extra',*Campos_Especie_invasora_extra)

##########################################################################
## Archivo_especie_invasora_extra
########################################################################

Campos_Archivo_especie_invasora_extra = [
    Field('especie_invasora_extra_id','reference Especie_invasora_extra',
    	required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_especie_invasora_extra',
	*Campos_Archivo_especie_invasora_extra)


# Registros Extras, es decir:
# Especie_invasora_extra,
# Huella_excreta_extra
# Especimen_restos_extra,
# Archivo_Especie_invasora_extra
# Archivo_Huella_excreta_extra
# Archivo_Especimen_restos_extra


##########################################################################
## Huella_excreta_extra
##########################################################################

Campos_Huella_excreta_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
    	required=True),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required=True),
    Field('fecha','date',label=T("Fecha"),required=True),
    Field('hora','time',label=T("Hora"),required=True),
    Field('tecnico','string',label=T("Técnico"),required=True),

	Field('lat_grado','integer',label=T("Grado"),required=True),
	Field('lat_min','integer',label=T("Minuto"),required=True),
	Field('lat_seg','double',label=T("Segundo"),required=True),
	Field('lon_grado','integer',label=T("Grado"),required=True),
	Field('lon_min','integer',label=T("Minuto"),required=True),
	Field('lon_seg','double',label=T("Segundo"),required=True),
    Field('altitud','double',label=T("Altitud(m)"),required=True),
    Field('gps_error','double',label=T("Error(m)"),required=True),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum"), 
		required=True), 	

	Field('es_huella','boolean',label=T("Huellas"),required=True),		
	Field('hay_nombre_comun','boolean',label=T("Nombre común"),required=True),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico','boolean',label=T("Nombre científico"),
        required=True),
    Field('nombre_cientifico','string'),
    Field('largo','double',label=T("Largo"),required=True),
    Field('ancho','double',label=T("Ancho"),required=True),

    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Huella_excreta_extra', *Campos_Huella_excreta_extra)

##########################################################################
## Archivo_huella_excreta_extra
########################################################################

Campos_Archivo_huella_excreta_extra = [
    Field('huella_excreta_extra_id','reference Huella_excreta_extra',
        required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)
    ]

db.define_table('Archivo_huella_excreta_extra',
	*Campos_Archivo_huella_excreta_extra)

