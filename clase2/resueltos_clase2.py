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
""""
a = np.array([1, 2, 3, 4, 5, 6]) # 1 dimensión
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # 2 dimensiones
print(a[1])
print(b[0])
print(b[2][3])
print(b[2,3])
print(np.zeros(2)) # matriz de ceros del tamaño indicado
np.zeros((2,3))"""

import csv
import pandas as pd
def leer_parque(nombre_archivo:str, parque:str):
    lista_arboles = []
    with open(nombre_archivo, 'r', encoding="utf8") as archivo:
        filas = csv.reader(archivo)
        encabezado=next(filas)
        for fila in filas:
            if fila[10] == parque:
                registro=dict(zip(encabezado,fila))
                lista_arboles.append(registro)
                
    return lista_arboles

#print(leer_parque("arboles.csv","DE PAKISTAN"))
#Conjuntos
#Se arman con llaves {}.
a = {2, 4}
citricos = {'Naranja', 'Limón', 'Mandarina'}
citricos = set(['Naranja', 'Limón', 'Mandarina'])
'Naranja' in citricos
citricos.add('Pomelo')
citricos.remove('Naranja')
len(a)

def especies(lista_arboles:list[dict]):
    conjunto=set()
    for i in range(0,len(lista_arboles)):
        diccionario=lista_arboles[i]
        nombre_arbol=diccionario["nombre_com"]
        conjunto.add(nombre_arbol)
    return conjunto


def contar_ejemplares(lista_arboles:list[dict]):

    frecuencia={}
    for i in range (0, len(lista_arboles)):
        nombre_arbol=lista_arboles[i]["nombre_com"]
        if nombre_arbol in frecuencia: ## Si ya esta la especie en el diccionario, entonces:
                frecuencia[nombre_arbol] += 1 #frecuencia[n] = frecuencia[n] + 1
                                                                    #frecuencia[palabra]=1+1
        else:                       # la línea frecuencia[n] += 1 incrementa en 1 el valor asociado a la clave palabra en el diccionario frecuencia. 
                frecuencia[nombre_arbol] = 1 
    return frecuencia


def obtener_alturas (lista_arboles:list[dict], especie:str):
    lista_alturas=[]
    for i in range (len(lista_arboles)):
          if especie==lista_arboles[i]["nombre_com"]: #lista_arb=[dic,dic,dic]
               altura=lista_arboles[i]["altura_tot"]
               altura=float(altura)
               lista_alturas.append(altura)
    return lista_alturas




#print(obtener_alturas([{'long': '-58.4276949484', 'lat': '-34.5626695086', 'id_arbol': '2519', 'altura_tot': '34', 'diametro': '113', 'inclinacio': '0', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103267.46115599999', 'coord_y': '107387.653399'}, {'long': '-58.423979035900004', 'lat': '-34.5639321271', 'id_arbol': '2520', 'altura_tot': '29', 'diametro': '84', 'inclinacio': '12', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103608.426612', 'coord_y': '107247.461347'}, {'long': '-58.4260824338', 'lat': '-34.563225950500005', 'id_arbol': '2526', 'altura_tot': '15', 'diametro': '15', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103415.421226', 'coord_y': '107325.87696699999'}, {'long': '-58.422928114399994', 'lat': '-34.563997685100006', 'id_arbol': '2527', 'altura_tot': '11', 'diametro': '50', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103704.86035700001', 'coord_y': '107240.152975'}, {'long': '-58.4227527407', 'lat': '-34.5643166504', 'id_arbol': '2528', 'altura_tot': '15', 'diametro': '18', 'inclinacio': '11', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103720.94797000001', 'coord_y': '107204.76022699999'}, {'long': '-58.42255730390001', 'lat': '-34.5644326026', 'id_arbol': '2529', 'altura_tot': '27', 'diametro': '56', 'inclinacio': '0', 'id_especie': '93', 'nombre_com': 'Kauri de corteza lisa', 'nombre_cie': 'Agathis robusta', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Araucariaceas', 'nombre_gen': 'Agathis', 'origen': 'Exótico', 'coord_x': '103738.874166', 'coord_y': '107191.890137'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}], "Pata de vaca  (Pezuña de vaca)"))

def maxima_altura (lista_arboles:list[dict], especie:str):
     alturas=obtener_alturas(lista_arboles, especie)
     return max(alturas)

#print(maxima_altura([{'long': '-58.4276949484', 'lat': '-34.5626695086', 'id_arbol': '2519', 'altura_tot': '34', 'diametro': '113', 'inclinacio': '0', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103267.46115599999', 'coord_y': '107387.653399'}, {'long': '-58.423979035900004', 'lat': '-34.5639321271', 'id_arbol': '2520', 'altura_tot': '29', 'diametro': '84', 'inclinacio': '12', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103608.426612', 'coord_y': '107247.461347'}, {'long': '-58.4260824338', 'lat': '-34.563225950500005', 'id_arbol': '2526', 'altura_tot': '15', 'diametro': '15', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103415.421226', 'coord_y': '107325.87696699999'}, {'long': '-58.422928114399994', 'lat': '-34.563997685100006', 'id_arbol': '2527', 'altura_tot': '11', 'diametro': '50', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103704.86035700001', 'coord_y': '107240.152975'}, {'long': '-58.4227527407', 'lat': '-34.5643166504', 'id_arbol': '2528', 'altura_tot': '15', 'diametro': '18', 'inclinacio': '11', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103720.94797000001', 'coord_y': '107204.76022699999'}, {'long': '-58.42255730390001', 'lat': '-34.5644326026', 'id_arbol': '2529', 'altura_tot': '27', 'diametro': '56', 'inclinacio': '0', 'id_especie': '93', 'nombre_com': 'Kauri de corteza lisa', 'nombre_cie': 'Agathis robusta', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Araucariaceas', 'nombre_gen': 'Agathis', 'origen': 'Exótico', 'coord_x': '103738.874166', 'coord_y': '107191.890137'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}], "Pata de vaca  (Pezuña de vaca)"))


def promedio_alturas (alturas: list[float]):     
   promedio=sum(alturas)/len(alturas)
   return promedio



#print(promedio_alturas([{'long': '-58.4276949484', 'lat': '-34.5626695086', 'id_arbol': '2519', 'altura_tot': '34', 'diametro': '113', 'inclinacio': '0', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103267.46115599999', 'coord_y': '107387.653399'}, {'long': '-58.423979035900004', 'lat': '-34.5639321271', 'id_arbol': '2520', 'altura_tot': '29', 'diametro': '84', 'inclinacio': '12', 'id_especie': '330', 'nombre_com': 'Eucalipto', 'nombre_cie': 'Eucalyptus sp.', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Mirtáceas', 'nombre_gen': 'Eucalyptus', 'origen': 'Exótico', 'coord_x': '103608.426612', 'coord_y': '107247.461347'}, {'long': '-58.4260824338', 'lat': '-34.563225950500005', 'id_arbol': '2526', 'altura_tot': '15', 'diametro': '15', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103415.421226', 'coord_y': '107325.87696699999'}, {'long': '-58.422928114399994', 'lat': '-34.563997685100006', 'id_arbol': '2527', 'altura_tot': '11', 'diametro': '50', 'inclinacio': '0', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103704.86035700001', 'coord_y': '107240.152975'}, {'long': '-58.4227527407', 'lat': '-34.5643166504', 'id_arbol': '2528', 'altura_tot': '15', 'diametro': '18', 'inclinacio': '11', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103720.94797000001', 'coord_y': '107204.76022699999'}, {'long': '-58.42255730390001', 'lat': '-34.5644326026', 'id_arbol': '2529', 'altura_tot': '27', 'diametro': '56', 'inclinacio': '0', 'id_especie': '93', 'nombre_com': 'Kauri de corteza lisa', 'nombre_cie': 'Agathis robusta', 'tipo_folla': 'Árbol Latifoliado Perenne', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Araucariaceas', 'nombre_gen': 'Agathis', 'origen': 'Exótico', 'coord_x': '103738.874166', 'coord_y': '107191.890137'}, {'long': '-58.423091223', 'lat': '-34.5644933544', 'id_arbol': '2530', 'altura_tot': '13', 'diametro': '32', 'inclinacio': '20', 'id_especie': '43', 'nombre_com': 'Pata de vaca  (Pezuña de vaca)', 'nombre_cie': 'Bauhinia forticata', 'tipo_folla': 'Árbol Latifoliado Caducifolio', 'espacio_ve': 'DE PAKISTAN', 'ubicacion': 'DORREGO, AV. - FIGUEROA ALCORTA, PRES., AV.- MENDEZ, AGUSTIN - CALLE DE ACCESO AL HIPODROMO', 'nombre_fam': 'Leguminosas', 'nombre_gen': 'Bauhinia', 'origen': 'Nativo/Autóctono', 'coord_x': '103689.875895', 'coord_y': '107185.179305'}], "Pata de vaca  (Pezuña de vaca)"))
def tabla_jacarandas ():
    altura_gral_paz = obtener_alturas(leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ"), "Jacarandá")
    altura_los_andes = obtener_alturas(leer_parque("arbolado-en-espacios-verdes.csv", "ANDES, LOS"), "Jacarandá")
    altura_centenario = obtener_alturas(leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO"), "Jacarandá")

    data = {'Medida':['Max', 'Prom'], 
           'General Paz' : [max(altura_gral_paz), promedio_alturas(altura_gral_paz)],
            'Los Andes' : [max(altura_los_andes), promedio_alturas(altura_los_andes)],
            'Centenario' : [max(altura_centenario), promedio_alturas(altura_centenario)],
        }  
    df = pd.DataFrame (data)
    return df
print(tabla_jacarandas())

def obtener_inclinaciones (lista_arboles:list[dict], especie:str):
    lista_inclinaciones=[]
    for i in range (len(lista_arboles)):
          if especie==lista_arboles[i]["nombre_com"]: #lista_arb=[dic,dic,dic]
               inclinacion=lista_arboles[i]["inclinacio"]
               inclinacion=float(inclinacion)
               lista_inclinaciones.append(inclinacion)
    return lista_inclinaciones


def especimen_mas_inclinado (lista_arboles:list[dict]):
    mayorIncli=0.0
    mas_inclinado=""
    lista_de_especies=especies(lista_arboles)
    for especie in lista_de_especies:
        comparado=max(obtener_inclinaciones(lista_arboles,especie))
        if comparado>mayorIncli:#Pisa todos las especies de la lista de especies que no tengan la inclinacion mayor
            mayorIncli=comparado
            mas_inclinado=especie 
    return mayorIncli,mas_inclinado
arboles_en_gral_paz=leer_parque("arbolado-en-espacios-verdes.csv","GENERAL PAZ")
arboles_en_centenario=leer_parque("arbolado-en-espacios-verdes.csv","CENTENARIO")
arboles_en_los_andes=leer_parque("arbolado-en-espacios-verdes.csv","ANDES, LOS")

     
#print(especimen_mas_inclinado(arboles_en_centenario))
#print(especimen_mas_inclinado(arboles_en_gral_paz))
#print(especimen_mas_inclinado(arboles_en_los_andes)) DADO UN ESPACIO VERDE RETORNA LA ESPECIE MAS INCLINADA DE TODAS LAS ESPECIES QUE HAY EN ESA LISTA

def especie_promedio_mas_inclinada(lista_arboles:list[dict]):
    especies_con_inclinaciones=[]
    lista_de_especies=especies(lista_arboles)
    inclinacion_mayor=0.0
    #especie_con_mayor_inclinacion = lista_de_especies[0]
    print(type(lista_de_especies), "\n",type(lista_arboles))
    for especie in lista_de_especies:
        #print(sum(obtener_inclinaciones(lista_arboles,especie)))
        #print(len(obtener_inclinaciones(lista_arboles,especie))) #TENGO QUE SACAR LOS CEROS DE LA LISTA!!
        promedio_inclinacion= sum(obtener_inclinaciones(lista_arboles,especie))/len(obtener_inclinaciones(lista_arboles,especie))
        #especie_con_promedio_inclinacion=(especie,promedio_inclinacion)
        if promedio_inclinacion > inclinacion_mayor: 
             inclinacion_mayor = promedio_inclinacion
             especie_con_mayor_inclinacion = especie
        
        #especies_con_inclinaciones.append(especie_con_promedio_inclinacion)
    return inclinacion_mayor, especie_con_mayor_inclinacion
    """
    for i in range (0, len(especies_con_inclinaciones)):
        if especies_con_inclinaciones[i][1]>inclinacion_mayor:
            especie_con_mayor_inclinacion_promedio=(especies_con_inclinaciones[i][0],especies_con_inclinaciones[i][1])
            return especie_con_mayor_inclinacion_promedio"""
        
print("ESPECIE MAS INCLINADA",especie_promedio_mas_inclinada(arboles_en_los_andes))