# coding: utf8

## En esta segción se definen las tablas correspondientes a la pestaña de 
## Huellas y Excretas, es decir: Transecto_huellas_excretas_muestra, 
## Huella_excreta, Archivo_huella_excreta
Campos_Transecto_Huellas_excretas = [
    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
        required='TRUE'),
    Field('transecto_numero',label=T("Transecto"),required='TRUE'),  
    Field('fecha','date',label=T("Fecha"),required='TRUE'),
    Field('hora_inicio','time',label=T("Hora inicio"),required='TRUE'),
    Field('hora_termino','time',label=T("Hora término"),required='TRUE'),
    Field('tecnico','string',label=T("Técnico"),required='TRUE'),
    Field('comentario','text',label=T("Observaciones"))
    ]

db.define_table('Transecto_huellas_excretas_muestra',
        *Campos_Transecto_Huellas_excretas)

Campos_Huella_excreta = [
    Field('transecto_huellas_excretas_id',
        'reference Transecto_huellas_excretas_muestra'),
    Field('es_huella','boolean',label=T("Huellas")),
    Field('hay_nombre_comun','boolean',label=T("Nombre común")),
    Field('nombre_comun','string'),
    Field('hay_nombre_cientifico','boolean',label=T("Nombre científico")),
    Field('nombre_cientifico','string'),
    Field('largo','double',label=T("Largo")),
    Field('ancho','double',label=T("Ancho"))
]

db.define_table('Huella_excreta',*Campos_Huella_excreta)

Campos_Archivo_huella_excreta = [
    Field('huella_excreta_id','reference Huella_excreta',required='TRUE'),
    Field('archivo_nombre',required='TRUE'),
    Field('archivo_nombre_original','upload',autodelete=True,
        label=T("Fotografía"),required='TRUE')
    ]

db.define_table('Archivo_huella_excreta',*Campos_Huella_excreta)
