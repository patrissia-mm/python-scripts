def readint(prompt, min, max):
    correcto=False
    while correcto==False:
        try:
            v=int(input(prompt))
            if (v>=-10 and v<=10):
                correcto=True
                return v
            else:
                correcto=False
                print("Error: el valor no está dentro del rango permitido (-10..10)")
        except ValueError:
            print("Error:Entrada incorrecta")
            correcto=False

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
print("El numero es:", v)
