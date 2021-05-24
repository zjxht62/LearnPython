"{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)  # 3 1 4 2

"{foo} {1} {bar} {0}".format(1, 2, foo=3, bar=4)  # 3 2 4 1

full_name = ['trevor', 'zhao']
print('Mr {name[1]}'.format(name=full_name))  # Mr zhao

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))