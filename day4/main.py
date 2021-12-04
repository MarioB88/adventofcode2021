from typing import Tuple
from board import Board

## Iniciamos el fichero y leemos la primera linea

fname = 'adventofcode2021\\day4\\data\\data-day4.txt'
fichero = open(fname)
firstline = fichero.readline()

## Creamos la lista de numeros y borramos el salto de linea del ultimo elemento
rnumbers = firstline.split(',')
rnumbers[-1] = rnumbers[-1].replace('\n', '')

board_list = []
board = Board()

## Cada vez que hay una linea entre tableros añadimos el anterior a la lista de tableros y creamos uno nuevo. Limpiamos la linea de texto de saltos de linea
## (igual que antes) y de elementos vacios con una funcion lambda para que sea rapido.

for line in fichero:
    if line[0] == '\n':
        board_list.append(board)
        board = Board()
        continue
    row = line.split(' ')
    row[-1] = row[-1].replace('\n', '')
    row = list(filter(lambda x: x != '', row))
    for z in range(0, len(row)):
        row[z] = [row[z], False]
    board.matriz.append(row)
board_list.append(board)

## Con cada numero, en cada tablero marcamos la coincidencia de numeros y comprobamos si ha ganado tanto horizontalmente como verticalmente. Si es asi, terminamos los bucles.

finish = False
for n in rnumbers:
    for b in board_list:
        b.check_coincidence(n)
        if b.winner_horizontal():
            finish = True
            break
        elif b.winner_vertical():
            finish = True
            break
    if finish:
        break

## Calculamos la puntuacion

score = int(n)*b.score()
print(score)

##### PART 2 #####

## Realizamos lo mismo que en la parte 1, pero quitando de la lista aquellos tableros que terminan hasta que solo quede uno. En el codigo esta puesto para que solo
## queden dos porque el ultimo es un tablero vacio.

finish = False
for n in rnumbers:
    i=0
    while i < len(board_list):
        b = board_list[i]
        b.check_coincidence(n)
        if b.winner_horizontal():
            if len(board_list)<3:
                finish = True
                break
            board_list.remove(b)
            i-=1
            continue
        elif b.winner_vertical():
            if len(board_list)<3:
                finish = True
                break
            len(board_list)
            board_list.remove(b)
            i-=1
            continue
        i+=1
    if finish:
        break
        
score = int(n)*b.score()
print(score)
            


