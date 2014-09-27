# coding: utf8

# def manage_users():
#     form = SQLFORM.grid(db.Huella_excreta.hay_nombre_comun==False,user_signature=False)
#     return dict(form=form)


# def admin_huella_excreta():
#     db.Huella_excreta.id.writable = False
#     db.Huella_excreta.id.readable = False
#     db.Huella_excreta.transecto_huellas_excretas_id.writable = False
#     form = SQLFORM.grid(db.Huella_excreta,user_signature=False)
#         #fields=[db.Huella_excreta.es_huella])
#     return dict(form=form)

# def admin_especies():
#     #db.Especie_invasora.id.writable = False
#     db.Especie_invasora.id.readable = False
#     db.Especie_invasora.transecto_especies_invasoras_id.writable = False
#     grid_especies = SQLFORM.grid(db.Especie_invasora,        
#         user_signature=False)
#         #fields=[db.Huella_excreta.es_huella])

#     db.Huella_excreta.id.writable = False
#     db.Huella_excreta.id.readable = False
#     db.Huella_excreta.transecto_huellas_excretas_id.writable = False
#     grid_huellas = SQLFORM.grid(db.Huella_excreta,user_signature=False)

#     return dict(form=form)

# def admin_conglomerado():
#     db.Conglomerado_muestra.id.writable = False
#     db.Conglomerado_muestra.id.readable = False
#     db.Conglomerado_muestra.estado.represent = lambda value,row: options_widget(db.Conglomerado_muestra.estado,value,**{'_name':'home_state_row_%s' % row.id})
#     form = SQLFORM.grid(db.Conglomerado_muestra,
#     	fields=[db.Conglomerado_muestra.estado],
#     	user_signature=False,
#     	selectable = lambda ids : redirect(URL('default', 'mapping_multiple', vars=dict(id=ids))))
#         #fields=[db.Huella_excreta.es_huella])
#     return dict(form=form)

# Conglomerado
db.Conglomerado_muestra.tipo.requires=IS_IN_DB(db,db.Cat_tipo_conglomerado.id,'%(nombre)s')
db.Conglomerado_muestra.estado.requires=IS_IN_DB(db,db.Cat_estado_conglomerado.id,'%(nombre)s')
db.Conglomerado_muestra.municipio.requires=IS_IN_DB(db,db.Cat_municipio_conglomerado.id,'%(nombre)s')
db.Conglomerado_muestra.tenencia.requires=IS_IN_DB(db,db.Cat_tenencia_conglomerado.id,'%(nombre)s')
db.Conglomerado_muestra.uso_suelo_tipo.requires=IS_IN_DB(db,db.Cat_suelo_conglomerado.id,'%(nombre)s')
db.Conglomerado_muestra.vegetacion_tipo.requires=IS_IN_DB(db,db.Cat_vegetacion_conglomerado.id,'%(nombre)s')

# Sitio
db.Sitio_muestra.sitio_numero.requires=IS_IN_DB(db,db.Cat_numero_sitio.id,'%(nombre)s')
db.Sitio_muestra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')

# Cámara
db.Camara.nombre.requires=IS_IN_DB(db,db.Cat_nombre_camara.id,'%(nombre)s')
db.Camara.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')
db.Camara.resolucion.requires=IS_IN_DB(db,db.Cat_resolucion_camara.id,'%(nombre)s')
db.Camara.sensibilidad.requires=IS_IN_DB(db,db.Cat_sensibilidad_camara.id,'%(nombre)s')

# Grabadora
db.Grabadora.nombre.requires=IS_IN_DB(db,db.Cat_nombre_grabadora.id,'%(nombre)s')
db.Grabadora.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide.id,'%(nombre)s')

# Especies
db.Transecto_especies_invasoras_muestra.transecto_numero.requires=IS_IN_DB(db,
    db.Cat_numero_transecto,'%(nombre)s')
db.Especie_invasora.numero_individuos.requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')

# Huellas excreta
db.Transecto_huellas_excretas_muestra.transecto_numero.requires=IS_IN_DB(db,
    db.Cat_numero_transecto,'%(nombre)s')

# Registros extra
db.Especie_invasora_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')
db.Especie_invasora_extra.numero_individuos.requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')

db.Huella_excreta_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')

db.Especimen_restos_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')
db.Especimen_restos_extra.numero_individuos.requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')

def editarConglomerado():
    db.Sitio_muestra.conglomerado_muestra_id.writable = False
    db.Imagen_referencia_sitio.sitio_muestra_id.writable = False
    form = SQLFORM.smartgrid(db.Conglomerado_muestra,
        linked_tables=['Sitio_muestra', 'Imagen_referencia_sitio'],
        user_signature=False, 
        csv=False,
        )
    return dict(form=form)
    
def editarCamara():
    db.Camara.sitio_muestra_id.writable = False
    db.Imagen_referencia_camara.camara_id.writable = False
    db.Archivo_camara.camara_id.writable = False
    form = SQLFORM.smartgrid(db.Camara,        
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarGrabadora():
    db.Grabadora.sitio_muestra_id.writable = False
    db.Imagen_referencia_grabadora.grabadora_id.writable = False
    db.Imagen_referencia_microfonos.grabadora_id.writable = False
    db.Archivo_referencia_grabadora.grabadora_id.writable = False
    db.Archivo_grabadora.grabadora_id.writable = False
    form = SQLFORM.smartgrid(db.Grabadora,
        #linked_tables=['Imagen_referencia_microfonos', 
        #    'Archivo_referencia_grabadora', 'Archivo_grabadora'],
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarEspeciesInvasoras():
    db.Transecto_especies_invasoras_muestra.conglomerado_muestra_id.writable = False
    db.Especie_invasora.transecto_especies_invasoras_id.writable = False
    db.Archivo_especie_invasora.especie_invasora_id.writable =False
    form = SQLFORM.smartgrid(db.Transecto_especies_invasoras_muestra,
        #linked_tables=['Especie_invasora'],
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarHuellasExcretas():
    db.Transecto_huellas_excretas_muestra.conglomerado_muestra_id.writable = False
    db.Huella_excreta.transecto_huellas_excretas_id.writable = False
    db.Archivo_huella_excreta.huella_excreta_id.writable =False
    form = SQLFORM.smartgrid(db.Transecto_huellas_excretas_muestra,
        linked_tables=['Huella_excreta'],
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarEspeciesInvasorasExtra():
    db.Especie_invasora_extra.conglomerado_muestra_id.writable = False
    db.Archivo_especie_invasora_extra.especie_invasora_extra_id.writable=False
    db.Huella_excreta_extra.conglomerado_muestra_id.writable = False
    db.Archivo_huella_excreta_extra.huella_excreta_extra_id.writable = False
    db.Especimen_restos_extra.conglomerado_muestra_id.writable = False
    db.Archivo_especimen_restos_extra.especimen_restos_extra = False
    form = SQLFORM.smartgrid(db.Especie_invasora_extra,
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarHuellasExcretasExtra():
    form = SQLFORM.smartgrid(db.Huella_excreta_extra,
        csv=False,
        user_signature=False)
    return dict(form=form)

def editarEspecimenExtra():
    form = SQLFORM.smartgrid(db.Especimen_restos_extra,
        csv=False,
        user_signature=False)
    return dict(form=form)


# def admin_huella_excreta():
#     form = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#     return dict(form=form)

# def admin_huella_excreta():
#    form = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#    return dict(form=form)

# def admin_huellas():
#     form = SQLFORM.smartgrid(db.Transecto_huellas_excretas_muestra)
#     return dict(form=form)
