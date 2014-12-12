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
                str(datosFoto.id) + "'/><center>"

        #Revisando la terminación del archivo para ver si desplegar una imagen
        #o un video:

        #nombre = datosFoto.archivo_nombre_original.split('.')
        #terminacion = nombre[1].lower()

        #Revisando la terminación del archivo:

        #if terminacion == 'avi':

            #revisionHTML += "<video src='/init/8_revision/download/"+datosFoto.archivo+\
            #    "' controls='controls' autoplay='autoplay' style='width:800px;height:600px;'/>"

            #revisionHTML += "<object id='MediaPlayer1' CLASSID='CLSID:22d6f312-b0f6-11d0-94ab-0080c74c7e95' "+\
                #"codebase='http://activex.microsoft.com/activex/controls/mplayer/en/nsmp2inf.cab#Version=5,1,52,701' "+\
                #"standby='Loading Microsoft Windows® Media Player components...' type='application/x-oleobject' width='280' height='256'>"+\
                #"<param name='fileName' value='/cliente_web2py/08_revision/download/"+datosFoto.archivo+"'>"+\
                #"<param name='animationatStart' value='true'>"+\
                #"<param name='transparentatStart' value='true'>"+\
                #"<param name='autoStart' value='true'>"+\
                #"<param name='showControls' value='true'>"+\
                #"<param name='Volume' value='-450'>"+\
                #"<embed type='application/x-mplayer2' pluginspage='http://www.microsoft.com/Windows/MediaPlayer/' "+\
                #"src='/cliente_web2py/08_revision/download/"+\
                #datosFoto.archivo+"' name='MediaPlayer1' width=280 height=256 autostart=1 showcontrols=1 volume=-450>"+\
                #"</object>"

        #else:

        revisionHTML += "<img src='/init/08_revision/download/"+datosFoto.archivo+\
            "' alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>"

        revisionHTML +="</center><hr/><div><div style='float:left;padding-right:60px;'><label "+\
                "for='tabla_con_fauna_evidente' style='float:left;padding-right:20px;'>"+\
                "Con fauna evidente</label><input type='radio' name='fauna_evidente' "+\
                "value='encontrada' id='tabla_con_fauna_evidente'"

        #Si el campo de presencia de la foto elegida es True, entonces la casilla "fauna evidente" aparece marcada.

        if datosFoto.presencia:

            revisionHTML += " checked='true'/>"

        else:

            revisionHTML += "/>"

        revisionHTML += "</div><div style='float:left;'><label for='tabla_sin_fauna_evidente' "+\
            "style='float:left;padding-right:20px;'>Sin fauna evidente</label><input type='radio' "+\
            "name='fauna_evidente' value='no_encontrada' id='tabla_sin_fauna_evidente'"
        
        #Si el campo de presencia de la foto elegida es False, entonces la casilla "Sin fauna evidente" aparece marcada.
        #Hay que revisar que sea igual a false, porque podría ser None.
        if datosFoto.presencia==False:

            revisionHTML += " checked='true'/>"

        else:

            revisionHTML += "/>"

        revisionHTML += "</div></div><div style='clear:both;'></div>"+\
            "<!--Para el fade-in/out: <div id='info_fauna'>--><br/><div>"+\
            "<label for='tabla_nombre_comun' style='float:left;padding-right:49px;'>"+\
            "Nombre común:</label><input type='text' name='nombre_comun' class='string' "+\
            "id='tabla_nombre_comun' value='"

        #Si hay nombre común, éste aparece en la casilla para ingresar el texto.
        if datosFoto.nombre_comun:

            revisionHTML += datosFoto.nombre_comun

        revisionHTML += "'/></div><br/><div><label for='tabla_nombre_cientifico' "+\
            "style='float:left;padding-right:37px;'>Nombre científico:</label>"+\
            "<input type='text' name='nombre_cientifico' class='string' id='tabla_nombre_cientifico' value='"

        #Si hay nombre científico, éste aparece en la casilla para ingresar el texto.
        if datosFoto.nombre_cientifico:

            revisionHTML += datosFoto.nombre_cientifico

        revisionHTML += "'/></div><br/><div><label for='tabla_numero_individuos' "+\
        "style='float:left;padding-right:10px;'>Número de individuos:</label>"+\
        "<input type='text' name='numero_individuos' class='integer' id='tabla_numero_individuos' value='"

        if datosFoto.numero_individuos:

            revisionHTML += str(datosFoto.numero_individuos)

        revisionHTML += "'/></div><!--</div>--><br/><input type='button' value='Enviar' id='tabla_enviar'/></form>"

#HTML generado:

#         <form id='forma_shadow'>
#           <input type='hidden' name='id_foto' value='datosFoto.id'/>
#           <img src='/cliente/8_revision/download/datosFoto.archivo'
#            alt='Error al cargar la fotografía' style='width:800px;height:600px;'/>
#           <hr/>
#           <div>
#               <div style='float:left;padding-right:60px;'>
#                   <label for='tabla_con_fauna_evidente' style='float:left;padding-right:20px;'>
#                       Con fauna evidente
#                   </label>
#                   <input type='radio' name='fauna_evidente' value='encontrada' id='tabla_con_fauna_evidente'
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
#               <label for='tabla_nombre_comun' style='float:left;padding-right:22px;'>
#                   Nombre común:
#               </label>
#               <input type='text' name='nombre_comun' class='string' id='tabla_nombre_comun' value=''/>
#           </div>
#           <br/>
#           <div>
#               <label for='tabla_nombre_cientifico' style='float:left;padding-right:10px;'>
#                   Nombre científico:
#               </label>
#               <input type='text' name='nombre_cientifico' class='string' id='tabla_nombre_cientifico' value=''/>
#           </div>
#           <br/>
#           <div>
#               <label for='tabla_numero_individuos' style='float:left;padding-right:10px;'>
#                   Número de individuos:
#               </label>
#               <input type='text' name='numero_individuos' class='integer' id='tabla_numero_individuos' value=''/>
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
    nombreComun = request.vars.nombre_comun
    nombreCientifico = request.vars.nombre_cientifico
    numeroIndividuos = request.vars.numero_individuos

    #Viendo si se encontró fauna evidente, no se encontró o la foto simplemente no fue revisada.
    if faunaEvidente == 'encontrada':
        db(db.Archivo_camara.id==fotoElegidaID).update(presencia=True,\
        nombre_comun=nombreComun, nombre_cientifico=nombreCientifico, numero_individuos=numeroIndividuos)

    else:
        db(db.Archivo_camara.id==fotoElegidaID).update(presencia=False,\
        nombre_comun=None, nombre_cientifico=None, numero_individuos=None)

def download():
    return response.download(request, db)
