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
#     grid = SQLFORM.grid(db.Huella_excreta,user_signature=False,
#         fields=[db.Huella_excreta.es_huella])
#     return locals()

db.Conglomerado_muestra.tipo.requires=IS_IN_DB(db,db.Cat_tipo_conglomerado.id,'%(nombre)s')

def editar_conglomerado():

	grid = SQLFORM.smartgrid(db.Conglomerado_muestra,user_signature=False)
	return locals()


# def admin_huella_excreta():
#     grid = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#     return locals()

# def admin_huellas():
#     grid = SQLFORM.smartgrid(db.Transecto_huellas_excretas_muestra)
#     return locals()