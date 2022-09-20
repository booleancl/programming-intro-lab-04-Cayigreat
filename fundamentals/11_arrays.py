# Los Arreglos (en python también se llaman listas) son ESTRUCTURAS DE DATOS FUNDAMENTAL
# que permite agrupar valores, separados por comas 

first_array = ['levantarse', 'bañarse', 'vestirse', 'tomar desayuno']

# En python el primer elemento de un arreglo tiene posición (índice) 0
print (first_array[0])

print (first_array[1])
print (first_array[2])
print (first_array[3])
# No fue creado este elemento, por eso pyhton da el error (el arreglo tiene 4 elementos y su índice comienza en 0)
# print (first_array[4])

# Podemos saber el largo de un arreglo o lista con la función pre definida len

print(len(first_array))

# Además podemos agregar elementos al arreglo 
# con append podemos agregar elementos al final de la lista

first_array.append('Comer')
first_array.append('Dormir')

# Podemos indicar la posición del nuevo elemento a agregar con insert
first_array.insert(0,'Lavarse los dientes')

# podemos imprimir la lista completa
print(first_array)