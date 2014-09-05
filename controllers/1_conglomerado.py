# coding: utf8

########################################
# import os
# controllers_dir = os.path.dirname(os.path.dirname(__file__))
# path = os.path.join(controllers_dir, 'imagenes')
# 
# ## Las siguientes dos funciones son para descargar las imágenes
# def descargar(): return response.download(request,db)
# def link(): return response.download(request,db,attachment=False)
########################################

#def procesamientoConglomerado(congForm):
    #if not congForm.vars.uso_suelo_tipo=='12':
        #congForm.vars.vegetacion_tipo = "0"

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)


#def validacionesSitio(sitioForm):
    #Si el sitio existe, entonces todos los campos deben ser validados.
    
    #Si uso_suelo_tipo no es 'Vegetación', entonces perturbado=None y vegetacion_tipo=No aplica
    #if not congForm.vars.uso_suelo_tipo==T('Vegetación'):
        #congForm.vars.vegetacion_tipo=0
        #congForm.vars.perturbado=None
    #response.flash = sitio1Form.vars.existe

    #Si uso_suelo_tipo es 'Vegetación', entonces la validación se realiza automáticamente 
    #porque en el campo vegetacion_tipo sólo se pueden incluir
    #tipos que están en el catálogo correspondiente. 
    #Además, la combobox siempre debe tener una opción seleccionada.

def index():

    
# Se define el formulario a partir de una única tabla virtual ya que necesitamos un único
#botón submit para las formas.

	Campos_pestana_1= [

		###############################
		#Campos del conglomerado
		###############################

#Hay que ver si es necesario el campo de reference

		Field('nombre','integer',label=T("Número de conglomerado"),
			requires=IS_NOT_EMPTY()),
		Field('fecha_visita', 'date',label=T("Fecha de visita"),
			requires=IS_NOT_EMPTY()),
		Field('tipo',label=T("Tipo de conglomerado"),
			requires=IS_IN_DB(db,db.Cat_tipo_conglomerado.id,'%(nombre)s')),
    	Field('estado',label=T("Estado"),
    		requires=IS_IN_DB(db,db.Cat_estado_conglomerado.id,'%(nombre)s')),
    	Field('municipio','integer',label=T("Clave del municipio"),
    		requires=IS_NOT_EMPTY()),
    	Field('predio','string',label=T("Predio"),
    		requires=IS_NOT_EMPTY()),
    	Field('tenencia', label=T("Tenencia"),
    		requires=IS_IN_DB(db,db.Cat_tenencia_conglomerado.id,'%(nombre)s')),
    	Field('uso_suelo_tipo',label=T("Tipo de uso de suelo"),
    		requires=IS_IN_DB(db,db.Cat_suelo_conglomerado.id,'%(nombre)s')),
		Field('vegetacion_tipo', label=T("Tipo de vegetación"),
			requires=IS_IN_DB(db(db.Cat_vegetacion_conglomerado.nombre!='No aplica'),
			db.Cat_vegetacion_conglomerado.id,'%(nombre)s')),
    	Field('perturbado','boolean',label=T("Perturbado")),
		Field('comentario','text',label=T("Observaciones")),

		################################
		#Campos del sitio 1
		###############################

		##Los campos sombreados se encuentran en las tablas pero no se preguntarán al usuario

		#Field('conglomerado_muestra_id','reference Conglomerado_muestra', required='TRUE'),
		#Field('sitio_numero', 'reference Cat_numero_sitio', label=T("Número de sitio"), required='TRUE'),
		#Field('existe', 'boolean', label=T("existe)", required='TRUE'),
		# El centro del conglomerado y el punto de control siempre existen.
		
    	Field('lat_grado_1','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
		Field('lat_min_1','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
		Field('lat_seg_1','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
		Field('lon_grado_1','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
		Field('lon_min_1','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
		Field('lon_seg_1','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
    	Field('altitud_1','double',label=T("Altitud(m)"), requires=IS_NOT_EMPTY()),
    	Field('gps_error_1','double',label=T("Error(m)"), requires=IS_NOT_EMPTY()),
		Field('elipsoide_1',label=T("Datum"),
			requires=IS_IN_DB(db(db.Cat_elipsoide_sitio.nombre!='No aplica'),
        	db.Cat_elipsoide_sitio.id,'%(nombre)s')),
    	Field('evidencia_1', 'boolean',label=XML("Evidencia <br/> anterior")),
    	
#     	###########Imagen############
# 		Field('archivo_nombre_original_1', 'upload', label=T("Fotografía")),
# 	
# 		##La validación de la imagen obligatoria se realizará directo en la vista, debido a 
# 		##que no es muy cómodo incluir una imagen default si el sitio no existe, y luego borrarla
# 		##en el controlador.
# 	
# 		###############################
# 		#Campos del sitio 2
# 		###############################
# 		
# 		##Los campos condicionales a existe se definirán como obligatorios, sin embargo, si el
# 		##sitio no existe, se esconderán y se les asignará un valor arbitrario para que pasen
# 		##la validación de la forma. Posteriormente aquí en el controlador se borrarán dichos valores.
# 		##Esto porque en Web2py no es sencillo definir:
# 		##	"si este campo está marcado, entonces este otro es obligatorio, si no, ni aparece".
# 	
# 		Field('existe_2', 'boolean',label=T("Existe")),
# 		Field('lat_grado_2','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lat_min_2','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lat_seg_2','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
# 		Field('lon_grado_2','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lon_min_2','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lon_seg_2','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
#     	Field('altitud_2','double',label=T("Altitud(m)"), requires=IS_NOT_EMPTY()),
#     	Field('gps_error_2','double',label=T("Error(m)"), requires=IS_NOT_EMPTY()),
# 		Field('elipsoide_2', label=T("Datum"),
# 			requires=IS_IN_DB(db(db.Cat_elipsoide_sitio.nombre!='No aplica'),
#         	db.Cat_elipsoide_sitio.id,'%(nombre)s')),
#     	Field('evidencia_2', 'boolean',label=XML("Evidencia <br/> anterior")),
#     	
#     	###########Imagen############
# 		Field('archivo_nombre_original_2', 'upload', label=T("Fotografía")),
# 
# 		###############################
# 		#Campos del sitio 3
# 		###############################
# 	
# 		Field('existe_3', 'boolean',label=T("Existe")),
# 		Field('lat_grado_3','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lat_min_3','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lat_seg_3','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
# 		Field('lon_grado_3','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lon_min_3','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lon_seg_3','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
#     	Field('altitud_3','double',label=T("Altitud(m)"), requires=IS_NOT_EMPTY()),
#     	Field('gps_error_3','double',label=T("Error(m)"), requires=IS_NOT_EMPTY()),
# 		Field('elipsoide_3', label=T("Datum"),
# 			requires=IS_IN_DB(db(db.Cat_elipsoide_sitio.nombre!='No aplica'),
#         	db.Cat_elipsoide_sitio.id,'%(nombre)s')),
#     	Field('evidencia_3', 'boolean',label=XML("Evidencia <br/> anterior")),
#     	
#     	###########Imagen############
# 		Field('archivo_nombre_original_3', 'upload', label=T("Fotografía")),
# 
# 		###############################
# 		#Campos del sitio 4
# 		###############################
# 	
# 		Field('existe_4', 'boolean',label=T("Existe")),
# 		Field('lat_grado_4','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lat_min_4','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lat_seg_4','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
# 		Field('lon_grado_4','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lon_min_4','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lon_seg_4','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
#     	Field('altitud_4','double',label=T("Altitud(m)"), requires=IS_NOT_EMPTY()),
#     	Field('gps_error_4','double',label=T("Error(m)"), requires=IS_NOT_EMPTY()),
# 		Field('elipsoide_4', label=T("Datum"),
# 			requires=IS_IN_DB(db(db.Cat_elipsoide_sitio.nombre!='No aplica'),
#         	db.Cat_elipsoide_sitio.id,'%(nombre)s')),
#     	Field('evidencia_4', 'boolean',label=XML("Evidencia <br/> anterior")),
#     	
#     	###########Imagen############
# 		Field('archivo_nombre_original_4', 'upload', label=T("Fotografía")),
# 
# 		###############################
# 		#Campos del punto de control
# 		###############################
# 
# 		Field('lat_grado_c','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lat_min_c','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lat_seg_c','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
# 		Field('lon_grado_c','integer',label=T("grado"), requires=IS_NOT_EMPTY()),
# 		Field('lon_min_c','integer',label=T("minuto"), requires=IS_NOT_EMPTY()),
# 		Field('lon_seg_c','double',label=T("segundo"), requires=IS_NOT_EMPTY()),
#     	Field('altitud_c','double',label=T("Altitud(m)"), requires=IS_NOT_EMPTY()),
#     	Field('gps_error_c','double',label=T("Error(m)"), requires=IS_NOT_EMPTY()),
# 		Field('elipsoide_c', label=T("Datum"),
# 			requires=IS_IN_DB(db(db.Cat_elipsoide_sitio.nombre!='No aplica'),
#         	db.Cat_elipsoide_sitio.id,'%(nombre)s')),
#     	Field('evidencia_c', 'boolean',label=XML("Evidencia <br/> anterior")),
#     	
#     	###########Imagen############
#     	Field('archivo_nombre_original_c', 'upload', label=T("Fotografía")),
# 

	##Cerrando la lista de campos para el formulario
	]

	forma=SQLFORM.factory(*Campos_pestana_1)

###############################+
	#CSS
        #table_name ='Conglomerado_muestra', _id='forma_conglomerado')
        #_id='forma_sitio1',table_name='Conjunta_sitio_imagen_4'
###############################

#########IMAGENES################# 
#     ### Cargar imágenes
#     imagenForm = FORM(
#         INPUT(_name='imagen_nombre',_type='text',required=True),
#         INPUT(_name='imagen_archivo',_type='file')
#     )
# 
#     if imagenForm.accepts(request.vars,formname='imagenForm'):
#         imagen = db.Imagen_referencia_sitio.archivo_nombre_original.store(
#             imagenForm.vars.imagen_archivo.file,imagenForm.vars.imagen_archivo.filename)
#         id = db.Imagen_referencia_sitio.insert(
#				archivo_nombre_original=imagen,archivo_nombre=imagenForm.vars.imagen_nombre)
# 
#     imagenes = db().select(db.Imagen_referencia_sitio.ALL)
#################################

	if forma.validate():
	
		##################Procesando los datos del conglomerado######################
		
		formaConglomerado=db.Conglomerado_muestra._filter_fields(forma.vars)
		ID_suelo_vegetacion = db(db.Cat_suelo_conglomerado.nombre=='Vegetación').select().first().id
  		
        #Casteando para asegurarnos que la comparación sea entre enteros.
		if int(formaConglomerado['uso_suelo_tipo'])!=int(ID_suelo_vegetacion):
		
		#Si el uso de suelo no es vegetación, el campo de 'perturbado' se anula y el campo de
		#'vegetacion_tipo' toma el ID de "no aplica".
			formaConglomerado['perturbado']=None
			
			ID_vegetacion_no_aplica = db(db.Cat_vegetacion_conglomerado.nombre=='No aplica').select().first().id
			formaConglomerado['vegetacion_tipo']=ID_vegetacion_no_aplica
			
		#Insertando en la base de datos:
		conglomeradoInsertado = db.Conglomerado_muestra.insert(**formaConglomerado)
		
		################Procesando los datos del sitio 1##############################

		#Agregando los datos que no se pidieron al usuario:
		formaSitio1 = {}
		formaSitio1['conglomerado_muestra_id']=conglomeradoInsertado
		formaSitio1['sitio_numero']=1
		formaSitio1['existe']=True
		
		#Leyendo los datos del formulario:
		formaSitio1['lat_grado']=forma.vars['lat_grado_1']
		formaSitio1['lat_min']=forma.vars['lat_min_1']
		formaSitio1['lat_seg']=forma.vars['lat_seg_1']
		formaSitio1['lon_grado']=forma.vars['lon_grado_1']
		formaSitio1['lon_min']=forma.vars['lon_min_1']
		formaSitio1['lon_seg']=forma.vars['lon_seg_1']
		formaSitio1['altitud']=forma.vars['altitud_1']
		formaSitio1['gps_error']=forma.vars['gps_error_1']
		formaSitio1['elipsoide']=forma.vars['elipsoide_1']
		formaSitio1['evidencia']=forma.vars['evidencia_1']
		
		#Insertando en la base de datos:
		db.Sitio_muestra.insert(**formaSitio1)

		
        #    variables['perturbado']=None
        #    variables['vegetacion_tipo']=opcion_vegetacion.id
        # elif opcion_suelo.id<variables['uso_suelo_tipo']:
        #     variables['perturbado']=None
        #     variables['vegetacion_tipo']=opcion_vegetacion.id
        #else:
        #    variables['vegetacion_tipo']=congForm.vars.vegetacion_tipo_aux
        #db.Conglomerado_muestra.insert(**variables)
        #response.flash = "Registro ingresado exitosamente"

	return dict(forma=forma)
