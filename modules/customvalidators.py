#!/usr/bin/env python
# coding: utf8
from gluon.validators import is_empty
from gluon.validators import Validator


class IS_NOT_EMPTY_IF_OTHER_TRUE(Validator):

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

        other = false
        for other in others:
            if other:
                break
        #value, empty = is_empty(value)
        if value=="" and other:
            return (value, T(self.error_message))
        else:
            return (value, None)
