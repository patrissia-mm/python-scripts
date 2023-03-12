def anagramas(palabra1, palabra2):
    for i in range(len(palabra1)):
        fnd=palabra2.find(palabra1[i])
        if fnd==-1:
           return(False)
    return(True)


p1=input("Introduzca la primera palabra: ")
p2=input("Introduzca la segunda palabra: ")
anag=anagramas(p1,p2)
if (anag==True):
    print("Son anagramas")
else:
    print("No son angramas")

        
