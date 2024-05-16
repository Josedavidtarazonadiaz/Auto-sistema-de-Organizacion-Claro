from Men_Asoc import *
from Servicios import *
from Menu_principal import *
from Asoc.proyecto_python.Guardador_y_cargadorr_de_datos import *
import datetime as dt

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

def Log_Up_User(datos):
    Usuario = {}
    
    print("Bienvenido Usuario")
    Usuario["Nombre Completo"] = input("Ingrese su nombre completo: ")
    
    try:
        Edad = int(input("Ingrese su edad: "))
        if Edad <= 18:
            return "No puedes acceder a este sitio"
        Usuario["Edad"] = Edad
    except ValueError:
        registrar_error("ValueError")
        return "Error: Edad inválida"
    
    Usuario["Sexo"] = input("Ingrese su sexo: ")
    
    try:
        Dc_identificacion = int(input("Ingrese su documento de identidad: "))
        Usuario["Dc identificacion"] = Dc_identificacion
    except ValueError:
        registrar_error("ValueError")
        return "Error: Documento de identidad inválido"
    
    Informacion_adicional = {}
    Informacion_adicional["Correo"] = input("Ingrese su Correo electrónico: ")
    Informacion_adicional["Telefono"] = input("Ingrese su número de teléfono: ")
    Informacion_adicional["Direccion"] = input("Ingrese su dirección: ")
    
    Usuario["Ciudad"] = input("Ingrese la ciudad donde está: ")
    Usuario["Tipo de cliente"] = "Nuevo cliente"
    Usuario["Informacion adicional"] = [Informacion_adicional]
    
    datos["Usuarios"].append(Usuario)
    
    print("Usuario registrado con éxito")
    return datos

def registrar_error(tipo_error):
    fecha_actual = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open("Count_Error.txt", "w") as file:
        file.write(f"Error Type: {tipo_error} {fecha_actual}")
