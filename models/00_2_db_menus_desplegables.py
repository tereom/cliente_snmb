# coding: utf8

## En esta sección se definen las tablas de los menus desplegables 
## correspondientes a CONANP

##########################################################################
## Pestaña Carbono
########################################################################

db.define_table('Cat_material_carbono',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_material_carbono.id>0).count() == 0:
	db.Cat_material_carbono.insert(nombre='HP - De pino')
	db.Cat_material_carbono.insert(nombre='HL - De latifoliadas')
	db.Cat_material_carbono.insert(nombre='HA - De abies')
	db.Cat_material_carbono.insert(nombre='MP - Madera putrefacta')
	db.Cat_material_carbono.insert(nombre='CO - Corteza')
	db.Cat_material_carbono.insert(nombre='RD - Roca desnuda')
	db.Cat_material_carbono.insert(nombre='MU - Musgo')
	db.Cat_material_carbono.insert(nombre='OS - Otros')
	db.Cat_material_carbono.insert(nombre='NO - No contiene')


db.define_table('Cat_grado_carbono',Field('nombre','integer',
	required='TRUE'))

if db(db.Cat_grado_carbono.id>0).count() == 0:
	db.Cat_grado_carbono.insert(nombre=1)
	db.Cat_grado_carbono.insert(nombre=2)
	db.Cat_grado_carbono.insert(nombre=3)
	db.Cat_grado_carbono.insert(nombre=4)
	db.Cat_grado_carbono.insert(nombre=5)


db.define_table('Cat_transecto_ramas',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_transecto_ramas.id>0).count() == 0:
	db.Cat_transecto_ramas.insert(nombre='Norte')
	db.Cat_transecto_ramas.insert(nombre='Este')
	db.Cat_transecto_ramas.insert(nombre='Sur')
	db.Cat_transecto_ramas.insert(nombre='Oeste')


db.define_table('Cat_forma_vida',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_forma_vida.id>0).count() == 0:
	db.Cat_forma_vida.insert(nombre='Arbustiva')
	db.Cat_forma_vida.insert(nombre='Arbórea')


##########################################################################
## Pestaña Impactos ambientales
########################################################################

# db.define_table('Cat_tipo_impacto',Field('nombre','string',
# 	required='TRUE'))

# if db(db.Cat_tipo_impacto.id>0).count() == 0:
# 	db.Cat_tipo_impacto.insert(nombre='Incendios')
# 	db.Cat_tipo_impacto.insert(nombre='Huracanes')
# 	db.Cat_tipo_impacto.insert(nombre='Inundaciones')
# 	db.Cat_tipo_impacto.insert(nombre='Apertura de caminos')
# 	db.Cat_tipo_impacto.insert(nombre='Aprovechamientos forestales')
# 	db.Cat_tipo_impacto.insert(nombre='Uso del suelo diferente al forestal')
# 	db.Cat_tipo_impacto.insert(nombre='Pastoreo')
# 	db.Cat_tipo_impacto.insert(nombre='Plagas y enfermedades')
# 	db.Cat_tipo_impacto.insert(nombre='Líneas eléctricas')
# 	db.Cat_tipo_impacto.insert(nombre='Actividades mineras')
# 	db.Cat_tipo_impacto.insert(nombre='Asentamientos humanos')


db.define_table('Cat_severidad_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_severidad_impactos.id>0).count() == 0:
	db.Cat_severidad_impactos.insert(nombre='1 No perceptible')
	db.Cat_severidad_impactos.insert(nombre='2 Menor')
	db.Cat_severidad_impactos.insert(nombre='3 Mediana')
	db.Cat_severidad_impactos.insert(nombre='4 Mayor')


db.define_table('Cat_agente_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_agente_impactos.id>0).count() == 0:
	db.Cat_agente_impactos.insert(nombre='1 Barrenador')
	db.Cat_agente_impactos.insert(nombre='2 Defoliador')
	db.Cat_agente_impactos.insert(nombre='3 Descortezador')
	db.Cat_agente_impactos.insert(nombre='4 Muérdagos')


db.define_table('Cat_estatus_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_estatus_impactos.id>0).count() == 0:
	db.Cat_estatus_impactos.insert(nombre='1 Activa')
	db.Cat_estatus_impactos.insert(nombre='2 Inactiva')

db.define_table('Cat_prop_afectacion',Field('nombre','string',required='TRUE'))

if db(db.Cat_prop_afectacion.id>0).count() == 0:
	db.Cat_prop_afectacion.insert(nombre='Menor a 10%')
	db.Cat_prop_afectacion.insert(nombre='10 a 30%')
	db.Cat_prop_afectacion.insert(nombre='30 a 50%')
	db.Cat_prop_afectacion.insert(nombre='50 a 70%')
	db.Cat_prop_afectacion.insert(nombre='70 a 90%')
	db.Cat_prop_afectacion.insert(nombre='Más de 90%')


db.define_table('Cat_incendio',Field('nombre','string',required='TRUE'))

if db(db.Cat_incendio.id>0).count() == 0:
	db.Cat_incendio.insert(nombre='Subterráneo')
	db.Cat_incendio.insert(nombre='Superficial')
	db.Cat_incendio.insert(nombre='Aéreo copa')


#########################################################################
