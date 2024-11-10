# The Python Standard Library. A set of modules with every Python installation.
# e.g lets look at one class called OrderedDict, from the module collections.
from collections import OrderedDict

favorite_program = OrderedDict()

favorite_program = {
         'lucy': 'python',
         'peter':'java',
         'nelson':'c',
         'john':'bash',
         }

for name, language in favorite_program.items():
    print(name.title() + "'s best language is " + language.title())






