import numpy as np
import pandas as pd

fichero = 'day1\\data\\data-day1.txt'
data = np.loadtxt(fichero, delimiter=' ', dtype = int)

contador = 0

np_grouped = np.zeros((len(data), 3), dtype=int)
np_grouped[0] = np.asarray([data[0], data[1], data[2]])

for i in range(0, len(data)):
    try:
        np_grouped[i] = np.asarray([data[i], data[i+1], data[i+2]])
    except IndexError:
        break

pd_grouped = pd.DataFrame(data=np_grouped, index=None, columns=None)
pd_grouped['sum'] = pd_grouped.sum(axis=1)

prev_sum = np.Inf

for _, row in pd_grouped.iterrows():
    if prev_sum < row['sum']:
        contador += 1
    prev_sum = row['sum']

print(contador)



