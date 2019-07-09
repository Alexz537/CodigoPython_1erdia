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

#String loop
print('****String loop****')
for x in 'banana':
    print(x)

#Continue
print('****Continue loop****')
for person in people:
    if person == 'Benito': 
       continue #esta instruccion, hace que la variable del ciclo aumente
                #ignorando las instrucciones siguientes
    print('Current person: {0}'.format(person))
    

#Range
print('****Range loop****')
for i in range(0,len(people)): #aqui va de 0 a un numero antes de len
    print(people[i])
    
#Range defined
for i in range(0,11+50): #de 0 hasta 10
    print('Number {0}'.format(i))

#Range de tres en tres
print('****Ciclo de tres en tres****')
for i in range(0,70,3):
    print('Number {0}'.format(i))

#Ciclo While
count = 0
while count <= 10:
      print('Count: {0}'.format(count))
      count+=1

