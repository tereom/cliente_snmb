# coding: utf8

## En esta sección se definen las tablas de los menus desplegables

##########################################################################
## Pestaña Conglomerado
########################################################################

db.define_table('Cat_tipo_conglomerado', Field('nombre', 'text', required='TRUE'))

## El if indica que las tablas se llenarán únicamente cuando estan vacías
if db(db.Cat_tipo_conglomerado.id>0).count() == 0:
    db.Cat_tipo_conglomerado.insert(nombre='Inicial')
    db.Cat_tipo_conglomerado.insert(nombre='Remplazo')
    db.Cat_tipo_conglomerado.insert(nombre='Inaccesible terreno/clima')
    db.Cat_tipo_conglomerado.insert(nombre='Inaccesible social')
    db.Cat_tipo_conglomerado.insert(nombre='Inaccesible gabinete')
    db.Cat_tipo_conglomerado.insert(nombre='Supervisión interna')

#########################################################################

db.define_table('Cat_estado_conglomerado', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_estado_conglomerado.id>0).count() == 0:
    db.Cat_estado_conglomerado.insert(nombre='Aguascalientes')
    db.Cat_estado_conglomerado.insert(nombre='Baja California')
    db.Cat_estado_conglomerado.insert(nombre='Baja California Sur')
    db.Cat_estado_conglomerado.insert(nombre='Campeche')
    db.Cat_estado_conglomerado.insert(nombre='Chiapas')
    db.Cat_estado_conglomerado.insert(nombre='Chihuahua')
    db.Cat_estado_conglomerado.insert(nombre='Coahuila')
    db.Cat_estado_conglomerado.insert(nombre='Colima')
    db.Cat_estado_conglomerado.insert(nombre='Durango')
    db.Cat_estado_conglomerado.insert(nombre='Estado de México')
    db.Cat_estado_conglomerado.insert(nombre='Guanajuato')
    db.Cat_estado_conglomerado.insert(nombre='Guerrero')
    db.Cat_estado_conglomerado.insert(nombre='Hidalgo')
    db.Cat_estado_conglomerado.insert(nombre='Jalisco')
    db.Cat_estado_conglomerado.insert(nombre='Michoacán')
    db.Cat_estado_conglomerado.insert(nombre='Morelos')
    db.Cat_estado_conglomerado.insert(nombre='Nayarit')
    db.Cat_estado_conglomerado.insert(nombre='Nuevo León')
    db.Cat_estado_conglomerado.insert(nombre='Oaxaca')
    db.Cat_estado_conglomerado.insert(nombre='Puebla')
    db.Cat_estado_conglomerado.insert(nombre='Querétaro')
    db.Cat_estado_conglomerado.insert(nombre='Quintana Roo')
    db.Cat_estado_conglomerado.insert(nombre='San Luis Potosí')
    db.Cat_estado_conglomerado.insert(nombre='Sinaloa')
    db.Cat_estado_conglomerado.insert(nombre='Sonora')
    db.Cat_estado_conglomerado.insert(nombre='Tabasco')
    db.Cat_estado_conglomerado.insert(nombre='Tamaulipas')
    db.Cat_estado_conglomerado.insert(nombre='Tlaxcala')
    db.Cat_estado_conglomerado.insert(nombre='Veracruz')
    db.Cat_estado_conglomerado.insert(nombre='Yucatán')
    db.Cat_estado_conglomerado.insert(nombre='Zacatecas')


#########################################################################

db.define_table('Cat_tenencia_conglomerado', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_tenencia_conglomerado.id>0).count() == 0:
    db.Cat_tenencia_conglomerado.insert(nombre='Ejidal')
    db.Cat_tenencia_conglomerado.insert(nombre='Comunal')
    db.Cat_tenencia_conglomerado.insert(nombre='Propiedad particular')
    db.Cat_tenencia_conglomerado.insert(nombre='Propiedad federal')


#########################################################################

db.define_table('Cat_suelo_conglomerado', Field('nombre', 'text'), required='TRUE')

if db(db.Cat_suelo_conglomerado.id>0).count() == 0:
    db.Cat_suelo_conglomerado.insert(nombre='Agricultura de riego')
    db.Cat_suelo_conglomerado.insert(nombre='Agricultura de temporal')
    db.Cat_suelo_conglomerado.insert(nombre='Pastizal inducido')
    db.Cat_suelo_conglomerado.insert(nombre='Pastizal cultivado')
    db.Cat_suelo_conglomerado.insert(nombre='Asentamiento humano')
    db.Cat_suelo_conglomerado.insert(nombre='Cuerpo de agua')
    db.Cat_suelo_conglomerado.insert(nombre='Acuacultura')
    db.Cat_suelo_conglomerado.insert(nombre='Área recién desmontada')
    db.Cat_suelo_conglomerado.insert(nombre='Minería a cielo abierto')
    db.Cat_suelo_conglomerado.insert(nombre='Jales mineros')
    db.Cat_suelo_conglomerado.insert(nombre='Incendios')
    db.Cat_suelo_conglomerado.insert(nombre='Vegetación')
    db.Cat_suelo_conglomerado.insert(nombre='Otros')


#########################################################################

db.define_table('Cat_vegetacion_conglomerado', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_vegetacion_conglomerado.id>0).count() == 0:
    db.Cat_vegetacion_conglomerado.insert( nombre='Bosque de coníferas')
    db.Cat_vegetacion_conglomerado.insert( nombre='Bosque templado de latifoliadas')
    db.Cat_vegetacion_conglomerado.insert( nombre='Bosque mesófilo de montaña')
    db.Cat_vegetacion_conglomerado.insert( nombre='Selva caducifolia o subcaducifolia')
    db.Cat_vegetacion_conglomerado.insert( nombre='Selva perennifolia  o subperennifolia')
    db.Cat_vegetacion_conglomerado.insert( nombre='Bosque o matorral espinoso')
    db.Cat_vegetacion_conglomerado.insert( nombre='Matorral sarcocaule o crasicaule o ambos')
    db.Cat_vegetacion_conglomerado.insert( nombre='Matorral desértico')
    db.Cat_vegetacion_conglomerado.insert( nombre='Humedal arbóreo')
    db.Cat_vegetacion_conglomerado.insert( nombre='Humedal herbáceo')

#########################################################################

db.define_table('Cat_numero_sitio', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_numero_sitio.id>0).count() == 0:
    db.Cat_numero_sitio.insert(nombre='Centro')
    db.Cat_numero_sitio.insert(nombre='Sitio 2')
    db.Cat_numero_sitio.insert(nombre='Sitio 3')
    db.Cat_numero_sitio.insert(nombre='Sitio 4')
    db.Cat_numero_sitio.insert(nombre='Punto de control')

#########################################################################

db.define_table('Cat_elipsoide_sitio', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_elipsoide_sitio.id>0).count() == 0:
    db.Cat_elipsoide_sitio.insert(nombre='NAD27')
    db.Cat_elipsoide_sitio.insert(nombre='WGS84')

##########################################################################
## Pestaña Camara
########################################################################

db.define_table('Cat_nombre_camara', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_nombre_camara.id>0).count() == 0:
    db.Cat_nombre_camara.insert(nombre='Cámara 1')
    db.Cat_nombre_camara.insert(nombre='Cámara 2')

#########################################################################

db.define_table('Cat_resolucion_camara', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_resolucion_camara.id>0).count() == 0:
    db.Cat_resolucion_camara.insert(nombre='Resolución 1')
    db.Cat_resolucion_camara.insert(nombre='Resolución 2')

#########################################################################

db.define_table('Cat_sensibilidad_camara', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_sensibilidad_camara.id>0).count() == 0:
    db.Cat_sensibilidad_camara.insert(nombre='Sensibilidad 1')
    db.Cat_sensibilidad_camara.insert(nombre='Sensibilidad 2')


##########################################################################
## Pestaña Grabadora
########################################################################

db.define_table('Cat_nombre_grabadora', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_nombre_grabadora.id>0).count() == 0:
    db.Cat_nombre_grabadora.insert(nombre='Grabadora 1')
    db.Cat_nombre_grabadora.insert(nombre='Grabadora 2')


##########################################################################
## Pestaña Especies Invasoras / Pestaña Huellas y excretas
######################################################################## 

db.define_table('Cat_numero_transecto', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_numero_transecto.id>0).count() == 0:
    db.Cat_numero_transecto.insert(nombre='Transecto 1')
    db.Cat_numero_transecto.insert(nombre='Transecto 2')
    db.Cat_numero_transecto.insert(nombre='Transecto 3')


##########################################################################
## Pestaña Especies Invasoras
######################################################################## 

db.define_table('Cat_numero_individuos', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_numero_individuos.id>0).count() == 0:
    db.Cat_numero_individuos.insert(nombre='No aplica')
    db.Cat_numero_individuos.insert(nombre='1 a 5')
    db.Cat_numero_individuos.insert(nombre='6 a 10')
    db.Cat_numero_individuos.insert(nombre='más de 10')

##########################################################################
## Lista CONABIO de especies invasoras
######################################################################## 

db.define_table('Cat_conabio_invasoras', Field('nombre', 'text', required='TRUE'))

if db(db.Cat_conabio_invasoras.id>0).count() == 0:
    db.Cat_conabio_invasoras.insert(nombre='Arundo donax - Carrizo gigante')
    db.Cat_conabio_invasoras.insert(nombre='Axis axis - Venado axis')
    db.Cat_conabio_invasoras.insert(nombre='Bassia scoparia - Rodadora')
    db.Cat_conabio_invasoras.insert(nombre='Bromus madritensis - Bromo')
    db.Cat_conabio_invasoras.insert(nombre='Cactoblastis cactorum - Palomilla de nopal')
    db.Cat_conabio_invasoras.insert(nombre='Carpobrotus sp (C. edulis) - Higo marino')
    db.Cat_conabio_invasoras.insert(nombre='Cyperus papyrus (ANP)')
    db.Cat_conabio_invasoras.insert(nombre='Eichhornia crassipes - Lirio acuático')
    db.Cat_conabio_invasoras.insert(nombre='Hedera helix - Hiedra')
    db.Cat_conabio_invasoras.insert(nombre='Lepidium draba /Cardaria draba - Flor bábol, capellanes')
    db.Cat_conabio_invasoras.insert(nombre='Melinis minutiflora - Paja rosada, pasto morado, zacate colorado')
    db.Cat_conabio_invasoras.insert(nombre='Melinis repens - Paja rosada, pasto morado, zacate colorado')
    db.Cat_conabio_invasoras.insert(nombre='Mesembryanthemum crystallinum - Vidrillo')
    db.Cat_conabio_invasoras.insert(nombre='Myiopsitta monachus - Perico monje')
    db.Cat_conabio_invasoras.insert(nombre='Myocastor coypus - Coipu')
    db.Cat_conabio_invasoras.insert(nombre='Oeceoclades maculata - Orquídea monje')
    db.Cat_conabio_invasoras.insert(nombre='Pennisetum clandestinum - Kikuyo, kuyuyú, tapete, colchoncillo')
    db.Cat_conabio_invasoras.insert(nombre='Pueraria sp. (montana lobata o phaseoloides - Kudzu')
    db.Cat_conabio_invasoras.insert(nombre='Rottboellia cochinchinensis - Caminadora')
    db.Cat_conabio_invasoras.insert(nombre='Salsola sp. (vermiculata o tragus) - Rodadora')
    db.Cat_conabio_invasoras.insert(nombre='Stizlobium prurienes - Picapica')
    db.Cat_conabio_invasoras.insert(nombre='Sus scrofa - Cerdo europeo')
    db.Cat_conabio_invasoras.insert(nombre='Tamarix sp. - Pino salado, cedro salado, tamarisco')
    db.Cat_conabio_invasoras.insert(nombre='Otros')

