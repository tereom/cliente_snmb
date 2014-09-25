# -*- coding: utf-8 -*-
def index():

    #Obteniendo los registros en la tabla de Archivo_camara
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
            "' alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>"+\
            "<hr/><div><label for='tabla_hay_individuo' style='float:left;padding-right:20px;'>Hay individuo</label>"+\
            "<input type='checkbox' name='hay_individuo' value='on' id='tabla_hay_individuo'"

#         <form id='forma_shadow'>
#           <input type='hidden' name='id_foto' value='datosFoto.id'/>
#           <img src='/cliente/8_revision/download/datosFoto.archivo'/>
#           <hr/>
#           <div>
#               <label for='tabla_hay_individuo'>Hay individuo</label>
#               <input type='checkbox' name='hay_individuo' value='on' id='tabla_hay_individuo' checked='true'/>
#           </div>
#           <br/>
#           <input type='button' value='Enviar' id='tabla_enviar'/>
#         </form>

        if datosFoto.presencia:

            revisionHTML += "checked='true'"
        
        revisionHTML += "/></div><br/><input type='button' value='Enviar' id='tabla_enviar'/></form>"

    except:

        revisionHTML = "<form id='forma_shadow'></form>"
    
    return XML(revisionHTML)

def actualizarFotografia():

    #Utilizando los datos enviados de la forma_shadow, se actualiza el registro
    #de una foto en la base de datos.

    fotoElegidaID = request.vars.id_foto
    hay_individuo = request.vars.hay_individuo

    if not(hay_individuo):
        hay_individuo = False

    db(db.Archivo_camara.id==fotoElegidaID).update(presencia=hay_individuo)

def download():
    return response.download(request, db)