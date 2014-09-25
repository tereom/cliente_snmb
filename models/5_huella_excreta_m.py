# coding: utf8

## En esta sección se definen las tablas correspondientes a la pestaña de 
## Huellas y Excretas, es decir: Transecto_huellas_excretas_muestra, 
## Huella_excreta, Archivo_huella_excreta

##########################################################################
## Transecto_huellas_excretas_muestra
########################################################################

Campos_Transecto_huellas_excretas_muestra = [

    Field('conglomerado_muestra_id','reference Conglomerado_muestra',
        required=True),
    Field('fecha','date',required=True),
    Field('transecto_numero','reference Cat_numero_transecto', required=True),
    Field('tecnico','string',required=True),
    Field('hora_inicio','time',required=True),
    Field('hora_termino','time',required=True),
    Field('comentario','text')
    ]

db.define_table('Transecto_huellas_excretas_muestra',
    *Campos_Transecto_huellas_excretas_muestra,
    singular='Transecto huellas y excretas',
    plural='Transectos huellas y excretas')

##########################################################################
## Huella_excreta
########################################################################


Campos_Huella_excreta = [

    Field('transecto_huellas_excretas_id','reference Transecto_huellas_excretas_muestra',
        required=True),
    Field('es_huella','boolean', required=True),
    Field('nombre_comun','string'),
    Field('nombre_cientifico','string'),
    Field('largo','double',required=True),
    Field('ancho','double',required=True)
    ]

db.define_table('Huella_excreta',*Campos_Huella_excreta,
    singular='Huellas/excretas',plural='Huellas/excretas')

##########################################################################
## Archivo_huella_excreta
########################################################################

Campos_Archivo_huella_excreta = [

    Field('huella_excreta_id','reference Huella_excreta',required=True),
    Field('archivo_nombre_original',required=True),
    Field('archivo', 'upload', autodelete=True,required=True)
    ]

db.define_table('Archivo_huella_excreta',*Campos_Archivo_huella_excreta,
    singular='Archivo huellas/excretas',plural='Archivos huellas/excretas')
