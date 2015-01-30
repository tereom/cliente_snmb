Grabadora
=========

La carpeta de vistas asociada a grabadora consta de 2 archivos, index1.html e index2.html.

Index1
------

A continuación describimos las clases e identificadores asociados al código JavaScript del archivo *index1.html*.

Clases
^^^^^^

* **No_GPS**, **GPS**, **Centrar** y **Enviar** se utilizan para dar distinto estilo a las celdas relativas a GPS.

* **integer, date, time, string, double, generic-widget** son clases de Web2py, y se utilizan para validación automática en la vista (por ejemplo, para evitar que se introduza un string en un campo de enteros). En particular, la clase *date* permite visualizar el calendario para seleccionar la fecha.

* **obligatorio** sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.

Identificadores
^^^^^^^^^^^^^^^

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **shadow_clone**, que consta de dos funcionalidades:

	1. Sirve para indicar el contenedor (<div></div>) donde se guardará el menú desplegable de sitios (buscados en la base de datos al seleccionar un conglomerado). Nota: el AJAX que se utiliza es una implementación simplificada de Web2py, que es conveniente cuando el resultado de la función invocada por AJAX se escribe directamente en el contenedor.

	2. Se utiliza para validar que no exista una grabadora en la base de datos asociada al conglomerado y sitio elegidos de los menús desplegables, es decir, para validar que sea declarada a lo más una grabadora en cada sitio de cada conglomerado. Para lograr estó se utiliza AJAX, sin embargo, en este caso no es posible utilizar el AJAX de Web2py ya que el objetivo es validación (más que impresión en pantalla de un menú).


Validaciones
^^^^^^^^^^^^

Hay dos tipos de validación, la primera (validación al momento) se lleva a cabo conforme el usuario captura la información y la segunda se lleva a cabo cuando se envía la forma.

1. Al momento. 

	+ Los rangos de los valores de variables que provienen del GPS: *latitud, longitud, datum, altitud* y *error*. 


2. Al enviar. 

	+ La clase *obligatorio*, todos los campos con esta clase deben tener información.

	+ El campo *sitio*, que no esté vacío.

	+ La clase *date* se usa para validar que la fecha esté en el formato correcto (aaaa-mm-dd), y si lo cumple se valida también que los rangos de día, mes y año sean válidos, para esto se utilizan los identificadores *tabla_fecha_inicio* y *tabla_fecha_termino*. Adicionalmente se valida que la fecha y hora de inicio sea menor que la fecha y hora de término, se utilizan los identificadores *tabla_hora_inicio* y *tabla_hora_termino*.
