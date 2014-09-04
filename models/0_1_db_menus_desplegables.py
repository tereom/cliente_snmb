# coding: utf8

## En esta sección se definen las tablas de los menus desplegables

#########################################################################
## Conglomerado_tipo_opcion
db.define_table('Conglomerado_tipo_opcion',
                Field('nombre_tipo', 'text', required='TRUE'))

## El if indica que las tablas se llenarán únicamente cuando estan vacías
if db(db.Conglomerado_tipo_opcion.id>0).count() == 0:
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Inicial')
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Remplazo')
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Inaccesible terreno/clima')
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Inaccesible social')
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Inaccesible gabinete')
    db.Conglomerado_tipo_opcion.insert(nombre_tipo='Supervisión interna')

#########################################################################
## Conglomerado_estado_opcion
db.define_table('Conglomerado_estado_opcion',
                Field('nombre_estado', 'text', required='TRUE'))

if db(db.Conglomerado_estado_opcion.id>0).count() == 0:
    db.Conglomerado_estado_opcion.insert(nombre_estado='Aguascalientes')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Baja California')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Baja California Sur')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Campeche')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Chiapas')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Chihuahua')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Coahuila')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Colima')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Durango')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Estado de México')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Guanajuato')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Guerrero')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Hidalgo')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Jalisco')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Michoacán')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Morelos')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Nayarit')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Nuevo León')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Oaxaca')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Puebla')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Querétaro')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Quintana Roo')
    db.Conglomerado_estado_opcion.insert(nombre_estado='San Luis Potosí')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Sinaloa')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Sonora')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Tabasco')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Tamaulipas')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Tlaxcala')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Veracruz')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Yucatán')
    db.Conglomerado_estado_opcion.insert(nombre_estado='Zacatecas')


#########################################################################
## Conglomerado_tenencia_opcion
db.define_table('Conglomerado_tenencia_opcion',
                Field('nombre_tenencia', 'text', required='TRUE'))

if db(db.Conglomerado_tenencia_opcion.id>0).count() == 0:
    db.Conglomerado_tenencia_opcion.insert(nombre_tenencia='Ejidal')
    db.Conglomerado_tenencia_opcion.insert(nombre_tenencia='Comunal')
    db.Conglomerado_tenencia_opcion.insert(nombre_tenencia='Propiedad particular')
    db.Conglomerado_tenencia_opcion.insert(nombre_tenencia='Propiedad federal')


######################################################################### Conglomerado_suelo_opcion
db.define_table('Conglomerado_suelo_opcion',
                Field('nombre_suelo', 'text'))

if db(db.Conglomerado_suelo_opcion.id>0).count() == 0:
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Agricultura de riego')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Agricultura de temporal')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Pastizal inducido')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Pastizal cultivado')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Asentamiento humano')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Cuerpo de agua')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Acuacultura')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Área recién desmontada')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Minería a cielo abierto')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Jales mineros')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Incendios')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Vegetación')
    db.Conglomerado_suelo_opcion.insert( nombre_suelo='Otros')


#########################################################################
## Conglomerado_vegetacion_opcion
db.define_table('Conglomerado_vegetacion_opcion',
                Field('nombre_vegetacion', 'text'),  required='TRUE')

if db(db.Conglomerado_vegetacion_opcion.id>0).count() == 0:
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Bosque de coníferas')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Bosque templado de latifoliadas')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Bosque mesófilo de montaña')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Selva caducifolia o subcaducifolia')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Selva perennifolia  o subperennifolia')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Bosque o matorral espinoso')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Matorral sarcocaule o crasicaule o ambos')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Matorral desértico')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Humedal arbóreo')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='Humedal herbáceo')
    db.Conglomerado_vegetacion_opcion.insert( nombre_vegetacion='No aplica')

#########################################################################
## Sitio_numero_opcion
db.define_table('Sitio_numero_opcion',
                Field('nombre_numero', 'text', required='TRUE'))

if db(db.Sitio_numero_opcion.id>0).count() == 0:
    db.Sitio_numero_opcion.insert( nombre_numero='Punto de control')
    db.Sitio_numero_opcion.insert( nombre_numero='Centro')
    db.Sitio_numero_opcion.insert( nombre_numero='Sitio 2')
    db.Sitio_numero_opcion.insert( nombre_numero='Sitio 3')
    db.Sitio_numero_opcion.insert( nombre_numero='Sitio 4')

#########################################################################
## 
db.define_table('Sitio_elipsoide_opcion',
                Field('nombre_elipsoide', 'text', required='TRUE'))

if db(db.Sitio_elipsoide_opcion.id>0).count() == 0:
    db.Sitio_elipsoide_opcion.insert( nombre_elipsoide='Elipsoide 1')
    db.Sitio_elipsoide_opcion.insert( nombre_elipsoide='Elipsoide 2')


##########################################################################
## Tab Camara
########################################################################
## 
db.define_table('Camara_nombre_opcion',
                Field('nombre_nombre', 'text', required='TRUE'))

if db(db.Camara_nombre_opcion.id>0).count() == 0:
    db.Camara_nombre_opcion.insert( nombre_nombre='Cámara 1')
    db.Camara_nombre_opcion.insert( nombre_nombre='Cámara 2')

#########################################################################
## 
db.define_table('Camara_resolucion_opcion',
                Field('nombre_resolucion', 'text', required='TRUE'))

if db(db.Camara_resolucion_opcion.id>0).count() == 0:
    db.Camara_resolucion_opcion.insert( nombre_resolucion='Resolución 1')
    db.Camara_resolucion_opcion.insert( nombre_resolucion='Resolución 2')

#########################################################################
## 
db.define_table('Camara_sensibilidad_opcion',

                Field('nombre_sensibilidad', 'text', required='TRUE'))

if db(db.Camara_sensibilidad_opcion.id>0).count() == 0:
    db.Camara_sensibilidad_opcion.insert( nombre_sensibilidad='Sensibilidad 1')
    db.Camara_sensibilidad_opcion.insert( nombre_sensibilidad='Sensibilidad 2')


##########################################################################
## Tab Grabadora
########################################################################

db.define_table('Grabadora_nombre_opcion',
                Field('nombre_nombre', 'text', required='TRUE'))

if db(db.Grabadora_nombre_opcion.id>0).count() == 0:
    db.Grabadora_nombre_opcion.insert( nombre_nombre='Grabadora 1')
    db.Grabadora_nombre_opcion.insert( nombre_nombre='Grabadora 2')


##########################################################################
## Tab Especies Invasoras / Tab Huellas Excretas
######################################################################## 

db.define_table('Transecto_numero_opcion',
                Field('nombre_transecto', 'text', required='TRUE'))

if db(db.Transecto_numero_opcion.id>0).count() == 0:
    db.Transecto_numero_opcion.insert( \
        nombre_transecto='T1')
    db.Transecto_numero_opcion.insert( \
        nombre_transecto='T2')
    db.Transecto_numero_opcion.insert( \
        nombre_transecto='T3')


##########################################################################
## Tab Especies Invasoras
######################################################################## 

db.define_table('Especie_individuos_opcion',
                Field('nombre_individuos', 'text', required='TRUE'))

if db(db.Especie_individuos_opcion.id>0).count() == 0:
    db.Especie_individuos_opcion.insert( \
        nombre_individuos='No aplica')
    db.Especie_individuos_opcion.insert( \
        nombre_individuos='1 a 5')
    db.Especie_individuos_opcion.insert( \
        nombre_individuos='6 a 10')
    db.Especie_individuos_opcion.insert( \
        nombre_individuos='más de 10')
