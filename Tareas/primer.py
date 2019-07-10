sl='supervised learning'
ul='unsupervised learning'
s1='linear regression'
s2='classification'
u1='clustering'
u2='association'

#poner estas dos funciones en un modulo
def subSL():
    print('Escribe un 1 si quieres predecir un valor continuo')
    print('O escribe un 2 si quieres predecir un valor discreto y clasificarlo')
    
    subtype = raw_input("1 o 2:")
    
    if validate_type(type):
   	User.setSubtypeSL(subtype)
    else:
        print('Este programa solo acepta 1 o 2, intenta de nuevo')
        #goto 

def subUL():
    print('Escribe un 1 si quieres agrupar en clusters tus valores')
    print('O escribe un 2 si quieres asociar tus valores')

    subtype = raw_input("1 o 2:")

    if validate_type(type):
        User.setSubtypeUL(subtype)
    else:
	print('Este programa solo acepta 1 o 2, intenta de nuevo')
        #goto 





class Usuario:
    #Constructor (funcion que corre cuando haces
    #una instanciacion de una clase)
    def __init__(self, nombre, email, type, stype):
        self.nombre = nombre #se manda llamar a si misma
        self.email = email
        self.type = type
        self.stype = stype

    def saludos(self, nombre=' ', type=' ', stype=' '):
        print('Hola ' + nombre + ', este es un programa de ML que')
        print('te ayudara a predecir tus datos')

    def setName(self, nombre=''):
        self.nombre = nombre
   
    def setSubtypeSL(self, subtype=''):
        if(subtype=='1'):
          print(' ')
          print('Usaremos el metodo de regresion linear!')
          self.subtype='linear regression'
        elif(subtype=='2'):
          print(' ')
          print('Usaremos el metodo de clasificacion!')
          self.subtype='classification'
 
    def setSubtypeUL(self, subtype=''):
	if(subtype=='1'):
          print(' ')
          print('Usaremos el metodo de clustering!')
          self.subtype='clustering'
        elif(type=='2'):
          print(' ')
          print('Usaremos el metodo de asociacion!')
          self.subtype='asociacion'

 
    def setEmail(self, email=''):
        self.email = email  
 
    def setType(self, type):
        if(type=='1'):
	  print(' ')
          print('Usaremos supervised learning!')
          self.type='supervised learning'
        elif(type=='2'):
          print(' ')
          print('Usaremos unsupervised learning!')
	  self.type='unsupervised learning'
        

print('Saludos, te pediremos algunos datos antes de empezar!!')
print(' ')

nombre = raw_input("Ingresa tu nombre: ")
print(' ')
email = raw_input("Ingresa tu email: ")

User = Usuario('nombre', 'correo@hotmail.com', 'nada', 'nada')
User.setName(nombre)
User.setEmail(email)

print('Escribe un 1 si usaras datos de entrenamiento')
print('O escribe un 2 si usaras datos desconocidos')

type = raw_input("1 o 2:")

from validador_type import validate_type
if validate_type(type):
   User.setType(type)
else:
   print('Este programa solo acepta 1 o 2, intenta de nuevo')
   #goto 

if(type=='1'):
   subSL()

elif(type=='2'):
   subUL()

#User = Usuario(nombre, email)
#print(type(Joel))
#print(Joel.nombre)   #data member de la funcion __init__
#print(Joel.saludos())#metodo o funcion de la clase

