# Pandas
#       https://platzi.com/clases/2681-datacademy/45484-tutorial-pandas/
#       https://platzi.com/blog/pandas/
# Pandas es una librería de Python que se usa para manipular datos de alto nivel. 
# Está construida sobre NumPy. Principalmente funciona con una estructura de datos 
# que guarda la información de manera tabular llamada DataFrame. 
# Esencialmente esto es una tabla, para analizar datos en forma tabular
# Cada fila dentro de un DataFrame lleva un índice que indica su posición.

import pandas as pd


# Diccionario de listas
students_dict = {
    "name": ["Miguel", "Juan David", "Carmen", "Facundo", "Romina"],
    "age": [29, 19, 24, 22, 25],
    "career path":  ["Data Analyst", "Data Scientist", "Data Analyst", "Data Engineer", "ML Engineer" ],
}

students_df = pd.DataFrame(students_dict)
students_df


# Lista de diccionarios (fila por fila)
students_df = pd.DataFrame(students_dict)
students_df

students_list = [
    {"name": "Miguel", "age": 29, "career path": "Data Analyst"},
    {"name": "Juan David", "age": 19, "career path": "Data Scientist"},
    {"name": "Carmen", "age": 24, "career path": "Data Analyst"},
]

students_df_2 = pd.DataFrame(students_list)
students_df_2


print(students_df.dtypes)
print(students_df_2.dtypes)

