cadena1=input("Introduce la primera cadena: ")
cadena2=input("Introduce la segunda cadena: ")
cadena1=cadena1.replace(" ","").upper()
cadena2=cadena2.replace(" ","").upper()
listac1=list(cadena1)
listac2=list(cadena2)
anag=False
if len(listac1)==len(listac2):
    for letra in cadena1:
        cant=cadena1.count(letra)
        count=0
        for element in listac2:
            if element==letra:
                count+=1
        if count==cant:
            anag=True
        else:
            anag=False
            break
else:
    anag=False

if anag==True:
    print("Son anagramas")
else:
    print("No son anagramas")
    
