import random
"""prueba=random.random()
print(prueba)"""

random.seed(34)
prueba=random.random()
print(prueba)

import math

# Ejemplo 1: Raíz cuadrada
raiz = math.sqrt(2)
print(f"La raíz cuadrada de 2 es {raiz}")

# Definimos x para los otros ejemplos
x = 3

# Ejemplo 2: Exponencial
exponencial = math.exp(x)
print(f"El valor de e elevado a {x} es {exponencial}")

# Ejemplo 3: Coseno
coseno = math.cos(x)
print(f"El coseno de {x} radianes es {coseno}")

# Ejemplo 4: MCD (Máximo Común Divisor)
mcd = math.gcd(15, 12)
print(f"El MCD de 15 y 12 es {mcd}")

"""def leer_parque(nombre_archivo,parque:str):
    with open (nombre_archivo,"r") as archivo:
        lineas=archivo.read()"""


import csv

f = open("arboles.csv")
filas = csv.reader(f)
for fila in filas:
    print(fila)
f.close()


import csv

def imprimir_todas_las_lineas():
    archivo_csv = "arboles.csv"
    # Abrimos el archivo y lo asociamos a la variable 'archivo_original'
    with open(archivo_csv, "r") as archivo_original:
        # Usamos csv.reader para leer el archivo
        filas = csv.reader(archivo_original)
        # Iteramos sobre cada fila
        for fila in filas:
            print(fila)

# Llamamos a la función para probarla
imprimir_todas_las_lineas()


f = open("arboles.csv")
filas = csv.reader(f)
encabezado = next(filas)  # un paso del iterador
for fila in filas:        # ahora el iterador sigue desde la segunda fila
    print(fila)
f.close()











    
