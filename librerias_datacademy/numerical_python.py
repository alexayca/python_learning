
# NumPy o Numerical Python es una librería para manejo de números de Python.
#       https://platzi.com/blog/numpy/
# Su principal uso es al manejar estructuras de datos matriciales y 
# funciones matemáticas de alto nivel.
# Viene integrada en las Jupyter Notebooks en la nube como: 
#       https://colab.research.google.com/
#       https://deepnote.com/

import numpy as np

# Para crear un array con NumPy utilizamos el método np.array(tu_lista).

vector = np.array([1, 2, 4, 8, 16])
print(vector)

matrix = np.array([[5, 10], [15, 30]])
print(matrix)

lista_1 = [100, 200, 300, 400]
lista_2 = [3, 4, 5, 6]

vector_2 = np.array(lista_1)
print(vector_2)

matrix_2 = np.array([lista_1, lista_2])
print(matrix_2)

# Identificar el tipo de dato, en este caso:  son ndarray de NumPy
print(type(vector))

#.shape nos da las dimensiones del array. En un tensor 
# el primer valor es "profundidad", 2o filas y columnas.
print(vector.shape)
print(matrix.shape)
print(matrix_2.shape)

#.dtype devuelve el tipo de datos que hay en un array.
print(vector.dtype)
print(matrix.dtype)
vector_4 = np.array([1.4, 5.6, 6.8])
vector_4.dtype
