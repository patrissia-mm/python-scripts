from random import randrange
def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|   ",end="")
        for j in range(3):
            print(board[i][j],"  |   ",end="")
        print("\n","|       |       |       |")
        print("+-------+-------+-------+")

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    valido=False
    while valido==False:
        valor=int(input("Qué casilla ocuparás?: "))
        if valor>0 and valor<10: 
            vacias=MakeListOfFreeFields(board)
            for elem in vacias:
                tupla=elem
                if board[tupla[0]][tupla[1]]==valor:
                    board[tupla[0]][tupla[1]]="O"
                    valido=True
    return board

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    casillasVacias=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]!="X" and board[i][j]!="O":
                tupla=(i,j)
                casillasVacias.append(tupla)
    return casillasVacias

def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
# 
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return True
        else:
            for j in range(3):
                 if board[0][j]==board[1][j]==board[2][j]:
                     return True
    return False                
        

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
   
    valido=False
    vacias=MakeListOfFreeFields(board)
    while valido==False:
        valor=randrange(10)
        for elem in vacias:
            tupla=elem
            if board[tupla[0]][tupla[1]]==valor:
                board[tupla[0]][tupla[1]]="X"
                valido=True
    return board


print("Bienvenido a Tic Tac Toe. Empecemos!")
ganador=False
board=[]
numero=1
for j in range(3):
    fila=[]
    for i in range(3):
        if j==1 and i==1:
            fila.append("X")
        else:
            fila.append(numero)
        numero+=1
    board.append(fila)
DisplayBoard(board)
casillasVacias=MakeListOfFreeFields(board)
while len(casillasVacias)>0:
    board=EnterMove(board)
    DisplayBoard(board)
    ganador=VictoryFor(board, "O")
    if ganador==True:
        print("Ganaste el juego. Felicidades!!")
        break
    board=DrawMove(board)
    DisplayBoard(board)
    ganador=VictoryFor(board, "X")
    if ganador==True:
        print("Lo siento. Perdiste!!!")
        break
    casillasVacias=MakeListOfFreeFields(board)

if ganador==False:
    print("Empate!!!")
    
    


