Descripción general
===================

El cliente de captura se desarrolló usando el marco de trabajo 
`Web2py <http://www.web2py.com/>`_. Sigue una estructura de 
Modelo-Vista-Controlador que se refleja en la estructura de carpetas.

Bajo el esquema de Web2py, el cliente de captura es una aplicación y todo el
código desarrollado se engloba en la carpeta *cliente_web2py* con las 
siguientes subcarpetas:

1. **controllers**: contiene los controladores que unen 
el modelo con la vista. Hay un archivo para cada sección: Conglomerado, 
Conteo de aves, Especies invasoras, Huellas y excretas, Vegetación y suelo, 
Epífitas, Impactos ambientales, Trampa cámara y Selección de fauna, Grabadora, 
Registros extra, Revisar registros y Exportar datos.

2. **databases**: contiene la base de datos generada por el cliente. Esta 
incluye catálogos para menús desplegables y la información que ingresa el 
usuario. Esta carpeta no contiene código, sus archivos se generan a través de
otros scripts.

3. **docs**: archivos de documentación del cliente. La documentación se hizo 
con `sphinx <http://sphinx-doc.org>`_.

4. **models**: contiene los modelos que generan la base de datos e incluye:
	
	+ el archivo de configuración de la base de datos *00_0_db.py*.  
	+ los modelos de menús desplegables.  
	+ los modelos que guardaran la información ingresada. Al igual que en los 
		controladores hay una archivo para cada sección.  
	+ el archivo *menu.py* donde se definió el menú de la barra superior del cliente.

5. **static**: aquí se agregan los logos que aparecen en el cliente (logos_footer
y logos_header), esta carpeta también incluye imágenes y estilos que agrega
web2py.

6. **uploads**: aquí se almacenan los archivos (imágenes, videos y grabaciones) 
ingresados al cliente.

7. **views**: contiene los archivos html de las vistas e incluye:
	
	+ una carpeta para las vistas de cada sección, el nombre de las carpetas 
		coincide con el nombre del controlador correspondiente y dentro de cada una
		están los archivos html de las subsecciones (ejemplo: 10_conteo_aves contiene 
		index_1.html para *Punto de conteo* e index_2.html para *Ovservaciones aves*).   
	+ los archivos *generic* (que no se modificaron).  
	+ *layout* donde se establecen estilos y logos para las vistas (se utilizaron 
		los valores default).  
	+ la carpeta *default* que incluye la vista de bienvenida y el archivo *user*
		que no se modificó.

8. **otras**: las carpetas restantes (*cron, errors, languages, modules, private, 
sessions*) no se modificaron.

