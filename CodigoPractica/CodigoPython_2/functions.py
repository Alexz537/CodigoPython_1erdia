#Para definir una funcion
def decirHola(nombre=''):#eso se inicializo como string vacio para indicar
			 #que el parametro de esa funcion es un string
    print('Hola {0}'.format(nombre))

decirHola('Andres')
decirHola()

#Funcion que me regresa un valor
def hacerSuma(num1, num2):#firma con dos argumentos
    total = num1 + num2
    return (str(total) + 'es el resultado') #aqui se cambia total de int a string

#es mejor asignar el resultado a una variable si se quiere usar
hacerSuma(2,3)
print(hacerSuma(2,3), type(hacerSuma(2,3)))


