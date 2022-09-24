
print("Conoce un poco de tu empresa")
print("------------------------------")

user_option = ""
def read_file(file_name):
    file = open("file_handling/" + file_name, "r", encoding="UTF-8")
    for line in file:
        print(line)

def print_menu(): 
    print("Selecciona el nombre de tu empresa")
    print("------------------------------") 
    print("1 Boolean\n")
    print("2 Microsystem\n")
    print("3 Google\n")
    print("exit para salir")
    print("------------------------------")
    

while user_option != "exit":
    print_menu()
    user_option = input()

    if user_option == "1":
        read_file("boolean.txt")
    elif user_option == "2":
        read_file("microsystem.txt")
    elif user_option == "3":
        read_file("google.txt")
    elif user_option == "exit":
        print("Adiós!!")
        exit()   

    else:
       
        print("opción incorrecta")