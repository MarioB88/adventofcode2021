#### PART 1 ####

import numpy as np
import pandas as pd

gamma_rate = ''
epsilon_rate = ''
fichero = 'adventofcode2021\\day3\\data\\data-day3.txt'
data = np.genfromtxt(fichero, delimiter=1, dtype=int)           ## Cargamos los datos
df = pd.DataFrame(data, index=None, columns=None)               ## Generamos el dataframe a partir de los datos

df_counted = df.apply(pd.value_counts)                          ## Aplicamos la funcion que cuenta valores unicos en todas las columnas del dataframe

print("Dataframe contado")
print(df_counted)

for c in df_counted:                                            ## Iteramos las columnas del dataframe contado
    if df_counted[c][0] > df_counted[c][1]:
        gamma_rate += str(0)
        epsilon_rate += str(1)
    else:
        gamma_rate += str(1)
        epsilon_rate += str(0)

decimal_gamma = int(gamma_rate, 2)                              ## Convertimos a decimal especificando la base a la que estaba el numero, en este caso binario o base 2
decimal_epsilon = int(epsilon_rate, 2)

print(decimal_gamma)
print(decimal_epsilon)

print(decimal_epsilon*decimal_gamma)

### PART 2 ###

oxygen_bin = ''
co2_bin = ''

df_filteredmax = df.copy()

## Por cada columna, ceamos una mascara de True y False donde se cumpla la condicion de que el valor de
## la columna del dataframe sea el mismo que el numero que mas aparece en esta y paramos cuando solo quede una fila.
## Como se indica en el enunciado, si hay la misma aparicion de unos y ceros cogeremos el 1 por defecto.
## Despues modificaremos el dataframe quedandonos con solo las filas que cumplan la condicion

for c in df_filteredmax:
    if len(df_filteredmax) < 2:
        break
    count = df_filteredmax[c].value_counts()
    if max(count) == min(count):
        indice = 1
    else:
        indice = count[count == max(count)].index[0]
    maskmax= df_filteredmax[c] == indice
    df_filteredmax.where(maskmax, inplace=True)
    df_filteredmax.dropna(inplace=True)

df_filteredmin = df.copy()

## Hacemos lo mismo que el maximo pero quedandonos con el minimo y con el 0 por defecto en caso de empate.

for c in df_filteredmin:
    if len(df_filteredmin) < 2:
        break
    count = df_filteredmin[c].value_counts()
    if min(count) == max(count):
        indice = 0 
    else:
        indice = count[count == min(count)].index[0]
    maskmin= df_filteredmin[c] == indice
    df_filteredmin.where(maskmin, inplace=True)
    df_filteredmin.dropna(inplace=True)

## Metemos la fila resultante en una string representando un numero binario para facilitar el cambio al decimal

for c in df_filteredmax:
    oxygen_bin += str(int(df_filteredmax[c]))

for c in df_filteredmin:
    co2_bin += str(int(df_filteredmin[c]))

## Lo transformamos en decimal

oxygen_decimal = int(oxygen_bin, 2)
co2_decimal = int(co2_bin, 2)

print(oxygen_decimal * co2_decimal)