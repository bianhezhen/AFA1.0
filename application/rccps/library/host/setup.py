
from distutils.core import setup, Extension
module1 = Extension('spam',sources=['transAcc.c'])
setup( name = 'spam package',
       version = '1.0',
       description = 'This is a spam package',
       ext_modules = [module1])
