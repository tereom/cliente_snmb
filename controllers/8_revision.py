# -*- coding: utf-8 -*-
def index():

	fotosCamara = db(db.Archivo_camara).select()
	return dict(fotosCamara=fotosCamara)

def obtenerFotografia():

	#Obteniendo la información del conglomerado que seleccionó el usuario:
    fotoElegidaID = request.vars.foto

    #Obteniendo la información de dicha foto
    datosFoto = db(db.Archivo_camara.id==fotoElegidaID).select().first()

    #Creando la pantalla de revisión de fotografía:

    revisionHTML = "<form id='forma'><input type='hidden' name='id_foto' value='" +\
    	str(datosFoto.id) + "'/><img source='"+datosFoto.archivo+\
    	"'/><input type='checkbox' name='presencia' value='on' "

    if datosFoto.presencia:

    	revisionHTML += "checked='true'"
    
    revisionHTML += "/><button id='enviar'>Enviar</button></form>"
    
    return XML(revisionHTML)

def actualizarFotografia():

	fotoElegidaID = request.vars.id_foto

	if not(presencia):
		presencia = False

	db(db.Archivo_camara.id==fotoElegidaID).update(presencia=presencia)
