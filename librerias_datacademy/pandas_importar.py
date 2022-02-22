# Importar datos de archivos con Pandas
# Es común importar datos de archivos CSV, JSON, Excel y SQL para crear DataFrames con ellos.
# utilizamos el método pd.read_{file_type}('path')
# Aqui podemos encontar gran cantidad de dataset de ejemplo
#       https://www.kaggle.com/

import pandas as pd

df = pd.read_csv('/content/studentsperformance.csv')    # No esta incluido el archivo
df


# Inspeccionar el DataFrame
#
# Para conocer qué hay dentro del DataFrame solemos utilizar el método .head().
# Permite conocer las 5 primeras filas del DataFrame
df.head()
#  También podemos darle un entero como parámetro 
# y devolverá esa cantidad de primeras filas dentro del notebook.
df.head(10)

# .tail() retorna las 5 últimas filas.
df.tail()

# df.sample() retorna filas como los dos métodos anteriores, 
# pero toma muestras al azar del DataFrame y 
# es necesario especificar en el parámetro la cantidad de filas.
df.sample(7)

# .shape retorna la cantidad de filas y columnas que tiene el DataFrame en ese orden.
df.shape 

# .size multiplica las filas y columnas y te da el total de datos del DataFrame.
df.size

# .info() da la cuenta de valores no nulos, el tipo de dato de cada columna 
# (recuerda que solo puede haber un único tipo de dato por columna) y el uso de memoria.
df.info()

# .describe() calcula algunas estadísticas descriptivas para cada columna.
df.describe()


# Para trabajar con datos de una sola columna utilizaremos código como df['nombre_columna'].
# Para ver las columnas de un DafaFrame usamos el método df.columns.
df.columns
df['math score']    # Usemos la columna 'math score' 
# Podemos usar métodos donde uno a uno podemos ver estadísticas descriptivas de esa columna.
df['math score'].mean()
df['math score'].median()
df['math score'].std()


