# coding: utf8

## En esta sección se definen las tablas de los menus desplegables

#########################################################################
## Conglomerado_tipo_opcion
db.define_table('Conglomerado_tipo_opcion',
                Field('num_tipo','integer', required='TRUE'),
                Field('nombre_tipo', 'text', required='TRUE'))

## El if indica que las tablas se llenarán únicamente cuando estan vacías
if db(db.Conglomerado_tipo_opcion.id>0).count() == 0:
    db.Conglomerado_tipo_opcion.insert(num_tipo='1',nombre_tipo='Inicial')
    db.Conglomerado_tipo_opcion.insert(num_tipo='2',nombre_tipo='Remplazo')
    db.Conglomerado_tipo_opcion.insert(num_tipo='3',nombre_tipo='Inaccesible terreno/clima')
    db.Conglomerado_tipo_opcion.insert(num_tipo='4',nombre_tipo='Inaccesible social')
    db.Conglomerado_tipo_opcion.insert(num_tipo='5',nombre_tipo='Inaccesible gabinete')
    db.Conglomerado_tipo_opcion.insert(num_tipo='6',nombre_tipo='Supervisión interna')

#########################################################################
## Conglomerado_estado_opcion
db.define_table('Conglomerado_estado_opcion',
                Field('num_estado','integer', required='TRUE'),
                Field('nombre_estado', 'text', required='TRUE'))

if db(db.Conglomerado_estado_opcion.id>0).count() == 0:
    db.Conglomerado_estado_opcion.insert(num_estado='1',nombre_estado='Aguascalientes')
    db.Conglomerado_estado_opcion.insert(num_estado='2',nombre_estado='Baja California')
    db.Conglomerado_estado_opcion.insert(num_estado='3',nombre_estado='Baja California Sur')
    db.Conglomerado_estado_opcion.insert(num_estado='4',nombre_estado='Campeche')
    db.Conglomerado_estado_opcion.insert(num_estado='5',nombre_estado='Chiapas')
    db.Conglomerado_estado_opcion.insert(num_estado='6',nombre_estado='Chihuahua')
    db.Conglomerado_estado_opcion.insert(num_estado='7',nombre_estado='Coahuila')
    db.Conglomerado_estado_opcion.insert(num_estado='8',nombre_estado='Colima')
    db.Conglomerado_estado_opcion.insert(num_estado='9',nombre_estado='Durango')
    db.Conglomerado_estado_opcion.insert(num_estado='10',nombre_estado='Estado de México')
    db.Conglomerado_estado_opcion.insert(num_estado='11',nombre_estado='Guanajuato')
    db.Conglomerado_estado_opcion.insert(num_estado='12',nombre_estado='Guerrero')
    db.Conglomerado_estado_opcion.insert(num_estado='13',nombre_estado='Hidalgo')
    db.Conglomerado_estado_opcion.insert(num_estado='14',nombre_estado='Jalisco')
    db.Conglomerado_estado_opcion.insert(num_estado='15',nombre_estado='Michoacán')
    db.Conglomerado_estado_opcion.insert(num_estado='16',nombre_estado='Morelos')
    db.Conglomerado_estado_opcion.insert(num_estado='17',nombre_estado='Nayarit')
    db.Conglomerado_estado_opcion.insert(num_estado='18',nombre_estado='Nuevo León')
    db.Conglomerado_estado_opcion.insert(num_estado='19',nombre_estado='Oaxaca')
    db.Conglomerado_estado_opcion.insert(num_estado='20',nombre_estado='Puebla')
    db.Conglomerado_estado_opcion.insert(num_estado='21',nombre_estado='Querétaro')
    db.Conglomerado_estado_opcion.insert(num_estado='22',nombre_estado='Quintana Roo')
    db.Conglomerado_estado_opcion.insert(num_estado='23',nombre_estado='San Luis Potosí')
    db.Conglomerado_estado_opcion.insert(num_estado='24',nombre_estado='Sinaloa')
    db.Conglomerado_estado_opcion.insert(num_estado='25',nombre_estado='Sonora')
    db.Conglomerado_estado_opcion.insert(num_estado='26',nombre_estado='Tabasco')
    db.Conglomerado_estado_opcion.insert(num_estado='27',nombre_estado='Tamaulipas')
    db.Conglomerado_estado_opcion.insert(num_estado='28',nombre_estado='Tlaxcala')
    db.Conglomerado_estado_opcion.insert(num_estado='29',nombre_estado='Veracruz')
    db.Conglomerado_estado_opcion.insert(num_estado='30',nombre_estado='Yucatán')
    db.Conglomerado_estado_opcion.insert(num_estado='31',nombre_estado='Zacatecas')


#########################################################################
## Conglomerado_tenencia_opcion
db.define_table('Conglomerado_tenencia_opcion',
                Field('num_tenencia','integer', required='TRUE'),
                Field('nombre_tenencia', 'text', required='TRUE'))

if db(db.Conglomerado_tenencia_opcion.id>0).count() == 0:
    db.Conglomerado_tenencia_opcion.insert(num_tenencia='1',nombre_tenencia='Ejidal')
    db.Conglomerado_tenencia_opcion.insert(num_tenencia='2',nombre_tenencia='Comunal')
    db.Conglomerado_tenencia_opcion.insert(num_tenencia='3',nombre_tenencia='Propiedad particular')
    db.Conglomerado_tenencia_opcion.insert(num_tenencia='4',nombre_tenencia='Propiedad federal')


######################################################################### Conglomerado_suelo_opcion
db.define_table('Conglomerado_suelo_opcion',
                Field('num_suelo','integer'),
                Field('nombre_suelo', 'text'))

if db(db.Conglomerado_suelo_opcion.id>0).count() == 0:
    db.Conglomerado_suelo_opcion.insert(num_suelo='1', nombre_suelo='Agricultura de riego')
    db.Conglomerado_suelo_opcion.insert(num_suelo='2', nombre_suelo='Agricultura de temporal')
    db.Conglomerado_suelo_opcion.insert(num_suelo='3', nombre_suelo='Pastizal inducido')
    db.Conglomerado_suelo_opcion.insert(num_suelo='4', nombre_suelo='Pastizal cultivado')
    db.Conglomerado_suelo_opcion.insert(num_suelo='5', nombre_suelo='Asentamiento humano')
    db.Conglomerado_suelo_opcion.insert(num_suelo='6', nombre_suelo='Cuerpo de agua')
    db.Conglomerado_suelo_opcion.insert(num_suelo='7', nombre_suelo='Acuacultura')
    db.Conglomerado_suelo_opcion.insert(num_suelo='8', nombre_suelo='Área recién desmontada')
    db.Conglomerado_suelo_opcion.insert(num_suelo='9', nombre_suelo='Minería a cielo abierto')
    db.Conglomerado_suelo_opcion.insert(num_suelo='10', nombre_suelo='Jales mineros')
    db.Conglomerado_suelo_opcion.insert(num_suelo='11', nombre_suelo='Incendios')
    db.Conglomerado_suelo_opcion.insert(num_suelo='12', nombre_suelo='Vegetación')
    db.Conglomerado_suelo_opcion.insert(num_suelo='13', nombre_suelo='Otros')


#########################################################################
## Conglomerado_vegetacion_opcion
db.define_table('Conglomerado_vegetacion_opcion',
                Field('num_vegetacion','integer', required='TRUE'),
                Field('nombre_vegetacion', 'text'),  required='TRUE')

if db(db.Conglomerado_vegetacion_opcion.id>0).count() == 0:
    #db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='0', nombre_vegetacion=None)
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='1', nombre_vegetacion='Bosque de coníferas')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='2', nombre_vegetacion='Bosque templado de latifoliadas')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='3', nombre_vegetacion='Bosque mesófilo de montaña')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='4', nombre_vegetacion='Selva caducifolia o subcaducifolia')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='5', nombre_vegetacion='Selva perennifolia  o subperennifolia')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='6', nombre_vegetacion='Bosque o matorral espinoso')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='7', nombre_vegetacion='Matorral sarcocaule o crasicaule o ambos')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='8', nombre_vegetacion='Matorral desértico')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='9', nombre_vegetacion='Humedal arbóreo')
    db.Conglomerado_vegetacion_opcion.insert(num_vegetacion='10', nombre_vegetacion='Humedal herbáceo')


#########################################################################
## Sitio_numero_opcion
db.define_table('Sitio_numero_opcion',
                Field('num_numero','integer', required='TRUE'),
                Field('nombre_numero', 'text', required='TRUE'))

if db(db.Sitio_numero_opcion.id>0).count() == 0:
    db.Sitio_numero_opcion.insert(num_numero='1', nombre_numero='Punto de control')
    db.Sitio_numero_opcion.insert(num_numero='1', nombre_numero='Centro')
    db.Sitio_numero_opcion.insert(num_numero='2', nombre_numero='Sitio 2')
    db.Sitio_numero_opcion.insert(num_numero='3', nombre_numero='Sitio 3')
    db.Sitio_numero_opcion.insert(num_numero='4', nombre_numero='Sitio 4')

#########################################################################
## 
db.define_table('Sitio_elipsoide_opcion',
                Field('num_elipsoide','integer', required='TRUE'),
                Field('nombre_elipsoide', 'text', required='TRUE'))

if db(db.Sitio_elipsoide_opcion.id>0).count() == 0:
    db.Sitio_elipsoide_opcion.insert(num_elipsoide='1', nombre_elipsoide='Elipsoide 1')
    db.Sitio_elipsoide_opcion.insert(num_elipsoide='2', nombre_elipsoide='Elipsoide 2')


##########################################################################
## Tab Camara
########################################################################
## 
db.define_table('Camara_nombre_opcion',
                Field('num_nombre','integer', required='TRUE'),
                Field('nombre_nombre', 'text', required='TRUE'))

if db(db.Camara_nombre_opcion.id>0).count() == 0:
    db.Camara_nombre_opcion.insert(num_nombre='1', nombre_nombre='Cámara 1')
    db.Camara_nombre_opcion.insert(num_nombre='2', nombre_nombre='Cámara 2')

#########################################################################
## 
db.define_table('Camara_resolucion_opcion',
                Field('num_resolucion','integer', required='TRUE'),
                Field('nombre_resolucion', 'text', required='TRUE'))

if db(db.Camara_resolucion_opcion.id>0).count() == 0:
    db.Camara_resolucion_opcion.insert(num_resolucion='1', nombre_resolucion='Resolución 1')
    db.Camara_resolucion_opcion.insert(num_resolucion='2', nombre_resolucion='Resolución 2')

#########################################################################
## 
db.define_table('Camara_sensibilidad_opcion',
                Field('num_sensibilidad','integer', required='TRUE'),
                Field('nombre_sensibilidad', 'text', required='TRUE'))

if db(db.Camara_sensibilidad_opcion.id>0).count() == 0:
    db.Camara_sensibilidad_opcion.insert(num_sensibilidad='1', nombre_sensibilidad='Sensibilidad 1')
    db.Camara_sensibilidad_opcion.insert(num_sensibilidad='2', nombre_sensibilidad='Sensibilidad 2')


##########################################################################
## Tab Grabadora
########################################################################
## 
db.define_table('Grabadora_nombre_opcion',
                Field('num_nombre','integer', required='TRUE'),
                Field('nombre_nombre', 'text', required='TRUE'))

if db(db.Grabadora_nombre_opcion.id>0).count() == 0:
    db.Grabadora_nombre_opcion.insert(num_nombre='1', nombre_nombre='Grabadora 1')
    db.Grabadora_nombre_opcion.insert(num_nombre='2', nombre_nombre='Grabadora 2')
