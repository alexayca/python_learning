# Funciones built-in


nombre="alex ac   "
#nombre=input("Cual es tu nombre? ")

# longitud de la cadena con len()
print(nombre, " tiene ",len(nombre), " caracteres.")
nombre=nombre.strip()   # elimina los espacios, y saltos de linea al final de la cadena {rstrip()}
print(nombre, " tiene ",len(nombre), " caracteres despues de invocar strip()")

print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())

# Replace: intercambia la letra indicada como primer parametro por la indicada en el segundo parametro
print(nombre.replace('a','X'))
print(nombre.replace('a','X').upper())  # algunas funciones son apilables

# index
print(nombre[0])

