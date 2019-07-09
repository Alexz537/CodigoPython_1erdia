#Una clase es como un plano para crear objetos. Un objeto tiene  

#Create a class
class Usuario:
    #Constructor (funcion que corre cuando haces
    #una instanciacion de una clase)
    def __init__(self, nombre, email, edad):
        self.nombre = nombre #se manda llamar a si misma
        self.email = email
        self.edad = edad

    def saludos(self, num1=1):
        print(num1)
        return('Me llamo {0} y tengo {1}'.format(self.nombre, self.edad))

    def tengo_cumple(self):
        self.edad+=1

#Extend the Usuario class
class Cliente(Usuario):
    def __init__(self, nombre, email, edad): #no se pone saldo para poder 
                                             #cambiarlo cuando se necesite
        self.nombre = nombre #se manda llamar a si misma
        self.email = email
        self.edad = edad
        self.saldo = 0

    def establecer_saldo(self, saldo):
        self.saldo = saldo

    def saludos(self):
        return ('Me llamo {0}, tengo {1} y mi saldo es ${2}'.format(self.nombre, self.edad, self.saldo))


#Init un objeto del tipo usuario
Joel = Usuario('Joel', 'joel@gmail.com', 18)
print(type(Joel))
print(Joel.nombre)   #data member de la funcion __init__
print(Joel.saludos())#metodo o funcion de la clase

#Init un objeto del tipo cliente
Alex = Cliente('Alex', 'alex@yahoo.com.mx', 21)
print(type(Alex))
print(Alex.nombre)
Alex.establecer_saldo(5e8)
print(Alex.saludos())


# Joel.tengo_cumple()
# print(Joel.salud)

