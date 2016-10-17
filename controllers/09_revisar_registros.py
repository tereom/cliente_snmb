# coding: utf8

def conglomerado():

	## Controlador correspondiente a la pestaña "Conglomerado", de la sección:
	## "Revisar_registros". Genera las tablas de revisión usando el método  
	## "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Conglomerado_muestra"
	###########################################

	db.Conglomerado_muestra.tipo.requires = IS_IN_DB(db,
		db.Cat_tipo_conglomerado.nombre, '%(nombre)s')

	db.Conglomerado_muestra.estado.requires = IS_IN_DB(db,
		db.Cat_estado_conglomerado.nombre, '%(nombre)s')

	db.Conglomerado_muestra.municipio.requires = IS_IN_DB(db,
		db.Cat_municipio_conglomerado.nombre, '%(nombre)s')

	db.Conglomerado_muestra.tenencia.requires = IS_IN_DB(db,
		db.Cat_tenencia_conglomerado.nombre, '%(nombre)s')

	db.Conglomerado_muestra.uso_suelo_tipo.requires = IS_IN_DB(db,
		db.Cat_suelo_conglomerado.nombre, '%(nombre)s')

	# Este lo quitamos para que no tengan problemas si no deben llenar el campo
	# "vegetacion_tipo".
	#db.Conglomerado_muestra.vegetacion_tipo.requires = IS_IN_DB(db,
	#    db.Cat_vegetacion_conglomerado.nombre,'%(nombre)s')

	###########################################
	# Menús desplegables de "Sitio_muestra"
	###########################################

	db.Sitio_muestra.sitio_numero.requires = IS_IN_DB(db,db.Cat_numero_sitio.nombre,
		'%(nombre)s')
	db.Sitio_muestra.elipsoide.requires = IS_IN_DB(db,db.Cat_elipsoide.nombre,
		'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Sitio_muestra.conglomerado_muestra_id.writable = False
	db.Imagen_referencia_sitio.sitio_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Conglomerado_muestra,
		linked_tables = ['Sitio_muestra', 'Imagen_referencia_sitio', 'Formato_campo'],
		user_signature = False,
		details = True,
		csv = True,
		maxtextlengths = {'Imagen_referencia_sitio.archivo_nombre_original' : 50},
		headers = {'Sitio_muestra.existe' : 'Muestreado'}
		)

	return dict(form = form)

def camara():

	## Controlador correspondiente a la pestaña "Cámara", de la sección:
	## "Revisar_registros". Genera las tablas de revisión usando el método  
	## "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Camara"
	###########################################

	db.Camara.elipsoide.requires = IS_IN_DB(db,db.Cat_elipsoide.nombre,
		'%(nombre)s')
	db.Camara.resolucion.requires=IS_IN_DB(db,db.Cat_resolucion_camara.nombre,
	'%(nombre)s')
	db.Camara.sensibilidad.requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.nombre,
	'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Camara.sitio_muestra_id.writable = False
	db.Imagen_referencia_camara.camara_id.writable = False
	db.Archivo_camara.camara_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Camara,
		linked_tables = [
			'Archivo_camara',
			'Imagen_referencia_camara'],
		user_signature = False, 
		details = True,
		csv = True,
		maxtextlengths = {'Archivo_camara.archivo_nombre_original' : 70,
		'Imagen_referencia_camara.archivo_nombre_original' : 50})

	return dict(form = form)

def grabadora():

	## Controlador correspondiente a la pestaña "Grabadora", de la sección:
	## "Revisar_registros". Genera las tablas de revisión usando el método  
	## "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Grabadora"
	###########################################

	db.Grabadora.elipsoide.requires = IS_IN_DB(db,db.Cat_elipsoide.nombre,
		'%(nombre)s')
	db.Grabadora.condiciones_ambientales.requires = IS_IN_DB(db,
		db.Cat_condiciones_ambientales.nombre, '%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Grabadora.sitio_muestra_id.writable = False
	db.Imagen_referencia_grabadora.grabadora_id.writable = False
	db.Imagen_referencia_microfonos.grabadora_id.writable = False
	db.Archivo_referencia_grabadora.grabadora_id.writable = False
	db.Archivo_grabadora.grabadora_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Grabadora,
		linked_tables = [
			'Archivo_grabadora',
			'Archivo_referencia_grabadora',
			'Imagen_referencia_grabadora',
			'Imagen_referencia_microfonos'
		],
		details = True,
		csv = True,
		user_signature = False, 
		maxtextlengths = {
			'Archivo_grabadora.archivo_nombre_original' : 70,
			'Archivo_referencia_grabadora.archivo_nombre_original' : 50,
			'Imagen_referencia_grabadora.archivo_nombre_original' : 50,
			'Imagen_referencia_microfonos.archivo_nombre_original' : 50,
		}
	)

	return dict(form = form)

def transecto_muestra():

	## Controlador correspondiente a la pestaña "Especies_invasoras y huellas/
	## excretas", de la sección: "Revisar_registros". Genera las tablas de
	## revisión usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Transecto_muestra"
	###########################################

	db.Transecto_muestra.transecto_numero.requires = IS_IN_DB(db,
		db.Cat_numero_transecto.nombre, '%(nombre)s')

	###########################################
	# Menús desplegables de "Especie_invasora"
	###########################################

	db.Especie_invasora.numero_individuos.requires = IS_IN_DB(db,
		db.Cat_numero_individuos.nombre, '%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Transecto_muestra.conglomerado_muestra_id.writable = False
	db.Especie_invasora.transecto_muestra_id.writable = False
	db.Archivo_especie_invasora.especie_invasora_id.writable = False
	db.Huella_excreta.transecto_muestra_id.writable = False
	db.Archivo_huella_excreta.huella_excreta_id.writable = False

	form = SQLFORM.smartgrid(db.Transecto_muestra,
		linked_tables = [
			'Especie_invasora',
			'Archivo_especie_invasora',
			'Huella_excreta',
			'Archivo_huella_excreta'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_especie_invasora.archivo_nombre_original' : 50,
			'Archivo_huella_excreta.archivo_nombre_original' : 50
		},
		headers = {
			'Huella_excreta.es_huella' : 'Huella'
		}
	)

	return dict(form = form)

def especie_invasora_extra():

	## Controlador correspondiente a la pestaña "Especies invasoras extra",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Especie_invasora_extra"
	###########################################

	db.Especie_invasora_extra.elipsoide.requires = IS_IN_DB(db,
		db.Cat_elipsoide.nombre, '%(nombre)s')
	db.Especie_invasora_extra.numero_individuos.requires = IS_IN_DB(db,
	db.Cat_numero_individuos.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Especie_invasora_extra.conglomerado_muestra_id.writable = False
	db.Archivo_especie_invasora_extra.especie_invasora_extra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Especie_invasora_extra,
		linked_tables = [
			'Archivo_especie_invasora_extra'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_especie_invasora_extra.archivo_nombre_original' : 50
		}
	)

	return dict(form = form)

def huella_excreta_extra():

	## Controlador correspondiente a la pestaña "Huellas/excretas extra",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Huella_excreta_extra"
	###########################################

	db.Huella_excreta_extra.elipsoide.requires = IS_IN_DB(db,
		db.Cat_elipsoide.nombre, '%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Huella_excreta_extra.conglomerado_muestra_id.writable = False
	db.Archivo_huella_excreta_extra.huella_excreta_extra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Huella_excreta_extra,
		linked_tables = [
			'Archivo_huella_excreta_extra'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_huella_excreta_extra.archivo_nombre_original' : 50
		},
		headers = {
			'Huella_excreta_extra.es_huella' : 'Huella'
		}
	)

	return dict(form = form)

def especimen_restos_extra():

	## Controlador correspondiente a la pestaña "Especímenes/restos extra",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Especimen_restos_extra"
	###########################################

	db.Especimen_restos_extra.elipsoide.requires = IS_IN_DB(db,
		db.Cat_elipsoide.nombre, '%(nombre)s')
	db.Especimen_restos_extra.numero_individuos.requires = IS_IN_DB(db,
		db.Cat_numero_individuos.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Especimen_restos_extra.conglomerado_muestra_id.writable = False
	db.Archivo_especimen_restos_extra.especimen_restos_extra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Especimen_restos_extra,
		linked_tables = [
			'Archivo_especimen_restos_extra'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_especimen_restos_extra.archivo_nombre_original' : 50
		},
		headers = {
			'Especimen_restos_extra.es_especimen' : 'Espécimen'
		}
	)

	return dict(form = form)

def punto_conteo_aves():

	## Controlador correspondiente a la pestaña "Conteo de aves",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Punto_conteo_aves"
	###########################################

	db.Punto_conteo_aves.condiciones_ambientales.requires=IS_IN_DB(db,
		db.Cat_condiciones_ambientales.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Punto_conteo_aves.sitio_muestra_id.writable = False
	db.Avistamiento_aves.punto_conteo_aves_id.writable = False
	db.Archivo_avistamiento_aves.avistamiento_aves_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Punto_conteo_aves,
		linked_tables = [
			'Avistamiento_aves',
			'Archivo_avistamiento_aves'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_avistamiento_aves.archivo_nombre_original' : 50
		},
	)

	return dict(form = form)

def transecto_ramas():

	## Controlador correspondiente a la pestaña "Material leñoso caído",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Transecto_ramas"
	###########################################

	db.Transecto_ramas.direccion.requires=IS_IN_DB(db,
		db.Cat_transecto_direccion.nombre,'%(nombre)s')

	###########################################
	# Menús desplegables de "Rama_1000h"
	###########################################

	db.Rama_1000h.grado.requires=IS_IN_DB(db,
		db.Cat_grado_carbono.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Transecto_ramas.sitio_muestra_id.writable = False
	db.Rama_1000h.transecto_ramas_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Transecto_ramas,
		linked_tables = [
			'Rama_1000h'
		],
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def punto_carbono():

	## Controlador correspondiente a la pestaña "Carbono en el mantillo",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Punto_carbono"
	###########################################

	db.Punto_carbono.material_tipo.requires=IS_IN_DB(db,
		db.Cat_material_carbono.nombre,'%(nombre)s')
	db.Punto_carbono.transecto_direccion.requires=IS_IN_DB(db,
	    db.Cat_transecto_direccion.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Punto_carbono.sitio_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Punto_carbono,
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def arbol_transecto():

	## Controlador correspondiente a la pestaña "Árboles pequeños y arbustos",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Arbol_transecto"
	###########################################

	db.Arbol_transecto.transecto.requires=IS_IN_DB(db,
		db.Cat_transecto_direccion.nombre,'%(nombre)s')
	db.Arbol_transecto.forma_vida.requires=IS_IN_DB(db,
		db.Cat_forma_vida.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Arbol_transecto.sitio_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Arbol_transecto,
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def arbol_cuadrante():

	## Controlador correspondiente a la pestaña "Árboles grandes",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Arbol_cuadrante"
	###########################################

	db.Arbol_cuadrante.forma_vida.requires=IS_IN_DB(db,
		db.Cat_forma_vida_arboles_grandes.nombre,'%(nombre)s')
	db.Arbol_cuadrante.cambios.requires=IS_IN_DB(db,
		db.Cat_cambios_arboles_grandes.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Arbol_cuadrante.sitio_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Arbol_cuadrante,
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def informacion_epifitas():

	## Controlador correspondiente a la pestaña "Epífitas",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Campos no modificables
	###########################################

	db.Informacion_epifitas.conglomerado_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Informacion_epifitas,
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def impacto_actual():

	## Controlador correspondiente a la pestaña "Impactos ambientales actuales",
	## de la sección: "Revisar_registros". Genera las tablas de revisión
	## usando el método "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Impacto_actual"
	###########################################

	db.Impacto_actual.tipo.requires=IS_IN_DB(db,
		db.Cat_tipo_impacto.nombre,'%(nombre)s')
	db.Impacto_actual.en_vegetacion.requires=IS_IN_DB(db,
		db.Cat_severidad_impactos.nombre,'%(nombre)s')
	db.Impacto_actual.en_suelo.requires=IS_IN_DB(db,
		db.Cat_severidad_impactos.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Impacto_actual.conglomerado_muestra_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Impacto_actual,
		details = True,
		csv = True,
		user_signature = False
	)

	return dict(form = form)

def plaga():

	## Controlador correspondiente a la pestaña "Plagas", de la sección:
	## "Revisar_registros". Genera las tablas de revisión usando el método
	## "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Plaga"
	###########################################

	db.Plaga.agente.requires=IS_IN_DB(db,
		db.Cat_agente_impactos.nombre,'%(nombre)s')
	db.Plaga.prop_afectacion_arborea.requires=IS_IN_DB(db,
		db.Cat_prop_afectacion.nombre,'%(nombre)s')
	db.Plaga.prop_afectacion_repoblado.requires=IS_IN_DB(db,
		db.Cat_prop_afectacion.nombre,'%(nombre)s')

	###########################################
	# Campos no modificables
	###########################################

	db.Plaga.conglomerado_muestra_id.writable = False
	db.Archivo_plaga.plaga_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Plaga,
		linked_tables = [
			'Archivo_plaga'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_plaga.archivo_nombre_original' : 50
		}
	)

	return dict(form = form)

def incendio():

	## Controlador correspondiente a la pestaña "Incendios", de la sección:
	## "Revisar_registros". Genera las tablas de revisión usando el método
	## "smartgrid" incluido en Web2py.

	###########################################
	# Menús desplegables de "Incendio"
	###########################################

	db.Incendio.tipo.requires=IS_IN_DB(db,db.Cat_incendio.nombre,'%(nombre)s')
	db.Incendio.prop_afectacion_herbacea.requires=IS_IN_DB(db,
	    db.Cat_prop_afectacion.nombre,'%(nombre)s')
	db.Incendio.prop_afectacion_arbustiva.requires=IS_IN_DB(db,
	    db.Cat_prop_afectacion.nombre,'%(nombre)s')
	db.Incendio.prop_afectacion_arborea.requires=IS_IN_DB(db,
	    db.Cat_prop_afectacion.nombre,'%(nombre)s')
	db.Incendio.prop_copa_quemada.requires=IS_IN_DB(db,
	    db.Cat_prop_afectacion.nombre,'%(nombre)s')	

	###########################################
	# Campos no modificables
	###########################################

	db.Incendio.conglomerado_muestra_id.writable = False
	db.Archivo_incendio.incendio_id.writable = False

	###########################################
	# Generando la forma
	###########################################

	form = SQLFORM.smartgrid(db.Incendio,
		linked_tables = [
			'Archivo_incendio'
		],
		details = True,
		csv = True,
		user_signature = False,
		maxtextlengths = {
			'Archivo_incendio.archivo_nombre_original' : 50
		}
	)

	return dict(form = form)