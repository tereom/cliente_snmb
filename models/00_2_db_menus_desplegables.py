# coding: utf8

## En esta sección se definen las tablas de los menus desplegables 
## correspondientes a CONANP



##########################################################################
## Pestaña Vegetación y suelos
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

#########################################################################

db.define_table('Cat_grado_carbono',Field('nombre','integer',
	required='TRUE'))

if db(db.Cat_grado_carbono.id>0).count() == 0:
	db.Cat_grado_carbono.insert(nombre=1)
	db.Cat_grado_carbono.insert(nombre=2)
	db.Cat_grado_carbono.insert(nombre=3)
	db.Cat_grado_carbono.insert(nombre=4)
	db.Cat_grado_carbono.insert(nombre=5)

#########################################################################

db.define_table('Cat_transecto_direccion',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_transecto_direccion.id>0).count() == 0:
	db.Cat_transecto_direccion.insert(nombre='Norte')
	db.Cat_transecto_direccion.insert(nombre='Este')
	db.Cat_transecto_direccion.insert(nombre='Sur')
	db.Cat_transecto_direccion.insert(nombre='Oeste')

#########################################################################

# Este catálogo es para árboles pequeños y arbustos
db.define_table('Cat_forma_vida',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_forma_vida.id>0).count() == 0:
	db.Cat_forma_vida.insert(nombre='Sin individuo')
	db.Cat_forma_vida.insert(nombre='Arbustiva')
	db.Cat_forma_vida.insert(nombre='Arbórea')

#########################################################################

# Este catálogo es para árboles grandes
db.define_table('Cat_forma_vida_arboles_grandes',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_forma_vida_arboles_grandes.id>0).count() == 0:
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Sin individuo')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Árbol')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Arbustiva')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Arborescente')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Cañas')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Cactáceas arborescentes')
	db.Cat_forma_vida_arboles_grandes.insert(nombre='Manglares')

db.define_table('Cat_cambios_arboles_grandes',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_cambios_arboles_grandes.id>0).count() == 0:
	db.Cat_cambios_arboles_grandes.insert(nombre='Árbol nuevo')
	db.Cat_cambios_arboles_grandes.insert(nombre='Árbol muerto nuevo')
	db.Cat_cambios_arboles_grandes.insert(nombre='Tocón nuevo')

##########################################################################
## Pestaña Impactos ambientales
########################################################################

db.define_table('Cat_tipo_impacto',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_tipo_impacto.id>0).count() == 0:
	db.Cat_tipo_impacto.insert(nombre='Incendios')
	db.Cat_tipo_impacto.insert(nombre='Huracanes')
	db.Cat_tipo_impacto.insert(nombre='Inundaciones')
	db.Cat_tipo_impacto.insert(nombre='Apertura de caminos')
	db.Cat_tipo_impacto.insert(nombre='Aprovechamientos forestales')
	db.Cat_tipo_impacto.insert(nombre='Uso del suelo diferente al forestal')
	db.Cat_tipo_impacto.insert(nombre='Pastoreo')
	db.Cat_tipo_impacto.insert(nombre='Plagas y enfermedades')
	db.Cat_tipo_impacto.insert(nombre='Líneas eléctricas')
	db.Cat_tipo_impacto.insert(nombre='Actividades mineras')
	db.Cat_tipo_impacto.insert(nombre='Asentamientos humanos')

#########################################################################

db.define_table('Cat_severidad_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_severidad_impactos.id>0).count() == 0:
	db.Cat_severidad_impactos.insert(nombre='1 No perceptible')
	db.Cat_severidad_impactos.insert(nombre='2 Menor')
	db.Cat_severidad_impactos.insert(nombre='3 Mediana')
	db.Cat_severidad_impactos.insert(nombre='4 Mayor')

#########################################################################

db.define_table('Cat_agente_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_agente_impactos.id>0).count() == 0:
	db.Cat_agente_impactos.insert(nombre='0 Sin plagas')
	db.Cat_agente_impactos.insert(nombre='1 Barrenador')
	db.Cat_agente_impactos.insert(nombre='2 Defoliador')
	db.Cat_agente_impactos.insert(nombre='3 Descortezador')
	db.Cat_agente_impactos.insert(nombre='4 Muérdagos')

#########################################################################

db.define_table('Cat_estatus_impactos',Field('nombre','string',
	required='TRUE'))

if db(db.Cat_estatus_impactos.id>0).count() == 0:
	db.Cat_estatus_impactos.insert(nombre='1 Activa')
	db.Cat_estatus_impactos.insert(nombre='2 Inactiva')

#########################################################################

db.define_table('Cat_prop_afectacion',Field('nombre','string',required='TRUE'))

if db(db.Cat_prop_afectacion.id>0).count() == 0:
	db.Cat_prop_afectacion.insert(nombre='Menor a 10%')
	db.Cat_prop_afectacion.insert(nombre='10 a 30%')
	db.Cat_prop_afectacion.insert(nombre='30 a 50%')
	db.Cat_prop_afectacion.insert(nombre='50 a 70%')
	db.Cat_prop_afectacion.insert(nombre='70 a 90%')
	db.Cat_prop_afectacion.insert(nombre='Más de 90%')

#########################################################################

db.define_table('Cat_incendio',Field('nombre','string',required='TRUE'))

if db(db.Cat_incendio.id>0).count() == 0:
	db.Cat_incendio.insert(nombre='Subterráneo')
	db.Cat_incendio.insert(nombre='Superficial')
	db.Cat_incendio.insert(nombre='Aéreo copa')

#########################################################################


##########################################################################
## Pestaña Aves
########################################################################
# Por la camtidad de registros, en esta pestaña se separan el nombre común del
# nombre científico
db.define_table('Cat_conabio_aves',
	Field('nombre_comun', 'string', required='TRUE'),
	Field('nombre_cientifico', 'string', required='TRUE'))

if db(db.Cat_conabio_aves.id>0).count() == 0:
	db.Cat_conabio_aves.insert(
		nombre_comun='Achichilique Pico Amarillo',
		nombre_cientifico='Aechmophorus occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Achichilique Pico Naranja',
		nombre_cientifico='Aechmophorus clarkii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Agachona Norteamericana',
		nombre_cientifico='Gallinago delicata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Albinegra',
		nombre_cientifico='Spizaetus melanoleucus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Arpía',
		nombre_cientifico='Harpia harpyja')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Cabeza Blanca',
		nombre_cientifico='Haliaeetus leucocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Crestada',
		nombre_cientifico='Morphnus guianensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Elegante',
		nombre_cientifico='Spizaetus ornatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Pescadora',
		nombre_cientifico='Pandion haliaetus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Real',
		nombre_cientifico='Aquila chrysaetos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Solitaria',
		nombre_cientifico='Buteogallus solitarius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Águila Tirana',
		nombre_cientifico='Spizaetus tyrannus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Alas Anchas',
		nombre_cientifico='Buteo platypterus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Ártica',
		nombre_cientifico='Buteo lagopus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Aura',
		nombre_cientifico='Buteo albonotatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Blanca',
		nombre_cientifico='Pseudastur albicollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Caminera',
		nombre_cientifico='Buteo magnirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Canela',
		nombre_cientifico='Busarellus nigricollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Cola Blanca',
		nombre_cientifico='Buteo albicaudatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Cola Corta',
		nombre_cientifico='Buteo brachyurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Cola Roja',
		nombre_cientifico='Buteo jamaicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla de Swainson',
		nombre_cientifico='Buteo swainsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Gris',
		nombre_cientifico='Buteo plagiatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Negra Mayor',
		nombre_cientifico='Buteogallus urubitinga')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Negra Menor',
		nombre_cientifico='Buteogallus anthracinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Pecho Rojo',
		nombre_cientifico='Buteo lineatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Real',
		nombre_cientifico='Buteo regalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Aguililla Rojinegra',
		nombre_cientifico='Parabuteo unicinctus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Albatros de Laysan',
		nombre_cientifico='Phoebastria immutabilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Albatros Patas Negras',
		nombre_cientifico='Phoebastria nigripes')
	db.Cat_conabio_aves.insert(
		nombre_comun='Albatros Rabón',
		nombre_cientifico='Phoebastria albatrus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alca Marmoleada',
		nombre_cientifico='Brachyramphus marmoratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alca Rinoceronte',
		nombre_cientifico='Cerorhinca monocerata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alcaraván Americano',
		nombre_cientifico='Burhinus bistriatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alondra Cornuda',
		nombre_cientifico='Eremophila alpestris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alquita Crestada',
		nombre_cientifico='Aethia cristatella')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alquita Oscura',
		nombre_cientifico='Ptychoramphus aleuticus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Alquita Perico',
		nombre_cientifico='Aethia psittacula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Anhinga Americana',
		nombre_cientifico='Anhinga anhinga')
	db.Cat_conabio_aves.insert(
		nombre_comun='Arao Común',
		nombre_cientifico='Uria aalge')
	db.Cat_conabio_aves.insert(
		nombre_comun='Arao Pichón',
		nombre_cientifico='Cepphus columba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Arrocero Americano',
		nombre_cientifico='Spiza americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ave Sol',
		nombre_cientifico='Eurypyga helias')
	db.Cat_conabio_aves.insert(
		nombre_comun='Avefría Tero',
		nombre_cientifico='Vanellus chilensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Avetoro Menor',
		nombre_cientifico='Ixobrychus exilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Avetoro Neotropical',
		nombre_cientifico='Botaurus pinnatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Avetoro Norteño',
		nombre_cientifico='Botaurus lentiginosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Avoceta Americana',
		nombre_cientifico='Recurvirostra americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Azulejo Garganta Azul',
		nombre_cientifico='Sialia mexicana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Azulejo Garganta Canela',
		nombre_cientifico='Sialia sialis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Azulejo Pálido',
		nombre_cientifico='Sialia currucoides')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bajapalos Enano',
		nombre_cientifico='Sitta pygmaea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bajapalos Pecho Blanco',
		nombre_cientifico='Sitta carolinensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bajapalos Pecho Canela',
		nombre_cientifico='Sitta canadensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Baloncillo',
		nombre_cientifico='Auriparus flaviceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Batará Barrado',
		nombre_cientifico='Thamnophilus doliatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Batará Canelo',
		nombre_cientifico='Thamnistes anabatinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Batará Mayor',
		nombre_cientifico='Taraba major')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bisbita de Oriente',
		nombre_cientifico='Anthus hodgsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bisbita Garganta Roja',
		nombre_cientifico='Anthus cervinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bisbita Llanera',
		nombre_cientifico='Anthus spragueii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bisbita Norteamericana',
		nombre_cientifico='Anthus rubescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo Café',
		nombre_cientifico='Sula leucogaster')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo de Nazca',
		nombre_cientifico='Sula granti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo Enmascarado',
		nombre_cientifico='Sula dactylatra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo Norteño',
		nombre_cientifico='Morus bassanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo Patas Azules',
		nombre_cientifico='Sula nebouxii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Bobo Patas Rojas',
		nombre_cientifico='Sula sula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Buco Barbón',
		nombre_cientifico='Malacoptila panamensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Buco de Collar',
		nombre_cientifico='Notharchus hyperrhynchus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Barrado',
		nombre_cientifico='Strix varia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Barrado Albinegro',
		nombre_cientifico='Ciccaba nigrolineata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Café',
		nombre_cientifico='Ciccaba virgata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Cara Blanca',
		nombre_cientifico='Pseudoscops clamator')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Cara Canela',
		nombre_cientifico='Asio otus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Cara Oscura',
		nombre_cientifico='Asio stygius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Cornudo',
		nombre_cientifico='Bubo virginianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Cuernos Blancos',
		nombre_cientifico='Lophostrix cristata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho de Anteojos',
		nombre_cientifico='Pulsatrix perspicillata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Leonado',
		nombre_cientifico='Strix fulvescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Moteado',
		nombre_cientifico='Strix occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Búho Sabanero',
		nombre_cientifico='Asio flammeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cabezón Alas Blancas',
		nombre_cientifico='Pachyramphus polychopterus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cabezón Canelo',
		nombre_cientifico='Pachyramphus cinnamomeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cabezón Degollado',
		nombre_cientifico='Pachyramphus aglaiae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cabezón Mexicano',
		nombre_cientifico='Pachyramphus major')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cacique Mexicano',
		nombre_cientifico='Cassiculus melanicterus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cacique Pico Claro',
		nombre_cientifico='Amblycercus holosericeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Caperuza Negra',
		nombre_cientifico='Icterus prosthemelas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Capucha Negra',
		nombre_cientifico='Icterus graduacauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Castaña',
		nombre_cientifico='Icterus spurius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Cejas Naranjas',
		nombre_cientifico='Icterus bullockii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Cola Amarilla',
		nombre_cientifico='Icterus mesomelas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria de Baltimore',
		nombre_cientifico='Icterus galbula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria de Wagler',
		nombre_cientifico='Icterus wagleri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Dorso Amarillo',
		nombre_cientifico='Icterus chrysater')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Dorso Naranja',
		nombre_cientifico='Icterus auratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Dorso Negro Mayor',
		nombre_cientifico='Icterus gularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Dorso Negro Menor',
		nombre_cientifico='Icterus cucullatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Dorso Rayado',
		nombre_cientifico='Icterus pustulatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Flancos Negros',
		nombre_cientifico='Icterus abeillei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Guatemalteca',
		nombre_cientifico='Icterus maculialatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Pecho Moteado',
		nombre_cientifico='Icterus pectoralis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Calandria Tunera',
		nombre_cientifico='Icterus parisorum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Camea',
		nombre_cientifico='Chamaea fasciata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Capuchino Pecho Escamoso',
		nombre_cientifico='Lonchura punctulata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Capuchino Tricolor',
		nombre_cientifico='Lonchura malacca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Capulinero Gris',
		nombre_cientifico='Ptiliogonys cinereus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Capulinero Negro',
		nombre_cientifico='Phainopepla nitens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Caracara Comecacao',
		nombre_cientifico='Ibycter americanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Caracara de Isla Guadalupe',
		nombre_cientifico='Caracara lutosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Caracara Quebrantahuesos',
		nombre_cientifico='Caracara cheriway')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero Cejas Blancas',
		nombre_cientifico='Poecile gambeli')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero Cresta Negra',
		nombre_cientifico='Baeolophus atricristatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero de Juníperos',
		nombre_cientifico='Baeolophus ridgwayi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero Embridado',
		nombre_cientifico='Baeolophus wollweberi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero Encinero',
		nombre_cientifico='Baeolophus inornatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carbonero Mexicano',
		nombre_cientifico='Poecile sclateri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cardenal Desértico',
		nombre_cientifico='Cardinalis sinuatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cardenal Rojo',
		nombre_cientifico='Cardinalis cardinalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Albinegro Mayor',
		nombre_cientifico='Picoides villosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Albinegro Menor',
		nombre_cientifico='Picoides pubescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Bellotero',
		nombre_cientifico='Melanerpes formicivorus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Café',
		nombre_cientifico='Picoides fumigatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Californiano',
		nombre_cientifico='Picoides nuttallii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Cara Negra',
		nombre_cientifico='Melanerpes pucherani')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Castaño',
		nombre_cientifico='Celeus castaneus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Cheje',
		nombre_cientifico='Melanerpes aurifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Corona Gris',
		nombre_cientifico='Colaptes auricularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero de Arizona',
		nombre_cientifico='Picoides arizonae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero de Lewis',
		nombre_cientifico='Melanerpes lewis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero de Pechera Común',
		nombre_cientifico='Colaptes auratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero de Pechera del Noroeste',
		nombre_cientifico='Colaptes chrysoides')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero del Balsas',
		nombre_cientifico='Melanerpes hypopolius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero del Desierto',
		nombre_cientifico='Melanerpes uropygialis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Elegante',
		nombre_cientifico='Sphyrapicus thyroideus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Enmascarado',
		nombre_cientifico='Melanerpes chrysogenys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Imperial',
		nombre_cientifico='Campephilus imperialis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Lineado',
		nombre_cientifico='Dryocopus lineatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Mexicano',
		nombre_cientifico='Picoides scalaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Moteado',
		nombre_cientifico='Sphyrapicus varius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Nuca Roja',
		nombre_cientifico='Sphyrapicus nuchalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Olivo',
		nombre_cientifico='Colaptes rubiginosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Pecho Rojo',
		nombre_cientifico='Sphyrapicus ruber')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Pico Plateado',
		nombre_cientifico='Campephilus guatemalensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Transvolcánico',
		nombre_cientifico='Picoides stricklandi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carpintero Yucateco',
		nombre_cientifico='Melanerpes pygmaeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Carrao',
		nombre_cientifico='Aramus guarauna')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cascanueces Americano',
		nombre_cientifico='Nucifraga columbiana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Centzontle de Isla Socorro',
		nombre_cientifico='Mimus graysoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Centzontle Norteño',
		nombre_cientifico='Mimus polyglottos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Centzontle Tropical',
		nombre_cientifico='Mimus gilvus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cerceta Alas Azules',
		nombre_cientifico='Anas discors')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cerceta Alas Verdes',
		nombre_cientifico='Anas crecca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cerceta Canela',
		nombre_cientifico='Anas cyanoptera')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cerceta Cejas Blancas',
		nombre_cientifico='Anas querquedula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cernícalo Americano',
		nombre_cientifico='Falco sparverius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chachalaca Oriental',
		nombre_cientifico='Ortalis vetula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chachalaca Pálida',
		nombre_cientifico='Ortalis poliocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chachalaca Vientre Blanco',
		nombre_cientifico='Ortalis leucogastra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chachalaca Vientre Castaño',
		nombre_cientifico='Ortalis wagleri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Copetona',
		nombre_cientifico='Cyanocitta stelleri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara de Collar',
		nombre_cientifico='Aphelocoma californica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara de Niebla',
		nombre_cientifico='Cyanolyca pumilo')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara de San Blas',
		nombre_cientifico='Cyanocorax sanblasianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Enana',
		nombre_cientifico='Cyanolyca nana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Garganta Blanca',
		nombre_cientifico='Cyanolyca mirabilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Gorro Azul',
		nombre_cientifico='Cyanolyca cucullata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Pea',
		nombre_cientifico='Psilorhinus morio')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Pecho Gris',
		nombre_cientifico='Aphelocoma wollweberi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Piñonera',
		nombre_cientifico='Gymnorhinus cyanocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Pinta',
		nombre_cientifico='Cyanocorax dickeyi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Sinaloense',
		nombre_cientifico='Cyanocorax beecheii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Transvolcánica',
		nombre_cientifico='Aphelocoma ultramarina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Unicolor',
		nombre_cientifico='Aphelocoma unicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Verde',
		nombre_cientifico='Cyanocorax yncas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chara Yucateca',
		nombre_cientifico='Cyanocorax yucatanicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Albinegro',
		nombre_cientifico='Onychoprion fuscatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Ártico',
		nombre_cientifico='Sterna paradisaea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Blanco',
		nombre_cientifico='Gygis alba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Café',
		nombre_cientifico='Anous stolidus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Común',
		nombre_cientifico='Sterna hirundo')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Corona Blanca',
		nombre_cientifico='Anous minutus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán de Forster',
		nombre_cientifico='Sterna forsteri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán de Sandwich',
		nombre_cientifico='Thalasseus sandvicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán del Caspio',
		nombre_cientifico='Hydroprogne caspia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Elegante',
		nombre_cientifico='Thalasseus elegans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Embridado',
		nombre_cientifico='Onychoprion anaethetus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Mínimo',
		nombre_cientifico='Sternula antillarum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Negro',
		nombre_cientifico='Chlidonias niger')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Pico Grueso',
		nombre_cientifico='Gelochelidon nilotica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Real',
		nombre_cientifico='Thalasseus maximus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Charrán Rosado',
		nombre_cientifico='Sterna dougallii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chinchinero Común',
		nombre_cientifico='Chlorospingus flavopectus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chinito',
		nombre_cientifico='Bombycilla cedrorum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Alas Amarillas',
		nombre_cientifico='Vermivora chrysoptera')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Alas Azules',
		nombre_cientifico='Vermivora cyanoptera')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Amarillo',
		nombre_cientifico='Setophaga petechia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Arroyero',
		nombre_cientifico='Parkesia motacilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Atigrado',
		nombre_cientifico='Setophaga tigrina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Azulnegro',
		nombre_cientifico='Setophaga caerulescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cabeza Amarilla',
		nombre_cientifico='Setophaga occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cabeza Gris',
		nombre_cientifico='Oreothlypis ruficapilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cabeza Negra',
		nombre_cientifico='Setophaga striata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cachetes Amarillos',
		nombre_cientifico='Setophaga chrysoparia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cara Roja',
		nombre_cientifico='Cardellina rubrifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Castaño',
		nombre_cientifico='Setophaga castanea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cejas Amarillas',
		nombre_cientifico='Setophaga graciae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cejas Blancas',
		nombre_cientifico='Oreothlypis superciliosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cejas Doradas',
		nombre_cientifico='Basileuterus belli')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Cejas Negras',
		nombre_cientifico='Basileuterus culicivorus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Celeste',
		nombre_cientifico='Setophaga cerulea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Charquero',
		nombre_cientifico='Parkesia noveboracensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Corona Café',
		nombre_cientifico='Limnothlypis swainsonii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Corona Negra',
		nombre_cientifico='Cardellina pusilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Colima',
		nombre_cientifico='Oreothlypis crissalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Collar',
		nombre_cientifico='Cardellina canadensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Connecticut',
		nombre_cientifico='Oporornis agilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Magnolias',
		nombre_cientifico='Setophaga magnolia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Pechera',
		nombre_cientifico='Geothlypis philadelphia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Pradera',
		nombre_cientifico='Setophaga discolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Townsend',
		nombre_cientifico='Setophaga townsendi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe de Virginia',
		nombre_cientifico='Oreothlypis virginiae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Dorado',
		nombre_cientifico='Protonotaria citrea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Dorso Verde',
		nombre_cientifico='Setophaga virens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Encapuchado',
		nombre_cientifico='Setophaga citrina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Flancos Castaños',
		nombre_cientifico='Setophaga pensylvanica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Garganta Amarilla',
		nombre_cientifico='Setophaga dominica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Garganta Naranja',
		nombre_cientifico='Setophaga fusca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Gorra Canela',
		nombre_cientifico='Basileuterus rufifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Grande',
		nombre_cientifico='Icteria virens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Gusanero',
		nombre_cientifico='Helmitheros vermivorum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Lores Negros',
		nombre_cientifico='Geothlypis tolmiei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Negrogris',
		nombre_cientifico='Setophaga nigrescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Oliváceo',
		nombre_cientifico='Oreothlypis celata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Patilludo',
		nombre_cientifico='Geothlypis formosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Pecho Manchado',
		nombre_cientifico='Setophaga americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Peregrino',
		nombre_cientifico='Oreothlypis peregrina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Pinero',
		nombre_cientifico='Setophaga pinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Playero',
		nombre_cientifico='Setophaga palmarum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Rabadilla Amarilla',
		nombre_cientifico='Setophaga coronata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Rabadilla Castaña',
		nombre_cientifico='Oreothlypis luciae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Rojo',
		nombre_cientifico='Cardellina rubra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Rosado',
		nombre_cientifico='Cardellina versicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Suelero',
		nombre_cientifico='Seiurus aurocapilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Trepador',
		nombre_cientifico='Mniotilta varia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chipe Tropical',
		nombre_cientifico='Setophaga pitiayumi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chocha del Este',
		nombre_cientifico='Scolopax minor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Carambolo',
		nombre_cientifico='Charadrius morinellus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Chiflador',
		nombre_cientifico='Charadrius melodus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo de Collar',
		nombre_cientifico='Charadrius collaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Dorado Americano',
		nombre_cientifico='Pluvialis dominica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Dorado del Pacífico',
		nombre_cientifico='Pluvialis fulva')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Gris',
		nombre_cientifico='Pluvialis squatarola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Llanero',
		nombre_cientifico='Charadrius montanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Nevado',
		nombre_cientifico='Charadrius nivosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Pico Grueso',
		nombre_cientifico='Charadrius wilsonia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Semipalmeado',
		nombre_cientifico='Charadrius semipalmatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chorlo Tildío',
		nombre_cientifico='Charadrius vociferus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chotacabras Cola Corta',
		nombre_cientifico='Lurocalis semitorquatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chotacabras Menor',
		nombre_cientifico='Chordeiles acutipennis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chotacabras Pauraque',
		nombre_cientifico='Nyctidromus albicollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Chotacabras Zumbón',
		nombre_cientifico='Chordeiles minor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cigüeña Americana',
		nombre_cientifico='Mycteria americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cigüeña Jabirú',
		nombre_cientifico='Jabiru mycteria')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cisne de Tundra',
		nombre_cientifico='Cygnus columbianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cisne Trompetero',
		nombre_cientifico='Cygnus buccinator')
	db.Cat_conabio_aves.insert(
		nombre_comun='Clarín Jilguero',
		nombre_cientifico='Myadestes occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Clarín Norteño',
		nombre_cientifico='Myadestes townsendi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Clarín Unicolor',
		nombre_cientifico='Myadestes unicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Clorofonia Corona Azul',
		nombre_cientifico='Chlorophonia occipitalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Cabeza Negra',
		nombre_cientifico='Trogon melanocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Citrina',
		nombre_cientifico='Trogon citreolus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Cola Oscura',
		nombre_cientifico='Trogon massena')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa de Collar',
		nombre_cientifico='Trogon collaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Elegante',
		nombre_cientifico='Trogon elegans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Mexicana',
		nombre_cientifico='Trogon mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coa Violácea Norteña',
		nombre_cientifico='Trogon caligatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Barrada',
		nombre_cientifico='Philortyx fasciatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Bolonchaco',
		nombre_cientifico='Odontophorus guttatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Californiana',
		nombre_cientifico='Callipepla californica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Coluda Centroamericana',
		nombre_cientifico='Dendrortyx leucophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Coluda Transvolcánica',
		nombre_cientifico='Dendrortyx macroura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Coluda Veracruzana',
		nombre_cientifico='Dendrortyx barbatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Cotuí',
		nombre_cientifico='Colinus virginianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Cresta Dorada',
		nombre_cientifico='Callipepla douglasii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz de Gambel',
		nombre_cientifico='Callipepla gambelii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz de Moctezuma',
		nombre_cientifico='Cyrtonyx montezumae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz de Montaña',
		nombre_cientifico='Oreortyx pictus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Escamosa',
		nombre_cientifico='Callipepla squamata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Ocelada',
		nombre_cientifico='Cyrtonyx ocellatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Silbadora',
		nombre_cientifico='Dactylortyx thoracicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Codorniz Yucateca',
		nombre_cientifico='Colinus nigrogularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Barba Negra',
		nombre_cientifico='Archilochus alexandri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Berilo',
		nombre_cientifico='Amazilia beryllina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cabeza Roja',
		nombre_cientifico='Calypte anna')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cabeza Violeta',
		nombre_cientifico='Calypte costae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cándido',
		nombre_cientifico='Amazilia candida')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Canelo',
		nombre_cientifico='Amazilia rutila')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Capucha Azul',
		nombre_cientifico='Florisuga mellivora')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cola Azul',
		nombre_cientifico='Amazilia cyanura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cola Canela',
		nombre_cientifico='Amazilia tzacatl')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cola Pinta',
		nombre_cientifico='Tilmatura dupontii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Cola Rayada',
		nombre_cientifico='Eupherusa eximia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Corona Azul',
		nombre_cientifico='Amazilia cyanocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Corona Violeta',
		nombre_cientifico='Amazilia violiceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Ermitaño Enano',
		nombre_cientifico='Phaethornis striigularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Ermitaño Mesoamericano',
		nombre_cientifico='Phaethornis longirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Frente Verde',
		nombre_cientifico='Amazilia viridifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Garganta Amatista',
		nombre_cientifico='Lampornis amethystinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Garganta Azul',
		nombre_cientifico='Lampornis clemenciae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Garganta Negra',
		nombre_cientifico='Anthracothorax prevostii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Garganta Rubí',
		nombre_cientifico='Archilochus colubris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Garganta Verde',
		nombre_cientifico='Lampornis viridipallens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Guerrerense',
		nombre_cientifico='Eupherusa poliocerca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Hada Enmascarada',
		nombre_cientifico='Heliothryx barroti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Lucifer',
		nombre_cientifico='Calothorax lucifer')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Magnífico',
		nombre_cientifico='Eugenes fulgens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Miahuatleco',
		nombre_cientifico='Eupherusa cyanophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Mixteco',
		nombre_cientifico='Calothorax pulcher')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Multicolor',
		nombre_cientifico='Lamprolaima rhami')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Opaco',
		nombre_cientifico='Cynanthus sordidus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Orejas Violetas',
		nombre_cientifico='Colibri thalassinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Pecho Escamoso',
		nombre_cientifico='Phaeochroa cuvierii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Pico Ancho',
		nombre_cientifico='Cynanthus latirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Pico Corto',
		nombre_cientifico='Abeillia abeillei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Picudo Coroniazul',
		nombre_cientifico='Heliomaster longirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Picudo Occidental',
		nombre_cientifico='Heliomaster constantii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Tijereta Guatemalteco',
		nombre_cientifico='Doricha enicura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Tijereta Mexicano',
		nombre_cientifico='Doricha eliza')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colibrí Vientre Canelo',
		nombre_cientifico='Amazilia yucatanensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colimbo Ártico',
		nombre_cientifico='Gavia arctica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colimbo Común',
		nombre_cientifico='Gavia immer')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colimbo del Pacífico',
		nombre_cientifico='Gavia pacifica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colimbo Menor',
		nombre_cientifico='Gavia stellata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colimbo Pico Amarillo',
		nombre_cientifico='Gavia adamsii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Collalba Norteña',
		nombre_cientifico='Oenanthe oenanthe')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Azul',
		nombre_cientifico='Passerina cyanea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Azulnegro',
		nombre_cientifico='Cyanocompsa parellina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Azulrosa',
		nombre_cientifico='Passerina rositae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Morado',
		nombre_cientifico='Passerina versicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Pecho Canela',
		nombre_cientifico='Passerina amoena')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Pecho Naranja',
		nombre_cientifico='Passerina leclancherii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Colorín Sietecolores',
		nombre_cientifico='Passerina ciris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cóndor Californiano',
		nombre_cientifico='Gymnogyps californianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coqueta Cresta Negra',
		nombre_cientifico='Lophornis helenae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Coqueta de Atoyac',
		nombre_cientifico='Lophornis brachylophus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cormorán de Brandt',
		nombre_cientifico='Phalacrocorax penicillatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cormorán Neotropical',
		nombre_cientifico='Phalacrocorax brasilianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cormorán Orejón',
		nombre_cientifico='Phalacrocorax auritus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cormorán Pelágico',
		nombre_cientifico='Phalacrocorax pelagicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Correcaminos Norteño',
		nombre_cientifico='Geococcyx californianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Correcaminos Tropical',
		nombre_cientifico='Geococcyx velox')
	db.Cat_conabio_aves.insert(
		nombre_comun='Costurero Pico Corto',
		nombre_cientifico='Limnodromus griseus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Costurero Pico Largo',
		nombre_cientifico='Limnodromus scolopaceus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cotinga Azuleja',
		nombre_cientifico='Cotinga amabilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cotorra Serrana Occidental',
		nombre_cientifico='Rhynchopsitta pachyrhyncha')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cotorra Serrana Oriental',
		nombre_cientifico='Rhynchopsitta terrisi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Canelo',
		nombre_cientifico='Piaya cayana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Faisán',
		nombre_cientifico='Dromococcyx phasianellus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Manglero',
		nombre_cientifico='Coccyzus minor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Pico Amarillo',
		nombre_cientifico='Coccyzus americanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Pico Negro',
		nombre_cientifico='Coccyzus erythropthalmus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Rayado',
		nombre_cientifico='Tapera naevia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuclillo Terrestre',
		nombre_cientifico='Morococcyx erythropygus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuervo Común',
		nombre_cientifico='Corvus corax')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuervo Llanero',
		nombre_cientifico='Corvus cryptoleucus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuervo Norteamericano',
		nombre_cientifico='Corvus brachyrhynchos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuervo Sinaloense',
		nombre_cientifico='Corvus sinaloae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuervo Tamaulipeco',
		nombre_cientifico='Corvus imparatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuevero de Nava',
		nombre_cientifico='Hylorchilus navai')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuevero de Sumichrast',
		nombre_cientifico='Hylorchilus sumichrasti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Bajacaliforniano',
		nombre_cientifico='Toxostoma cinereum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Californiano',
		nombre_cientifico='Toxostoma redivivum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Castaño',
		nombre_cientifico='Toxostoma rufum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Chato',
		nombre_cientifico='Oreoscoptes montanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Crisal',
		nombre_cientifico='Toxostoma crissale')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche de Cozumel',
		nombre_cientifico='Toxostoma guttatum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Moteado',
		nombre_cientifico='Toxostoma ocellatum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Pálido',
		nombre_cientifico='Toxostoma lecontei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Pico Corto',
		nombre_cientifico='Toxostoma bendirei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Pico Curvo',
		nombre_cientifico='Toxostoma curvirostre')
	db.Cat_conabio_aves.insert(
		nombre_comun='Cuicacoche Pico Largo',
		nombre_cientifico='Toxostoma longirostre')
	db.Cat_conabio_aves.insert(
		nombre_comun='Escribano Ártico',
		nombre_cientifico='Calcarius lapponicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Escribano Collar Castaño',
		nombre_cientifico='Calcarius ornatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Escribano de McCown',
		nombre_cientifico='Rhynchophanes mccownii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Escribano Pigmeo',
		nombre_cientifico='Emberiza pusilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Esmeralda de Cozumel',
		nombre_cientifico='Chlorostilbon forficatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Esmeralda Occidental',
		nombre_cientifico='Chlorostilbon auriceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Esmeralda Oriental',
		nombre_cientifico='Chlorostilbon canivetii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Espátula Rosada',
		nombre_cientifico='Platalea ajaja')
	db.Cat_conabio_aves.insert(
		nombre_comun='Estornino Pinto',
		nombre_cientifico='Sturnus vulgaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Eufonia Garganta Amarilla',
		nombre_cientifico='Euphonia hirundinacea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Eufonia Garganta Negra',
		nombre_cientifico='Euphonia affinis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Eufonia Gorra Azul',
		nombre_cientifico='Euphonia elegantissima')
	db.Cat_conabio_aves.insert(
		nombre_comun='Eufonia Olivácea',
		nombre_cientifico='Euphonia gouldi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Eufonia Vientre Blanco',
		nombre_cientifico='Euphonia minuta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Faisán de Collar',
		nombre_cientifico='Phasianus colchicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Falaropo Cuello Rojo',
		nombre_cientifico='Phalaropus lobatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Falaropo Pico Grueso',
		nombre_cientifico='Phalaropus fulicarius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Falaropo Pico Largo',
		nombre_cientifico='Phalaropus tricolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fandanguero Canelo',
		nombre_cientifico='Campylopterus rufus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fandanguero Mexicano',
		nombre_cientifico='Campylopterus curvipennis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fandanguero Morado',
		nombre_cientifico='Campylopterus hemileucurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fandanguero Tuxtleño',
		nombre_cientifico='Campylopterus excellens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Flamenco Americano',
		nombre_cientifico='Phoenicopterus ruber')
	db.Cat_conabio_aves.insert(
		nombre_comun='Flautín Cabezón Mesoamericano',
		nombre_cientifico='Schiffornis veraepacis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fragata Pelágica',
		nombre_cientifico='Fregata minor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fragata Tijereta',
		nombre_cientifico='Fregata magnificens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Fulmar Norteño',
		nombre_cientifico='Fulmarus glacialis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gallareta Americana',
		nombre_cientifico='Fulica americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gallineta Frente Roja',
		nombre_cientifico='Gallinula galeata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gallineta Morada',
		nombre_cientifico='Porphyrio martinicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso Blanco',
		nombre_cientifico='Chen caerulescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso Canadiense Mayor',
		nombre_cientifico='Branta canadensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso Canadiense Menor',
		nombre_cientifico='Branta hutchinsii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso Careto Mayor',
		nombre_cientifico='Anser albifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso de Collar',
		nombre_cientifico='Branta bernicla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ganso de Ross',
		nombre_cientifico='Chen rossii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garcita Verde',
		nombre_cientifico='Butorides virescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garrapatero Pico Liso',
		nombre_cientifico='Crotophaga ani')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garrapatero Pijuy',
		nombre_cientifico='Crotophaga sulcirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Agami',
		nombre_cientifico='Agamia agami')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Azul',
		nombre_cientifico='Egretta caerulea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Blanca',
		nombre_cientifico='Ardea alba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Cucharón',
		nombre_cientifico='Cochlearius cochlearius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Dedos Dorados',
		nombre_cientifico='Egretta thula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Ganadera',
		nombre_cientifico='Bubulcus ibis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Morena',
		nombre_cientifico='Ardea herodias')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Nocturna Corona Clara',
		nombre_cientifico='Nyctanassa violacea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Nocturna Corona Negra',
		nombre_cientifico='Nycticorax nycticorax')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Rojiza',
		nombre_cientifico='Egretta rufescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Tigre Mexicana',
		nombre_cientifico='Tigrisoma mexicanum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Garza Tricolor',
		nombre_cientifico='Egretta tricolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Azor',
		nombre_cientifico='Accipiter gentilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Bicolor',
		nombre_cientifico='Accipiter bicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Bidentado',
		nombre_cientifico='Harpagus bidentatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Cabeza Gris',
		nombre_cientifico='Leptodon cayanensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Caracolero',
		nombre_cientifico='Rostrhamus sociabilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán de Cooper',
		nombre_cientifico='Accipiter cooperii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Pecho Canela',
		nombre_cientifico='Accipiter striatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Pico de Gancho',
		nombre_cientifico='Chondrohierax uncinatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Rastrero',
		nombre_cientifico='Circus cyaneus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gavilán Zancón',
		nombre_cientifico='Geranospiza caerulescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Alas Blancas',
		nombre_cientifico='Larus glaucescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Bajacaliforniana',
		nombre_cientifico='Larus livens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Blanca',
		nombre_cientifico='Larus hyperboreus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Californiana',
		nombre_cientifico='Larus californicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Cana',
		nombre_cientifico='Larus canus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Cola Hendida',
		nombre_cientifico='Xema sabini')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Cola Negra',
		nombre_cientifico='Larus crassirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota de Bonaparte',
		nombre_cientifico='Chroicocephalus philadelphia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota de Franklin',
		nombre_cientifico='Leucophaeus pipixcan')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota de Thayer',
		nombre_cientifico='Larus thayeri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Encapuchada',
		nombre_cientifico='Chroicocephalus ridibundus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Gris',
		nombre_cientifico='Leucophaeus modestus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Mayor',
		nombre_cientifico='Larus marinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Menor',
		nombre_cientifico='Hydrocoloeus minutus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Meridional',
		nombre_cientifico='Larus dominicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Occidental',
		nombre_cientifico='Larus occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Patas Negras',
		nombre_cientifico='Rissa tridactyla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Pico Anillado',
		nombre_cientifico='Larus delawarensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Plateada',
		nombre_cientifico='Larus argentatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Plomiza',
		nombre_cientifico='Larus heermanni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Reidora',
		nombre_cientifico='Leucophaeus atricilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gaviota Sombría',
		nombre_cientifico='Larus fuscus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Alas Aserradas',
		nombre_cientifico='Stelgidopteryx serripennis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Albiazul',
		nombre_cientifico='Pygochelidon cyanoleuca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Azulnegra',
		nombre_cientifico='Progne subis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Bicolor',
		nombre_cientifico='Tachycineta bicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Gorra Negra',
		nombre_cientifico='Notiochelidon pileata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Manglera',
		nombre_cientifico='Tachycineta albilinea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Pecho Gris',
		nombre_cientifico='Progne chalybea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Pueblera',
		nombre_cientifico='Petrochelidon fulva')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Ribereña',
		nombre_cientifico='Riparia riparia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Risquera',
		nombre_cientifico='Petrochelidon pyrrhonota')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Sinaloense',
		nombre_cientifico='Progne sinaloae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Tijereta',
		nombre_cientifico='Hirundo rustica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Golondrina Verdemar',
		nombre_cientifico='Tachycineta thalassina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Alas Blancas',
		nombre_cientifico='Calamospiza melanocorys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Arlequín',
		nombre_cientifico='Chondestes grammacus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Barba Negra',
		nombre_cientifico='Spizella atrogularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Canario Sabanero',
		nombre_cientifico='Sicalis luteola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Cantor',
		nombre_cientifico='Melospiza melodia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Cejas Blancas',
		nombre_cientifico='Spizella passerina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Chapulín',
		nombre_cientifico='Ammodramus savannarum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Chingolo',
		nombre_cientifico='Zonotrichia capensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Cola Blanca',
		nombre_cientifico='Pooecetes gramineus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Corona Amarilla',
		nombre_cientifico='Zonotrichia atricapilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Corona Blanca',
		nombre_cientifico='Zonotrichia leucophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Costero',
		nombre_cientifico='Ammodramus maritimus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Baird',
		nombre_cientifico='Ammodramus bairdii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Brewer',
		nombre_cientifico='Spizella breweri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Harris',
		nombre_cientifico='Zonotrichia querula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Le Conte',
		nombre_cientifico='Ammodramus leconteii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Lincoln',
		nombre_cientifico='Melospiza lincolnii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Nelson',
		nombre_cientifico='Ammodramus nelsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión de Worthen',
		nombre_cientifico='Spizella wortheni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Doméstico',
		nombre_cientifico='Passer domesticus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Garganta Blanca',
		nombre_cientifico='Zonotrichia albicollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Llanero',
		nombre_cientifico='Spizella pusilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Pálido',
		nombre_cientifico='Spizella pallida')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Pantanero',
		nombre_cientifico='Melospiza georgiana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Rascador',
		nombre_cientifico='Passerella iliaca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Sabanero',
		nombre_cientifico='Passerculus sandwichensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Gorrión Serrano',
		nombre_cientifico='Xenospiza baileyi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Granatelo Mexicano',
		nombre_cientifico='Granatellus venustus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Granatelo Yucateco',
		nombre_cientifico='Granatellus sallaei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Grulla Blanca',
		nombre_cientifico='Grus americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Grulla Gris',
		nombre_cientifico='Grus canadensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Guacamaya Roja',
		nombre_cientifico='Ara macao')
	db.Cat_conabio_aves.insert(
		nombre_comun='Guacamaya Verde',
		nombre_cientifico='Ara militaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Guajolote Norteño',
		nombre_cientifico='Meleagris gallopavo')
	db.Cat_conabio_aves.insert(
		nombre_comun='Guajolote Ocelado',
		nombre_cientifico='Meleagris ocellata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Esmerejón',
		nombre_cientifico='Falco columbarius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Fajado',
		nombre_cientifico='Falco femoralis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Guaco',
		nombre_cientifico='Herpetotheres cachinnans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Mexicano',
		nombre_cientifico='Falco mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Murcielaguero',
		nombre_cientifico='Falco rufigularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Pecho Canela',
		nombre_cientifico='Falco deiroleucus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Peregrino',
		nombre_cientifico='Falco peregrinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Selvático Barrado',
		nombre_cientifico='Micrastur ruficollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Halcón Selvático de Collar',
		nombre_cientifico='Micrastur semitorquatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hocofaisán',
		nombre_cientifico='Crax rubra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hojarasquero Oscuro',
		nombre_cientifico='Sclerurus guatemalensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hojarasquero Pecho Canela',
		nombre_cientifico='Sclerurus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Alas Punteadas',
		nombre_cientifico='Microrhopias quixensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Cantor',
		nombre_cientifico='Cercomacra tyrannina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Cholino Cara Negra',
		nombre_cientifico='Formicarius analis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Cholino Escamoso',
		nombre_cientifico='Grallaria guatimalensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Pepito',
		nombre_cientifico='Synallaxis erythrothorax')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Plomizo',
		nombre_cientifico='Myrmotherula schisticolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Hormiguero Sencillo',
		nombre_cientifico='Dysithamnus mentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Huilota Caribeña',
		nombre_cientifico='Zenaida aurita')
	db.Cat_conabio_aves.insert(
		nombre_comun='Huilota Común',
		nombre_cientifico='Zenaida macroura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Huilota de Socorro',
		nombre_cientifico='Zenaida graysoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ibis Blanco',
		nombre_cientifico='Eudocimus albus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ibis Cara Oscura',
		nombre_cientifico='Plegadis falcinellus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ibis Ojos Rojos',
		nombre_cientifico='Plegadis chihi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jacamar Cola Canela',
		nombre_cientifico='Galbula ruficauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jacana Norteña',
		nombre_cientifico='Jacana spinosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Canario',
		nombre_cientifico='Spinus tristis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Cara Negra',
		nombre_cientifico='Spinus lawrencei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Corona Negra',
		nombre_cientifico='Spinus atriceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Dominico',
		nombre_cientifico='Spinus psaltria')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Encapuchado',
		nombre_cientifico='Spinus notatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Jilguerito Pinero',
		nombre_cientifico='Spinus pinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Junco de Isla Guadalupe',
		nombre_cientifico='Junco insularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Junco Ojos de Lumbre',
		nombre_cientifico='Junco phaeonotus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Junco Ojos Negros',
		nombre_cientifico='Junco hyemalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Lavandera Amarilla',
		nombre_cientifico='Motacilla tschutschensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Lavandera Blanca',
		nombre_cientifico='Motacilla alba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Lechuza de Campanario',
		nombre_cientifico='Tyto alba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Llorón Fioié',
		nombre_cientifico='Laniocera rufescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Cabeza Amarilla',
		nombre_cientifico='Amazona oratrix')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Cabeza Oscura',
		nombre_cientifico='Pyrilia haematotis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Cachetes Amarillos',
		nombre_cientifico='Amazona autumnalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Corona Azul',
		nombre_cientifico='Amazona farinosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Corona Blanca',
		nombre_cientifico='Pionus senilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Corona Lila',
		nombre_cientifico='Amazona finschi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Frente Blanca',
		nombre_cientifico='Amazona albifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Nuca Amarilla',
		nombre_cientifico='Amazona auropalliata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Tamaulipeco',
		nombre_cientifico='Amazona viridigenalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Loro Yucateco',
		nombre_cientifico='Amazona xantholora')
	db.Cat_conabio_aves.insert(
		nombre_comun='Luis Bienteveo',
		nombre_cientifico='Pitangus sulphuratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Luis Pico Grueso',
		nombre_cientifico='Megarynchus pitangua')
	db.Cat_conabio_aves.insert(
		nombre_comun='Luisito Común',
		nombre_cientifico='Myiozetetes similis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Martín Pescador Amazónico',
		nombre_cientifico='Chloroceryle amazona')
	db.Cat_conabio_aves.insert(
		nombre_comun='Martín Pescador de Collar',
		nombre_cientifico='Megaceryle torquata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Martín Pescador Enano',
		nombre_cientifico='Chloroceryle aenea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Martín Pescador Norteño',
		nombre_cientifico='Megaceryle alcyon')
	db.Cat_conabio_aves.insert(
		nombre_comun='Martín Pescador Verde',
		nombre_cientifico='Chloroceryle americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita Bajacaliforniana',
		nombre_cientifico='Geothlypis beldingi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita Común',
		nombre_cientifico='Geothlypis trichas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita de Altamira',
		nombre_cientifico='Geothlypis flavovelata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita del Lerma',
		nombre_cientifico='Geothlypis speciosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita Matorralera',
		nombre_cientifico='Geothlypis nelsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mascarita Pico Grueso',
		nombre_cientifico='Geothlypis poliocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Barrada',
		nombre_cientifico='Campylorhynchus megalopterus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Chiapaneca',
		nombre_cientifico='Campylorhynchus chiapensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca del Balsas',
		nombre_cientifico='Campylorhynchus jocosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca del Desierto',
		nombre_cientifico='Campylorhynchus brunneicapillus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Nuca Canela',
		nombre_cientifico='Campylorhynchus rufinucha')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Serrana',
		nombre_cientifico='Campylorhynchus gularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Tropical',
		nombre_cientifico='Campylorhynchus zonatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Matraca Yucateca',
		nombre_cientifico='Campylorhynchus yucatanicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Maullador Gris',
		nombre_cientifico='Dumetella carolinensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Maullador Negro',
		nombre_cientifico='Melanoptila glabrirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mergo Copetón',
		nombre_cientifico='Mergus serrator')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mergo Cresta Blanca',
		nombre_cientifico='Lophodytes cucullatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mergo Mayor',
		nombre_cientifico='Mergus merganser')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mérgulo Antiguo',
		nombre_cientifico='Synthliboramphus antiquus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mérgulo de Craveri',
		nombre_cientifico='Synthliboramphus craveri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mérgulo de Scripps',
		nombre_cientifico='Synthliboramphus scrippsi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mérgulo de Xantus',
		nombre_cientifico='Synthliboramphus hypoleucus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mielero Patas Amarillas',
		nombre_cientifico='Cyanerpes lucidus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mielero Patas Rojas',
		nombre_cientifico='Cyanerpes cyaneus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mielero Verde',
		nombre_cientifico='Chlorophanes spiza')
	db.Cat_conabio_aves.insert(
		nombre_comun='Milano Cola Blanca',
		nombre_cientifico='Elanus leucurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Milano de Mississippi',
		nombre_cientifico='Ictinia mississippiensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Milano Plomizo',
		nombre_cientifico='Ictinia plumbea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Milano Tijereta',
		nombre_cientifico='Elanoides forficatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Acuático Norteamericano',
		nombre_cientifico='Cinclus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Azteca',
		nombre_cientifico='Ridgwayia pinicola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Café',
		nombre_cientifico='Turdus grayi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Cinchado',
		nombre_cientifico='Ixoreus naevius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Cuello Canela',
		nombre_cientifico='Turdus rufitorques')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Dorso Canela',
		nombre_cientifico='Turdus rufopalliatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Garganta Blanca',
		nombre_cientifico='Turdus assimilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Negro',
		nombre_cientifico='Turdus infuscatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Primavera',
		nombre_cientifico='Turdus migratorius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mirlo Serrano',
		nombre_cientifico='Turdus plebejus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Cejas Azules',
		nombre_cientifico='Eumomota superciliosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Corona Azul',
		nombre_cientifico='Momotus momota')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Corona Canela',
		nombre_cientifico='Momotus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Enano',
		nombre_cientifico='Hylomanes momotula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Garganta Azul',
		nombre_cientifico='Aspatha gularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Momoto Pico Quillado',
		nombre_cientifico='Electron carinatum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Monjita Americana',
		nombre_cientifico='Himantopus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Cejas Blancas',
		nombre_cientifico='Zimmerius vilissimus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Chillón',
		nombre_cientifico='Camptostoma imberbe')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Cola Castaña',
		nombre_cientifico='Terenotriccus erythrurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Enano',
		nombre_cientifico='Ornithion semiflavum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Espatulilla Común',
		nombre_cientifico='Todirostrum cinereum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Espatulilla Gris',
		nombre_cientifico='Poecilotriccus sylvia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Fajado',
		nombre_cientifico='Xenotriccus callizonus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Gorra Café',
		nombre_cientifico='Leptopogon amaurocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Ocre',
		nombre_cientifico='Mionectes oleagineus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Ojos Blancos',
		nombre_cientifico='Tolmomyias sulphurescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Pico Chato',
		nombre_cientifico='Platyrinchus cancrominus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Pico Curvo',
		nombre_cientifico='Oncostoma cinereigulare')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Pico Plano',
		nombre_cientifico='Rhynchocyclus brevirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Rabadilla Amarilla',
		nombre_cientifico='Myiobius sulphureipygius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquerito Verdoso',
		nombre_cientifico='Myiopagis viridicata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero Atila',
		nombre_cientifico='Attila spadiceus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero Canelo',
		nombre_cientifico='Rhytipterna holerythra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero del Balsas',
		nombre_cientifico='Xenotriccus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero Elenia Caribeño',
		nombre_cientifico='Elaenia martinica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero Elenia Copetón',
		nombre_cientifico='Elaenia flavogaster')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquero Real',
		nombre_cientifico='Onychorhynchus coronatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquitero Ártico',
		nombre_cientifico='Phylloscopus borealis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquitero Cejas Amarillas',
		nombre_cientifico='Phylloscopus inornatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mosquitero Sombrío',
		nombre_cientifico='Phylloscopus fuscatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mulato Azul',
		nombre_cientifico='Melanotis caerulescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Mulato Pecho Blanco',
		nombre_cientifico='Melanotis hypoleucus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Musguero Castaño',
		nombre_cientifico='Clibanornis rubiginosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Musguero Garganta Pálida',
		nombre_cientifico='Automolus ochrolaemus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Musguero Trepador',
		nombre_cientifico='Anabacerthia variegaticeps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Negreta Alas Blancas',
		nombre_cientifico='Melanitta fusca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Negreta Nuca Blanca',
		nombre_cientifico='Melanitta perspicillata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Negreta Pico Amarillo',
		nombre_cientifico='Melanitta americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ninfa Mexicana',
		nombre_cientifico='Thalurania ridgwayi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ocotero Enmascarado',
		nombre_cientifico='Peucedramus taeniatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Oropéndola Cabeza Castaña',
		nombre_cientifico='Psarocolius wagleri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Oropéndola de Moctezuma',
		nombre_cientifico='Psarocolius montezuma')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ostrero Americano',
		nombre_cientifico='Haematopus palliatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Ostrero Negro',
		nombre_cientifico='Haematopus bachmani')
	db.Cat_conabio_aves.insert(
		nombre_comun='Págalo Sureño',
		nombre_cientifico='Stercorarius maccormicki')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño Cenizo',
		nombre_cientifico='Oceanodroma homochroa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño de Galápagos',
		nombre_cientifico='Oceanodroma tethys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño de Harcourt',
		nombre_cientifico='Oceanodroma castro')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño de Isla Guadalupe',
		nombre_cientifico='Oceanodroma macrodactyla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño de Leach',
		nombre_cientifico='Oceanodroma leucorhoa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño de Wilson',
		nombre_cientifico='Oceanites oceanicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño Gris',
		nombre_cientifico='Oceanodroma furcata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño Mínimo',
		nombre_cientifico='Oceanodroma microsoma')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paíño Negro',
		nombre_cientifico='Oceanodroma melania')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pájaro Cantil',
		nombre_cientifico='Heliornis fulica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pájaro Estaca Mayor',
		nombre_cientifico='Nyctibius grandis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pájaro Estaca Norteño',
		nombre_cientifico='Nyctibius jamaicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pajuil',
		nombre_cientifico='Penelopina nigra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Alas Blancas',
		nombre_cientifico='Zenaida asiatica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Arroyera',
		nombre_cientifico='Leptotila verreauxi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Cabeza Gris',
		nombre_cientifico='Leptotila plumbeiceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Canela',
		nombre_cientifico='Geotrygon montana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Cara Blanca',
		nombre_cientifico='Zentrygon albifacies')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Caribeña',
		nombre_cientifico='Leptotila jamaicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Colorada',
		nombre_cientifico='Patagioenas cayennensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Corona Blanca',
		nombre_cientifico='Patagioenas leucocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma de Collar Africana',
		nombre_cientifico='Streptopelia roseogrisea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma de Collar Turca',
		nombre_cientifico='Streptopelia decaocto')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma de Oriente',
		nombre_cientifico='Streptopelia chinensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Doméstica',
		nombre_cientifico='Columba livia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Encinera',
		nombre_cientifico='Patagioenas fasciata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Escamosa',
		nombre_cientifico='Patagioenas speciosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Migratoria',
		nombre_cientifico='Ectopistes migratorius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Morada',
		nombre_cientifico='Patagioenas flavirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Pecho Gris',
		nombre_cientifico='Leptotila cassini')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Triste',
		nombre_cientifico='Patagioenas nigrirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Paloma Tuxtleña',
		nombre_cientifico='Zentrygon carrikeri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Ailero',
		nombre_cientifico='Empidonax alnorum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Amarillo Barranqueño',
		nombre_cientifico='Empidonax occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Amarillo del Pacífico',
		nombre_cientifico='Empidonax difficilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Amarillo Sureño',
		nombre_cientifico='Empidonax flavescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Bajacolita',
		nombre_cientifico='Empidonax wrightii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Boreal',
		nombre_cientifico='Contopus cooperi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Cardenalito',
		nombre_cientifico='Pyrocephalus rubinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Cenizo',
		nombre_cientifico='Myiarchus cinerascens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Chico',
		nombre_cientifico='Empidonax minimus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Copetón',
		nombre_cientifico='Mitrephanes phaeocercus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas de Hammond',
		nombre_cientifico='Empidonax hammondii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas del Este',
		nombre_cientifico='Contopus virens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas del Oeste',
		nombre_cientifico='Contopus sordidulus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Fibí',
		nombre_cientifico='Sayornis phoebe')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Garganta Blanca',
		nombre_cientifico='Empidonax albigularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Gritón',
		nombre_cientifico='Myiarchus tyrannulus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Huí',
		nombre_cientifico='Myiarchus nuttingi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas José María',
		nombre_cientifico='Contopus pertinax')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Llanero',
		nombre_cientifico='Sayornis saya')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Matorralero',
		nombre_cientifico='Empidonax oberholseri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Mexicano',
		nombre_cientifico='Deltarhynchus flammulatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Negro',
		nombre_cientifico='Sayornis nigricans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Pecho Canela',
		nombre_cientifico='Empidonax fulvifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Pinero',
		nombre_cientifico='Empidonax affinis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Rayado Cheje',
		nombre_cientifico='Myiodynastes maculatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Rayado Chico',
		nombre_cientifico='Legatus leucophaius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Rayado Común',
		nombre_cientifico='Myiodynastes luteiventris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Saucero',
		nombre_cientifico='Empidonax traillii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Triste',
		nombre_cientifico='Myiarchus tuberculifer')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Tropical',
		nombre_cientifico='Contopus cinereus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Verdoso',
		nombre_cientifico='Empidonax virescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Viajero',
		nombre_cientifico='Myiarchus crinitus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Vientre Amarillo',
		nombre_cientifico='Empidonax flaviventris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Papamoscas Yucateco',
		nombre_cientifico='Myiarchus yucatanensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Boreal',
		nombre_cientifico='Puffinus puffinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Cola Corta',
		nombre_cientifico='Puffinus tenuirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Cola Cuña',
		nombre_cientifico='Puffinus pacificus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Audubon',
		nombre_cientifico='Puffinus lherminieri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Buller',
		nombre_cientifico='Puffinus bulleri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Cory',
		nombre_cientifico='Calonectris diomedea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Galápagos',
		nombre_cientifico='Puffinus subalaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Isla Navidad',
		nombre_cientifico='Puffinus nativitatis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela de Islas Revillagigedo',
		nombre_cientifico='Puffinus auricularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Gris',
		nombre_cientifico='Puffinus griseus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Mayor',
		nombre_cientifico='Puffinus gravis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Mexicana',
		nombre_cientifico='Puffinus opisthomelas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Patas Pálidas',
		nombre_cientifico='Puffinus carneipes')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pardela Patas Rosadas',
		nombre_cientifico='Puffinus creatopus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Patamarilla Euroasiática',
		nombre_cientifico='Tringa stagnatilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Patamarilla Mayor',
		nombre_cientifico='Tringa melanoleuca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Patamarilla Menor',
		nombre_cientifico='Tringa flavipes')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Arcoíris',
		nombre_cientifico='Aix sponsa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Arlequín',
		nombre_cientifico='Histrionicus histrionicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Boludo Mayor',
		nombre_cientifico='Aythya marila')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Boludo Menor',
		nombre_cientifico='Aythya affinis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Cabeza Roja',
		nombre_cientifico='Aythya americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Chalcuán',
		nombre_cientifico='Anas americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Chillón',
		nombre_cientifico='Bucephala clangula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Coacoxtle',
		nombre_cientifico='Aythya valisineria')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Cola Larga',
		nombre_cientifico='Clangula hyemalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Cucharón Norteño',
		nombre_cientifico='Anas clypeata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato de Collar',
		nombre_cientifico='Anas platyrhynchos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Enmascarado',
		nombre_cientifico='Nomonyx dominicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Friso',
		nombre_cientifico='Anas strepera')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Golondrino',
		nombre_cientifico='Anas acuta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Islándico',
		nombre_cientifico='Bucephala islandica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Monja',
		nombre_cientifico='Bucephala albeola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Pico Anillado',
		nombre_cientifico='Aythya collaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Real',
		nombre_cientifico='Cairina moschata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Silbón',
		nombre_cientifico='Anas penelope')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Tejano',
		nombre_cientifico='Anas fulvigula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pato Tepalcate',
		nombre_cientifico='Oxyura jamaicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pava Cojolita',
		nombre_cientifico='Penelope purpurascens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pavito Alas Blancas',
		nombre_cientifico='Myioborus pictus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pavito Alas Negras',
		nombre_cientifico='Myioborus miniatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pavito de Rocas',
		nombre_cientifico='Basileuterus lachrymosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pavito Migratorio',
		nombre_cientifico='Setophaga ruticilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pavón Cornudo',
		nombre_cientifico='Oreophasis derbianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pelícano Blanco Americano',
		nombre_cientifico='Pelecanus erythrorhynchos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pelícano Café',
		nombre_cientifico='Pelecanus occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perico Centroamericano',
		nombre_cientifico='Psittacara strenuus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perico Frente Naranja',
		nombre_cientifico='Eupsittula canicularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perico Mexicano',
		nombre_cientifico='Psittacara holochlorus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perico Monje Argentino',
		nombre_cientifico='Myiopsitta monachus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perico Pecho Sucio',
		nombre_cientifico='Eupsittula nana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Periquito Alas Amarillas',
		nombre_cientifico='Brotogeris jugularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Periquito Barrado',
		nombre_cientifico='Bolborhynchus lineola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Periquito Catarino',
		nombre_cientifico='Forpus cyanopygius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita Azulgris',
		nombre_cientifico='Polioptila caerulea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita Californiana',
		nombre_cientifico='Polioptila californica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita del Desierto',
		nombre_cientifico='Polioptila melanura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita Pispirria',
		nombre_cientifico='Polioptila albiloris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita Sinaloense',
		nombre_cientifico='Polioptila nigriceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Perlita Tropical',
		nombre_cientifico='Polioptila plumbea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Bulwer',
		nombre_cientifico='Bulweria bulwerii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Cook',
		nombre_cientifico='Pterodroma cookii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Galápagos',
		nombre_cientifico='Pterodroma phaeopygia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Isla Juan Fernández',
		nombre_cientifico='Pterodroma externa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Kermadec',
		nombre_cientifico='Pterodroma neglecta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel de Parkinson',
		nombre_cientifico='Procellaria parkinsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Petrel Heráldico',
		nombre_cientifico='Pterodroma arminjoniana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pía Guardabosques',
		nombre_cientifico='Lipaugus unirufus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picochueco Vientre Canela',
		nombre_cientifico='Diglossa baritula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Amarillo',
		nombre_cientifico='Pheucticus chrysopeplus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Azul',
		nombre_cientifico='Passerina caerulea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Azulnegro',
		nombre_cientifico='Cyanocompsa cyanoides')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Cara Negra',
		nombre_cientifico='Caryothraustes poliogaster')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Cuello Rojo',
		nombre_cientifico='Rhodothraupis celaeno')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Degollado',
		nombre_cientifico='Pheucticus ludovicianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogordo Tigrillo',
		nombre_cientifico='Pheucticus melanocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogrueso Encapuchado',
		nombre_cientifico='Coccothraustes abeillei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picogrueso Norteño',
		nombre_cientifico='Coccothraustes vespertinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picolezna Común',
		nombre_cientifico='Xenops minutus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picopando Canelo',
		nombre_cientifico='Limosa fedoa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picopando Cola Barrada',
		nombre_cientifico='Limosa lapponica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picopando del Este',
		nombre_cientifico='Limosa haemastica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Picotuerto Rojo',
		nombre_cientifico='Loxia curvirostra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pijije Alas Blancas',
		nombre_cientifico='Dendrocygna autumnalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pijije Canelo',
		nombre_cientifico='Dendrocygna bicolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pinzón Colorado',
		nombre_cientifico='Haemorhous purpureus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pinzón Mexicano',
		nombre_cientifico='Haemorhous mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pinzón Serrano',
		nombre_cientifico='Haemorhous cassinii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Alas Blancas',
		nombre_cientifico='Piranga leucoptera')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Cabeza Roja',
		nombre_cientifico='Piranga erythrocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Capucha Roja',
		nombre_cientifico='Piranga ludoviciana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Dorso Rayado',
		nombre_cientifico='Piranga bidentata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Encinera',
		nombre_cientifico='Piranga flava')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Escarlata',
		nombre_cientifico='Piranga olivacea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Hormiguera Corona Roja',
		nombre_cientifico='Habia rubica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Hormiguera Garganta Roja',
		nombre_cientifico='Habia fuscicauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Roja',
		nombre_cientifico='Piranga rubra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Piranga Yucateca',
		nombre_cientifico='Piranga roseogularis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Alzacolita',
		nombre_cientifico='Actitis macularius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Andarríos',
		nombre_cientifico='Tringa glareola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Blanco',
		nombre_cientifico='Calidris alba')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Brincaolas',
		nombre_cientifico='Calidris virgata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Combatiente',
		nombre_cientifico='Calidris pugnax')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero de Baird',
		nombre_cientifico='Calidris bairdii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Diminuto',
		nombre_cientifico='Calidris minutilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Dorso Rojo',
		nombre_cientifico='Calidris alpina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Menor',
		nombre_cientifico='Calidris minuta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Occidental',
		nombre_cientifico='Calidris mauri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Ocre',
		nombre_cientifico='Calidris subruficollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Pectoral',
		nombre_cientifico='Calidris melanotos')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Picopando',
		nombre_cientifico='Xenus cinereus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Pihuiuí',
		nombre_cientifico='Tringa semipalmata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Rabadilla Blanca',
		nombre_cientifico='Calidris fuscicollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Rojo',
		nombre_cientifico='Calidris canutus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Semipalmeado',
		nombre_cientifico='Calidris pusilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Solitario',
		nombre_cientifico='Tringa solitaria')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Vagabundo',
		nombre_cientifico='Tringa incana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Zancón',
		nombre_cientifico='Calidris himantopus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Playero Zarapito',
		nombre_cientifico='Calidris ferruginea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Amarilla',
		nombre_cientifico='Coturnicops noveboracensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Canela',
		nombre_cientifico='Laterallus ruber')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Negra',
		nombre_cientifico='Laterallus jamaicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Pecho Amarillo',
		nombre_cientifico='Porzana flaviventer')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Pecho Gris',
		nombre_cientifico='Laterallus exilis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Polluela Sora',
		nombre_cientifico='Porzana carolina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pradero del Oeste',
		nombre_cientifico='Sturnella neglecta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Pradero Tortillaconchile',
		nombre_cientifico='Sturnella magna')
	db.Cat_conabio_aves.insert(
		nombre_comun='Quetzal Mesoamericano',
		nombre_cientifico='Pharomachrus mocinno')
	db.Cat_conabio_aves.insert(
		nombre_comun='Quetzal Orejón',
		nombre_cientifico='Euptilotis neoxenus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rabijunco Cola Blanca',
		nombre_cientifico='Phaethon lepturus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rabijunco Cola Roja',
		nombre_cientifico='Phaethon rubricauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rabijunco Pico Rojo',
		nombre_cientifico='Phaethon aethereus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Californiano',
		nombre_cientifico='Melozone crissalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Cejas Verdes',
		nombre_cientifico='Arremon virenticeps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Cola Verde',
		nombre_cientifico='Pipilo chlorurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador de Collar',
		nombre_cientifico='Pipilo ocai')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Dorso Verde',
		nombre_cientifico='Arremonops chloronotus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Enmascarado',
		nombre_cientifico='Melozone aberti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Gorra Canela',
		nombre_cientifico='Atlapetes pileatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Gorra Castaña',
		nombre_cientifico='Arremon brunneinucha')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Moteado',
		nombre_cientifico='Pipilo maculatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Nuca Blanca',
		nombre_cientifico='Atlapetes albinucha')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Nuca Canela',
		nombre_cientifico='Melozone kieneri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Oaxaqueño',
		nombre_cientifico='Melozone albicollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Oliváceo',
		nombre_cientifico='Arremonops rufivirgatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Orejas Blancas',
		nombre_cientifico='Melozone leucotis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Patilludo',
		nombre_cientifico='Melozone biarcuata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Pico Naranja',
		nombre_cientifico='Arremon aurantiirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascador Viejita',
		nombre_cientifico='Melozone fusca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Azteca',
		nombre_cientifico='Rallus tenuirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Canelo',
		nombre_cientifico='Amaurolimnas concolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Cara Gris',
		nombre_cientifico='Rallus limicola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Costero del Atlántico',
		nombre_cientifico='Rallus crepitans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Costero del Pacífico',
		nombre_cientifico='Rallus obsoletus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Cuello Canela',
		nombre_cientifico='Aramides axillaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Cuello Gris',
		nombre_cientifico='Aramides cajaneus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rascón Pinto',
		nombre_cientifico='Pardirallus maculatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Rayador Americano',
		nombre_cientifico='Rynchops niger')
	db.Cat_conabio_aves.insert(
		nombre_comun='Reinita Mielera',
		nombre_cientifico='Coereba flaveola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Reyezuelo Corona Amarilla',
		nombre_cientifico='Regulus satrapa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Reyezuelo Matraquita',
		nombre_cientifico='Regulus calendula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltador Cabeza Negra',
		nombre_cientifico='Saltator atriceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltador Garganta Ocre',
		nombre_cientifico='Saltator maximus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltador Gris',
		nombre_cientifico='Saltator coerulescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Albicanelo',
		nombre_cientifico='Thryophilus rufalbus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Barrado',
		nombre_cientifico='Thryophilus pleurostictus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Barranqueño',
		nombre_cientifico='Catherpes mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Cejas Canela',
		nombre_cientifico='Troglodytes rufociliatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Chinchibul',
		nombre_cientifico='Cantorchilus modestus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Cholino del Este',
		nombre_cientifico='Troglodytes hiemalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Cholino del Oeste',
		nombre_cientifico='Troglodytes pacificus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Cola Larga',
		nombre_cientifico='Thryomanes bewickii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Común',
		nombre_cientifico='Troglodytes aedon')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared de Carolina',
		nombre_cientifico='Thryothorus ludovicianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared de Isla Clarión',
		nombre_cientifico='Troglodytes tanneri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared de Isla Socorro',
		nombre_cientifico='Troglodytes sissonii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared de Rocas',
		nombre_cientifico='Salpinctes obsoletus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Feliz',
		nombre_cientifico='Pheugopedius felix')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Moteado',
		nombre_cientifico='Pheugopedius maculipectus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Pantanero',
		nombre_cientifico='Cistothorus palustris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Pecho Blanco',
		nombre_cientifico='Henicorhina leucosticta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Pecho Gris',
		nombre_cientifico='Henicorhina leucophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Ruiseñor',
		nombre_cientifico='Microcerculus philomela')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Sabanero',
		nombre_cientifico='Cistothorus platensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Sinaloense',
		nombre_cientifico='Thryophilus sinaloa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltapared Vientre Blanco',
		nombre_cientifico='Uropsila leucogastra')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltarín Cabeza Roja',
		nombre_cientifico='Ceratopipra mentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltarín Cuello Blanco',
		nombre_cientifico='Manacus candei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltarín Toledo',
		nombre_cientifico='Chiroxiphia linearis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Salteador Cola Larga',
		nombre_cientifico='Stercorarius longicaudus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Salteador Parásito',
		nombre_cientifico='Stercorarius parasiticus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Salteador Robusto',
		nombre_cientifico='Stercorarius pomarinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Saltón Picudo',
		nombre_cientifico='Ramphocaenus melanurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Sastrecillo',
		nombre_cientifico='Psaltriparus minimus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Azul',
		nombre_cientifico='Amaurospiza concolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Brincador',
		nombre_cientifico='Volatinia jacarina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero de Collar',
		nombre_cientifico='Sporophila torqueola')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Oliváceo',
		nombre_cientifico='Tiaris olivaceus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Pecho Canela',
		nombre_cientifico='Sporophila minuta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Pico Grueso',
		nombre_cientifico='Sporophila funerea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Pizarra',
		nombre_cientifico='Haplospiza rustica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Plomizo',
		nombre_cientifico='Sporophila schistacea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Semillero Variable',
		nombre_cientifico='Sporophila corvina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Alas Amarillas',
		nombre_cientifico='Thraupis abbas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Azulgris',
		nombre_cientifico='Thraupis episcopus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Cabeza Gris',
		nombre_cientifico='Eucometis penicillata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Cabeza Rayada',
		nombre_cientifico='Spindalis zena')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Capucha Dorada',
		nombre_cientifico='Tangara larvata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Capucha Negra',
		nombre_cientifico='Lanio aurantius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Chiapaneca',
		nombre_cientifico='Tangara cabanisi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Pecho Rosa',
		nombre_cientifico='Rhodinocichla rosea')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Rabadilla Roja',
		nombre_cientifico='Ramphocelus passerinii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tangara Rojinegra',
		nombre_cientifico='Ramphocelus sanguinolentus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Cuerporruín Mexicano',
		nombre_cientifico='Antrostomus arizonae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Cuerporruín Norteño',
		nombre_cientifico='Antrostomus vociferus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos de Carolina',
		nombre_cientifico='Antrostomus carolinensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Huil',
		nombre_cientifico='Nyctiphrynus yucatanicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Pandeagua',
		nombre_cientifico='Phalaenoptilus nuttallii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Prío',
		nombre_cientifico='Nyctiphrynus mcleodii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Sabanero',
		nombre_cientifico='Hydropsalis maculicaudus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Ticurú',
		nombre_cientifico='Antrostomus salvini')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Tucuchillo',
		nombre_cientifico='Antrostomus ridgwayi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tapacaminos Yucateco',
		nombre_cientifico='Antrostomus badius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Bajeño',
		nombre_cientifico='Glaucidium brasilianum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Barbudo',
		nombre_cientifico='Megascops barbarus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Colimense',
		nombre_cientifico='Glaucidium palmarum')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote de Cooper',
		nombre_cientifico='Megascops cooperi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote del Balsas',
		nombre_cientifico='Megascops seductus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote del Este',
		nombre_cientifico='Megascops asio')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote del Oeste',
		nombre_cientifico='Megascops kennicottii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Enano',
		nombre_cientifico='Micrathene whitneyi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Llanero',
		nombre_cientifico='Athene cunicularia')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Mesoamericano',
		nombre_cientifico='Glaucidium griseiceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Ojos Oscuros',
		nombre_cientifico='Psiloscops flammeolus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Oyamelero Norteño',
		nombre_cientifico='Aegolius acadicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Oyamelero Sureño',
		nombre_cientifico='Aegolius ridgwayi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Rítmico',
		nombre_cientifico='Megascops trichopsis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Sapo',
		nombre_cientifico='Megascops guatemalae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Serrano',
		nombre_cientifico='Glaucidium gnoma')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tecolote Tamaulipeco',
		nombre_cientifico='Glaucidium sanchezi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tinamú Canelo',
		nombre_cientifico='Crypturellus cinnamomeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tinamú Jamuey',
		nombre_cientifico='Crypturellus boucardi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tinamú Mayor',
		nombre_cientifico='Tinamus major')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tinamú Menor',
		nombre_cientifico='Crypturellus soui')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Chibiú',
		nombre_cientifico='Tyrannus vociferans')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Cuír',
		nombre_cientifico='Tyrannus couchii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Dorso Negro',
		nombre_cientifico='Tyrannus tyrannus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Gris',
		nombre_cientifico='Tyrannus dominicensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Pálido',
		nombre_cientifico='Tyrannus verticalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Pico Grueso',
		nombre_cientifico='Tyrannus crassirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Pirirí',
		nombre_cientifico='Tyrannus melancholicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Tijereta Gris',
		nombre_cientifico='Tyrannus savana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tirano Tijereta Rosado',
		nombre_cientifico='Tyrannus forficatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Titira Pico Negro',
		nombre_cientifico='Tityra inquisitor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Titira Puerquito',
		nombre_cientifico='Tityra semifasciata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Arrocero',
		nombre_cientifico='Dolichonyx oryzivorus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Cabeza Amarilla',
		nombre_cientifico='Xanthocephalus xanthocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Cabeza Café',
		nombre_cientifico='Molothrus ater')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Canadiense',
		nombre_cientifico='Euphagus carolinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Cantor',
		nombre_cientifico='Dives dives')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Gigante',
		nombre_cientifico='Molothrus oryzivorus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Ojos Amarillos',
		nombre_cientifico='Euphagus cyanocephalus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Ojos Rojos',
		nombre_cientifico='Molothrus aeneus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Sargento',
		nombre_cientifico='Agelaius phoeniceus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Sudamericano',
		nombre_cientifico='Molothrus bonariensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tordo Tricolor',
		nombre_cientifico='Agelaius tricolor')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tórtola Azul',
		nombre_cientifico='Claravis pretiosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tórtola Pecho Morado',
		nombre_cientifico='Claravis mondetoura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tortolita Canela',
		nombre_cientifico='Columbina talpacoti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tortolita Cola Larga',
		nombre_cientifico='Columbina inca')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tortolita Pecho Liso',
		nombre_cientifico='Columbina minuta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tortolita Pico Rojo',
		nombre_cientifico='Columbina passerina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepadorcito Americano',
		nombre_cientifico='Certhia americana')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Barrado',
		nombre_cientifico='Dendrocolaptes sanctithomae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Bigotudo',
		nombre_cientifico='Xiphorhynchus flavigaster')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Cabeza Gris',
		nombre_cientifico='Sittasomus griseicapillus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Canelo',
		nombre_cientifico='Dendrocincla homochroa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Corona Punteada',
		nombre_cientifico='Lepidocolaptes affinis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Corona Rayada',
		nombre_cientifico='Lepidocolaptes souleyetii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Gigante',
		nombre_cientifico='Xiphocolaptes promeropirhynchus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Mexicano',
		nombre_cientifico='Lepidocolaptes leucogaster')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Moteado',
		nombre_cientifico='Xiphorhynchus erythropygius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Pico Cuña',
		nombre_cientifico='Glyphorynchus spirurus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Sepia',
		nombre_cientifico='Dendrocincla anabatina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Trepatroncos Vientre Barrado',
		nombre_cientifico='Dendrocolaptes picumnus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tucán Pico Canoa',
		nombre_cientifico='Ramphastos sulfuratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tucancillo Collarejo',
		nombre_cientifico='Pteroglossus torquatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Tucancillo Verde',
		nombre_cientifico='Aulacorhynchus prasinus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Urraca Cara Blanca',
		nombre_cientifico='Calocitta formosa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Urraca Cara Negra',
		nombre_cientifico='Calocitta colliei')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Cara Blanca',
		nombre_cientifico='Cypseloides storeri')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Collar Blanco',
		nombre_cientifico='Streptoprocne zonaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Cuello Castaño',
		nombre_cientifico='Streptoprocne rutila')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo de Chimenea',
		nombre_cientifico='Chaetura pelagica')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo de Vaux',
		nombre_cientifico='Chaetura vauxi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Negro',
		nombre_cientifico='Cypseloides niger')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Nuca Blanca',
		nombre_cientifico='Streptoprocne semicollaris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Pecho Blanco',
		nombre_cientifico='Aeronautes saxatalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Tijereta Mayor',
		nombre_cientifico='Panyptila sanctihieronymi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vencejo Tijereta Menor',
		nombre_cientifico='Panyptila cayennensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Verdugo Americano',
		nombre_cientifico='Lanius ludovicianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Amarillo',
		nombre_cientifico='Vireo hypochryseus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Anteojillo',
		nombre_cientifico='Vireo solitarius')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Bigotudo',
		nombre_cientifico='Vireo altiloquus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo de Bell',
		nombre_cientifico='Vireo bellii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo de Cassin',
		nombre_cientifico='Vireo cassinii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo de Cozumel',
		nombre_cientifico='Vireo bairdi')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo de Filadelfia',
		nombre_cientifico='Vireo philadelphicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Enano',
		nombre_cientifico='Vireo nelsoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Garganta Amarilla',
		nombre_cientifico='Vireo flavifrons')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Gorjeador',
		nombre_cientifico='Vireo gilvus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Gorra Café',
		nombre_cientifico='Vireo leucophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Gorra Negra',
		nombre_cientifico='Vireo atricapilla')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Gris',
		nombre_cientifico='Vireo vicinior')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Manglero',
		nombre_cientifico='Vireo pallens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Ojos Blancos',
		nombre_cientifico='Vireo griseus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Ojos Rojos',
		nombre_cientifico='Vireo olivaceus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Pizarra',
		nombre_cientifico='Vireo brevipennis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Plomizo',
		nombre_cientifico='Vireo plumbeus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Reyezuelo',
		nombre_cientifico='Vireo huttoni')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Verdeamarillo',
		nombre_cientifico='Vireo flavoviridis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireo Yucateco',
		nombre_cientifico='Vireo magister')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireocillo Cabeza Gris',
		nombre_cientifico='Hylophilus decurtatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireocillo Corona Canela',
		nombre_cientifico='Hylophilus ochraceiceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireón Arlequín',
		nombre_cientifico='Vireolanius melitophrys')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireón Cejas Canela',
		nombre_cientifico='Cyclarhis gujanensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vireón Esmeralda',
		nombre_cientifico='Vireolanius pulchellus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vuelvepiedras Negro',
		nombre_cientifico='Arenaria melanocephala')
	db.Cat_conabio_aves.insert(
		nombre_comun='Vuelvepiedras Rojizo',
		nombre_cientifico='Arenaria interpres')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Californiano',
		nombre_cientifico='Artemisiospiza belli')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Canelo',
		nombre_cientifico='Aimophila rufescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Cinco Rayas',
		nombre_cientifico='Amphispiza quinquestriata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Corona Canela',
		nombre_cientifico='Aimophila ruficeps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Corona Rayada',
		nombre_cientifico='Peucaea ruficauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero de Artemisas',
		nombre_cientifico='Artemisiospiza nevadensis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero de Botteri',
		nombre_cientifico='Peucaea botterii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero de Cassin',
		nombre_cientifico='Peucaea cassinii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Embridado',
		nombre_cientifico='Peucaea mystacalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Garganta Negra',
		nombre_cientifico='Amphispiza bilineata')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Hombros Canela',
		nombre_cientifico='Peucaea carpalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Istmeño',
		nombre_cientifico='Peucaea sumichrasti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Oaxaqueño',
		nombre_cientifico='Aimophila notosticta')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Pecho Negro',
		nombre_cientifico='Peucaea humeralis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zacatonero Serrano',
		nombre_cientifico='Oriturus superciliosus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zafiro Bajacaliforniano',
		nombre_cientifico='Hylocharis xantusii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zafiro Garganta Azul',
		nombre_cientifico='Hylocharis eliciae')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zafiro Orejas Blancas',
		nombre_cientifico='Hylocharis leucotis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zambullidor Cornudo',
		nombre_cientifico='Podiceps auritus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zambullidor Cuello Rojo',
		nombre_cientifico='Podiceps grisegena')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zambullidor Menor',
		nombre_cientifico='Tachybaptus dominicus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zambullidor Orejón',
		nombre_cientifico='Podiceps nigricollis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zambullidor Pico Grueso',
		nombre_cientifico='Podilymbus podiceps')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zanate del Lerma',
		nombre_cientifico='Quiscalus palustris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zanate Mayor',
		nombre_cientifico='Quiscalus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zanate Norteño',
		nombre_cientifico='Quiscalus quiscula')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zarapito Boreal',
		nombre_cientifico='Numenius borealis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zarapito Ganga',
		nombre_cientifico='Bartramia longicauda')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zarapito Pico Largo',
		nombre_cientifico='Numenius americanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zarapito Trinador',
		nombre_cientifico='Numenius phaeopus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zopilote Aura',
		nombre_cientifico='Cathartes aura')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zopilote Común',
		nombre_cientifico='Coragyps atratus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zopilote Rey',
		nombre_cientifico='Sarcoramphus papa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zopilote Sabanero',
		nombre_cientifico='Cathartes burrovianus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Canelo',
		nombre_cientifico='Catharus fuscescens')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Cara Gris',
		nombre_cientifico='Catharus minimus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Cola Canela',
		nombre_cientifico='Catharus guttatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Corona Negra',
		nombre_cientifico='Catharus mexicanus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal de Anteojos',
		nombre_cientifico='Catharus ustulatus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal de Frantzius',
		nombre_cientifico='Catharus frantzii')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Mexicano',
		nombre_cientifico='Catharus occidentalis')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Moteado',
		nombre_cientifico='Hylocichla mustelina')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Pecho Amarillo',
		nombre_cientifico='Catharus dryas')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zorzal Pico Naranja',
		nombre_cientifico='Catharus aurantiirostris')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador Canelo',
		nombre_cientifico='Selasphorus rufus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador Cola Ancha',
		nombre_cientifico='Selasphorus platycercus')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador de Allen',
		nombre_cientifico='Selasphorus sasin')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador Garganta Rayada',
		nombre_cientifico='Selasphorus calliope')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador Guatemalteco',
		nombre_cientifico='Atthis ellioti')
	db.Cat_conabio_aves.insert(
		nombre_comun='Zumbador Mexicano',
		nombre_cientifico='Atthis heloisa')
	db.Cat_conabio_aves.insert(
		nombre_comun='Otros',
		nombre_cientifico='Otros')
