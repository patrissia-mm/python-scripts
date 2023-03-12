def misplit(strng):
    palabra=""
    palabras=[]
    for letra in strng:
        if letra!=" " and letra!="''" and letra!=None:
            palabra+=letra
        else:
            palabras.append(palabra)
            palabra=""
    return palabras

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
