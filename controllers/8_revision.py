# -*- coding: utf-8 -*-
def index():

    fotosCamara = db(db.Archivo_camara).select()
    return dict(fotosCamara=fotosCamara)

def obtenerFotografia():

    #Obteniendo la información del conglomerado que seleccionó el usuario:
    fotoElegidaID = request.vars.foto

    #Obteniendo la información de dicha foto
    datosFoto = db(db.Archivo_camara.id==fotoElegidaID).select().first()

    #Creando la pantalla de revisión de fotografía, considerando el caso en el
    #que se seleccione la opción vacía:

    try:

        revisionHTML = "<form id='forma_shadow'><input type='hidden' name='id_foto' value='" +\
            str(datosFoto.id) + "'/><img src='/cliente/8_revision/download/"+datosFoto.archivo+\
            "' alt='Error al cargar la fotografía' style='width:304px;height:228px'/>"+\
            "<br/><div><label for='tabla_hay_individuo' style='float:left;'>Hay individuo</label>"+\
            "<input type='checkbox' name='hay_individuo' value='on' id='tabla_hay_individuo'"

        if datosFoto.presencia:

            revisionHTML += "checked='true'"
        
        revisionHTML += "/></div><input type='button' value='Enviar' id='tabla_enviar'/></form>"

    except:

        revisionHTML = "<form id='forma_shadow'></form>"
    
    return XML(revisionHTML)

def actualizarFotografia():

    fotoElegidaID = request.vars.id_foto
    hay_individuo = request.vars.hay_individuo

    if not(hay_individuo):
        hay_individuo = False

    db(db.Archivo_camara.id==fotoElegidaID).update(presencia=hay_individuo)

def download():
    return response.download(request, db)