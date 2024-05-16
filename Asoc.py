import datetime as dt
from Men_Asoc import *
from Guardador_y_cargadorr_de_datos import *
from confirmador_de_contraseña import *
from Organizador_de_codigo_json import *
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

def Menu_prin():
    print("Bienvenido")
    print("1. Iniciar sesion")
    print("2. Registarse")
    print("3. Salir")

def mostrar_servicios(datos):
    print("Servicios que se ofrecen:")
    for categoria in ["Servicios Moviles", "Servicios C.Hogar", "Servicios de Innovacion", "Servicios de Entretenimiento"]:
        for servicio in datos[categoria]:
            print(servicio["Nombre"])
            print(servicio["Descripcion"])
            print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

def agregar_servicio_sistema(datos, Opc):
    Servicio = {}
    
    print("Ingrese el nombre del nuevo Servicio:")
    Servicio["Nombre"] = input("")
    print("Ingrese una descripción para el servicio:")
    Servicio["Descripcion"] = input()

    categorias = ["Servicios Moviles", "Servicios C.Hogar", "Servicios de Innovacion", "Servicios de Entretenimiento"]
    
    if 1 <= Opc <= 4:
        datos[categorias[Opc - 1]].append(Servicio)
    
    return datos

def eliminar_servicio_sistema(datos):
    print("Ingrese el nombre del servicio")
    Servicio = input("")
    
    for categoria in ["Servicios Moviles", "Servicios C.Hogar", "Servicios de Innovacion", "Servicios de Entretenimiento"]:
        for servicio in datos[categoria]:
            if servicio["Nombre"] == Servicio:
                datos[categoria].remove(servicio)
                print("El servicio fue eliminado")
                return datos
    print("El servicio no fue encontrado")
    return datos

def agregar_servicios_usuario(datos):
    Servicio = {}

    print("Ingrese su nombre:")
    Nombre = input("")
    print("¿Qué servicio adquirió?")
    Servicio["Servicio"] = input("")

    for usuario in datos["H_usuarios"]:
        if usuario["Nombre"] == Nombre:
            usuario["servicios comprados"].append(Servicio)
            return datos

    return datos

def agregar_celulares_usuario(datos):
    print("Ingrese su nombre:")
    nombre = input("")
    print("¿Qué celular adquirió?")
    celular = input("")

    for usuario in datos["H_usuarios"]:
        if usuario["Nombre"] == nombre:
            usuario["Celulares"].append({"Celular": celular})
            return datos

    return datos

def agregar_Productos_sistema(datos):
    Celular = {}
    
    print("Ingrese la marca del celular:")
    Celular["Marca"] = input("")
    print("Ingrese el modelo del celular:")
    Celular["Modelo"] = input("")
    print("Ingrese la referencia del celular:")
    Celular["Referencia"] = input("")
    print("Ingrese la cantidad de celulares que hay en stock:")
    Celular["Cantidad_Total"] = input("")
    print("Ingrese el valor del celular:")
    Celular["Valor"] = input("")
    
    while True:
        try:
            C_Colores = int(input("¿Cuántos colores del celular hay?: "))
            break
        except ValueError:
            print("Error: Cantidad de colores inválida")
            registrar_error("ValueError")
    
    Celular["Colores"] = []
    for _ in range(C_Colores):
        Colores = {}
        print("Ingrese el color:")
        Colores["Color"] = input("")
        print("¿Cuántos celulares hay de ese color?:")
        Colores["Cantidad"] = input("")
        Celular["Colores"].append(Colores)
    
    datos["Celulares"].append(Celular)
    return datos

def registrar_error(tipo_error):
    fecha_actual = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open("Count_Error.txt", "w") as file:
        file.write(f"Error Type: {tipo_error} {fecha_actual}\n")

def venta_Cel(datos, D_atos):
    ventas = {
        "Nombre": input("Ingrese el nombre completo del usuario: "),
        "Celular": input("Ingrese la marca y modelo del celular: "),
        "Color": input("Ingrese el color del celular: "),
        "Referencia": input("Ingrese la referencia del celular: "),
        "Fecha": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }
    venta(D_atos)
    datos["Ventas"].append(ventas)
    return datos, D_atos

def Mostrar_datos(datos):
    usuarios = open(datos,"r")
    for usuario in usuarios:
        print(usuario)
    return datos

def venta(datos):
    print("Ingrese la marca del celular:")
    marca = input("")
    print("Ingrese el modelo del celular:")
    modelo = input("")
    print("Ingrese el color del celular:")
    color = input("")

    for celular in datos["Celulares"]:
        if celular["Marca"] == marca and celular["Modelo"] == modelo:
            celular["Cantidad_Total"] -= 1
            for color_info in celular["Colores"]:
                if color_info["Color"] == color and color_info["Cantidad"] > 0:
                    color_info["Cantidad"] -= 1
                    return datos
            print("No hay celulares de ese color en stock")
            return datos

    print("Celular no existente en el almacén")
    return datos

def Agregar_interaciones_sistema(datos):
    Clientes = input("Ingresa el nombre de la persona: ")
    print("Qué tipo de interacción hizo:")
    print("1. Servicio al cliente")
    print("2. Reclamo")
    print("3. Sugerencia")
    Op = pedir_Opc()
    interacciones = {
        1: "Servicio al cliente",
        2: "Reclamaciones",
        3: "Sugerencias"
    }
    if Op in interacciones:
        for interaccion in datos[interacciones[Op]]:
            if interaccion["Clientes"] == "Clientes":
                interaccion["Clientes"].append(Clientes)
                interaccion["C_ interaciones"] += 1
                return datos
    else:
        print("Opción no válida")
    return datos

def Contador_de_interacciones(datos):
    print("Ingrese su nombre:")
    nombre = input("")

    for usuario in datos["H_usuarios"]:
        if usuario["Nombre completo"] == nombre:
            usuario["C_ interaciones"] += 1
            return datos

    return datos

def mostrador_de_Servicio_Mu(datos):
    print("De cada categoría, los servicios más solicitados son:")
    servicio_mas_vendido_M()
    servicio_mas_vendido_hogar()
    servicio_mas_vendido_innovacion()
    servicio_mas_vendido_entretenimiento()
    return datos

def clasificador_de_clientes(datos, Opc):
    print("Ingrese el número de identidad:")
    try:
        Dc_identificacion = int(input(""))
    except ValueError:
        registrar_error("ValueError")
        return datos

    for usuario in datos["Usuarios"]:
        if usuario["Dc identificacion"] == Dc_identificacion:
            if Opc == 1:
                usuario["Tipo de cliente"] = "Cliente Regular"
            elif Opc == 2:
                usuario["Tipo de cliente"] = "Cliente Leal"
            return datos

    print("No hay ninguna persona con el número de identificación.")
    return datos

def personalizador_de_promociones(datos):
    datos = dict(datos)
    
    print("Que promoción quieres crear ahora")
    print("1. Descuento, con o sin servicio adicional")
    print("2. Promoción de datos")
    o_c = pedir_Opc()

    if o_c == 1:
        for descuento in datos["descuentos"]:
            print(descuento)
            print("Siendo cada número correspondiente al descuento mostrado")
            Ops = pedir_Opc()

            if Ops == 1:
                Des = "15%"
                print("Quieres agregar un servicio adicional")
                print("1. Sí")
                print("2. No")
                Ops = pedir_Opc()

                if Ops == 1:
                    for servicio in datos["Servicio adicional"]:
                        print(servicio)
                    print("Siendo cada número correspondiente al Servicio adicional mostrado")
                    Op = pedir_Opc()
                    servicios = {
                        1: "Netflix",
                        2: "Amazon Prime Video",
                        3: "Win Sports",
                        4: "Star+",
                        5: "Disney+"
                    }
                    if Op in servicios:
                        Serv = servicios[Op]
                        print("ok se está creando la promoción")
                        print("--------------------------------------")
                        print(f"hoy hay un {Des} en todos los celulares, además de tener {Serv} para ver todas las series y películas que quieras")
                    else:
                        print("No servicio seleccionado")
                else:
                    print("ok se está creando la promoción")
                    print("--------------------------------------")
                    print(f"hoy hay un {Des} en todos los celulares, para que puedas hacer videos para todas tus redes sociales y compartir fotografías en ellas")
            elif Ops == 2:
                Des = "20%"
                print("Quieres agregar un servicio adicional")
                print("1. Sí")
                print("2. No")
                Ops = pedir_Opc()

                if Ops == 1:
                    for servicio in datos["Servicio adicional"]:
                        print(servicio)
                    print("Siendo cada número correspondiente al Servicio adicional mostrado")
                    Op = pedir_Opc()
                    servicios = {
                        1: "Netflix",
                        2: "Amazon Prime Video",
                        3: "Win Sports",
                        4: "Star+",
                        5: "Disney+"
                    }
                    if Op in servicios:
                        Serv = servicios[Op]
                        print("ok se está creando la promoción")
                        print("--------------------------------------")
                        print(f"hoy hay un {Des} en todos los celulares, además de tener {Serv} para ver todas las series y películas que quieras")
                    else:
                        print("No servicio seleccionado")
                else:
                    print("ok se está creando la promoción")
                    print("--------------------------------------")
                    print(f"hoy hay un {Des} en todos los celulares, para que puedas hacer videos para todas tus redes sociales y compartir fotografías en ellas")
            elif Ops == 3:
                Des = "25%"
                print("Quieres agregar un servicio adicional")
                print("1. Sí")
                print("2. No")
                Ops = pedir_Opc()

                if Ops == 1:
                    for servicio in datos["Servicio adicional"]:
                        print(servicio)
                    print("Siendo cada número correspondiente al Servicio adicional mostrado")
                    Op = pedir_Opc()
                    servicios = {
                        1: "Netflix",
                        2: "Amazon Prime Video",
                        3: "Win Sports",
                        4: "Star+",
                        5: "Disney+"
                    }
                    if Op in servicios:
                        Serv = servicios[Op]
                        print("ok se está creando la promoción")
                        print("--------------------------------------")
                        print(f"hoy hay un {Des} en todos los celulares, además de tener {Serv} para ver todas las series y películas que quieras")
                    else:
                        print("No servicio seleccionado")
                else:
                    print("ok se está creando la promoción")
                    print("--------------------------------------")
                    print(f"hoy hay un {Des} en todos los celulares, para que puedas hacer videos para todas tus redes sociales y compartir fotografías en ellas")
            elif Ops == 4:
                Des = "30%"
                print("Quieres agregar un servicio adicional")
                print("1. Sí")
                print("2. No")
                Ops = pedir_Opc()

                if Ops == 1:
                    for servicio in datos["Servicio adicional"]:
                        print(servicio)
                    print("Siendo cada número correspondiente al Servicio adicional mostrado")
                    Op = pedir_Opc()
                    servicios = {
                        1: "Netflix",
                        2: "Amazon Prime Video",
                        3: "Win Sports",
                        4: "Star+",
                        5: "Disney+"
                    }
                    if Op in servicios:
                        Serv = servicios[Op]
                        print("ok se está creando la promoción")
                        print("--------------------------------------")
                        print(f"hoy hay un {Des} en todos los celulares, además de tener {Serv} para ver todas las series y películas que quieras")
                    else:
                        print("No servicio seleccionado")
                else:
                    print("ok se está creando la promoción")
                    print("--------------------------------------")
                    print(f"hoy hay un {Des} en todos los celulares, para que puedas hacer videos para todas tus redes sociales y compartir fotografías en ellas")
    else:
        for dato in datos["Datos"]:
            print(dato)
        print("¿Qué cantidad de datos quieres promocionar?")
        DaOp = input("").lower()
        promociones = {
            "30gb": "$55900",
            "40gb": "$64900",
            "50gb": "$69900",
            "75gb": "$79900",
            "datos ilimitados": "$99900"
        }
        if DaOp in promociones:
            valor = promociones[DaOp]
            print("Creando promoción")
            print("--------------------------------------")
            print(f"Si compras {valor}, adquirirás {DaOp} para que navegues y chatees con todos tus amigos")
        else:
            print("Promoción no encontrada")

def Modificar_Servicio(datos):
    print("¿Qué servicio planea modificar?")
    Op = pedir_Opc()
    print("Escriba el nombre del servicio a modificar:")
    N_bre = input("")

    if Op in range(1, 4):
        print("¿Qué va a modificar?")
        print("1. Nombre")
        print("2. Descripción")
        On = pedir_Opc()

        for categoria in ["Servicios Moviles", "Servicios C.Hogar", "Servicios de Innovacion", "Servicios de Entretenimiento"]:
            for servicio in datos[categoria]:
                if servicio["Nombre"] == N_bre:
                    if On == 1:
                        servicio["Nombre"] = input("")
                    elif On == 2:
                        servicio["Descripcion"] = input("")

        return datos
    else:
        print("Opción no válida")
        return datos

def Agregar_usuario_a_servicios(datos, Opc):
    print("Ingresa el nombre del servicio al que se unirá el usuario:")
    Servicio = input("")
    
    if Opc == 1:
        servicios = datos["Servicios moviles"]
    elif Opc == 2:
        servicios = datos["Servicios C.Hogar"]
    elif Opc == 3:
        servicios = datos["Servicios de Innovacion"]
    elif Opc == 4:
        servicios = datos["Servicios de Entretenimiento"]
    else:
        print("Opcion no valida")
        return datos

    for servicio in servicios:
        if servicio["Nombre"] == Servicio:
            servicio["C_ usuarios"] += 1
            break
    else:
        print("Servicio no encontrado.")
    
    return datos

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
    with open(archivo, "r") as file:
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
    with open(datos,"r") as file:
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
    with open(archivo", "w") as file:
        json.dump(datos, file, indent=4)

datos = {key: cargar_datos(value) for key, 
         value in BASES_DE_DATOS.items()}

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
