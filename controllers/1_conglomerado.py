# coding: utf8

def additionalValidations(congform):
    #Si uso_suelo_tipo no es 'Vegetación' entonce perturbado=None
    if not congform.vars.uso_suelo_tipo==T('Vegetación'):
        congform.vars.vegetacion_tipo=None
        congform.vars.perturbado=None
    # Revisamos si se ingresó vegetacion_tipo cuando uso_suelo_tipo='Vegetación'
    elif congform.vars.vegetacion_tipo==None:
        congform.errors.vegetacion_tipo=T("Debe elegir un tipo de vegetación predominante")

# def controladorConglomerado():
#     congform = SQLFORM(db.Conglomerado_muestra, _id='forma_conglomerado')
#     sitio1form = SQLFORM(db.Sitio_muestra, _id='forma_sitio1')
#     sitio2form = SQLFORM(db.Sitio_muestra, _id='forma_sitio2')
#     sitio3form = SQLFORM(db.Sitio_muestra, _id='forma_sitio3')
#     sitio4form = SQLFORM(db.Sitio_muestra, _id='forma_sitio4')
#     controlform = SQLFORM(db.Sitio_muestra, _id='forma_control')
#     if congform.process(onvalidation=additionalValidations).accepted\
#     and sitio1form.process().accepted and sitio2form.process().accepted\
#     and sitio3form.process().accepted and sitio4form.process().accepted\
#     and controlform.process().accepted:
#         response.flash = "Registro ingresado exitosamente"
#     return dict(congform=congform, sitio1form=sitio1form, sitio2form=sitio2form, sitio3form=sitio3form,\
#                 sitio4form=sitio4form, controlform=controlform)


def controladorConglomerado():
    congform = SQLFORM(db.Conglomerado_muestra, _id='forma_conglomerado')
    sitio1form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
        _id='forma_sitio1', table_name='conjunta_sitio_imagen')
    sitio2form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
        _id='forma_sitio2', table_name='conjunta_sitio_imagen')
    sitio3form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
        _id='forma_sitio3', table_name='conjunta_sitio_imagen')
    sitio4form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
        _id='forma_sitio4', table_name='conjunta_sitio_imagen')
    controlform = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio,\
     _id='forma_control', table_name='conjunta_sitio_imagen')
    if congform.process(onvalidation=additionalValidations).accepted\
    and sitio1form.process().accepted and sitio2form.process().accepted\
    and sitio3form.process().accepted and sitio4form.process().accepted\
    and controlform.process().accepted:
        response.flash = "Registro ingresado exitosamente"
    return dict(congform=congform, sitio1form=sitio1form, sitio2form=sitio2form, sitio3form=sitio3form,\
                sitio4form=sitio4form, controlform=controlform)


#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
