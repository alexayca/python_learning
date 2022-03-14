# Para ejecutar los archivos en la consola de comandos
# escribimos py./nombre_archivo.py
# En python es necesario respetar la identacion para los bloques de codigo


'''
Dot strings para comentarios
colab.research.google.com
'''

# Datos de usuario
print("Hola")
nombre = "Alex AC"
print(nombre)
nombre

# Escribir en varias lineas
texto = "Es un texto dividido en\
   varias lineas\
   para la linea de comandos."
print(texto)

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
