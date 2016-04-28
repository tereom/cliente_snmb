### Descripción general

El cliente de captura es una aplicación Web que sirve para la digitalización de
los datos colectados en campo, como parte del proyecto del Sistema Nacional de
Monitoreo de Biodiversidad (SNMB).

Éste se desarrolló usando el marco de trabajo [Web2py](http://www.web2py.com/),
el cuál tiene las siguientes características:

* Sigue un paradigma de modelo-vista-controlador, en el cuál el modelo define
el esquema de la base de datos; la vista, la interfaz gráfica que utiliza el
usuario, y el controlador, la liga entre el input del usuario y la base de datos.

* Se descarga como un paquete, que incluye su propio intérprete de Python, un
servidor local, un DBMS SQLite e incluso un IDE para programar.

* Crear una nueva aplicación es muy sencillo: simplemente se utiliza la interfaz
gráfica, y automáticamente se inserta una carpeta en applications con el nombre
de la aplicación creada.

* Cada aplicación tiene una estructura de carpetas como sigue:
	+ __controllers__
	+ cron
	+ databases
	+ errors
	+ languages
	+ __models__
	+ __modules__
	+ __private__
	+ sessions
	+ __static__
	+ uploads
	+ __views__
		
Las carpetas resaltadas son las que contienen el código propio de la aplicación que
estamos desarrollando. Sin embargo, también pueden contener código precargado que
es indispensable para que nuestra aplicación corra adecuadamente.

Con respecto a las carpetas "cron", "databses", "errors", "languages", "sessions" y
"uploads", su contenido se genera con el uso de la aplicación, por lo que pueden
ser eliminadas una y otra vez sin problemas (siempre que los datos capturados no
sean importantes).

Se eligió programar el cliente utilizando Web2py, debido a que:
* Al empaquetar un intérprete de Python, un servidor local, y un DBMS SQlite,
es ideal para nuestros fines: una aplicación de escritorio de fácil instalación,
que sirva para capturar datos en una base local y fácilmente distribuíble (SQLite);
pero que eventualmente pueda escalar para estar en un servidor remoto.
* Permite hacer exportaciones CSV de la base local SQLite, que sirve para diseminar
* los datos entre los que levantan la información y la capturan.
* Por medio de esos archivos CSV, permite fusionar la información de varias bases
de datos en una sola (lidiando automáticamente con los problemas de las ID's).

Bajo el esquema de Web2py, el cliente de captura es una aplicación y todo el código
desarrollado se engloba en la carpeta *cliente_web2py*, dentro de sus subcarpetas
adecuadas.

El código está modularizado en scripts numerados, cada número representa una
sección distinta. Dichas secciones se reflejan en la interfaz gráfica del cliente
como secciones en el menú.

1. **models**: los scripts están numerados, cada uno de ellos contiene las tablas
correspondientes a su sección. También se incluyen scripts que definen los parámetros
de la base de datos, así como los modelos de los menús desplegables. Por alguna razón
Web2py incluye aquí el código que define el menú principal de la interfaz gráfica.

2. **controllers**: cada script numerado contiene todos los controladores de las
pestañas correspondientes a una sección, así como funciones asociadas. Adicionalmente,
están los controladores que definen el funcionamiento general de la aplicación, así como
el controlador con funcionalidades default.

3. **views**: como cada script del controlador contiene todos los controladores de las
pestañas correspondientes a una sección, y cada pestaña tiene su propia interfaz gráfica,
los scripts de controladores se mapean a carpetas en la vista; y las funciones
(controladores) se mapean a archivos html. Esta carpeta contiene también la vista default,
algunas funciones para el AJAX propio de Web2py, así como la plantilla (layout) general
para la interfaz gráfica de Web2py, que se extiende para crear las nuestras propias.

4. **modules**: contiene código reutilizable en toda la aplicación. Su contenido se importa
como el de cualquier paquete de Python.

5. **static**: contiene archivos estáticos necesarios para el correcto funcionamiento de
la aplicación (CSS, JS, imágenes, entre otros). Muchos archivos son precargados, pero aquí
podemos guardar los logos que utilicemos en nuestra aplicación particular.

6. **private**: esta carpeta es nueva (la versión 2.13.4 no la tenía, pero la versión 2.14.5
sí). Agrupa varios parámetros de la aplicación en un mismo lugar, para facilitar la configuración
de la misma.

### Instalación

1. [Descargar Web2py](http://www.web2py.com/), ya sea para Windows o para Mac.
2. Ir a la carpeta de __applications__
3. Clonar o copiar el repositorio ahí. Automáticamente se tendrá una versión funcional.
4. En "modules/estructura_archivos_admin.py" verificar que el path específico para cada sistema
operativo está siendo utilizado.
