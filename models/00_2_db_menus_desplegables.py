# coding: utf8

## En esta sección se definen las tablas de los menus desplegables 
## correspondientes a CONANP

##########################################################################
## Pestaña Carbono
########################################################################

db.define_table('Cat_numero_transecto_carbono',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_numero_transecto_carbono.id>0).count() == 0:
	db.Cat_numero_transecto_carbono.insert(nombre='Transecto norte')
	db.Cat_numero_transecto_carbono.insert(nombre='Transecto este')
	db.Cat_numero_transecto_carbono.insert(nombre='Transecto sur')
	db.Cat_numero_transecto_carbono.insert(nombre='Transecto oeste')


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
#########################################################################
