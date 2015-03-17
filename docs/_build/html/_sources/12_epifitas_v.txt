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



##### 

Notas adicionales
=================

Ajax 

1. Web2py. Este ajax funciona con .change porque cuando se selecciona Estado se llena mediante ajax la combobox de municipios.

    //AJAX para llenar la combobox con los municipios asociados al estado elegido
    $('#tabla_estado').change
    (
        function()
        {
            $('#tabla_municipio').remove();

            //ajax es una función de Web2py que simplifica la función homónima de JQuery
            //recibe el URL destino, los nombres de los campos que se enviarán y el ID
            // del elemento donde se insertará la respuesta
            ajax("{{=URL('asignarMunicipios')}}", ['estado'], 'shadow_clone');
        }
    )

2. Ajax que valida un campo generado a la hora de cargar la página.

    //AJAX para advertir al usuario que un conglomerado ya ha sido asignado con anterioridad


    $('#tabla_nombre').keyup
    (
        function()
        {
            $.ajax
            (
                {
                    type: "POST",
                    data: $('#tabla_nombre').serialize(),
                    url: "{{=URL('conglomeradoExistente')}}",
                    success: function(resultado)
                    {
                        //alert(resultado);
                        if(resultado>=1)
                        {
                            alert('Este conglomerado ya ha sido declarado');
                            $('#tabla_nombre').val("");
                        }
                        else if(resultado==-1)
                        {
                            alert('El número de conglomerado consta de 6 dígitos. Ejemplo: 012345 (para conglomerados del INFyS) ó 123456 para conglomerados que no son del INFyS');
                            $('#tabla_nombre').val("");
                        }
                    }
                }
            );
        }
    );

3. Porque algunas veces se necesitan dos clases.
Ajax que valida un campo generado mediante Ajax. En el ejemplo de epífitas (código de abajo), el campo generado es *Sitio*, después se utiliza Ajax para validarlo; sin embargo, los campos generados por Ajax no están considerados en el DOM (Document Object Model) por lo que la validación tiene que apuntar al objeto más cercano considerado en el DOM. Es por esto que, a diferencia del punto anterior, se utilizan dos clases en la validación: *shadow_clone* y *tabla_sitio_muestra_id*.

    $('#shadow_clone').on('change','#tabla_sitio_muestra_id',function (){
        $.ajax
        (
        {
            type: "POST",
            data: $('#tabla_sitio_muestra_id').serialize(),
            url: "{{=URL('informacionEpifitasExistente')}}",
                success: function(resultado)
                {
                    //alert(resultado);
                    if(resultado>0)
                    {
                        alert('La información de epífitas ya ha sido insertada para el sitio seleccionado');
                        $('#tabla_sitio_muestra_id').val("");
                    }
                }
            }
            );
        }
        );