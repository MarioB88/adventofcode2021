import numpy as np
import pandas as pd


fichero = 'C:\\OwnProjects\\advent_code2021\\day2\\data\\data-day2.txt'

data = np.loadtxt(fichero, delimiter=' ', dtype=str)
df = pd.DataFrame(data=data, index=None, columns=['Move', 'Distance'])

x_pos = 0
y_pos = 0
aim = 0

for _, row in df.iterrows():
    if row['Move'][0] == 'f':
        x_pos += int(row['Distance'])
        y_pos += aim*int(row['Distance']) 
    elif row['Move'][0] == 'd':
        aim += int(row['Distance'])
    elif row['Move'][0] == 'u':
        aim -= int(row['Distance'])

print(x_pos * y_pos)
    

