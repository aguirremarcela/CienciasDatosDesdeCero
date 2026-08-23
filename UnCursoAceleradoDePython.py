#Formato con espacios en blanco
# El signo de la almohadilla marca el comienzo de un comentario. Python
# ignora los comentarios, pero son útiles para cualquiera que lea el código.
for i in [1, 2, 3, 4, 5]:
    print(i) # primera línea del bloque "for i"
for j in [1, 2, 3, 4, 5]:
    print(j) # primera línea del bloque "for j"
    print(i + j) # última línea del bloque "for j"

print(i) # última línea del bloque "for i"
print("done looping")

for i in [1, 2, 3, 4, 5]:
# observe la línea en blanco
    print(i)
    
##Modulos

import re
my_refex= re.compile("[0-9]",re.I)

#Otro forma analoga 
# import re as regex
#my_refex= regex.compile("[0-9]",regex.I)

#Algo similar cuando se quiere visualizar datos con con matplotlib
#import matplotlib.pyplot as plt
#plt.plot(...) para usarlo


###Funciones

def double(x):
    "Esta funcion multiplica por dos la entrada"
    return x*2

print(double(5))
#Output :10

def apply_to_one(f):
    "Calls the function f with 1 as its argument"
    return f(1)
my_double = double # se refiere a la función anteriormente definida
x =apply_to_one(my_double)
y = apply_to_one(lambda x: x + 4) # es igual a 5
print(y)
