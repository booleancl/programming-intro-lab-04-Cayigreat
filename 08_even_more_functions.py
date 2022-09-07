# Las funciones pueden hacer cosas y también pueden retornar valores

def circle_area(radius):
  area= 3.1415*radius**2  
  return area
  
  # En este caso me entrega o devuelve el valor

result = circle_area(4)
print(result)

def circle_volume(radius,heihgt):
  volume= 3.1415*radius**2*heihgt
  return volume 

result_two = circle_volume(4,10)
print(result_two)
print(area)

def circle_volume(radius,heihgt):
  volume= circle_area(radius)*heihgt
  return volume