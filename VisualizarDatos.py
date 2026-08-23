# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:43:23 2026

@author: aguire marcela
"""
#matplotlib

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# crea un gráfico de líneas, años en el eje x, cantidades en el eje y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# añade un título
plt.title("Nominal GDP")
# añade una etiqueta al eje y
plt.ylabel("Billions of $")
plt.show()

##Graficos de Barras 
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# dibuja barras con coordenadas x de la izquierda [0, 1, 2, 3, 4], alturas
[num_oscars]
plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies") # añade un título
plt.ylabel("# of Academy Awards") # etiqueta el eje y
# etiqueta el eje x con los nombres de las películas en el centro de las barras
plt.xticks(range(len(movies)), movies)
plt.show()

##Matrices
# Otro alias de tipo
from typing import List
Matrix = List[List[float]]
A = [[1, 2, 3], # A tiene 2 filas y 3 columnas
[4, 5, 6]]
B = [[1, 2], # B tiene 3 filas y 2 columnas
[3, 4],
[5, 6]]
print("La matriz A")
print(A)
print("La matriz B")
print(B)


from typing import Tuple
def shape(A: Matrix) -> Tuple[int, int]:
    "Returns (# of rows of A, # of columns of A)"
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # número de elementos de la primera fila
    return num_rows, num_cols
print(shape(A))
assert(A)==(2, 3)


##Estadistica
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

from collections import Counter
import matplotlib.pyplot as plt

friend_counts = Counter(num_friends)
xs = range(101)                         # largest value is 100
ys = [friend_counts[x] for x in xs]     # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])## el eje de x se mueve entre 0 y 101 .. el de las y va de 0 a 25
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points=len(num_friends)#204 tamaño o cantidad de datos
#el maximo valor 
largest_value=max(num_friends) #le mayor es el numero 100
#el minimo valor 
smallest_value=min(num_friends)# el menor es 1
#ordenamos sin cambiar el original y lo guardamos en una nueva variable
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]           # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 49

##Para calcular la media o promedio de los datos 
from typing import List

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

promedio=mean(num_friends)
print(promedio)

##Mediana para una cantidad de datos impares
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]
v1=[2,5,8,7,9]
print(len(v1)//2) #es la division por dos y toma la parte entera
_median_odd(v1)# primero lo ordena [2,5,7,8,9] y busca en la posicion 5//2

#Mediana para una cantidad de datos pares
def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)#ordena
    hi_midpoint = len(xs) // 2  # punto medio
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

##generico seria .. si la cantidad de elementos es par entonces que calcule o 
##use mendian_event sino usara median_odd
def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

print(_median_even(num_friends))# me da 6 con los dos OK
print(median(num_friends))

##Percentil de los datos que la mediana conincide con el 50%
def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]
#Para este caso recibe dos parametros , la lista y el percentil que queremos calcular
percentil10=quantile(num_friends, 0.10)
cuartil1=quantile(num_friends, 0.25)

quartil3= quantile(num_friends, 0.75) 
quartil2= quantile(num_friends, 0.50) 

#Moda

def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)#me da de cada valor cuantas veces de repite Counter({4: 3, 2: 2, 1: 1, 3: 1, 5: 1})
    max_count = max(counts.values())# counts.values() toma los valores de la frecuencia [3, 2, 1, 1, 1] 
    ## el max toma el mas grande que seria 3
    return [x_i for x_i, count in counts.items()#Recorre cada par (valor, frecuencia) en counts.items()#Solo guarda los valores (x_i) cuya frecuencia (count) sea igual a max_coun
            if count == max_count]
print(mode(num_friends))
#devuelve el numero [6,1] que seria que el numero 1 se repite 6 veces . seria ese la moda

#Rango es la diferencia entre el valor max y min
def data_range(xs:List[float()])->float:
    return max(xs)-min(xs)
rango= data_range(num_friends) # es 99
## Varianza 
#La varianza es una medida de dispersión estadística que indica qué tan 
#separados están los datos de un conjunto con respecto a su valor medio
from linear_algebra import sum_of_squares

def de_mean(xs: List[float])->List[float]:
    """guardamos en una lista [x1-media, x2-media....]"""
    x_bar=mean(xs)
    return [x-x_bar for x in xs]
def variance(xs:List[float])->float:
    "varianza"
    assert len(xs)>=2
    n=len(xs)
    deviations=de_mean(xs)
    return sum_of_squares(deviations)/(n-1)

varianza=variance(num_friends)
import math
##Desviacion estandar
def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))
s=standard_deviation(num_friends)
## Correlacion

from linear_algebra import dot
def covariance(xs: List[float], ys: List[float])-> float:
    assert len(xs)== len(ys)
    return dot(de_mean(xs),de_mean(ys))/(len(xs)-1)
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]

covarianzaMinutos=covariance(num_friends, daily_minutes) 
covarianzaHoras=covariance(num_friends, daily_hours) 

#esto significa las dos variables se mueven en la misma dirección.
#
