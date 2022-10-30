import time


def crear_cuenta():
    def pasword():
        while True:
            print("Enter your pasword: ")
            pasword = input("")
            if len(pasword) >= 6:
                return pasword
            else:
                print("el tamaño de su contraseña debe ser mayor a 6, ingrese una nueva")

    def user():
        while True:
            print("ingrese un nombre de usuario: ")
            user = input("")
            if len(user) >= 6:
                return user
            else:
                print("your user no esta disponible, ingrese uno nuevamente")

    datos_iniciales = [user(), pasword()]
    print("Creando cuenta......")
    time.sleep(2.5)
    print("Cuenta creada con exito\n")
    return datos_iniciales


def login():
    def pasword():
        while True:
            print("Enter your pasword: ")
            pasword = input("")
            if len(pasword) >= 6:
                return pasword
            else:
                print("el tamaño de su contraseña debe ser mayor a 6, ingrese una nueva")

    def user():
        while True:
            print("ingrese un nombre de usuario: ")
            user = input("")
            if len(user) >= 6:
                return user
            else:
                print("your user no esta disponible, ingrese uno nuevamente")

    datos_ingresados = [user(), pasword()]
    return datos_ingresados


def comprobar_datos(datos_ingresados, datos_iniciales):
    if (datos_ingresados[0] == datos_iniciales[0]) and (datos_ingresados[1] == datos_iniciales[1]):
        print("Ingresando.....")
        time.sleep(2.5)
        print("ingreso exitoso")
        return True
    elif datos_ingresados[0] == datos_iniciales[0] and datos_ingresados[1] != datos_iniciales[1]:
        print("la contraseña es incorrecta")
        return False
    elif datos_ingresados[0] != datos_iniciales[0] and datos_ingresados[1] == datos_iniciales[1]:
        print("el ususario es incorrecto")
        return False
    else:
        print("la contraseña y el ususario son incorrectos")
        return False
