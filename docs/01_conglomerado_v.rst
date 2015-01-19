Conglomerado
=============

El script está dividido en tres secciones:

1. CSS: estilos para tablas.

2. HTML: vista del cliente.

3. JS: javascript que implementa las validaciones y el *fade-in fade-out*de los campos.

Las clases *No_GPS* y *GPS* se utilizan para dar distinto estilo a la tabla para ingresar información de GPS.

Las clases *integer, date, string, double, generic-widget* son de Web2py, y se utilizan para validación automática en la vista (por ejemplo, para evitar que se introduza un string en un campo de enteros). En particular, la clase *date* permite visualizar el calendario para seleccionar la fecha.

La clase *shadow_clone* sirve para indicar el contenedor donde se guardará la dropdown de municipios, generada mediante AJAX.

La clase *obligatorio* sirve para indicar campos obligatorios, mismos que serán validados al enviar la forma.

Las clases *Vegetación, Sitio_info_2, Sitio_info_3, Sitio_info_4* sirven para fade-in/fade-out.

Los rangos de los valores de variables que provienen del GPS (*latitud, longitud, datum, altitud* y *error*) son validadas al momento, es decir, antes de enviar la forma. También números de conglomerado muy largos o ya ingresados son rechazados al momento.

A la hora de enviar la forma se validan los siguientes puntos:

1. La clase *obligatorio*.

2. El campo de *municipio* (que se generó mediante AJAX).

3. Los campos adicionales que aparecen si se seleccionó la opción de *Vegetación* en *Tipo de uso de suelo*.

4. Que los campos asociados a cada sitio estén completados si se marcó que los sitios existen.

5. Que el nombre del conglomerado conste de 6 caracteres (no menos).

6. Que la fecha esté en el formato correcto (aaaa-mm-dd), y si así es, los rangos de día, mes y año para la fecha.