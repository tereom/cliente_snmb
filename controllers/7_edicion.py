# coding: utf8

# def manage_users():
#     grid = SQLFORM.grid(db.Huella_excreta.hay_nombre_comun==False,user_signature=False)
#     return locals()

# def manage():
#     table = request.args(0) or 'auth_user'
#     if not table in db.tables(): redirect(URL('error'))
#     grid = SQLFORM.smartgrid(db[table],args=request.args[:1])
#     return locals()

# # coding: utf8

# def admin_huella_excreta():
#     db.Huella_excreta.id.writable = False
#     db.Huella_excreta.id.readable = False
#     db.Huella_excreta.transecto_huellas_excretas_id.writable = False
#     grid = SQLFORM.grid(db.Huella_excreta,user_signature=False)
#         #fields=[db.Huella_excreta.es_huella])
#     return locals()

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

#     return locals()

# def admin_conglomerado():
#     db.Conglomerado_muestra.id.writable = False
#     db.Conglomerado_muestra.id.readable = False
#     db.Conglomerado_muestra.estado.represent = lambda value,row: options_widget(db.Conglomerado_muestra.estado,value,**{'_name':'home_state_row_%s' % row.id})
#     grid = SQLFORM.grid(db.Conglomerado_muestra,
#     	fields=[db.Conglomerado_muestra.estado],
#     	user_signature=False,
#     	selectable = lambda ids : redirect(URL('default', 'mapping_multiple', vars=dict(id=ids))))
#         #fields=[db.Huella_excreta.es_huella])
#     return locals()

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
db.Especie_invasora.numero_individuos.requires=(db,db.Cat_numero_individuos,'%(nombre)s')

# Huellas excreta
db.Transecto_huellas_excretas_muestra.transecto_numero.requires=IS_IN_DB(db,
    db.Cat_numero_transecto,'%(nombre)s')

# Registros extra
db.Especie_invasora_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')
db.Especie_invasora_extra.numero_individuos.requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')

db.Huella_excreta_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')

db.Especimen_restos_extra.elipsoide.requires=IS_IN_DB(db,db.Cat_elipsoide,'%(nombre)s')
db.Especimen_restos_extra.numero_individuos.requires=IS_IN_DB(db,db.Cat_numero_individuos,'%(nombre)s')

def editar():
    pestana1 = SQLFORM.smartgrid(db.Conglomerado_muestra,
        linked_tables=['Sitio_muestra'],
        user_signature=False, 
        csv=False
        )
    pestana2 = SQLFORM.smartgrid(db.Camara,user_signature=False)
    grid = SQLFORM.smartgrid(db.Archivo_camara,user_signature=False)
    return locals()

# def admin_huella_excreta():
#     grid = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#     return locals()

# def admin_huella_excreta():
#    grid = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#    return locals()

# def admin_huellas():
#     grid = SQLFORM.smartgrid(db.Transecto_huellas_excretas_muestra)
#     return locals()