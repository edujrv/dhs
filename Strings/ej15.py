# Diseñar un programa que permita validar que la estructura 
# de una dirección de mail es correcta (debe tener un @ y al menos un punto).
#  Por otro lado, realizar un validador de contraseñas 
# (debe tener al menos una letra mayúscula, una minúscula,un número o un símbolo)

mail = input("User: ")
mail = mail.split("@")
may = False
mini = False
sim = False

if len(mail) == 1:
    print("Falto el @ para el mail")
    exit()

password = input("Password: ")
for i in password:
    if i >= 'A' and i <= 'Z':
        may = True
    if i >= 'a' and i <= 'z':
        mini = True
    if i == " ":
        continue
    else:
        sim = True

if(may == True and mini == True and sim == True):
    print("Bienvenido pá")
else:
    print("Su contraseña es invalida pá")