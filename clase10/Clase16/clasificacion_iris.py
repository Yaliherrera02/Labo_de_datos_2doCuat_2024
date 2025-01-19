#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:05:03 2023

@author: mcerdeiro
"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import tree
import pandas as pd

#%%######################

        ####            Análisis exploratorio

#########################
#%%        


iris = load_iris(as_frame = True)

data = iris.frame #: Un DataFrame que combina tanto los atributos (características) como la columna target.
atributos = iris.data
Y = iris.target

diccionario = dict(zip( [0,1,2], iris.target_names))
print(diccionario)



#%% Plot attribute histograms

nbins = 35

f, s = plt.subplots(2,2)
plt.suptitle('Histogramas de los 4 atributos', size = 'large')


sns.histplot(data = data, x = 'sepal length (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[0,0], palette = 'viridis')

sns.histplot(data = data, x = 'sepal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[0,1], palette = 'viridis')

sns.histplot(data = data, x = 'petal length (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[1,0], palette = 'viridis')

sns.histplot(data = data, x = 'petal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[1,1], palette = 'viridis')


#%%######################

        ####            Métodos de umbral

#########################
#%%        

def clasificador_iris(fila):
    pet_l = fila['petal length (cm)']
    if pet_l < 2.5:
        clase = 0
    elif pet_l < 4.5:
        clase = 1
    else:
        clase = 2
    return clase


#%% Definición de umbrales

umbral_0 = 2.5
umbral_1 = 4.5

plt.figure()
plt.title('Histograma de petal length y los umbrales utilizados')
sns.histplot(data = data, x = 'petal length (cm)', hue = 'target', bins = nbins, stat = 'probability',  palette = 'viridis')
plt.axvline(x=umbral_0)
plt.axvline(x=umbral_1)


#%% Clasificar de acuerdo a umbrales

data_clasif = data.copy()
data_clasif['clase_asignada'] = atributos.apply(lambda row: clasificador_iris(row), axis=1)

print(data_clasif)
#clasificador_iris(data['sepal length (cm)'], data['sepal width (cm)'], data['petal length (cm)'], data['petal width (cm)'])


#%% Matriz de confusión

clases = set(data['target'])
matriz_confusion = np.zeros((3,3))


for i in range(3):
  for j in range(3):
    filtro = (data_clasif['target']== i) & (data_clasif['clase_asignada'] == j)
    cuenta = len(data_clasif[filtro])
    matriz_confusion[i, j] = cuenta
  
print(matriz_confusion)


#%%

#exacti = sum(data_clasif['target']== data_clasif['clase_asignada'])

#%% Exactitud (accuracy)

def exactitud(clasif):
    data_temp = data_clasif.copy()
    data_temp['clase_asignada'] = atributos.apply(lambda row: clasif(row), axis=1)
    suma = sum(data_temp['target']== data_temp['clase_asignada'])
    total = len(data_clasif)
    return suma/total

    
posibles_cortes = np.arange(start= 4, stop= 6, step=0.1)
exactitudes = []

for c in posibles_cortes:
    def clasificador_temp(fila):
        pet_l = fila['petal length (cm)']
        if pet_l < 2.5:
            clase = 0
        elif pet_l < c:
            clase = 1
        else:
            clase = 2
        return clase
    exact_c = exactitud(clasificador_temp)
    exactitudes.append(exact_c)


#%% Plot accuracy

plt.figure()

plt.plot(posibles_cortes, exactitudes)
plt.xlabel('posibles cortes')
plt.ylabel('exactitud')
plt.title('Exactitud en función del corte elegido')

# umbral que da la máxima exactitud
corte_selec = posibles_cortes[np.argmax(exactitudes)]
print(corte_selec)


#%%######################

        ####            Árboles de decisión

#########################
#%%

X = atributos
Y = data['target']


#%% Plot decision tree

clf_info = tree.DecisionTreeClassifier(criterion = "entropy", max_depth=4)
clf_info = clf_info.fit(X, Y)


plt.figure(figsize= [14,8])
tree.plot_tree(clf_info, feature_names = iris['feature_names'], class_names = iris['target_names'].tolist(),filled = True, rounded = True, fontsize = 10)



#%% Class prediction

datonuevo= pd.DataFrame([dict(zip(iris['feature_names'], [6.8,3,4.5, 2.15]))])
clase_predicha = clf_info.predict(datonuevo)

print('dato nuevo:\n' + datonuevo.to_string(index=False) + '\n' + 'clase predicha: ' + str(clase_predicha))



plt.figure()
sns.scatterplot(data = data, x = 'sepal length (cm)', y = 'sepal width (cm)', hue = 'target', palette = 'viridis')
plt.scatter(datonuevo['sepal length (cm)'], datonuevo['sepal width (cm)'], color = 'magenta')
plt.title('')




#%% Class prediction (II)


f, s = plt.subplots(2,2)


sns.scatterplot(data = data, x = 'sepal length (cm)', y = 'sepal width (cm)', hue = 'target', ax=s[0,0], palette = 'viridis')
s[0,0].scatter(datonuevo['sepal length (cm)'], datonuevo['sepal width (cm)'], color = 'magenta')

sns.scatterplot(data = data, x = 'petal length (cm)', y = 'sepal width (cm)', hue = 'target', ax=s[0,1], palette = 'viridis')
s[0,1].scatter(datonuevo['petal length (cm)'], datonuevo['sepal width (cm)'], color = 'magenta')

sns.scatterplot(data = data, x = 'sepal length (cm)', y = 'petal width (cm)', hue = 'target', ax=s[1,0], palette = 'viridis')
s[1,0].scatter(datonuevo['sepal length (cm)'], datonuevo['petal width (cm)'], color = 'magenta')

sns.scatterplot(data = data, x = 'petal length (cm)', y = 'petal width (cm)', hue = 'target', ax=s[1,1], palette = 'viridis')
s[1,1].scatter(datonuevo['petal length (cm)'], datonuevo['petal width (cm)'], color = 'magenta')



#%%

# otra forma de ver el arbol
r = tree.export_text(clf_info, feature_names=iris['feature_names'])
print(r)


#%%


































