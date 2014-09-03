# coding: utf8

#def validacionesConglomerado(congForm):
    #Si uso_suelo_tipo no es 'Vegetación', entonces perturbado=None y vegetacion_tipo=No aplica
    #if not congForm.vars.uso_suelo_tipo==T('Vegetación'):
        #congForm.vars.vegetacion_tipo=0
        #congForm.vars.perturbado=None
    #response.flash = sitio1Form.vars.existe

    #Si uso_suelo_tipo es 'Vegetación', entonces la validación se realiza automáticamente porque en el campo vegetacion_tipo sólo se pueden incluir
    #tipos que están en el catálogo correspondiente. Además, la combobox siempre debe tener una opción seleccionada.

#def validacionesSitio(sitioForm):
    #Si el sitio existe, entonces todos los campos deben ser validados.

def controladorConglomerado():

    # Definimos los formularios correspondientes a cada una de las tablas, el atributo id se utiliza principalmente para el envío del formularios,
    # Se define el formulario a partir de una tabla virtual ya que queremos que la combobox de vegetación no visualize la opción "No aplica".
    congForm = SQLFORM.factory(
        Field('nombre','integer',label=T("Num. conglomerado"),requires=IS_NOT_EMPTY()),
        Field('fecha_visita', 'date',label=T("Fecha de visita"),requires=IS_NOT_EMPTY()),
        Field('tipo', 'reference Conglomerado_tipo_opcion',label=T("Tipo de conglomerado"),\
            requires=IS_IN_DB(db,db.Conglomerado_tipo_opcion.num_tipo,'%(nombre_tipo)s')),
        Field('estado', 'reference Conglomerado_estado_opcion',label=T("Estado"),\
            requires=IS_IN_DB(db,db.Conglomerado_estado_opcion.num_estado,'%(nombre_estado)s')),
        Field('municipio', 'integer',label=T("Municipio"),requires=IS_NOT_EMPTY()),
        Field('predio','string',label=T("Predio"),requires=IS_NOT_EMPTY()),
        Field('tenencia', 'reference Conglomerado_tenencia_opcion',label=T("Tenencia"),\
            requires=IS_IN_DB(db,db.Conglomerado_tenencia_opcion.num_tenencia,'%(nombre_tenencia)s')),
        Field('uso_suelo_tipo', 'reference Conglomerado_suelo_opcion',label=T("Tipo de uso de suelo"),\
            requires=IS_IN_DB(db,db.Conglomerado_suelo_opcion.num_suelo,'%(nombre_suelo)s')),
        Field('vegetacion_tipo','reference Conglomerado_vegetacion_opcion',label=T("Tipo de vegetación"),\
            requires=IS_IN_DB(db(db.Conglomerado_vegetacion_opcion.num_vegetacion>0),\
            db.Conglomerado_vegetacion_opcion.num_vegetacion,'%(nombre_vegetacion)s')),
        Field('perturbado', 'boolean',label=T("Perturbado")),
        Field('comentario', 'text',label=T("Observaciones")),
        table_name ='Conglomerado_muestra', _id='forma_conglomerado')

    # Se combinan Sitio_muestra e Imagen_referencia_sitio en un solo formulario porque campos correspondientes a ambas tablas se encuentran en la misma
    # tabla de HTML.
    # El nombre de la tabla "virtual" de la cuál se derivan los formularios conjuntos se utiliza para CSS.
    #sitio1Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, _id='forma_sitio1', table_name='Conjunta_sitio_imagen')
    #sitio2Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, _id='forma_sitio2', table_name='Conjunta_sitio_imagen')
    #sitio3Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, _id='forma_sitio3', table_name='Conjunta_sitio_imagen')
    #sitio4Form = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio, _id='forma_sitio4', table_name='Conjunta_sitio_imagen')
    #controlForm = SQLFORM.factory(db.Sitio_muestra, db.Imagen_referencia_sitio,_id='forma_control', table_name='Conjunta_sitio_imagen')

    # De acuerdo con el documento que explica el comportamiento del controlador,
    # se definirá la combobox para vegetacion_tipo (conglomerado) aquí y en la vista.
    
    # Haciendo un query a la tabla Conglomerado_vegetacion_opcion para llenar la combobox:
    #vegOpcionesNombre=[]
    #vegOpcionesNumero=[]
    #for row in db(db.Conglomerado_vegetacion_opcion.num_vegetacion>0).select():
        #vegOpcionesNombre.append(row.nombre_vegetacion)
        #vegOpcionesNumero.append(row.num_vegetacion)

    #seleccion = 'comboVeg = SELECT('
    #for row in db(db.Conglomerado_vegetacion_opcion.num_vegetacion>0).select():
        #seleccion += 'OPTION(\''+row.nombre_vegetacion+'\', _value=\'%d\'), ' % (row.num_vegetacion,)
    #seleccion = seleccion+'value=\'1\')'
    #exec(seleccion)

    #onvalidation=validacionesConglomerado
    #onvalidation=validacionesSitio
    if congForm.validate():
        
    #and sitio1Form.process().accepted and sitio2Form.process().accepted\
    #and sitio3Form.process().accepted and sitio4Form.process().accepted\
    #and controlForm.process().accepted:
        response.flash = "Registro ingresado exitosamente"
    return dict(congForm=congForm)#, sitio1Form=sitio1Form, sitio2Form=sitio2Form, sitio3Form=sitio3Form,\
                #sitio4Form=sitio4Form, controlForm=controlForm)#, vegOpcionesNombre=vegOpcionesNombre, vegOpcionesNumero=vegOpcionesNumero)

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
