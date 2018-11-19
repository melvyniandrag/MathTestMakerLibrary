
# coding=utf8
import sys
language = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != None else 'en' 
from fractions import Fraction
import gettext 
languageTranslations = gettext.translation('base', localedir='locales', languages=[language])
languageTranslations.install()
_ = languageTranslations.gettext

class StringFormatter(object):
    def format(self, msgId):        
        return _(msgId).decode("utf-8")