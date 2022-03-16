# Listas
# Las listas es una estructura que pueden 
# guardar diferentes tipos de valores
# Se pueden expandir dinamicamente 
# anadiendo nuevos elementos
# 
# nombre_lista=[elem1,elem2,elem3,...]
# Observe que va entre corchetes 
#

mi_lista = ["Ariety","Susana", "Magaly","Karla","Lizbeth"]

# para mostrar un elemento se indica el indice
# para toda la lista se usa :
print(mi_lista[1])
print(mi_lista[:])

# Si se introduce un indice negativo, empieza a contar de
# derecha a izquierda
print(mi_lista[-1])

# Listas muy largas, se utiliza una porcion de listas
# o rebanadas [indice_inicial : indice_final]
print(mi_lista[0:3])

# Para agregar elementos usamos append, los agrega al final
# concatena los elementos
mi_lista.append("Sandra")

# para agregar a un punto intermendio usamos insert
# como parametro se indica el indice para la ubicacion
mi_lista.insert(2,"Elizabeth")

# para agregar varios elementos se usa extend (observe los tipos)
# los elementos se agregan al final
mi_lista.extend(["Ana","Lucia","Martha",3.14, 85, True])

print(mi_lista[:])

# devolver el indice de un elemento, si no existe genera error
# si hay varios elementos iguales, devuelve el primero de la lista
print(mi_lista.index("Ana"))

# Comprobar si un elemento se encuentra o no en una lista
# devuelve un boolean con la funcion in
print("Paula esta  en la lista?: ","Paula" in mi_lista)

# Para eliminar elementos se usa remove
mi_lista.remove("Ariety")
# pop elimina el ultimo elemento de la lista
mi_lista.pop()

print(mi_lista[:])

# para sumar o concatenar listas
lista1=[1,2,3]
lista2=[4,5,6]
lista3=lista1+lista2
print(lista3[:])

#el operador *, funciona a modo de repetidor
lista_repetida = ['A','B','C']*3
print(lista_repetida[:])
