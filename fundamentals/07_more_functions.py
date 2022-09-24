# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def"
# Y el cuerpo de la función debe ir correctamente indentado 

def chuchuwa(inst):
  print("Chuchuwa chuchuwa chuchuwa wa wa!")
  print("Chuchuwa chuchuwa chuchuwa wa wa!")
  print("Atención!, compañía")
  print(inst)

print(chuchuwa)
print(type(chuchuwa))
# Lo que da en la terminal con números y letras, es la dirección en la que se alojó esta función en la Ram
# Para que la función corra correctamente, siempre debe la indentación debe ir siempre más cerca de la orilla
# El llamado de la función, para que se ejecute debe terminar con ()

chuchuwa("Mano hacia el frente")
chuchuwa("Hombro hacia atrás")
# Entre los paréntesis van comillas

# Las funciones deben ejecutarse con los mismo parámetros que se definió
result = chuchuwa("Lengua afuera")

# Si la función no tiene un valor de retorno, nos entregará "None", que es para representar: "Nada"
print(result)
