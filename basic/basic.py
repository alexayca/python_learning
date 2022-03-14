
'''
Dot strings para comentarios
colab.research.google.com
'''

# Datos de usuario
print("Hola")
nombre = "Alex AC"
print(nombre)
nombre

edad_usuario = 36
salario_usuario = 1000

# Requisitos del banco
salario_requerido = 350
edad_minima = 18

# Logica
if edad_usuario >= edad_minima and salario_usuario >= salario_requerido:
  print(f"{nombre} es apto para obtener Tarjeta")
else:
  print(f"NO es posible otorgar una Tarjeta a {nombre}")
