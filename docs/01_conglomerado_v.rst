Conglomerado
=============

Clases:

* **No_GPS** y **GPS** se utilizan para dar distinto estilo a las celdas relativas a GPS.

* **integer, date, time, string, double, generic-widget** son clases de Web2py, y se utilizan para validación automática en la vista (por ejemplo, para evitar que se introduza un string en un campo de enteros). En particular, la clase *date* permite visualizar el calendario para seleccionar la fecha.

* **obligatorio** sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.

* **Vegetación, Sitio_info_2, Sitio_info_3, Sitio_info_4** son clases que sirven para las acciones fade-in/fade-out, esto es, controlan que ciertos campos se desvanezan o aparezcan de acuerdo a la información ingresada.

Identificadores:

A continuación se describen los identificadores con funcionalidades ligadas a AJAX.

* **shadow_clone** sirve para indicar el contenedor (<div></div>) donde se guardará el menú desplegable de municipios, las opciones de este menú dependen del *Estado* seleccionado en el campo anterior, por lo que se utiliza AJAX para generar el menú. Nota: el AJAX que se utiliza es una implementación simplificada de Web2py, que es conveniente cuando el resultado de la función invocada por AJAX se escribe directamente en el contenedor.

* **tabla_nombre** es el id correspondiente al campo *Conglomerado*, se utiliza para validar dos aspectos: 1) si el número de conglomerado que se escribió ya está registrado en la base de datos, y 2) para rechazar números de conglomerados con más de 6 dígitos. Para lograr estó se utiliza AJAX, sin embargo, no es posible utilizar el AJAX de Web2py ya que el objetivo es validación (en contraste con el caso de *shadow_clone* donde se requiere imprimir un menú en pantalla).

Validaciones:

Hay dos tipos de validación, la primera se lleva a cabo conforme el usuario captura la información y la segunda se lleva a cabo cuando se envía la forma.

1. Validaciones al momento. Los rangos de los valores de variables que provienen del GPS: *latitud, longitud, datum, altitud* y *error*. También la validación de *tabla_nombre* descrita arriba.


A la hora de enviar la forma se validan los siguientes puntos:

1. La clase *obligatorio*.

2. El campo de *municipio* (que se generó mediante AJAX).

3. Los campos adicionales (Tipo de vegetación y perturbado) que aparecen si se seleccionó la opción de *Vegetación* en *Tipo de uso de suelo*.

4. Que los campos asociados a cada sitio no estén vacíos si se marcó que los sitios existen.

5. Que el nombre del conglomerado conste de exactamente 6 caracteres.

6. Que la fecha esté en el formato correcto (aaaa-mm-dd), y que los rangos de día, mes y año sean válidos.