#Este programa toma una base de datos (de condiciones climaticas)
#e identifica cuales son las regiones
#donde se espera que exista mas lluvia
#usando el algoritmo de kMeans de ML

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

#funcion para estimar los controles de cada cluster
def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)

    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum(())
  return idx

#Carguemos una base de datos del clima
data = loadmat('data/clustering_colors.mat')
X = data['X']

#Propongamos unos centroides iniciales (aleatorios o con valores dados)
initial_centroids = initial_centroids = np.array([[3, 3], [6, 2], [8,]])

#Estimemos 
