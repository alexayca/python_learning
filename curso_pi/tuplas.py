# Tuplas
# las tuplas son listas inmutables, no se pueden modificar despues de crearse
# NO [append, extend, remove]
# permite extraer porciones, pero el resultado es una tupla nueva
# No permiten busquedas (no index antes de la version ~2.6)
# Si permite comprobar si un elemento existe en la lista
# 
# Su utilidad y ventajas respecto a las listas
#   Mas rapidas en ejecucion
#   Menos espacio (optimizacion)
#   Formatean Strings
#   Pueden utilizarse como claves en un diccionario (las listas no)
#
# las tuplas van entre parentesis aunque son opcionales, las listas entre corchetes
# nombre_tupla = (elem1, elem2, elem3)

from operator import le


mi_tupla = ("Juan", 13,1,1995,"Juan")
print(mi_tupla[1])

# Convertir tuplas en listas
lista_cdetupla=list(mi_tupla)
print(type(lista_cdetupla))

# Convertir lista en tupla
mi_lista = ["Ariety","Susana", "Magaly","Karla","Lizbeth"]
tupla_cdelista=tuple(mi_lista)
print(type(tupla_cdelista))

# comprobar si existe un elemento
print("Pedro" in mi_tupla)  # false

# cuantos elementos se encuentran dentro de una tupla
print(mi_tupla.count("Juan"))   # 2 elementos

# len permite conocer la longitud
print(len(mi_tupla))    # 5 elementos

# tuplas unitarias
# tuplas con un unico elemento
# observe la coma al final
# o en este caso los considerara como 3 char
mono_tupla=("Jay",)
print(type(mono_tupla), len(mono_tupla))

# parentesis opcionales, empaquetado de tupla
tupla_sin_parentesis = "Carol", "Jessy", "Sofia"
print(tupla_sin_parentesis)

# desempaquetado de tupla
# forma para asignar los valores de una tupla a variables independientes
# observe como se asignan los valores a cada nombre de variable
tupla_para_desempaquetar = "enero","febrero", "marzo", "abril"
mes1, mes2, mes3, mes4=tupla_para_desempaquetar
print(mes4,mes3,mes2,mes1)

