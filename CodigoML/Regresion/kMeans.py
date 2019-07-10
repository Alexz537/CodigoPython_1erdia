#Importing Numpy, matplotlib and sklearn libraries

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")# para darle estilo

#Que tipo de machine learning usaremos
from sklearn.cluster import KMeans

#Preprocesamiento
x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show()#esto muestra la grafica

#Like we did before, convert our data to a numpy array
x = np.array([[1,2], [5,8], [1.5,1.8], [8,8], [1,0.6], [9,11]])#igual que 
							       #reshape

#Initialize the kMeans algorithm
kmeans = KMeans(n_cluster=2)#define cuantos clusters queremos
kmeans.fit(x)#corre el algoritmo

#Getting the values of centroids and labels based in the fitment
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
print(**********)
print(type(centroids))
print(type(labels))


colors =["g.","r.","c.","y."]

for i in range(len(x)):
    print('coordinate: ', X[i], 'label: ', labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
    #esto anterior solo muestra los puntos en el plano

plt.scatter(centroids[:, 0], centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
