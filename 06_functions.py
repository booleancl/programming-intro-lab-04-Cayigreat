# Una función es un grupo de sentencias con un nombre, que realizan una computación.
# Primero uno define una función y luego llama o ejecuta esa función

# Python viene con muchas funciones listas para usar
# Solo hay que llamarlas o ejecutarlas 
print("Hola Claudia")

# La mayoría de las funciones entregan un valor, es decir, nos devuelven el resultado . Ejemplo:

str_num = '32' # Esto es un string que parece número, lo dictaminan las comillas que
real_num = int(str_num) # Esta función transforma a entero
print(type(real_num))

float_num = 3.9999
int_num = int(float_num) # No aproxima, la variable int lo lleva a número entero
print(int_num)

# La siguiente línea es un error
#int("Hola mundo"), porque la variable int se refiere a números

print(float ('32')) # Esta función entrega un float, lo toma como número con parte fraccionaria
print(str(3.1415)) # Esta función entrega un str, porque lo lee como cadena de caracteres o frase, no como número
# Nunca olvidar que para escribir la variable, el complemento debe ir entre paréntesis

# Composición de funciones= anidar funciones

print(str(3.1415))
