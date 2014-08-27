# coding: utf8

def additionalValidations(congform):
    #If soil_use_type is not 'Vegetación' then is_perturbed=None
    if not congform.vars.soil_use_type==T('Vegetación'):
        congform.vars.vegetation_type=None
        congform.vars.is_perturbed=None
    #Checking if the vegetation_type control is filled when soil_use_type='Vegetación'
    elif not congform.vars.vegetation_type:
        congform.errors.vegetation_type=T("Debe elegir un tipo de vegetación predominante")

def controladorConglomerado():
    congform = SQLFORM(db.Conglomerate_sample,  _id='forma_conglomerado', formstyle='table3cols')
    site1form = SQLFORM(db.Site_sample)
    site2form = SQLFORM(db.Site_sample)
    site3form = SQLFORM(db.Site_sample)
    site4form = SQLFORM(db.Site_sample)
    controlform = SQLFORM(db.Site_sample)
    if congform.process(onvalidation=additionalValidations).accepted\
    and site1form.process().accepted and site2form.process().accepted\
    and site3form.process().accepted and site4form.process().accepted\
    and controlform.process().accepted:
        response.flash = "Registro ingresado exitosamente"
    return dict(congform=congform, site1form=site1form, site2form=site2form, site3form=site3form,\
                site4form=site4form, controlform=controlform)

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
