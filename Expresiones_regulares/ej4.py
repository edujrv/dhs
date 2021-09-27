'''4. Escribir un programa en Python que a partir de un string, veriﬁque cuales
lineas del mismo contienen un signo +,-,*,/ y/o = en su interior.'''

import re

text = "La vida es + bella;\n \
Pero + bella;\n \
Es la sandia;\n \
Y las sunboxes;\n \
- los cuervos pero *k?\n \
// diría el mc\n \
= no sé que significa\n \
solo sé que no sé nada "


pattern = re.compile(r"[\+|\-|\=|\*|\/]+")


for txt in text.split("\n"):
   print(pattern.search(txt))

