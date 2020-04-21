#Importar librerias
import getpass

#Pantalla de Bienvenida


print("Bienvenido Al Servicio Secreto introduzca su usuario y contraseña")

#Usuario y contraseña


nombre = input("Usuario:")

p = getpass.getpass()

print(f"Bienvenido Agente, {nombre}")







