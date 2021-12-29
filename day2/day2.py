import numpy as np
import pandas as pd


fichero = 'day2\\data\\data-day2.txt'

data = np.loadtxt(fichero, delimiter=' ', dtype=str)                            ## Cargamos los datos del fichero
df = pd.DataFrame(data=data, index=None, columns=['Move', 'Distance'])          ## Generamos el dataframe a partir de los datos

x_pos = 0
y_pos = 0
aim = 0

for _, row in df.iterrows():                                                    ## Iteramos por las filas y hacemos un 'switch' con cada caso
    if row['Move'][0] == 'f':
        x_pos += int(row['Distance'])
        y_pos += aim*int(row['Distance']) 
    elif row['Move'][0] == 'd':
        aim += int(row['Distance'])
    elif row['Move'][0] == 'u':
        aim -= int(row['Distance'])

print(x_pos * y_pos)
    

