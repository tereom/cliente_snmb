# coding: utf8

# En esta sección se definen las tablas correspondientes a la pestaña de 
# epífitas, es decir: Informacion_epifitas

##########################################################################
## Informacion_epifitas
##########################################################################

Campos_Informacion_epifitas = [

    Field('sitio_muestra_id','reference Sitio_muestra',required=True),
    Field('helechos_observados','boolean',required=True),
    Field('orquideas_observadas','boolean',required=True),
    Field('musgos_observados','boolean',required=True),
    Field('liquenes_observados','boolean',required=True),
    Field('cactaceas_observadas','boolean',required=True),
    Field('bromeliaceas_observadas','boolean',required=True),
    Field('otras_observadas','boolean',required=True),
    Field('nombre_otras','string')
    ]

db.define_table('Informacion_epifitas',*Campos_Informacion_epifitas,
    singular='Epífita',plural='Epífitas')