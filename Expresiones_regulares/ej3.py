'''3. Escribir un programa en Python que a partir de un string, verifique si
todas las lineas del mismo contienen un ; al final.'''

import re

text = "La vida es bella;\n \
Pero mas bella;\n \
Es la sandia;"
        
pattern = re.compile(r"\n")
print(pattern.split(text))