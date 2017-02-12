"""
Laboratorio 1 _ Introduccion a la Ciencia de Datos

Dayrut Simancas
21412683
"""

import matplotlib.pyplot as plt
import pandas as pd

# --- Cargar dataset
miaData = pd.read_csv("student-por.csv", sep=';')


# --- Mostrar propiedades de la data
miaData.describe()


# --- Histograma de una variable numerica
miaData['age'].plot(kind="hist", title="EdadesEstudiantes")
plt.show()


# --- Diagrama de Dispersion entre par de variables numericas
notas1er = miaData['G1']
notas3er = miaData['G3']
plt.scatter(notas1er, notas3er)
plt.title("Notas_1er vs 3er")
plt.xlabel("notas1er")
plt.ylabel("notas3er")
plt.show()
# Correlacion Positiva
# Hipotesis: Estudiantes q salen bien al principio terminan con buenas notas


# --- Explorar la data

# promedio notas 1er
miaData['G1'].mean()

# promedio notas 3er
miaData['G3'].mean()

# nota minima 1er
miaData['G1'].min()

# nota maxima 3er
miaData['G1'].max()


# --- Preguntas:
#P1: edad estudiante mas viejo recibiendo ayuda
preg1 = miaData[miaData['schoolsup'] == 'yes']
preg1['age'].max()

#P2: promedio de notas_3er estudiantes con al menos 10 inasistencias
preg2 = miaData.query('absences > 9')
preg2['G3'].mean()

#P3: sex_M saca mejoras notas que sex_F?
preg3M = miaData[miaData['sex'] == 'M']
preg3F = miaData[miaData['sex'] == 'F']
preg3M['G3'].mean() > preg3F['G3'].mean()

