# Laboratorio 2 _ Introduccion a la Ciencia de Datos

_Dayrut Simancas 21412683_

Una vez tenemos un modelo de regresion

Podemos utilizar varias graficas de diagnostico proporcionadas por R, las cuales nos permiten revisar que tan bien el modelo creado se esta ajustando a la data con la que trabajamos

Entre ellas encontramos:

**1. Residual vs fitted values plot:** La cual es una grafica de dispersion(scatter plot) en donde observamos en el eje Y residuales, y en el eje X los valores ajustados(respuestas estimadas). Esta grafica es utilizada comunmente para detectar no-linearidad, variaciones de errores desiguales y valores atipicos(outliers).

**2. Q-Q plot:** es una grafica de dispersion donde se comparan los valores observados en la data frente a una distribucion normal estandar. Y se trata de determinar si ambos conjuntos de quantiles provienen de la misma distribucion, si los errores estan distribuidos normalmente observariamos que todos los puntos forman una linea recta.

**3. Scale Location plot:** tambien conocido como Spread-Location plot; esta grafica muestra si los residuos se distribuyen de igual manera a lo largo de los rangos de predictores. Con esta grafica se pueden comprobar la asuncion de igual varianza(homocedasticidad); si observamos una linea horizontal con puntos de propagacion igualmente dispersos y aleatorios.

**4. Cook's distance plot:** tambien llamdo Residuals vs Leverage plot. Este grafico nos ayuda a encontrar aquellos puntos que poseen la mayor influencia dentro de nuestro modelo de regresion(leverage points). No todos los outliers son necesariamente influyentes, ya que podemos tener data con valores extremos y que estos resulten de poco interes dentro de nuestro modelo ya que no seria muy diferente si los incluimos o los excluimos de los analisis.


