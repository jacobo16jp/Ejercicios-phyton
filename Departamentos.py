#  Lectura de archivos tipo excel
#  Importar librerías
import pandas as pd

#  Leer archivo excel
df_archivoExcel = pd.read_excel('Departamentos.xlsx',index_col="Departamento")
df_archivoExcel = df_archivoExcel[:36].copy()
print(df_archivoExcel)


print(df_archivoExcel)

# Grafica Vertical
df_archivoExcel.plot(kind = 'bar')

# Grafica Horizontal
df_archivoExcel.plot(kind = 'barh')

#  Ocupar todo el espacio
df_archivoExcel.plot(kind = 'barh', width=1)

#  Grozor de las barras
df_archivoExcel.plot(kind = 'barh', width=3)

# Gráfica Apilada
df_archivoExcel.plot(kind = 'bar', 
                     stacked = 'True',          # barras apiladas
                     alpha = 0.4,               # nivel de transparencia
                     width = 0.9,               # Grosor espacio entre ellas
                     figsize=(9,4));   

# Gráfico por una medalla

df_archivoExcel.plot(kind = 'bar',
                     width=0.8,
                     subplots=True,
                     figsize=(10,20));

# Cambiar colores
colores = ['YELLOW','BLUE','RED']

df_archivoExcel.plot(kind = 'bar',
             width=0.8,
             figsize=(10,4),
             color = colores);



# Funciones propias del desarrollador

