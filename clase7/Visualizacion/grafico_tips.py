import pandas as pd
import matplotlib.pyplot as plt # Para graficar series multiples
from   matplotlib import ticker

carpeta = "/home/alison/Documents/FACULTAD 2024/Labo_de_datos_2doCuat_2024/clase7/Visualizacion/"
tips= pd.read_csv(carpeta+"tips.csv")

"""
#%%############## DISTRIBUCION SEGUN DOS VARIABLES

# Armamos dos subsets: Male y Female
obsFemale=ageAtDeath[ageAtDeath['Sex']=='Female']['AgeAtDeath']
obsMale  =ageAtDeath[ageAtDeath['Sex']=='Male'  ]['AgeAtDeath']


fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
# bins ...
width = 7                                                              # Cada esta cantidad de anios
bins = np.arange(1,114, width)                                         # Desde 1 a 113 (inclusive) cada width anios
# Contamos cuantos de los datos caen en cada uno de los bins
countsFemale, bins = np.histogram(obsFemale, bins=bins)     # Hace el histograma (por bin)
countsMale  , bins = np.histogram(obsMale  , bins=bins)     # Hace el histograma (por bin)
# Si queremos graficar la frecuencia en vez de la cantidad, la calculamos
freqFemale = countsFemale / float(countsFemale.sum())
freqMale   = countsMale   / float(countsMale.sum())

# Fijamos la ubicacion de cada bin
center = (bins[:-1] + bins[1:]) / 2                         # Calcula el centro de cada barra

# Graficamos Female
ax.bar(x=center-width*0.2,        # Ubicacion en el eje x de cada bin
   height=countsFemale, # Alto de la barra
   width=width*.4,         # Ancho de la barra
   align='center',      # Barra centrada
   color='orange',     # Color de la barra
   edgecolor='black')   # Color del borde de la barra

# Graficamos Male
ax.bar(x=center+width*0.2,        # Ubicacion en el eje x de cada bin
   height=countsMale,   # Alto de la barra
   width=width*.4,      # Ancho de la barra
   align='center',      # Barra centrada
   color='skyblue',     # Color de la barra
   edgecolor='black')   # Color del borde de la barra

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Cantidad de personas')
ax.set_ylim(0,100)

# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]              # Define los limites de los bins

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
       for i, edge in enumerate(bin_edges[:-1])] # Genera el string de los labels del estilo (v1, v2]

ax.set_xticks(bin_edges[:-1])                        # Ubica los ticks del eje x
ax.set_xticklabels(labels, rotation=45, fontsize=12) # Asigna labels a los ticks del eje x
ax.tick_params(bottom = False)                       # Remueve los ticks del eje x

#Agrega leyenda
ax.legend(['Femenino', 'Masculino'], loc='upper left')
plt.show()
"""

