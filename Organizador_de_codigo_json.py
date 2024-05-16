from Asoc import *

def servicio_mas_vendido_M(datos):
    servicios = datos["Servicios Moviles"]
    nombres_servicios = [servicio["Nombre"] for servicio in servicios]
    usuarios_servicios = [servicio["C_ usuarios"] for servicio in servicios]

    servicio_mas_vendido_index = usuarios_servicios.index(max(usuarios_servicios))
    servicio_mas_vendido_nombre = nombres_servicios[servicio_mas_vendido_index]
    cantidad_usuarios = max(usuarios_servicios)

    print("El servicio más vendido es:", servicio_mas_vendido_nombre, "con", cantidad_usuarios, "usuarios.")
    return cantidad_usuarios, datos

def servicio_mas_vendido_hogar(datos):
    servicios = datos["Servicios C.Hogar"]
    nombres_servicios = [servicio["Nombre"] for servicio in servicios]
    usuarios_servicios = [servicio["C_ usuarios"] for servicio in servicios]

    servicio_mas_vendido_index = usuarios_servicios.index(max(usuarios_servicios))
    servicio_mas_vendido_nombre = nombres_servicios[servicio_mas_vendido_index]
    cantidad_usuarios = max(usuarios_servicios)

    print("El servicio más vendido es:", servicio_mas_vendido_nombre, "con", cantidad_usuarios, "usuarios.")
    return datos

def servicio_mas_vendido_innovacion(datos):
    servicios = datos["Servicios de Innovacion"]
    nombres_servicios = [servicio["Nombre"] for servicio in servicios]
    usuarios_servicios = [servicio["C_ usuarios"] for servicio in servicios]

    servicio_mas_vendido_index = usuarios_servicios.index(max(usuarios_servicios))
    servicio_mas_vendido_nombre = nombres_servicios[servicio_mas_vendido_index]
    cantidad_usuarios = max(usuarios_servicios)

    print("El servicio más vendido es:", servicio_mas_vendido_nombre, "con", cantidad_usuarios, "usuarios.")
    return datos

def servicio_mas_vendido_entretenimiento(datos):
    servicios = datos["Servicios de Entretenimiento"]
    nombres_servicios = [servicio["Nombre"] for servicio in servicios]
    usuarios_servicios = [servicio["C_ usuarios"] for servicio in servicios]

    servicio_mas_vendido_index = usuarios_servicios.index(max(usuarios_servicios))
    servicio_mas_vendido_nombre = nombres_servicios[servicio_mas_vendido_index]
    cantidad_usuarios = max(usuarios_servicios)

    print("El servicio más vendido es:", servicio_mas_vendido_nombre, "con", cantidad_usuarios, "usuarios.")
    return datos

