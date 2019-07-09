#Python tiene funciones para crear, leer, actualizar y eliminar archivos

#Abrir un archivo
miArchivo = open('miArchivo.txt','w')#open es el constructor y w es de write

#Obtener info de este archivo
print('Name: ', miArchivo.name)
print('Esta cerrado: ', miArchivo.closed)
print('Modo abierto: ', miArchivo.mode)

#Escribir algo al archivo
miArchivo.write('Me encanta Python')
miArchivo.write(' y ROOT')
miArchivo.close()

#Agregar al archivo
miArchivo = open('miArchivo.txt', 'a')#a de add
miArchivo.write(' y tambien C++')
miArchivo.close()

#Leer un archivo
miArchivo = open('miArchivo.txt', 'r+')#read
texto = miArchivo.read()
print(texto)
miArchivo.close()

