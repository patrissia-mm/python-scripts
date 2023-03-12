def polindromos(frase):
    fraseAux=frase.replace(" ","")
    fraseAux=fraseAux.lower()
    i=len(fraseAux)

    for letra in range((len(fraseAux)//2)+1):
        if(fraseAux[letra]==fraseAux[i-1]):
            i-=1
        else:
            return(False)
    
    return(True)
    
frase=input("Introduzca una cadena: ")
if(polindromos(frase)==True):
    print("Son polindromos")
else:
    print("No son políndromos")
