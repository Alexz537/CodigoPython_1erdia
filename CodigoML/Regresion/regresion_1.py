#import
import matplotlib.pyplot as plt #este nombre se le puso por plotting
#plt.use('TkAgg')
import numpy as np #buscar que opciones tiene

#importing from scikit-learn
from sklearn import datasets, linear_model

#Load dataset
house_price = [245,321,279,308,199,219,405,324,319,255]
size = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

print(len(house_price))
print(len(size))

#Reshape the input to your regression
size2 = np.array(size).reshape((-1,1)) #aqui se usa el numpy para que ordene 
                                       #los datos de 1 en 1, no puede 
                                       #ordenarlos en un numero no divisible
				       #entre el tamano

print(size2)

#by using fit module in linear regression, user can fit the data rapido
#y seguido
regr = linear_model.LinearRegression()#clase
regr.fit(size2, house_price)
print('Coeficients: {0}'.format(regr.coef_))
print('intercepts: {0}'.format(regr.intercept_))

#Formula obtained for the trained model
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)

#PLotting the prediction line
graph('regr.coef_*x + regr.intercept_', range(500,2000))#esto es para visualizar
plt.scatter(size, house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
#plt.show()
plt.savefig("regresion.pdf")
