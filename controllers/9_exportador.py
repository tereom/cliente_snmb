# -*- coding: utf-8 -*-
# intente algo como
def index():

#Forma para que el usuario introduzca el nombre del archivo a exportar.

    Campos_forma = [
        INPUT(_name='nombre_archivo',_type='string',requires=IS_ALPHANUMERIC()),
    ]

    forma = FORM(*Campos_forma)

    if forma.accepts(request.vars,formname='formaHTML'):
        
        #Asignando el nombre al archivo CSV que contendrá la base de datos
        nombreCSV = "exportacion_" + forma.vars['nombre_archivo'] + ".csv"
        
        #Generando el archivo
        db.export_to_csv_file(open(nombreCSV,'w'))

        response.flash = 'Éxito'

    elif forma.errors:

        response.flash = 'Por favor, verifique que el nombre ingresado sea alfanumérico'

    else:

        response.flash = 'Por favor, ingrese un nombre alfanumérico para el archivo'

    return dict()
