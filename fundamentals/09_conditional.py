# Tenemos expresiones que se pueden evaluar en términos booleanos
# O dicotómicos (sólo se puede seleccionar 1 u otra variable)
# Ejemplo:

print(10>9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

gaby_age = 4
claudia_age = 50

# Estas siguientes instrucciones las podríamos leer como:
# Si el resultado de is_adult ejecutada con la variable gaby_age es
# verdadero, entonces el programa imprime "Quieres una cerveza?"
# de otro modo (else), imprime "Cantemos Chuchuwa?"

if is_adult(claudia_age):
    print("Quieres una cerveza?")
else:
    print("Cantemos Chuchuwa?")  

 # elif es una abreviación de "else if", nos permite seguir evaluando expresiones. Podemos tener tantos como necesitamos

if claudia_age > gaby_age: 
  print ("Claudia es mayor que Gaby")
elif  claudia_age < gaby_age:
  print("Claudia es menor que Gaby")
else:  
  print ("Tienen la misma edad Gaby y Claudia")
 