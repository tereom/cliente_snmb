# coding: utf8

def validacionesConglomerado(congForm):
    #Si uso_suelo_tipo no es 'Vegetación', entonces perturbado=None y vegetacion_tipo=No aplica
    if not congForm.vars.uso_suelo_tipo==T('Vegetación'):
        congForm.vars.vegetacion_tipo=0
        congForm.vars.perturbado=None
    #Si uso_suelo_tipo es 'Vegetación', entonces la validación se realiza automáticamente por el .requires (más abajo).

#def validacionesSitio(sitioForm):
    #Si el atributo existe=True, entonces todos los campos deben ser validados.
    #if not sitioForm.var.lat_grado

def controladorConglomerado():

# Definimos los formularios correspondientes a cada una de las tablas, el atributo id se utiliza principalmente para el envío del formularios,
# Se combinan Sitio_muestra e Imagen_referencia_sitio en un solo formulario porque campos correspondientes a ambas tablas se encuentran en la misma
# tabla de HTML.
# El nombre de la tabla "virtual" de la cuál se derivan los formularios conjuntos se utiliza para CSS.

# De acuerdo con el documento que explica el comportamiento del controlador,
# se definirá la combobox para vegetacion_tipo (conglomerado) aquí.

# Haciendo un query a la tabla Conglomerado_vegetacion_opcion para llenar la combobox:

    query = (db.Conglomerado_vegetacion_opcion.num_vegetacion>0)
    #db.Conglomerado_muestra.vegetacion_tipo.requires=IS_IN_DB(db(query), '%(nombre_vegetacion)s' )
    db.Conglomerado_muestra.vegetacion_tipo.default=(db.Conglomerado_vegetacion_opcion.num_vegetacion==1)
    congForm = SQLFORM(db.Conglomerado_muestra, _id='forma_conglomerado')

    #seleccion = 'comboVeg = SELECT('
    #for row in db(db.Conglomerado_vegetacion_opcion.num_vegetacion>0).select():
    #    seleccion += 'OPTION(\''+row.nombre_vegetacion+'\', _value=\'%d\'), ' % (row.num_vegetacion,)
    #selection += 'value=\'1\')'
    #exec(seleccion)

    sitio1Form = SQLFORM(db.Sitio_muestra, _id='forma_sitio1')
    sitio2Form = SQLFORM(db.Sitio_muestra, _id='forma_sitio2')
    sitio3Form = SQLFORM(db.Sitio_muestra, _id='forma_sitio3')
    sitio4Form = SQLFORM(db.Sitio_muestra, _id='forma_sitio4')
    controlForm = SQLFORM(db.Sitio_muestra, _id='forma_control')


    #sitio1Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
    #    _id='forma_sitio1', table_name='conjunta_sitio_imagen')
    #sitio2Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
    #    _id='forma_sitio2', table_name='conjunta_sitio_imagen')
    #sitio3Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
    #    _id='forma_sitio3', table_name='conjunta_sitio_imagen')
    #sitio4Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, \
    #    _id='forma_sitio4', table_name='conjunta_sitio_imagen')
    #controlForm = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio,\
    # _id='forma_control', table_name='conjunta_sitio_imagen')

    if congForm.process(onvalidation=validacionesConglomerado).accepted\
    and sitio1Form.process().accepted and sitio2Form.process().accepted\
    and sitio3Form.process().accepted and sitio4Form.process().accepted\
    and controlForm.process().accepted:
        response.flash = "Registro ingresado exitosamente"
    return dict(congForm=congForm, sitio1Form=sitio1Form, sitio2Form=sitio2Form, sitio3Form=sitio3Form,\
                sitio4Form=sitio4Form, controlForm=controlForm)#, comboVeg=comboVeg)


#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
