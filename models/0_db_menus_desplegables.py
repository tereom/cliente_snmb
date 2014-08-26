# coding: utf8

## En esta sección se definen las tablas de los menus desplegables

#########################################################################
## Conglomerate_type_option
db.define_table('Conglomerate_type_option',
                Field('num_type','integer', required='TRUE'),
                Field('name_type', 'text', required='TRUE'))

## Fill catalogs when they are empty
if db(db.Conglomerate_type_option.id>0).count() == 0:
    db.Conglomerate_type_option.insert(num_type='1',name_type='Inicial')
    db.Conglomerate_type_option.insert(num_type='2',name_type='Remplazo')
    db.Conglomerate_type_option.insert(num_type='3',name_type='Inaccesible terreno/clima')
    db.Conglomerate_type_option.insert(num_type='4',name_type='Inaccesible social')
    db.Conglomerate_type_option.insert(num_type='5',name_type='Inaccesible gabinete')
    db.Conglomerate_type_option.insert(num_type='6',name_type='Supervisión interna')

#########################################################################
## Conglomerate_state_option
db.define_table('Conglomerate_state_option',
                Field('num_state','integer', required='TRUE'),
                Field('name_state', 'text', required='TRUE'))

if db(db.Conglomerate_state_option.id>0).count() == 0:
    db.Conglomerate_state_option.insert(num_state='1',name_state='Aguascalientes')
    db.Conglomerate_state_option.insert(num_state='2',name_state='Baja California')
    db.Conglomerate_state_option.insert(num_state='3',name_state='Baja California Sur')
    db.Conglomerate_state_option.insert(num_state='4',name_state='Campeche')
    db.Conglomerate_state_option.insert(num_state='5',name_state='Chiapas')
    db.Conglomerate_state_option.insert(num_state='6',name_state='Chihuahua')
    db.Conglomerate_state_option.insert(num_state='7',name_state='Coahuila')
    db.Conglomerate_state_option.insert(num_state='8',name_state='Colima')
    db.Conglomerate_state_option.insert(num_state='9',name_state='Durango')
    db.Conglomerate_state_option.insert(num_state='10',name_state='Estado de México')
    db.Conglomerate_state_option.insert(num_state='11',name_state='Guanajuato')
    db.Conglomerate_state_option.insert(num_state='12',name_state='Guerrero')
    db.Conglomerate_state_option.insert(num_state='13',name_state='Hidalgo')
    db.Conglomerate_state_option.insert(num_state='14',name_state='Jalisco')
    db.Conglomerate_state_option.insert(num_state='15',name_state='Michoacán')
    db.Conglomerate_state_option.insert(num_state='16',name_state='Morelos')
    db.Conglomerate_state_option.insert(num_state='17',name_state='Nayarit')
    db.Conglomerate_state_option.insert(num_state='18',name_state='Nuevo León')
    db.Conglomerate_state_option.insert(num_state='19',name_state='Oaxaca')
    db.Conglomerate_state_option.insert(num_state='20',name_state='Puebla')
    db.Conglomerate_state_option.insert(num_state='21',name_state='Querétaro')
    db.Conglomerate_state_option.insert(num_state='22',name_state='Quintana Roo')
    db.Conglomerate_state_option.insert(num_state='23',name_state='San Luis Potosí')
    db.Conglomerate_state_option.insert(num_state='24',name_state='Sinaloa')
    db.Conglomerate_state_option.insert(num_state='25',name_state='Sonora')
    db.Conglomerate_state_option.insert(num_state='26',name_state='Tabasco')
    db.Conglomerate_state_option.insert(num_state='27',name_state='Tamaulipas')
    db.Conglomerate_state_option.insert(num_state='28',name_state='Tlaxcala')
    db.Conglomerate_state_option.insert(num_state='29',name_state='Veracruz')
    db.Conglomerate_state_option.insert(num_state='30',name_state='Yucatán')
    db.Conglomerate_state_option.insert(num_state='31',name_state='Zacatecas')


#########################################################################
## Conglomerate_property_option
db.define_table('Conglomerate_property_option',
                Field('num_property','integer', required='TRUE'),
                Field('name_property', 'text', required='TRUE'))

if db(db.Conglomerate_property_option.id>0).count() == 0:
    db.Conglomerate_property_option.insert(num_property='1',name_property='Ejidal')
    db.Conglomerate_property_option.insert(num_property='2',name_property='Comunal')
    db.Conglomerate_property_option.insert(num_property='3',name_property='Propiedad particular')
    db.Conglomerate_property_option.insert(num_property='4',name_property='Propiedad federal')


######################################################################### Conglomerate_soil_option
db.define_table('Conglomerate_soil_option',
                Field('num_soil','integer', required='TRUE'),
                Field('name_soil', 'text', required='TRUE'))

if db(db.Conglomerate_soil_option.id>0).count() == 0:
    db.Conglomerate_soil_option.insert(num_soil='1', name_soil='Agricultura de riego')
    db.Conglomerate_soil_option.insert(num_soil='2', name_soil='Agricultura de temporal')
    db.Conglomerate_soil_option.insert(num_soil='3', name_soil='Pastizal inducido')
    db.Conglomerate_soil_option.insert(num_soil='4', name_soil='Pastizal cultivado')
    db.Conglomerate_soil_option.insert(num_soil='5', name_soil='Asentamiento humano')
    db.Conglomerate_soil_option.insert(num_soil='6', name_soil='Cuerpo de agua')
    db.Conglomerate_soil_option.insert(num_soil='7', name_soil='Acuacultura')
    db.Conglomerate_soil_option.insert(num_soil='8', name_soil='Área recién desmontada')
    db.Conglomerate_soil_option.insert(num_soil='9', name_soil='Minería a cielo abierto')
    db.Conglomerate_soil_option.insert(num_soil='10', name_soil='Jales mineros')
    db.Conglomerate_soil_option.insert(num_soil='11', name_soil='Incendios')
    db.Conglomerate_soil_option.insert(num_soil='12', name_soil='Tipo de vegetación')
    db.Conglomerate_soil_option.insert(num_soil='13', name_soil='Otros')


#########################################################################
## Conglomerate_vegetation_option
db.define_table('Conglomerate_vegetation_option',
                Field('num_vegetation','integer', required='TRUE'),
                Field('name_vegetation', 'text', required='TRUE'))

if db(db.Conglomerate_vegetation_option.id>0).count() == 0:
    db.Conglomerate_vegetation_option.insert(num_vegetation='1', name_vegetation='Bosque de coníferas')
    db.Conglomerate_vegetation_option.insert(num_vegetation='2', name_vegetation='Bosque templado de latifoliadas')
    db.Conglomerate_vegetation_option.insert(num_vegetation='3', name_vegetation='Bosque mesófilo de montaña')
    db.Conglomerate_vegetation_option.insert(num_vegetation='4', name_vegetation='Selva caducifolia o subcaducifolia')
    db.Conglomerate_vegetation_option.insert(num_vegetation='5', name_vegetation='Selva perennifolia  o subperennifolia')
    db.Conglomerate_vegetation_option.insert(num_vegetation='6', name_vegetation='Bosque o matorral espinoso')
    db.Conglomerate_vegetation_option.insert(num_vegetation='7', name_vegetation='Matorral sarcocaule o crasicaule o ambos')
    db.Conglomerate_vegetation_option.insert(num_vegetation='8', name_vegetation='Matorral desértico')
    db.Conglomerate_vegetation_option.insert(num_vegetation='9', name_vegetation='Humedal arbóreo')
    db.Conglomerate_vegetation_option.insert(num_vegetation='10', name_vegetation='Humedal herbáceo')
