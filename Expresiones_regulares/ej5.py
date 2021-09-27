'''5. Escribir un programa en Python que a partir de un string, extraiga las
fechas con formato dd/mm/yyyy'''

import re

text = "La sandia es una fruta que fue descubierta el 25/02/1524 por Arquimides nacido el 03/08/1523."


pattern = re.compile(r"[\d\d\/\d\d\/\d\d\d\d\d]+")
print(pattern.findall(text))


