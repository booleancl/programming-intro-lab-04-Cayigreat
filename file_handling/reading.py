# Hay tres modos para leer un archivo con la función open()

# "r" para leer
# "a" para agregar al final (append)
# "w" para sobreescribir el contenido

file = open("file_handling/sample.txt", "r", encoding="UTF-8")

# La función open entrega un objeto
# entenderemos como objeto algo que tiene datos y métodos
# los métodos son para manipular sus datos

print(file)

# Para leer el contenido del objeto file, tenemos el método del objeto
# read()

print(file.read())

# Podemos leer el archivo usando for
file = open("file_handling/sample.txt", "r", encoding="UTF-8")

for line in file:
    print(line)

# Luego de utilizar el archivo (manipularlo) debe cerrarse
file.close()