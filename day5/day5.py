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
        for i in range(row['y1'], row['y2'] + 1):
            points[(row['x1'], i)] = points.get((row['x1'], i), 0) + 1
    elif row['y1'] == row['y2']:
        for i in range(row['x1'], row['x2'] + 1):
            points[(i, row['y1'])] = points.get((i, row['y1']), 0) + 1

contador = 0
for value in list(points.values()):
    if value >=2:
        contador += 1

print(contador)

