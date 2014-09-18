# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 

# Registros Extras, es decir: Especimen_restos_extra, 
# Huella_excreta, Archivo_huella_excreta
'''
Campos_Especimen_restos_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required='TRUE'),
    Field('fecha','date',label=T("Fecha"),required='TRUE'),
    Field('hora', 'time',label=T("Hora"),required='TRUE'),
    Field('tecnico','string',label=T("Técnico"),required='TRUE'),
	Field('lat_grado','integer',label=T("Grado")),
	Field('lat_min','integer',label=T("Minuto")),
	Field('lat_seg','double',label=T("Segundo")),
	Field('lon_grado','integer',label=T("Grado")),
	Field('lon_min','integer',label=T("Minuto")),
	Field('lon_seg','double',label=T("Segundo")),
    Field('altitud','double',label=T("Altitud(m)")),
    Field('gps_error','double',label=T("Error(m)")),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum")), 
	Field('es_especimen','boolean',label=T("Especimen")),
	Field('hay_nombre_comun','boolean',label=T("Nombre común")),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico', 'boolean',label=T("Nombre científico")),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Especie_individuos_opcion',
		label=T("Número de individuos")),
    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Especimen_restos_extra',*Campos_Especimen_restos_extra)

Campos_Archivo_especimen_restos_extra = [
    Field('huella_excreta_id','reference Huella_excreta',required='TRUE'),
    Field('archivo_nombre',required='TRUE'),
    Field('archivo_nombre_original','upload',autodelete=True,
        label=T("Fotografía"),required='TRUE')
    ]

db.define_table('Archivo_especimen_restos_extra',
	*Campos_Archivo_especimen_restos_extra)

Campos_Especie_invasora_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required='TRUE'),
    Field('fecha','date',label=T("Fecha"),required='TRUE'),
    Field('hora','time',label=T("Hora"),required='TRUE'),
    Field('tecnico','string',label=T("Técnico"),required='TRUE'),
	Field('lat_grado','integer',label=T("Grado")),
	Field('lat_min','integer',label=T("Minuto")),
	Field('lat_seg','double',label=T("Segundo")),
	Field('lon_grado','integer',label=T("Grado")),
	Field('lon_min','integer',label=T("Minuto")),
	Field('lon_seg','double',label=T("Segundo")),
    Field('altitud','double',label=T("Altitud(m)")),
    Field('gps_error','double',label=T("Error(m)")),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum")), 	
	Field('nombre_en_lista','boolean',label=T("Lista CONABIO de especies")),
	Field('hay_nombre_comun', 'boolean', label=T("Nombre común")),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico', 'boolean', label=T("Nombre científico")),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Especie_individuos_opcion',
		label=T("Número de individuos")),
    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Especie_invasora_extra',*Campos_Especie_invasora_extra)

Campos_Archivo_especie_invasora_extra = [
    Field('huella_excreta_id','reference Huella_excreta',required='TRUE'),
    Field('archivo_nombre',required='TRUE'),
    Field('archivo_nombre_original','upload',autodelete=True,
        label=T("Fotografía"),required='TRUE')
=======
# Registros Extras, es decir:
# Especie_invasora_extra,
# Huella_excreta_extra
# Especimen_restos_extra,
# Archivo_Especie_invasora_extra
# Archivo_Huella_excreta_extra
# Archivo_Especimen_restos_extra

##########################################################################
## Especie_invasora_extra
##########################################################################

# Campos_Especie_invasora_extra = [
# 	Field('conglomerado_muestra_id','reference Conglomerado_muestra', required=True),
#     Field('esta_dentro_conglomerado','boolean',required=True),
#     Field('tecnico','string',required=True),
# 	Field('fecha','date',required=True),
# 	Field('hora','time',required=True),
	
# 	Field('lat_grado','integer',required=True),
# 	Field('lat_min','integer',required=True),
# 	Field('lat_seg','double',required=True),
# 	Field('lon_grado','integer',required=True),
# 	Field('lon_min','integer',required=True),
# 	Field('lon_seg','double',required=True),
# 	Field('altitud','double',required=True),
# 	Field('gps_error','double',required=True),
# 	Field('elipsoide', 'reference Cat_elipsoide_sitio',required=True),
	
# 	Field('nombre_en_lista','boolean', required=True),
# 	Field('hay_nombre_comun', 'boolean', required=True),
# 	Field('nombre_comun','string'),
# 	Field('hay_nombre_cientifico', 'boolean', required=True),
#     Field('nombre_cientifico','string'),
#     Field('numero_individuos', 'integer', required=True),
    
#     Field('comentario','text')
# ]

# db.define_table('Especie_invasora_extra', *Campos_Especie_invasora_extra)

# ##########################################################################
# ## Huella_excreta_extra
# ##########################################################################

# Campos_Huella_excreta_extra = [
  
#   	Field('conglomerado_muestra_id','reference Conglomerado_muestra', required=True),
#     Field('esta_dentro_conglomerado','boolean',required=True),
#     Field('tecnico','string',required=True),
# 	Field('fecha','date',required=True),
# 	Field('hora','time',required=True),
	
# 	Field('lat_grado','integer',required=True),
# 	Field('lat_min','integer',required=True),
# 	Field('lat_seg','double',required=True),
# 	Field('lon_grado','integer',required=True),
# 	Field('lon_min','integer',required=True),
# 	Field('lon_seg','double',required=True),
# 	Field('altitud','double',required=True),
# 	Field('gps_error','double',required=True),
# 	Field('elipsoide', 'reference Cat_elipsoide_sitio',required=True),
	
# 	Field('es_huella', 'boolean', required=True),
# 	Field('hay_nombre_comun', 'boolean', required=True),
# 	Field('nombre_comun','string'),
# 	Field('hay_nombre_cientifico', 'boolean', required=True),
#     Field('nombre_cientifico','string'),
#     Field('largo','double',required=True),
#     Field('ancho','double',required=True),
    
#     Field('comentario','text')
# ]

# db.define_table('Huella_excreta_extra', *Campos_Huella_excreta_extra)

# ##########################################################################
# ## Especimen_restos_extra
# ##########################################################################


# Campos_Especimen_restos_extra = [
  
#   	Field('conglomerado_muestra_id','reference Conglomerado_muestra', required=True),
#     Field('esta_dentro_conglomerado','boolean',required=True),
#     Field('tecnico','string',required=True),
# 	Field('fecha','date',required=True),
# 	Field('hora','time',required=True),
	
# 	Field('lat_grado','integer',required=True),
# 	Field('lat_min','integer',required=True),
# 	Field('lat_seg','double',required=True),
# 	Field('lon_grado','integer',required=True),
# 	Field('lon_min','integer',required=True),
# 	Field('lon_seg','double',required=True),
# 	Field('altitud','double',required=True),
# 	Field('gps_error','double',required=True),
# 	Field('elipsoide', 'reference Cat_elipsoide_sitio',required=True),
	
# 	Field('es_especimen', 'boolean', required=True),
# 	Field('hay_nombre_comun', 'boolean', required=True),
# 	Field('nombre_comun','string'),
# 	Field('hay_nombre_cientifico', 'boolean', required=True),
#     Field('nombre_cientifico','string'),
#     Field('numero_individuos', 'integer', required=True)
    
#     Field('comentario','text')
# ]

# db.define_table('Especimen_restos_extra', *Campos_Especimen_restos_extra)

# ##########################################################################
# ## Archivo_especie_invasora_extra
# ########################################################################

# Campos_Archivo_especie_invasora_extra = [
#     Field('especie_invasora_extra_id','reference Especie_invasora_extra',required=True),
#     Field('archivo_nombre_original',required=True),
#     Field('archivo', 'upload', autodelete=True,required=True)
#     ]

# db.define_table('Archivo_especie_invasora_extra',
# 	*Campos_Archivo_especie_invasora_extra)
	
# ##########################################################################
# ## Archivo_huella_excreta_extra
# ########################################################################

# Campos_Archivo_huella_excreta_extra = [
#     Field('huella_excreta_extra_id','reference Huella_excreta_extra',required=True),
#     Field('archivo_nombre_original',required=True),
#     Field('archivo', 'upload', autodelete=True,required=True)
#     ]

# db.define_table('Archivo_huella_excreta_extra',
# 	*Campos_Archivo_huella_excreta_extra)

# ##########################################################################
# ## Archivo_Especimen_restos_extra
# ########################################################################

# Campos_Archivo_especimen_restos_extra = [
#     Field('especimen_restos_extra_id','reference Especimen_restos_extra',required=True),
#     Field('archivo_nombre_original',required=True),
#     Field('archivo', 'upload', autodelete=True,required=True)
#     ]

# db.define_table('Archivo_especimen_restos_extra',
# 	*Campos_Archivo_especimen_restos_extra)
#    ]

db.define_table('Archivo_especie_invasora_extra',
	*Campos_Archivo_especie_invasora_extra)
<<<<<<< HEAD

Campos_Huella_excreta_extra = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra'),
    Field('esta_dentro_conglomerado','boolean',
    	label=T("Dentro del conglomerado"),required='TRUE'),
    Field('fecha','date',label=T("Fecha"),required='TRUE'),
    Field('hora', 'time',label=T("Hora"),required='TRUE'),
    Field('tecnico','string',label=T("Técnico"),required='TRUE'),
	Field('lat_grado','integer',label=T("Grado")),
	Field('lat_min','integer',label=T("Minuto")),
	Field('lat_seg','double',label=T("Segundo")),
	Field('lon_grado','integer',label=T("Grado")),
	Field('lon_min','integer',label=T("Minuto")),
	Field('lon_seg','double',label=T("Segundo")),
    Field('altitud','double',label=T("Altitud(m)")),
    Field('gps_error','double',label=T("Error(m)")),
	Field('elipsoide','reference Cat_elipsoide_sitio',label=T("Datum")), 	
	Field('es_huella', 'boolean',label=T("Huellas")),		
	Field('hay_nombre_comun', 'boolean',label=T("Nombre común")),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico', 'boolean',label=T("Nombre científico")),
    Field('nombre_cientifico','string'),
    Field('numero_individuos','reference Cat_numero_individuos',
		label=T("Número de individuos")),
    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Especie_invasora_extra',*Campos_Especie_invasora_extra)

Campos_Archivo_huella_excreta_extra = [
    Field('huella_excreta_id','reference Huella_excreta',required='TRUE'),
    Field('archivo_nombre',required='TRUE'),
    Field('archivo_nombre_original','upload',autodelete=True,
        label=T("Fotografía"),required='TRUE')
=======
	
##########################################################################
## Archivo_huella_excreta_extra
########################################################################

Campos_Archivo_huella_excreta_extra = [
    Field('huella_excreta_extra_id','reference Huella_excreta_extra',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
>>>>>>> 90bd548bf5a94b9834bc744db8bcde5f2f23f7ba
    ]

db.define_table('Archivo_huella_excreta_extra',
	*Campos_Archivo_huella_excreta_extra)
<<<<<<< HEAD
'''
##########################################################################
## Archivo_Especimen_restos_extra
########################################################################

Campos_Archivo_especimen_restos_extra = [
    Field('especimen_restos_extra_id','reference Especimen_restos_extra',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_especimen_restos_extra',
	*Campos_Archivo_especimen_restos_extra)
>>>>>>> FETCH_HEAD


