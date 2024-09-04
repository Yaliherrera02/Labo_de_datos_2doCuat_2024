import pandas as pd
import csv

#
def leer_parque(nombre_archivo, parque: str):
    # Leer el archivo CSV directamente con pandas
    df = pd.read_csv(nombre_archivo)
    
    # Filtrar el DataFrame por el nombre del parque
    df_filtrado = df[df['espacio_ve'] == parque] 
    return df_filtrado
print(leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ"))