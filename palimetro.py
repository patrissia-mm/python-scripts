cadena=input("Ingrese una cadena: ")
cadena=cadena.replace(" ","").upper()
palimetre=False
lista=list(cadena)
for i in range(0,len(lista)//2):
    if lista[i]==lista[len(lista)-(i+1)]:
        palimetre=True
    else:
        palimetre=False
        break
if palimetre==False:
    print("No es un palímetro")
else:
    print("Sí es un aplímetro")