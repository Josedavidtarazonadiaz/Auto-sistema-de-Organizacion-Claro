
def eliminar_User_Admin(datos):
    nombre = input("Ingrese el nombre del Admin: ")
    for admin in datos["d_Admin"]:
        if admin["Usuario"] == nombre:
            datos["d_Admin"].remove(admin)
            print("User Admin Eliminado")
            return datos
    print("User Admin No existe")
    return datos

def eliminar_User(datos):
    documento = input("Ingrese el documento del usuario: ")
    for usuario in datos["Usuarios"]:
        if usuario["Dc identidad"] == documento:
            datos["Usuarios"].remove(usuario)
            print("Usuario eliminado")
            return datos
    print("Usuario no existe")
    return datos
