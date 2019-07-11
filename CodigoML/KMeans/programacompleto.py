import numpy as npy
import pandas as pds
import matplotlib.pyplot as pltt
import seaborn as sbb
from scipy.io import loadmat

import modulokMeans as god

#primero la grafica
#Carguemos una base de datos del clima
data = loadmat('data/clustering_colors.mat')
X = data['X']

#Propongamos unos centroides iniciales (deben ser aleatorios o con valores dados)
initial_centroids = npy.array([[3, 3], [6, 2], [8,5]])
#pusimos solo 3

#Estimemos donde estan los centroides mas cercanos a nuestros puntos 
idx = god.find_closest_centroids(X, initial_centroids)
print(idx[0:1000])#el indice del centroide en el que esta cada dato en el rango

#Escribimos el algoritmo (nuestro resultado es las posiciones de los centroides)
idx, centroids = god.run_k_means(X, initial_centroids, 10)#el 10 es las veces definidas que busca, mientras mas, mejor
#print(idx)
print(centroids)

#hacer graficas
#Aqui definimos nuestros cluster
cluster1 = X[npy.where(idx == 0)[0],:]
cluster2 = X[npy.where(idx == 1)[0],:]
cluster3 = X[npy.where(idx == 2)[0],:]

fig, ax = pltt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()

pltt.xlabel('Diferencia de temperatura')
pltt.ylabel('Diferencia de presion')
pltt.savefig("god_graphic.pdf")

#Ahora haremos el pajaro

#Cargamos la imagen
data_imagen = loadmat('data/bird_small_kmeans.mat')
A = data_imagen['A']
A.shape

#Normalicemos los rangos de los valores
A = A / 255.

#reshape el arreglo 
Y = npy.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

#iniciar los centroides aleatoriamente
initial_centroids_2 = god.init_centroids(Y, 16)

#Correr el algoritmo
idy, centroids_2 = god.run_k_means(Y, initial_centroids_2, 10)

#Obtener los centroides mas cercanos una vez mas
idy = god.find_closest_centroids(Y, centroids_2)

#mapear cada pixel al valor del centroide
Y_recovered = centroids_2[idy.astype(int),:]

#Recambiar a las dimensiones originales
Y_recovered = npy.reshape(Y_recovered, (A.shape[0], A.shape[1], A.shape[2]))

pltt.imshow(Y_recovered)
pltt.savefig('godbird.png')

