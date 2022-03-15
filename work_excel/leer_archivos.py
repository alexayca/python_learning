# Archivo por checar su correcto funcionamiento

# ----- / ----- / ----- / ----- / ----- / ----- / ----- / ----- / -----  
# Lectura con pandas

# importamos la libreria pandas
# en la mayoria de los casos read_excel es suficiente
import pandas as pd
# podemos indicar la ruta absoluta o relativa
archivo = 'sample.xlsx'
df = pd.read_excel(archivo, sheet_name='Sheet1')
# describe() informa sobre los datos estadísticos de un DataFrame.
df.describe()


# ----- / ----- / ----- / ----- / ----- / ----- / ----- / ----- / -----  
# Lectura de Excel con xlrd, solo lee archivos xls (1997-2003)
import xlrd
archivo2 = 'C:/nubes/alexaycaBASH/python_learning/work_excel/sample.xls'
# abre el archivo de excel para trabajar con el
wb = xlrd.open_workbook(archivo2) 

# seleccionamos la hoja por indice
hoja = wb.sheet_by_index(0) 
# con la hoja seleccionada vemos el numero de filas, columnas
print("Rows: ",hoja.nrows) 
print("Columns: ",hoja.ncols) 
# seleccionamos una celda mediante indices
print("celda A1: ",hoja.cell_value(0, 0))

# seleccionamos la hoja por nombre
hoja = wb.sheet_by_name('Sheet1a') 
# para conocer las cabeceras o nombres de columna
for i in range(0,hoja.nrows):
    print(hoja.cell_value(i,1))

# para conocer las cabeceras o nombres de columna
nombres = hoja.row(0)  
print(nombres)

# Y mediante xlrd podemos crear data frames de pandas 
# con lo que es posible realizar lecturas de rangos:
# tomamos el archivo abierto previamente
# Creamos listas
filas = []
for fila in range(1,hoja.nrows):
    columnas = []
    for columna in range(0,2):
        columnas.append(hoja.cell_value(fila,columna))
    filas.append(columnas)

df = pd.DataFrame(filas)
df.head()

