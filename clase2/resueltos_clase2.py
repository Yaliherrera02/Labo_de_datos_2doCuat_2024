import random
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
print("aca")

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6]) # 1 dimensión
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # 2 dimensiones
print(a[1])
print(b[0])
print(b[2][3])
print(b[2,3])
print(np.zeros(2)) # matriz de ceros del tamaño indicado
np.zeros((2,3))

import csv

print("hola")
def leer_parque(nombre_archivo,parque:str):
        with open (nombre_archivo,"r") as archivo_original:
            filas = csv.reader(archivo_original) 
            encabezado = next(filas)
            filas = list(filas) 
            encabezado= list(encabezado)
        # Iteramos sobre cada fila
        lista_con_info= []
        diccionario ={}
        for i in range (0, len(filas)):
            if filas[i][10]==parque:
                for j in range (0,len(encabezado)):
                    if filas[i][10]==parque: #recorro lista encabezado (donde van a estar las claves)
                        claves=encabezado[j] #claves= [id_arbol,altura_tot,diametro...]
                        print(claves)
                        diccionario[claves]=filas[i][j] # HASTA ACÁ CREE EL PRIMER DICCIONARIO, AHORA NECESITO RECORRER LA SEGUNDA LINEA filas[i][j]=filas[3][]
                        print(diccionario[claves])
                        elementos=diccionario
                lista_con_info.append(elementos)

        return lista_con_info

print(leer_parque("arboles.csv","DE PAKISTAN"))
#Conjuntos
#Se arman con llaves {}.
a = {2, 4}
citricos = {'Naranja', 'Limón', 'Mandarina'}
citricos = set(['Naranja', 'Limón', 'Mandarina'])
'Naranja' in citricos
citricos.add('Pomelo')
citricos.remove('Naranja')
len(a)

def especies(lista_arboles):
    conjunto=set()
    for i in range(0,len(lista_arboles)):
        diccionario=lista_arboles[i]
        nombre_arbol=diccionario["nombre_com"]
        conjunto.add(nombre_arbol)
    return conjunto


def contar_ejemplares(lista_arboles):

    frecuencia={}
    for i in range (0, len(lista_arboles)):
        nombre_arbol=lista_arboles[i]["nombre_com"]
        if nombre_arbol in frecuencia: ## Si ya esta la especie en el diccionario, entonces:
                frecuencia[nombre_arbol] += 1 #frecuencia[n] = frecuencia[n] + 1
                                                                    #frecuencia[palabra]=1+1
        else:                       # la línea frecuencia[n] += 1 incrementa en 1 el valor asociado a la clave palabra en el diccionario frecuencia. 
                frecuencia[nombre_arbol] = 1 
    return frecuencia


def obtener_alturas(lista_arboles,especie:str):
    lista_alturas=[]
    for i in range (len(lista_arboles)):
          if especie==lista_arboles[i]["nombre_com"]:
               altura=lista_arboles[i]["altura_tot"]
               altura=float(altura)
               lista_alturas.append(altura)
    return lista_alturas
     
#print(obtener_alturas([{'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}],"Pata de vaca  (Pezuña de vaca)"))