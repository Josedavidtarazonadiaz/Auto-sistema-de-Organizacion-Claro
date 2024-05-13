import datetime as dt
from Asoc import * 

def Menu_prin():
    print("Bienvenido")
    print("1. Iniciar sesion")
    print("2. Registarse")
    print("3. Salir")

def Menu_user():
    print("Ingrese: ")
    print("1. como Admin")
    print("2. como Usuario")
    print("3. Volver al menu")

def pedir_Opc():
    while True:
        try:
            Opc = int(input("Ingrese la opción: "))
            return Opc
        except ValueError:
            registrar_error("ValueError")
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")
            print("Error de opción")
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")

def registrar_error(tipo_error):
    fecha_actual = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open("Asoc/Contador_de_Errores.txt", "a") as file:
        file.write(f"Error Type: {tipo_error} {fecha_actual}\n")

def menu_para_agregar_servicio():
    print("Ingresa en qué catálogo vas a agregar el nuevo servicio:")
    print("1. Para el catálogo de Servicios Móviles")
    print("2. Para el catálogo de Servicios C.Hogar")
    print("3. Para el catálogo de Servicios de Innovación")
    print("4. Para el catálogo de Servicios de Entretenimiento")

def menu_para_mod_servicio_U():
    print("Ingresa en qué catálogo vas a agregar el nuevo usuario:")
    print("1. Para el catálogo de Servicios Móviles")
    print("2. Para el catálogo de Servicios C.Hogar")
    print("3. Para el catálogo de Servicios de Innovación")
    print("4. Para el catálogo de Servicios de Entretenimiento")


def Men_sec():
    print("Que le vas a cambiar")
    print("1. Nombre")
    print("2. Descripcion")