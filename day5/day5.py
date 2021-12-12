from os import sep
import numpy as np
import pandas as pd

## PART 1 ##

fname = "day5\data\data-day5.txt"
f = open(fname)
newname = "day5\data\\new-data-day5.txt"
fnew = open(newname, "w+")

newf = f.read().replace(' -> ', ',')
fnew.write(newf)
fnew.close()
f.close()

data = np.loadtxt(newname, dtype=int, delimiter=',')
df = pd.DataFrame(data, index= None, columns=['x1', 'y1', 'x2', 'y2'])

points = {}

for _, row in df.iterrows():

    if row['x1'] == row['x2']:
        if row['y1'] < row['y2']:
            for i in range(row['y1'], row['y2'] + 1):
                points[(row['x1'], i)] = points.get((row['x1'], i), 0) + 1
        else:
            for i in range(row['y2'], row['y1'] + 1):
                points[(row['x1'], i)] = points.get((row['x1'], i), 0) + 1
    elif row['y1'] == row['y2']:
        if row['x1'] < row['x2']:
            for i in range(row['x1'], row['x2'] + 1):
                points[(i, row['y1'])] = points.get((i, row['y1']), 0) + 1
        else:
            for i in range(row['x2'], row['x1'] + 1):
                points[(i, row['y1'])] = points.get((i, row['y1']), 0) + 1
    else:
        x_inicio = row['x1']
        x_final = row['x2']
        y_inicio = row['y1']
        y_final = row['y2']
        if x_inicio < x_final:
            j = 1
        else:
            j = -1
        if y_inicio < y_final:
            k = 1
        else:
            k = -1

        if j > 0:
            while x_inicio <= x_final:
                points[(x_inicio, y_inicio)] = points.get((x_inicio, y_inicio),0) +1
                x_inicio += j
                y_inicio += k
        else:
            while x_inicio >= x_final:
                points[(x_inicio, y_inicio)] = points.get((x_inicio, y_inicio),0) +1
                x_inicio += j
                y_inicio += k

contador = 0
for value in list(points.values()):
    if value >=2:
        contador += 1

print(contador)

## PARTE 2 es la ultima condicion del primer if dentro del anterior bucle for ##



