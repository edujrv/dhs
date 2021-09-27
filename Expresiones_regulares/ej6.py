'''6. Escribir un programa en Python que a partir de un string, extraiga todas
las direcciones de mail en el mismo'''

import re

text = "La sandia es una fruta que fue descubierta el 25/02/1524 segun datocurioso@gmail.com por Arquimides nacido el 03/08/1523 cuyo mail es arquimides355@gmail.com."


pattern = re.compile(r"[\w+@]+\w\.com")
print(pattern.findall(text))


