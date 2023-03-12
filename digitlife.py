fecha=input("Intriduce la fecha de tu nacimiento: ")
lista=list(fecha)
valor=0
for item in lista:
    valor+=int(item)
while valor>9:
    cadena=str(valor)
    nvalor=0
    for dig in cadena:
        nvalor+=int(dig)
    valor=nvalor
print(valor)