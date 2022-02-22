# Matplotlib es una librería de Python para crear visualizaciones estáticas, 
# animadas e interactivas para analizarlos de manera visual.

import matplotlib.pyplot as plt


# Gráficas de líneas
x = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [1, 2, 5, 10, 21, 40, 54]
plt.plot(x, y)  # graficamos estas dos variables con el método
plt.show()      # crear nuestra gráfica de línea

# Podemos agregarle más detalles para mejorar la visualización de los datos.
#       marker para marcar cada punto de dato…
#       linestyle que define el estilo de línea.
#       color para definir el color de la línea.
plt.plot(x, y, marker='o', linestyle='--', color='g')
plt.xlabel('Years')             # nombre al eje X
plt.ylabel('Revenue')           # nombre al eje Y
plt.title('Revenue per year')   # Indica el título de la gráfica
plt.show()


# Graficas de barras
x = ['Data Science', 'Web Development', 'Mobile Development']
y = [400, 500, 250]
plt.bar(x, y)
plt.show()


# Histogramas
prices = [1000, 2300, 3001, 3450, 4200, 4780, 5100, 5500, 6000, 7500]
bins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
plt.hist(prices, bins)
plt.show()


# Gráfica de dispersión - Scatter plot
# Las gráficas de dispersión nos sirven para comparar dos variables y ver si tienen alguna relación entre ellas.
x = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [1, 2, 5, 10, 21, 40, 54]
plt.scatter(x, y)
plt.show()


# Gráfica con Pandas
import pandas as pd
df = pd.read_csv('/content/studentsperformance.csv')    # No esta incluido el archivo
df.head()
df.columns
# La primera gráfica que crearemos será un histograma de las calificaciones de matemáticas, 
# es decir con la columna math score.
# Crearemos los bins del 0 al 100 en saltos de 10 para separar nuestros datos de esa manera.
bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Para la creación de los bins durante la elaboración de los histogramas podemos usar 
# la función range o list comprehensions. 
#       bins = list(range(0,101,10))
#       bins = [i for i in range(0, 101, 10)]

plt.hist(df['math score'], bins)
plt.xlabel('Math score')
plt.ylabel('Number of students')

plt.show()  # Para que se vea la grafica en Jupyter no es necesario usar el metodo plt.show(), en un script .py si lo es.

# Para nuestra segunda gráfica crearemos un diagrama de dispersión de las columnas math score y reading score para ver qué tanto se pueden relacionar.

y = df['math score']
x = df['reading score']

plt.scatter(x, y)
plt.xlabel('Math score')
plt.ylabel('Reading score')

plt.show()