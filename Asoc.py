import datetime as dt
from Men_Asoc import *
from Guardador_y_cargadorr_de_datos import *
from confirmador_de_contraseña import *
from Servicios import *
import json

BASES_DE_DATOS = {
    "BaseDatos_1": "BDA.json",
    "BaseDatos_2": "BDAS.json",
    "BaseDatos_3": "BDHU.json",
    "BaseDatos_4": "BDP.json",
    "BaseDatos_5": "BDU.json",
    "BaseDatos_6": "contrasena.json",
    "BaseDatos_7": "BDV.json",
    "BaseDatos_8": "BDIS.json"
}

def Log_Up_Admin(datos):
    datos_admin = {}
    
    print("Bienvenido usuario")
    datos_admin["Usuario"] = input("Ingrese su nombre: ")
    datos_admin["Contrasena"] = input("Cree una contraseña: ")
    
    while True:
        contrasena_verificar = input("Verificar contraseña: ")
        if datos_admin["Contrasena"] == contrasena_verificar:
            datos["d_Admin"].append(datos_admin)
            print("Usuario creado exitosamente")
            return datos_admin
        else:
            print("Las contraseñas no coinciden")
1
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

def cargar_datos(archivo):
    with open(f"Asoc/{archivo}", "r") as file:
        datos = json.load(file)
    return datos

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

def Log_in_user(datos, datos_1):
    print("Bienvenido Usuario")
    Nombre = input("Ingrese su nombre: ")
    try:
        Dc_identidad = int(input("Ingrese su documento de identidad: "))
    except ValueError:
        registrar_error("ValueError")
        return datos
    
    for usuario in datos["Usuarios"]:
        if usuario["Nombre Completo"] == Nombre and usuario["Dc identificacion"] == Dc_identidad:
            while True:
                Menu_Asoc_UserC()
                Ol = pedir_Opc()
                if Ol == 1:
                    mostrar_servicios(datos_1)
                elif Ol == 0:
                    print("Ok, se va saliendo")
                    return usuario

    print("Usuario no encontrado.")
    return None

def Mostrar_datos(datos):
    with open(f"Asoc/{datos}","r") as file:
        datos = json.readlines(file)
    return datos

def Log_in_Admin(datos, datos_1,datos_2,datos_3,datos_4,datos_5,datos_6,datos_7):
    print("Bienvenido usuario")
    Nombre = input("Ingrese su nombre: ")
    Contrasena_R = input("Ingrese su contraseña: ")
    
    for admin in datos["d_Admin"]:
        if admin["Usuario"] == Nombre:
            while admin["Contrasena"] != Contrasena_R:
                print("Contraseña incorrecta")
                Contrasena_R = input("Ingrese su contraseña: ")
            while True:
                Menu_Asoc_Admin()
                O_s = pedir_Opc()
                if O_s == 1:
                    Mostrar_datos(datos_1)
                elif O_s == 2:
                    print("¿Qué quieres hacer?")
                    print("1. Eliminar un servicio")
                    print("2. Modificar un servicio")
                    O_L = pedir_Opc()
                    if O_L == 1:
                        eliminar_servicio_sistema(datos_2)
                    elif O_L == 2:
                        Modificar_Servicio(datos_2)
                elif O_s == 3:
                    clasificador_de_clientes(datos_1)
                elif O_s == 4:
                    print("¿Qué tipo de usuario va a eliminar?")
                    print("1. Admin")
                    print("2. Usuario")
                    O_sl = pedir_Opc()
                    if O_sl == 1:
                        eliminar_User_Admin(datos)
                    elif O_sl == 2:
                        eliminar_User(datos_2)
                    else:
                        print("Opción no válida")
                elif O_s == 5:
                    Mostrar_datos(datos_3)
                    Mostrar_datos(datos_2)
                elif O_s == 6:
                    mostrador_de_Servicio_Mu(datos_2)
                elif O_s == 7:
                    Mostrar_datos(datos_7)
                elif O_s == 8:
                    Mostrar_datos(datos_6)
                elif O_s == 9:
                    print("¿Qué quieres hacer?")
                    print("1. Crear un servicio")
                    print("2. Crear una promoción")
                    Opk = pedir_Opc()
                    if Opk == 1:
                        menu_para_agregar_servicio()
                        Opl = pedir_Opc()
                        agregar_servicio_sistema(datos_2, Opl)
                    elif Opk == 2:
                        personalizador_de_promociones(datos_5)
                elif O_s == 10:
                    Agregar_interaciones_sistema(datos_7)
                elif O_s == 11:
                    venta_Cel(datos_6, datos_3)
                elif O_s == 12:
                    agregar_celulares_usuario(datos_4)
                elif O_s == 13:
                    agregar_Productos_sistema(datos_3)
                elif O_s == 14:
                    agregar_servicios_usuario(datos_4)
                elif O_s == 15:
                    Agregar_usuario_a_servicios(datos_2)
                elif O_s == 0:
                    print("Sesión finalizada")
                    return datos
                else:
                    print("Opción no válida")

def Men_sec():
    print("Que le vas a cambiar")
    print("1. Nombre")
    print("2. Descripcion")

def guardar_datos(datos, archivo):
    with open(f"Asoc/{archivo}", "w") as file:
        json.dump(datos, file, indent=4)

datos = {key: cargar_datos(value) for key, value in BASES_DE_DATOS.items()}

while True:
    Menu_prin()
    Opc = pedir_Opc()
    
    if Opc == 1:
        Menu_user()
        Ops = pedir_Opc()
        if Ops == 1:
            Log_Up_Admin(datos["BaseDatos_6"])
        elif Ops == 2:
            Log_Up_User(datos["BaseDatos_5"])
        elif Ops == 3:
            print("Salida exitosa")
            for key, value in BASES_DE_DATOS.items():
                guardar_datos(datos[key], value)
            break
    elif Opc == 2:
        Menu_user()
        Ops = pedir_Opc()
        if Ops == 1:
            Log_in_Admin(datos["BaseDatos_6"],datos["BaseDatos_5"],datos["BaseDatos_2"],datos["BaseDatos_1"],datos["BaseDatos_3"],datos["BaseDatos_4"],datos["BaseDatos_7"],datos["BaseDatos_8"])
        elif Ops == 2:
            Log_in_user(datos["BaseDatos_5"],datos["BaseDatos_2"])
        elif Ops == 3:
            print("Salida exitosa")
            for key, value in BASES_DE_DATOS.items():
                guardar_datos(datos[key], value)
            break
    elif Opc == 3:
        print("Sesión finalizada")
        for key, value in BASES_DE_DATOS.items():
            guardar_datos(datos[key], value)
        break