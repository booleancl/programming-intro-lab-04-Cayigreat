# Podemos escribir un archivo con el modo "a"

file = open("file_handling/demo.txt", "a")

file.write("Hola mundo")

file.close()

# Precaución, el modo "w" borra el contenido anterior
file = open("file_handling/demo.txt", "w", encoding = "UTF-8")

file.write("oppss, se borró el contenido anterior")
 
file.close()
