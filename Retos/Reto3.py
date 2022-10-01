# Función lambda que recibe nombre, edad y ocupación de una persona y devuelva un diccionario con esta información
key_usuarios = ["name","age","job"]
usuarios = []

usuarioFuncion = lambda dato : usuarios.append(dato) 

for i in range(3):
    dato = input("Ingrese el dato: ")
    usuarioFuncion(dato)

diccionario = dict(zip(key_usuarios,usuarios))

for valor in diccionario.values():
    print(valor)