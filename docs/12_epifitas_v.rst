Epífitas
==================

El archivo de vista está dividido en tres secciones: CSS, HTML y JavaScript. 

Index1
------
A continuación describimos las clases utilizadas en el archivo *index1.html*, así como los identificadores asociados al código JavaScript. Éste corresponde a la vista *Epífitas*.

Clases
^^^^^^

* **Tabla** y **Centrar** se utilizan para dar distinto estilo a las celdas de la tabla.

* **obligatorio** sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.

Identificadores
^^^^^^^^^^^^^^^

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **shadow_clone** y **tabla_sitio_muestra_id** son los ids correspondiente al campo *Sitio*, se utilizan para validar si el sitio que se escribió ya está registrado en la base de datos. Para lograr estó se utiliza AJAX, sin embargo, no es posible utilizar el AJAX simplificado de Web2py.

EXPLICAR PORQUE SE NECESITAN 2 CLASES!

Validaciones
^^^^^^^^^^^^

Hay dos tipos de validación, la primera (validación al momento) se lleva a cabo conforme el usuario captura la información y la segunda se lleva a cabo cuando se envía la forma.

1. Al momento. 
	+ Sitio (id *tabla_sitio_muestra_id*), se utiliza para validar si el número de sitio que se seleccionó ya está registrado en la base de datos. Para lograr estó se utiliza AJAX, sin embargo, no es posible utilizar el AJAX de Web2py ya que el objetivo es validación (en contraste con el caso de *shadow_clone* donde se requiere imprimir un menú en pantalla)


2. Al enviar. 
	+ La clase *obligatorio*, todos los campos con esta clase deben tener información.
	+ La clase *date*, se usa para validar que la fecha esté en el formato correcto (aaaa-mm-dd), y si lo cumple se valida también que los rangos de día, mes y año sean válidos.
	+ Los identificadores *tabla_hora_inicio* y *tabla_hora_termino* se utilizan para validar que la hora de inicio sea menor a la hora de término.


