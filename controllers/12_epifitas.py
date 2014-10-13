# coding: utf8

def index1():

    Campos_forma = [

    	# Utilizamos una FORM porque nos brinda mayor flexibilidad, como por ejemplo,
    	# para incluir las dropdowns en cascada.
    
    	#Ésta forma únicamente se utilizará para validar antes de ingresar a la base
    	#de datos y así, evitar excepciones.

      	#Datos para localizar un sitio único y la información de epífitas a éste.

        SELECT(_name='conglomerado_muestra_id',
            requires=IS_IN_DB(db,db.Conglomerado_muestra.id,'%(nombre)s')),
        SELECT(_name='sitio_muestra_id',
            requires=IS_IN_DB(db,db.Sitio_muestra.id,'%(nombre)s')),

        #Datos de epífitas:

        INPUT(_name='helechos_observados',_type='boolean'),
        INPUT(_name='orquideas_observadas',_type='boolean'),
        INPUT(_name='musgos_observados',_type='boolean'),
        INPUT(_name='liquenes_observados',_type='boolean'),
        INPUT(_name='cactaceas_observadas',_type='boolean'),
        INPUT(_name='bromeliaceas_observadas',_type='boolean'),
        INPUT(_name='otras_observadas',_type='boolean'),
        INPUT(_name='nombre_otras',_type='string')

    ]

    forma = FORM(*Campos_forma)

    if forma.accepts(request.vars,formname='formaHTML'):

    	formaEpifitas = {}

    	formaEpifitas['sitio_muestra_id']=forma.vars['sitio_muestra_id']

    	#Insertando "False" cuando se recibe "None" del HTML:

    	if bool(forma.vars['helechos_observados']):
			formaEpifitas['helechos_observados']=forma.vars['helechos_observados']
		else:
			formaEpifitas['helechos_observados']=False

		if bool(forma.vars['orquideas_observadas']):
			formaEpifitas['orquideas_observadas']=forma.vars['orquideas_observadas']
		else:
			formaEpifitas['orquideas_observadas']=False

		if bool(forma.vars['musgos_observados']):
			formaEpifitas['musgos_observados']=forma.vars['musgos_observados']
		else:
			formaEpifitas['musgos_observados']=False

    	if bool(forma.vars['liquenes_observados']):
			formaEpifitas['liquenes_observados']=forma.vars['liquenes_observados']
		else:
			formaEpifitas['liquenes_observados']=False

    	if bool(forma.vars['cactaceas_observadas']):
			formaEpifitas['cactaceas_observadas']=forma.vars['cactaceas_observadas']
		else:
			formaEpifitas['cactaceas_observadas']=False

    	if bool(forma.vars['bromeliaceas_observadas']):
			formaEpifitas['bromeliaceas_observadas']=forma.vars['bromeliaceas_observadas']
		else:
			formaEpifitas['bromeliaceas_observadas']=False

    	if bool(forma.vars['otras_observadas']):
			formaEpifitas['otras_observadas']=forma.vars['otras_observadas']
			formaEpifitas['nombre_otras']forma.vars['nombre_otras']
		else:
			formaEpifitas['otras_observadas']=False

		#insertando en la base de datos:
		db.Informacion_epifitas.insert(**formaEpifitas)

		response.flash = 'Éxito'
        
    elif formaPuntos.errors:

        response.flash = 'Hubo un error al llenar la forma'

    else:
        
        response.flash ='Por favor, introduzca los campos obligatorios'







