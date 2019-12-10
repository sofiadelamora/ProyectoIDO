import matplotlib.pyplot as plt
import pandas as pd
from scipy import spatial
##from docplex.mp.model import Model
#import docplex.mp.solution as Solucion

#Primero creamos los nodos que son las ciudades y los arcos que son los caminos.
coordenadas=pd.read_csv(r"C:\Users\J16911\Downloads\data.csv") #Importamos el documento que contiene las coordendas de las ciudades
coordenadas.columns=["ciudad", "c_x", "c_y"] #nombres de las columnas del dataframe
coordenadas = coordenadas.drop("ciudad", axis=1)

ciudades=[i for i in range(len(coordenadas))] #Se crean las 980 ciuades
caminos =[(i,j) for i in ciudades for j in ciudades if i!=j] #todos las uniones posibles entre ciudades



lo=coordenadas["c_x"].tolist() #coordendas de longitud
la=coordenadas["c_y"].tolist() #coordenadas de latitud


plt.figure(figsize=(10,7)) #Grafiquemos las ciudades de Luxemburgo
plt.scatter(lo,la,color='black')
plt.xlabel("Distancia X")
plt.ylabel("Distancia Y")
plt.title("Ciudades en Luxemburgo")  
plt.show()

matriz_distances = spatial.distance.cdist(coordenadas, coordenadas, metric='euclidean') #Creamos la matriz de distancias donde la entrada (i,j) es la distancia de la ciudad i a la ciudad j

##-------------------------------------------------------------

