# Diccionarios
# Estructura de datos que nos permite almacenar valores de diferente
# tipo, incluso listas y otros diccionarios
# La principal caracteristica de los diccionarios es que los datos 
# se alamcenan asociados a una clave : valor para cada elemento almacenado
# Los elementos almacenados no estan ordenados. El orden es indiferente
# al momento de almacenar informacion en un diccionario.
# Observe que van entre llaves, no hay dos claves iguales

mi_diccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Rusia":"Moscu"}

# para consultar un valor, indicamos su clave
print(mi_diccionario["Francia"])

# para consultar un diccionario completo
print(mi_diccionario)

# agregar elementos a un diccionario ya construido
# [clave]=valor
mi_diccionario["Italia"]="Milan"
print(mi_diccionario)

# Modificar un valor, se sobreescribe
mi_diccionario["Italia"]="Roma"
print(mi_diccionario)

# eliminar un elemento, se usa su key
del mi_diccionario["Reino Unido"]
print(mi_diccionario)

segundo_diccionario = {23:"Jordan","Mosqueteros":3}
print(segundo_diccionario)

# Usar una tupla para asignar las keys
tupla_claves=["Rojo","Verde","Amarillo","Azul"]
diccionario_colores={tupla_claves[0]:"Red",
                    tupla_claves[1]:"Green",
                    tupla_claves[2]:"Yellow",
                    tupla_claves[3]:"Blue"}
print(diccionario_colores)
print(diccionario_colores["Verde"]) # case sensitive

# un diccionario almacena una tupla
diccionario_tuplas={23:"Jordan",
                    "Nombre":"Michael",
                    "Equipo":"Chicago",
                    "anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario_tuplas)
print(diccionario_tuplas["anillos"])

# guardar un diccionario dentro de otro diccionario
dic_diccionario={23:"Jordan",
                "Nombre":"Michael",
                "Equipo":"Chicago",
                "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(dic_diccionario)
print(dic_diccionario["anillos"])
# Como consultar el diccionario dentro del diccionario

# keys() devuelve las claves del diccionario
print(dic_diccionario.keys())

# values() devuelve los valores
print(dic_diccionario.values())

# len() devuelve la longitud del diccionario
print(len(dic_diccionario))



