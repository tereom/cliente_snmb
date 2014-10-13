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

##########################################################################
## Pestaña Conteo de aves
########################################################################

db.define_table('Cat_condiciones_ambientales',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_condiciones_ambientales.id>0).count() == 0:
	db.Cat_condiciones_ambientales.insert(nombre='condición 1')
	db.Cat_condiciones_ambientales.insert(nombre='condición 2')
	db.Cat_condiciones_ambientales.insert(nombre='condición 3')


#########################################################################
