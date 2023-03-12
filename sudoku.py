print("Inserte las 9 filas de sudoku compuesta cada una de 9 dígitos para verificar su validez.\n")
sudoku=[]
for i in range(9):
    fila=input("")
    if not fila.isdigit():
        print("Los valores introducidos no son dígitos, ejecute nuevamente")
        break
    else:
        sudoku.append(list(fila))

#verificación x filas 
for y in range(9):
    for digito in range(1,10):
        for x in range(9):
            if sudoku[y][x]==str(digito):
                encF=True
                break
            else:
                encF=False
        if encF==False:
            break
    if encF==False:
            break

#verificación por columnas
if encF==True:
    for x in range(9):
        for digito in range(1,10):
            for y in range(9):
                if sudoku[y][x]==str(digito):
                    encC=True
                    break
                else:
                    encC=False
            if encC==False:
                break
        if encC==False:
            break
    #verificación de grupos de 3 x 3
    if encC==True:
        filaI=0
        filaF=3
        columnaI=0
        columnaF=3
        encontrados=[]
        encG=False

        for cuad in range(0,3):
            for cuadrados in range(0,3):
                for dig in range(1,10):
                    encG=False
                    for j in range(filaI,filaF):
                        if encG==True:
                            break
                        for i in range(columnaI,columnaF):
                            print(sudoku[j][i], "-", dig, end=" * ")
                            if sudoku[j][i]==str(dig):
                                encG=True
                                break
                            else:
                                encG=False
                    if encG==False:
                        print("digito",dig,"no encontrado\n")
                        print("fin")
                        break
                print("Cuadro verificado",encG)
                if encG==False:
                    print("Sudoku inválido.")
                    break
                columnaI+=3
                columnaF+=3
            filaI+=3
            filaF+=3
            columnaI=0
            columnaF=0
            if encG==False:
                print("Sudoku inválido.")
                break

        if encG==True:
            print("Sudoku válido")
            
               
    else:
        print("acabamos el programa columnas")
else:
    print("acabamos el programa filas")
    



            
            


    
