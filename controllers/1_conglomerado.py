# coding: utf8

def vegetation_typeCheck(form):
    if form.vars.soil_use_type==T('Vegetación') and not form.vars.vegetation_type:
        form.errors.vegetation_type=T("Debe elegir un tipo de vegetación predominante")

def controladorConglomerado():
    form = SQLFORM(db.Conglomerate_sample)
    if form.process(onvalidation=vegetation_typeCheck).accepted:
        response.flash = "success"
    return dict(form=form)

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
