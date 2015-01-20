Conglomerado
=============

La carpeta de vistas asociada a conglomerado sólo consta de un archivo (index.html).

Index
-----

A continuación describimos las clases utilizadas en el archivo *index.html*, así como los identificadores asociados al código JavaScript.


Clases
^^^^^^

* **No_GPS**, **GPS**, **Centrar**. **FlotaIzquierda se utilizan para dar distinto estilo a las celdas relativas a GPS.

* **integer, date, time, string, double, generic-widget** son clases de Web2py, y se utilizan para validación automática en la vista (por ejemplo, para evitar que se introduza un string en un campo de enteros). En particular, la clase *date* permite visualizar el calendario para seleccionar la fecha.

* **obligatorio** sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.

* **Vegetacion, Sitio_info_2, Sitio_info_3, Sitio_info_4** son clases que sirven para las acciones fade-in/fade-out, esto es, controlan que ciertos campos se desvanezan o aparezcan de acuerdo a la información ingresada. También sirven para validar los campos correspondientes.

Identificadores
^^^^^^^^^^^^^^^

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **shadow_clone** sirve para indicar el contenedor (<div></div>) donde se guardará el menú desplegable de municipios, las opciones de este menú dependen del *Estado* seleccionado en el campo anterior, por lo que se utiliza AJAX para generar el menú. Nota: el AJAX que se utiliza es una implementación simplificada de Web2py, que es conveniente cuando el resultado de la función invocada por AJAX se escribe directamente en el contenedor.

* **tabla_nombre** es el id correspondiente al campo *Conglomerado*, se utiliza para validar dos aspectos: 1) si el número de conglomerado que se escribió ya está registrado en la base de datos, y 2) para rechazar números de conglomerados con más de 6 dígitos. Para lograr estó se utiliza AJAX, sin embargo, no es posible utilizar el AJAX de Web2py ya que el objetivo es validación (en contraste con el caso de *shadow_clone* donde se requiere imprimir un menú en pantalla).

Validaciones
^^^^^^^^^^^^

Hay dos tipos de validación, la primera (validación al momento) se lleva a cabo conforme el usuario captura la información y la segunda se lleva a cabo cuando se envía la forma.

1. Al momento. 
	+ Los rangos de los valores de variables que provienen del GPS: *latitud*, longitud, datum, altitud* y *error*. 
	+ Número de conglomerado (id *tabla_nombre* descrito arriba), se valida que conste de no más de 6 dígitos y no exista previamente en la base de datos.


2. Al enviar. 
	+ La clase *obligatorio*, todos los campos con esta clase deben tener información.
	+ El campo *municipio*, que no esté vacío.
	+ Los campos adicionales (*Vegetacion* y *tabla_perturbado*), en caso de que se seleccione la opción de *Vegetación* en *Tipo de uso de suelo* (id *tabla_uso_suelo_tipo*), se valida que los campos tengan información.
	+ Los campos asociados a cada sitio. En caso de que se haya marcado que el sitio existe (ids *tabla_existe_2*, *tabla_existe_3*, *tabla_existe_4*) el usuario debe ingresar todos los campos del renglón correspondiente, para esta validación se usan las clases *Sitio_info_2*, *Sitio_info_3* y *Sitio_info_4* respectivamente.
	+ Número de conglomerado (id *tabla_nombre* descrito), se valida que conste de exactamente 6 dígitos.
	+ La clase *date*, se usa para validar que la fecha esté en el formato correcto (aaaa-mm-dd), y si lo cumple se valida también que los rangos de día, mes y año sean válidos.