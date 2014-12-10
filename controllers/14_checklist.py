# coding: utf8
def index():

    ##########Enviando la información de las dropdowns##########################

    #Regresando los nombres de todos los conglomerados insertados en la tabla de
    #conglomerado junto con sus id's para llenar la combobox de conglomerado.

    listaConglomerado = db(db.Conglomerado_muestra).select(
        db.Conglomerado_muestra.id, db.Conglomerado_muestra.nombre)

    return dict(listaConglomerado=listaConglomerado)

#Haciendo queries para ver si ya se llenaron las pestañas del cliente:

def datosCamara():

    # El campo sitio_muestra_id es únicamente auxiliar y se utiliza para buscar
    # la cámara asociada a un sitio (mediante AJAX).

    conglomeradoElegidoID = request.vars.conglomerado_muestra_id

    #Obteniendo los sitios que existen en dicho conglomerado
    sitiosAsignados = db(
        (db.Sitio_muestra.conglomerado_muestra_id==conglomeradoElegidoID)&\
        (db.Sitio_muestra.existe==True)&\
        (db.Sitio_muestra.sitio_numero!='Punto de control')
        ).select(db.Sitio_muestra.sitio_numero,db.Sitio_muestra.id)

    id_camara = 0;

    for sitio in sitiosAsignados:
        if db(db.Camara.sitio_muestra_id==sitio.id).count() > 0:
            id_camara = db(db.Camara.sitio_muestra_id==sitio.id).select().first().id
            break

    return(id_camara)

# def archivosCamara():





#     #Obteniendo las cámaras que han sido declaradas en dicho sitio

#     camarasAsignadas = db(db.Camara.sitio_muestra_id==\
#         sitioElegidoID).select(db.Camara.id, db.Camara.nombre)

#     camara = camarasAsignadas.first()

#     #Bajo el supuesto que sólo existe una cámara por sitio, no se requiere hacer dropdowns:

#     respuestaHTML = "<p>Cámara localizada: </p>"

#     if len(camarasAsignadas)==0:

#         respuestaHTML += "<p>No se encontró ninguna cámara declarada en el sitio elegido</p>"

#         respuestaHTML += "<input type='hidden' name='camara_id' "+\
#             "id='tabla_camara_id' value=''/>"

#     else:

#         respuestaHTML += "<p>" + str(camara.nombre) +"</p>"

#         respuestaHTML += "<input type='hidden' name='camara_id' "+\
#             "id='tabla_camara_id' value='" + str(camara.id)+ "'/>"

#     return XML(respuestaHTML)