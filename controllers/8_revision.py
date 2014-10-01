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
            str(datosFoto.id) + "'/><img src='/cliente_web2py/8_revision/download/"+datosFoto.archivo+\
            "' alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>"+\
            "<hr/><div><div style='float:left;padding-right:60px;'><label for='tabla_fauna_evidente' "+\
            "style='float:left;padding-right:20px;'>Fauna evidente</label><input type='radio' "+\
            "name='fauna_evidente' value='encontrada' id='tabla_fauna_evidente'"

#
        if datosFoto.presencia:

            revisionHTML += " checked='true'/>"

        else:

            revisionHTML += "/>"

        revisionHTML += "</div><div style='float:left;'><label for='tabla_sin_fauna_evidente' "+\
            "style='float:left;padding-right:20px;'>Sin fauna evidente</label><input type='radio' "+\
            "name='fauna_evidente' value='no_encontrada' id='tabla_sin_fauna_evidente'"
        
        #Hay que revisar que sea igual a false, porque podría ser None.
        if datosFoto.presencia==False:

            revisionHTML += " checked='true'/>"

        else:

            revisionHTML += "/>"

        revisionHTML += "</div></div><div style='clear:both;'></div><br/><div><label "+\
            "for='tabla_especie_encontrada'  style='float:left;padding-right:20px;'>Especie:</label>"+\
            "<input type='text' name='especie_encontrada' value='"

        if datosFoto.especie:

            revisionHTML += datosFoto.especie

        revisionHTML += "' id='tabla_especie_encontrada'/>"+\
            "</div><br/><input type='button' value='Enviar' id='tabla_enviar'/></form>"

#HTML generado:

#         <form id='forma_shadow'>
#           <input type='hidden' name='id_foto' value='datosFoto.id'/>
#           <img src='/cliente/8_revision/download/datosFoto.archivo'
#            alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>
#           <hr/>
#           <div>
#               <div style='float:left;padding-right:60px;'>
#                   <label for='tabla_fauna_evidente' style='float:left;padding-right:20px;'>
#                       Fauna evidente
#                   </label>
#                   <input type='radio' name='fauna_evidente' value='encontrada' id='tabla_fauna_evidente'
#                   checked='true'/>
#               </div>
#               <div style='float:left;'>
#                   <label for='tabla_sin_fauna_evidente' style='float:left;padding-right:20px;'>
#                       Sin fauna evidente
#                   </label>
#                   <input type='radio' name='fauna_evidente' value='no_encontrada' id='tabla_sin_fauna_evidente'/>
#               </div>
#           </div>
#           <div style='clear:both;'></div>
#           <br/>
#           <div>
#               <label for='tabla_especie_encontrada'  style='float:left;padding-right:20px;'>
#                   Especie:
#               </label>
#               <input type='text' name='especie_encontrada' value='' id='tabla_especie_encontrada'/>
#           </div>
#           <br/>
#           <input type='button' value='Enviar' id='tabla_enviar'/>
#         </form>

    except:

        revisionHTML = "<form id='forma_shadow'></form>"
    
    return XML(revisionHTML)

def actualizarFotografia():

    #Utilizando los datos enviados de la forma_shadow, se actualiza el registro
    #de una foto en la base de datos.

    fotoElegidaID = request.vars.id_foto
    faunaEvidente = request.vars.fauna_evidente
    especieEncontrada = request.vars.especie_encontrada

    #Viendo si se encontró fauna evidente, no se encontró o la foto simplemente no fue revisada.
    if faunaEvidente == 'encontrada':
        faunaEvidente = True
    elif faunaEvidente == 'no_encontrada':
        faunaEvidente = False
    else:
        faunaEvidente = None

    db(db.Archivo_camara.id==fotoElegidaID).update(presencia=faunaEvidente, especie=especieEncontrada)

def download():
    return response.download(request, db)