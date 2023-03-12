def Fcero():
    cero=[]
    cero.append("###")
    cero.append("# #")
    cero.append("# #")
    cero.append("# #")
    cero.append("###")
    return cero
    
def Funo():
    uno=[]
    uno.append("  #")
    uno.append("  #")
    uno.append("  #")
    uno.append("  #")
    uno.append("  #")
    return uno

def Fdos():
    dos=[]
    dos.append("###")
    dos.append("  #")
    dos.append("###")
    dos.append("#  ")
    dos.append("###")
    return dos

def Ftres():
    tres=[]
    tres.append("###")
    tres.append("  #")
    tres.append("###")
    tres.append("  #")
    tres.append("###")
    return tres

def Fcuatro():
    cuatro=[]
    cuatro.append("# #")
    cuatro.append("# #")
    cuatro.append("###")
    cuatro.append("  #")
    cuatro.append("  #")
    return cuatro

def Fcinco():
    cinco=[]
    cinco.append("###")
    cinco.append("#  ")
    cinco.append("###")
    cinco.append("  #")
    cinco.append("###")
    return cinco

def Fseis():
    seis=[]
    seis.append("###")
    seis.append("#  ")
    seis.append("###")
    seis.append("# #")
    seis.append("###")
    return seis

def Fsiete():
    siete=[]
    siete.append("###")
    siete.append("  #")
    siete.append(" # ")
    siete.append("#  ")
    siete.append("#  ")
    return siete

def Focho():
    ocho=[]
    ocho.append("###")
    ocho.append("# #")
    ocho.append("###")
    ocho.append("# #")
    ocho.append("###")
    return ocho

def Fnueve():
    nueve=[]
    nueve.append("###")
    nueve.append("# #")
    nueve.append("###")
    nueve.append("  #")
    nueve.append("  #")
    return nueve



def crearLista():
    numeros=[]
    cero=Fcero()
    uno=Funo()
    dos=Fdos()
    tres=Ftres()
    cuatro=Fcuatro()
    cinco=Fcinco()
    seis=Fseis()
    siete=Fsiete()
    ocho=Focho()
    nueve=Fnueve()
    numeros.append(cero)
    numeros.append(uno)
    numeros.append(dos)
    numeros.append(tres)
    numeros.append(cuatro)
    numeros.append(cinco)
    numeros.append(seis)
    numeros.append(siete)
    numeros.append(ocho)
    numeros.append(nueve)
    return numeros

    
listaNum=crearLista()
mostrarNumeros=[]
mostrar=input("Número a mostrar:")
for numero in mostrar:
    mostrarNumeros.append(int(numero))

for i in range(5):
    fin=" "
    for item in mostrarNumeros:
        print(listaNum[item][i],end=fin)
    print("\n")   
