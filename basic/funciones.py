# Presenta error por corregir

# def nombre_funcion(parámetros, separados):
#	 #Código de la función indentado (4 espacios)
#    return variable_regresada
#
# Las funciones deben definirse en la parte superior, 
# en la parte inferior generan error
#
# Revisar la siguiente pagina para validaciones
# https://uniwebsidad.com/libros/algoritmos-python/capitulo-12/validaciones


def do_mensaje(op):
    if op>=1 and op<=9:
        print("el parametro recibido es " , op)
    elif op!=(op>0 and op<=9):
        print(op, " NO es una opción")
    else:       # No deberia ejecutarse, pero lo hace con el cero
        print(f'{type(op)} - {op} no es un valor valido.\nAdios')   
        

opcion=int(input("Elige una opción (1 - 9): "))
do_mensaje(opcion)


# Obtenemos todos los métodos disponibles para ejecutar 
# de un objeto, variable o tipo de dato.
dir(str)

# Entrega la documentación disponible para esa variable.
help(str)
