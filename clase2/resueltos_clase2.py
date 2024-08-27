import random
import numpy as np
prueba=random.random()
print(prueba)

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

"""
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
f.close()"""

"""def lanzar_dados():
    # Establecemos una semilla fija para asegurar reproducibilidad
    #random.seed(10)
    
    resultados = []
    for i in range(0,5):  # Tiramos 5 veces el dado
        # Generamos un número aleatorio entre 1 y 6
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    
    return resultados
# Ejecución de la simulación

print(lanzar_dados())"""


def generala_tirar():
    result=[]
    for i in range(0,5): 
        resultado=random.randint(1,6)
        result.append(resultado)
    print(result)
generala_tirar()

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6]) # 1 dimensión
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # 2 dimensiones
print(a[0])
print(b[0])
print(b[2][3])
print(b[2,3])
np.zeros(2) # matriz de ceros del tamaño indicado
np.zeros((2,3))


import csv

print("hola")
"""def leer_parque(nombre_archivo,parque:str):
        with open (nombre_archivo,"r" )as archivo_original:
            filas = csv.reader(archivo_original) 
            encabezado = next(filas)
            filas = list(filas) 
            encabezado= list(encabezado)
        # Iteramos sobre cada fila
        lista_con_info= []
        diccionario ={}
        for i in range (0, len(filas)):
            if filas[i][10]==parque:
                for j in range (0,len(encabezado)): #recorro lista encabezado (donde van a estar las claves)
                    claves=encabezado[j] #claves= [id_arbol,altura_tot,diametro...]
                    print(claves)
                    diccionario[claves]=filas[i][j] # HASTA ACÁ CREE EL PRIMER DICCIONARIO, AHORA NECESITO RECORRER LA SEGUNDA LINEA
                    print(diccionario[claves])
                elementos=diccionario
                print(elementos)
                lista_con_info.append(elementos)
        return lista_con_info
print(leer_parque("arboles.csv","DE PAKISTAN"))"""