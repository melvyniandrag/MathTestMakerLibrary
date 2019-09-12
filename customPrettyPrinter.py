# coding=utf8
# https://stackoverflow.com/a/10883893/852841

import pprint

class CustomPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        #if isinstance(object, unicode):
        #    return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
