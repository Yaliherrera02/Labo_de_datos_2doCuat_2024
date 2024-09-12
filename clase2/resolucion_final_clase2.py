import pandas as pd
import csv
import numpy as np
#EJEMPLO DE DF:

import pandas as pd

# Crear un DataFrame con nombres de columnas como enteros
data = {
    0: ['Juan', 'Ricardo', 'Rocio', 'Mariela', 'Lucia', 'Martina', 'Sofia'],
    1: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    2: [1, 2, 3, 4, 5, 6, 7],
    3: [3, 2, 1, 4, 6, 2, 4]
}
df = pd.DataFrame(data)


def leer_parque(nombre_archivo, parque: str):
    # Leer el archivo CSV directamente con pandas
    df = pd.read_csv(nombre_archivo)
    filas = csv.reader(nombre_archivo) 
    # Filtrar el DataFrame por el nombre del parque
    df_filtrado = df[df['espacio_ve'] == parque] 
    lista_con_info = []
    for i, row in df_filtrado.iterrows():
        # Crear un diccionario para la fila actual
        diccionario = {}
        print(i,row)
        # Iterar sobre cada columna y agregar al diccionario
        for col in df_filtrado.columns:
            diccionario[col] = row[col] #SACO EL ELEMENTO QUE HAY EN ESA FILA, OSEA SACO EL ELEMENTO ROW[LONG]
        
        # Agregar el diccionario a la lista
        lista_con_info.append(diccionario)
    return lista_con_info

print(leer_parque("arboles.csv", "HOLANDA"))

#print((leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ')))
def especies(lista_arboles):
    conjunto=set()
    for i in range(0,len(lista_arboles)):
        diccionario=lista_arboles[i]
        nombre_arbol=diccionario["nombre_com"]
        conjunto.add(nombre_arbol)
    return conjunto
#print(especies([{'long': -58.4187986351, 'lat': -34.5723165414, 'id_arbol': 2517, 'altura_tot': 16, 'diametro': 70, 'inclinacio': 0, 'id_especie': 55, 'nombre_com': 'Fenix', 'nombre_cie': 'Phoenix canariensis', 'tipo_folla': 'Palmera', 'espacio_ve': 'HOLANDA', 'ubicacion': 'ISABEL, INFANTA, AV. - IRAOLA, AV. - MONTT, PEDRO, PRES., AV. - DEL LIBERTADOR, AV.', 'nombre_fam': 'Arecaceas', 'nombre_gen': 'Phoenix', 'origen': 'Exótico', 'coord_x': 104083.42188, 'coord_y': 106317.168175}, {'long': -58.4185582155, 'lat': -34.5723381796, 'id_arbol': 2518, 'altura_tot': 2, 'diametro': 200, 'inclinacio': 0, 'id_especie': 138, 'nombre_com': 'Palmito', 'nombre_cie': 'Chamaerops humilis', 'tipo_folla': 'Palmera', 'espacio_ve': 'HOLANDA', 'ubicacion': 'ISABEL, INFANTA, AV. - IRAOLA, AV. - MONTT, PEDRO, PRES., AV. - DEL LIBERTADOR, AV.', 'nombre_fam': 'Arecaceas', 'nombre_gen': 'Chamaerops', 'origen': 'Exótico', 'coord_x': 104105.485039, 'coord_y': 106314.756253}]))