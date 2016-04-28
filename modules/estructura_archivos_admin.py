# coding: utf8

## Este módulo implementa funciones para trabajar con las carpetas que
## contendrán los archivos de la fototrampa y grabadora correspondientes
## a un muestreo de conglomerado (nombre del cgl + fecha de visita):

# cliente_snmb_windows/mac_v5
# ├───web2py
# ├───conglomerados
# |   ├───nombre_aaaa-mm-dd
# |   |   ├───c
# |   |   ├───ga
# |   |   ├───gu

import os

def crearRutaCarpeta(nombre, fecha_visita):

	## Esta función crea la ruta de la carpeta "nombre_aaaa-mm-dd", relativa a
	## la carpeta Resources de la aplicación de Web2py para Mac, o a la carpeta
	## Web2py de la aplicación para Windows.

	## Tanto su input como su output son strings.

	dirActual = os.getcwd()

	########### Para Windows ###########
	#dirDestino = os.path.normpath(dirActual + os.sep + os.pardir)

	############ Para Mac ###########
	dirDestino = os.path.normpath(dirActual +\
		os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)

	# Asegurándonos que el nombre no tenga ceros a la izquierda, por ejemplo:
	# no queremos que sea: "000123", sino simplemente "123".

	nombre = str(int(nombre))

	nombreDirCglMuestra = nombre + '_' + fecha_visita

	rutaDirConglomeradoMuestra = os.path.join(dirDestino, 'conglomerados',
		nombreDirCglMuestra)

	return(rutaDirConglomeradoMuestra)

def crearEstructuraCarpetas(nombre, fecha_visita):

	## Esta función crea la estructura de carpetas especificada anteriormente,
	## para ello, primero genera la ruta relativa a la carpeta "nombre_aaaa-mm-dd"

	## Sus inputs son strings.

	rutaDirConglomeradoMuestra = crearRutaCarpeta(nombre, fecha_visita)

	if not os.path.exists(rutaDirConglomeradoMuestra):
		os.makedirs(rutaDirConglomeradoMuestra)
		os.makedirs(os.path.join(rutaDirConglomeradoMuestra,'c'))
		os.makedirs(os.path.join(rutaDirConglomeradoMuestra,'g_a'))
		os.makedirs(os.path.join(rutaDirConglomeradoMuestra,'g_u'))


