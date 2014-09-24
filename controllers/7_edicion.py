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

def options_widget(field,value,**kwargs):
    """ Use web2py's intelligence to set up the right HTML for the select field
     the widgets knows about the database model """
    w = SQLFORM.widgets.options.widget
    xml = w(field,value,**kwargs)
    return xml

def admin_huella_excreta():
    db.Huella_excreta.id.writable = False
    db.Huella_excreta.id.readable = False
    db.Huella_excreta.transecto_huellas_excretas_id.writable = False
    grid = SQLFORM.grid(db.Huella_excreta,user_signature=False)
        #fields=[db.Huella_excreta.es_huella])
    return locals()

def admin_especies():
    db.Especie_invasora.id.writable = False
    db.Especie_invasora.id.readable = False
    db.Especie_invasora.transecto_especies_invasoras_id.writable = False
    grid_especies = SQLFORM.grid(db.Especie_invasora,user_signature=False)
        #fields=[db.Huella_excreta.es_huella])

    db.Huella_excreta.id.writable = False
    db.Huella_excreta.id.readable = False
    db.Huella_excreta.transecto_huellas_excretas_id.writable = False
    grid_huellas = SQLFORM.grid(db.Huella_excreta,user_signature=False)

    return locals()

def admin_conglomerado():
    db.Conglomerado_muestra.id.writable = False
    db.Conglomerado_muestra.id.readable = False
    db.Conglomerado_muestra.estado.represent = lambda value,row: options_widget(db.Conglomerado_muestra.estado,value,**{'_name':'home_state_row_%s' % row.id})
    grid = SQLFORM.grid(db.Conglomerado_muestra,
    	fields=[db.Conglomerado_muestra.estado],
    	user_signature=False,
    	selectable = lambda ids : redirect(URL('default', 'mapping_multiple', vars=dict(id=ids))))
        #fields=[db.Huella_excreta.es_huella])
    return locals()

# def admin_huella_excreta():
#    grid = SQLFORM.grid(db.Archivo_huella_excreta,user_signature=False)
#    return locals()

# def admin_huellas():
#     grid = SQLFORM.smartgrid(db.Transecto_huellas_excretas_muestra)
#     return locals()