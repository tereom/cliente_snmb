Conteo de aves
==================

El archivo de vista está dividido en tres secciones: CSS, HTML y JavaScript. 

Index1
------
A continuación describimos las clases utilizadas en el archivo *index1.html*, así como los identificadores asociados al código JavaScript. Éste corresponde a la vista *Transecto especies invasoras*.

Clases
^^^^^^

* **Tabla** y **Centrar** se utilizan para dar distinto estilo a las celdas de la tabla.

* **date, time, string, generic-widget** son clases de Web2py, y se utilizan para validación automática en la vista (por ejemplo, para evitar que se introduza un string en un campo de enteros). En particular, la clase *date* permite visualizar el calendario para seleccionar la fecha.

* **obligatorio** sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.


Identificadores
^^^^^^^^^^^^^^^

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **tabla_transecto_numero** es el id correspondiente al campo *Transecto*, se utiliza para validar si el número de conglomerado que se escribió ya está registrado en la base de datos. Para lograr estó se utiliza AJAX, sin embargo, no es posible utilizar el AJAX de Web2py.

Validaciones
^^^^^^^^^^^^

Hay dos tipos de validación, la primera (validación al momento) se lleva a cabo conforme el usuario captura la información y la segunda se lleva a cabo cuando se envía la forma.

1. Al momento. 
	+ Transecto (id *tabla_transecto_numero* descrito arriba), se valida que no exista previamente en la base de datos.


2. Al enviar. 
	+ La clase *obligatorio*, todos los campos con esta clase deben tener información.
	+ La clase *date*, se usa para validar que la fecha esté en el formato correcto (aaaa-mm-dd), y si lo cumple se valida también que los rangos de día, mes y año sean válidos.
	+ Los identificadores *tabla_hora_inicio* y *tabla_hora_termino* se utilizan para validar que la hora de inicio sea menor a la hora de término.


Index2
------
A continuación describimos las clases utilizadas en el archivo *index2.html*, así como los identificadores asociados al código JavaScript. Éste corresponde a la vista *Registros especies invasoras*. 

Nota: Esta vista esta compuesta por dos secciones, en la primera (*Especies Invasoras*) se ingresa la información de campo y la segunda *Revisión de registros* sirve para revisar la información guardada en la base de datos. Las clases, identificadores y validación de este documento corresponden a la sección de *Especies Invasoras* mientras que la segunda sección se genera con la función *smartgrid* de Web2py.

Clases
^^^^^^

* **Tabla** y **CentrarV** se utilizan para dar distinto estilo a las celdas de la tabla.

* **FlotaIzquierda** se utiliza para ubicar el botón de *Enviar* y los campos *Nombre común*, *Nombre científico*.

* **Nombre** sirve para las acciones fade-in/fade-out, esto es, controlan que los campos *Nombre común* y *Nombre científico* se desvanezcan o aparezcan de acuerdo a la información ingresada.

* **tabla_conabio_lista**, **tabla_hay_nombre_comun**, **tabla_nombre_comun**, **tabla_hay_nombre_cientifico**, **tabla_nombre_cientifico** se utilizan para la validación de los campos *Nombre común* y *Nombre científico*.

Identificadores
^^^^^^^^^^^^^^^

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **shadow_clone** sirve para indicar el contenedor (<div></div>) donde se guardará el menú desplegable de *Transecto*, las opciones de este menú dependen del *Conglomerado* seleccionado en el campo anterior, por lo que se utiliza AJAX para generar el menú. Nota: el AJAX que se utiliza es una implementación simplificada de Web2py, que es conveniente cuando el resultado de la función invocada por AJAX se escribe directamente en el contenedor.

Validaciones
^^^^^^^^^^^^

La validación se lleva a cabo cuando se envía la forma.

	+ La clase *obligatorio*, todos los campos con esta clase deben tener información.
	+ En caso de que se seleccione la opción *Otros* en Lista CONABIO (id *tabla_conabio_lista*) se deberá ingresar el nombre común y/o el nombre científico de la especie para validar esto primero se verifica que al menos uno de los dos campos esté palomeado usando *tabla_hay_nombre_comun* y *tabla_hay_nombre_cientifico*, después se verifica que si el campo se palomeó los campos Nombre común (id *tabla_nombre_comun*) y/o Nombre científico (id *tabla_nombre_cientifico*) contengan información.