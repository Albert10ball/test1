# encoding = utf-8

import unittest


class Dict(dict):
    def __int__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict'object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

