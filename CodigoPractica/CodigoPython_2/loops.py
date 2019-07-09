#Simple loop
people = ['Andres', 'Alejandra', 'Benito', 'Jose']

print('****Simple loop****')

#el contador es person y toma los valores del arreglo, no sus posiciones
#si se desea usar las posiciones del arreglo se tiene que usar
#una variable extra, nombrar otra
x=0
for person in people:
  print('Current person: {0}'.format(person))  
  if(person=='Benito'):
    print ('La posicion del arreglo en donde esta Benito es: {0}'.format(x))
  x=x+1

#Break
print('****Break loop****')
for person in people:
    if person == 'Benito':
     break
    print('Current person: {0}'.format(person))
