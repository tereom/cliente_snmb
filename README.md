### Descripción general

El cliente de captura es una aplicación Web que sirve para la digitalización de los
datos colectados en campo, como parte del proyecto del Sistema Nacional de
Monitoreo de Biodiversidad (SNMB).

Éste se desarrolló usando el marco de trabajo [Web2py](http://www.web2py.com/), el
cuál tiene las siguientes características:
* Se descarga como un paquete, que incluye su propio intérprete de Python, un
	servidor local, un DBMS SQLite e incluso un IDE para programar.
* Crear una nueva aplicación es muy sencillo: simplemente se utiliza la interfaz
	gráfica, y automáticamente se inserta una carpete en applications con el nombre
	de la aplicación creada.
* Cada aplicación tiene una estructura de carpetas como sigue:
	+ __controllers__
	+ cron
	+ databases
	+ errors
	+ languages
	+ __models__
	+ __modules__
	+ sessions
	+ __static__
	+ uploads
	+ __views__
	
	Las carpetas resaltadas son las que contienen el código propio de la aplicación
	que estamos desarrollando. Sin embargo, también pueden contener código autogenerado
	que es indispensable para que nuestra aplicación corra adecuadamente. Con respecto
	a las carpetas "sessions", "errors", "databases" y "uploads", su contenido
	se genera con el uso de la aplicación, por lo que pueden ser eliminadas una
	y otra vez sin porblemas (siempre que los datos capturados no sean importantes).

Se eligió progrmar el cliente utilizando Web2py, debido a que:
* Al empaquetar un intérprete de python y un servidor local, es ideal
	para nuestros fines: una aplicación de escritorio que sirva para capturar
	datos en una base de datos local y fácilmente distribuíble (SQLite); pero
	que eventualmente pueda escalar para estar en un servidor remoto.
* Permite hacer exportaciones CSV de la base local SQLite, que sirve para
	diseminar los datos entre los que levantan la información y la capturan.
* Por medio de esos archivos CSV, permite fusionar la información de varias bases
	de datos en una sola (lidiando automáticamente con los problemas de los ID's).
	Éste proceso es indispensable para la integración de los datos en CONABIO.


Bajo el esquema de Web2py, el cliente de captura es una aplicación y todo el
código desarrollado se engloba en la carpeta *cliente_web2py* con las 
siguientes subcarpetas:

1. **controllers**: contiene los controladores que unen el modelo con la vista. Hay un archivo para cada sección: Conglomerado, Conteo de aves, Especies invasorasHuellas y excretas, Vegetación y suelo, Epífitas, Impactos ambientales, Trampa cámara y Selección de fauna, Grabadora, Registros extra, Revisar registros y Exportar datos.

2. **databases**: contiene la base de datos generada por el cliente. Esta incluye catálogos para menús desplegables y la información que ingresa el usuario. Esta carpeta no contiene código, sus archivos se generan a través de otros scripts.

3. **docs**: archivos de documentación del cliente. La documentación se hizo con `sphinx <http://sphinx-doc.org>`_.

4. **models**: contiene los modelos que generan la base de datos e incluye:
	
	+ el archivo de configuración de la base de datos *00_0_db.py*.  
	+ los modelos de menús desplegables.  
	+ los modelos que guardaran la información ingresada. Al igual que en los controladores hay una archivo para cada sección.  
	+ el archivo *menu.py* donde se definió el menú de la barra superior del cliente.

5. **static**: aquí se agregan los logos que aparecen en el cliente (logos_footer y logos_header), esta carpeta también incluye imágenes y estilos que agrega web2py.

6. **uploads**: aquí se almacenan los archivos (imágenes, videos y grabaciones) ingresados al cliente.

7. **views**: contiene los archivos html de las vistas e incluye:
	
	+ una carpeta para las vistas de cada sección, el nombre de las carpetas  coincide con el nombre del controlador correspondiente y dentro de cada una están los archivos html de las subsecciones (ejemplo: 10_conteo_aves contiene index_1.html para *Punto de conteo* e index_2.html para *Ovservaciones aves*).   
	+ los archivos *generic* (que no se modificaron).  
	+ *layout* donde se establecen estilos y logos para las vistas (se utilizaron los valores default).  
	+ la carpeta *default* que incluye la vista de bienvenida y el archivo *user* que no se modificó.

8. **otras**: las carpetas restantes (*cron, errors, languages, modules, private, 
sessions*) no se modificaron.

