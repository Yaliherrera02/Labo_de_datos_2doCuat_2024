from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import tree
import pandas as pd

carpeta = '/home/Estudiante/Descargas/'

test =pd.read_csv('test_titanic.csv')
competencia = pd.read_csv('titanic_competencia.csv')
training = pd.read_csv('titanic_training.csv')

#%% 
nbins = 35

f, s = plt.subplots(2,2)
plt.suptitle('Histogramas de los 4 atributos', size = 'large')


sns.histplot(data = training, x = 'Survived', hue = 'Survived', bins = nbins, stat = 'probability', ax=s[0,0], palette = 'viridis')

sns.histplot(data = training, x = 'Age', hue = 'Survived', bins = nbins, stat = 'probability', ax=s[1,0], palette = 'viridis')

sns.histplot(data = training, x = 'Sex', hue = 'Survived', bins = nbins, stat = 'probability', ax=s[0,1], palette = 'viridis')

sns.histplot(data = training, x = 'Pclass', hue = 'Survived', bins = nbins, stat = 'probability', ax=s[1,1], palette = 'viridis')
#%% 
def clasificador_titanic(competencia):
    vive = False
    if ( competencia['Sex'] == 'female' or competencia['Pclass'] == 1.0 or (competencia['Age'] >=0 and competencia['Age'] <= 20 )):
        vive = True
    return vive

titanic_clasif = competencia.copy()
titanic_clasif['¿vive?'] = competencia.apply(lambda row: clasificador_titanic(row), axis=1)

print(titanic_clasif)



"""def clasificador_titanic2(competencia):
    vive = False
    if ( competencia['Sex'] == 'female' and competencia['Pclass'] == 1.0 and competencia['Age'] >= 10 and competencia['Age'] <= 30 ):
        vive = True
    return vive

titanic_clasif = competencia.copy()
titanic_clasif['¿vive?'] = competencia.apply(lambda row: clasificador_titanic(row), axis=1)

print(titanic_clasif)

"""