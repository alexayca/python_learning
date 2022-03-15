# sintaxis de las funciones
#   declaracion de funciones propias
#   def nombre_funcion(parametros_si_son_necesarios):
#       instrucciones de la funcion
#       return(opcional)
#
# nombre_funcion()  llamada a la funcion
# python pasa los valores por referencia



def funcion():
    pass


def suma(n1,n2):
    print(n1+n2)

def resta(n1,n2):
    resultado=n1-n2
    return resultado

# Ejecutamos la funcion suma con diferentes parametros
suma(5,5)
suma(8,3)
resultado_recibido=resta(8,5)
print(resultado_recibido)

