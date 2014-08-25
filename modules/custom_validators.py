#!/usr/bin/env python
# coding: utf8

#Este archivo contiene validadores especiales, que no se encuentran incluidos en Web2py.

from gluon.validators import is_empty
from gluon.validators import Validator

class IS_NOT_EMPTY_IF_OTHER(Validator):
    '''Allow a field to be empty unless any some other value is present.
 
    Note: "other" field may be a list of fields. If any of them is not
          empty, the field must be filled.
    '''
    def __init__(self, other,
                 error_message='must be filled because other value '
                               'is present'):
        self.other = other
        self.error_message = error_message
 
    def __call__(self, value):
        if isinstance(self.other, (list, tuple)):
            others = self.other
        else:
            others = [self.other]
 
        has_other = False
        for other in others:
            other, empty = is_empty(other)
            if not empty:
                has_other = True
                break
        value, empty = is_empty(value)
        if empty and has_other:
            return (value, T(self.error_message))
        else:
            return (value, None)

#def check(form):
#    if form.vars.b and not form.vars.c:
#        form.errors.c = "If the b is checked, c must be filled"

#def action():
#    form = SQLFORM(db.foo)
#    if form.process(onvalidation=check).accepted:
#        response.flash = "success"
#    return dict(form=form)
