print("<<<<Bienvenido a tu horóscopo semanal>>>>\n")
user_option = ""
 
def read_file(file_name):
    file = open("file_handling/" + file_name, "r", encoding="UTF-8")
    for line in file:
        print(line)
   

def print_menu(): 
    print("<<<<Selecciona el nombre de tu signo zodiacal>>>>\n")
    print("1 Aries (21 de Marzo al 19 de Abril)")
    print("2 Tauro (20 de Abril al 20 de Mayo)")
    print("3 Géminis (21 de Mayo al 20 de Junio)")
    print("4 Cáncer (21 de Junio al 22 de Julio)")
    print("5 Leo (23 de Julio al 22 de Agosto)")
    print("6 Virgo (23 de Agosto al 22 de Septiembre)")
    print("7 Libra (23 de Septiembre al 22 de Octubre)")
    print("8 Escorpio (23 de Octubre al 21 de Noviembre)")
    print("9 Sagitario (22 de Noviembre al 21 de Diciembre)")
    print("10 Capricornio (22 de Diciembre al 20 de Enero)")
    print("11 Acuario (21 de Enero al 19 de Febrero)")
    print("12 Piscis (20 de Febrero al 20 de Marzo)\n")
    print("Escriba exit para salir")
    print("   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ")  

while user_option != "exit":
    print_menu()  
    user_option = input()

    if user_option == "1":
        read_file("aries.txt")
    elif user_option == "2":
        read_file("tauro.txt")  
    elif user_option == "3":
        read_file("géminis.txt")
    elif user_option == "4":
        read_file("cáncer.txt")
    elif user_option == "5":
        read_file("leo.txt")
    elif user_option == "6":
        read_file("virgo.txt")  
    elif user_option == "7":
        read_file("libra.txt")  
    elif user_option == "8":
        read_file("escorpio.txt")
    elif user_option == "9":
        read_file("sagitario.txt") 
    elif user_option == "10":
        read_file("capricornio.txt")  
    elif user_option == "11":
        read_file("acuario.txt") 
    elif user_option == "12":
        read_file("piscis.txt")                                               
    elif user_option == "exit":
        print("Adiós, que los astros acompañen tu vida")
        exit()   

    else:
       
        print("----opción incorrecta----")    
    