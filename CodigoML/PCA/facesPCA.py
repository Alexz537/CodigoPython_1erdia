import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

def pca(X):
    #Normalizar las caracteristicas
    X = (X - X.mean()) / X.std()
    
    #Obtener la matriz de covarianza
    X = np.matrix(X)#np agarra un set y convierte en matriz
    cov = (X.T * X) / X.shape[0]

    #Obtener SVD
    U, S, V = np.linalg.svd(cov)
  
    return U, S, V

def project_data(X, U, k):
    U_reduced = U[:,:k]
    return np.dot(X, U_reduced) #entre dos vectores hace el producto punto

def recover_data(Z, U, k):
    U_reduced = U[:,:k]
    return np.dot(Z, U_reduced.T)

faces = loadmat('data/pca_faces.mat')
X = faces['X']
X.shape

#for i in range(100):
	face = np.reshape(X[i,:], (32, 32))#aqui si quieres varias imagenes
	plt.imshow(face)
	plt.savefig(str(i)+'face_inicial.png')

