#Mi primer programa

#int=1, float=1.5, str='Hola', bool=True

print('Hola Mundo')

x = 1		 #int
y = 3.0		 #float
name = 'Andres'	 #name
is_cool = True	 #bool

#multiple assigments
x, y, name, is_cool = (1, 2.5,'Joel', True)

#basic math
a = x + y

print x,y,name,is_cool

print a

#check the type
print(type(x))
print(type(name))

#cast, e.g. x to string

x = str(x)	#passing x
y = int(y)	#passing y
z = float(y) 	#z es ahora el flotante de y

print(type(x),x)
print(type(y),y)
print(type(z),z)

