# TEOREMA DE KARUSH-KUHN-TUCKER

Un asesor financiero está evaluando la compra de acciones de firmas de cierto sector industrial. Desea minimizar la variación de la cartera resultante compuesta por acciones de dos firmas, pero también quiere tener un tasa de retorno de al menos un 9%. Después de obtener datos históricos sobre la variación y rendimientos de ambos instrumentos, desarrolla el siguiente modelo de optimización no-lineal:

```
    0.16*x**2 + 0.2*x*y + 0.09*y**2

    s.a. 
    x + y = 1
    0.11*x + 0.08*y >= 0.09
    x, y >= 0
```

Donde x e y representan la proporción de dinero invertida en cada acción. Formule explícitamente todas las condiciones de optimalidad del Teorema de Karush-Kuhn-Tucker para este problema y úselas para determinar la cartera óptima. Justifique adecuadamente su respuesta. Analice todos los posibles casos.

## Solución

Las condiciones del Teorema de Karush-Kuhn-Tucker para este problema son:

1.  

0.32x + 0.20y + λ1 – 0.11μ1 – μ2 = 0
0.18y + 0.20x + λ1 – 0.08μ1 – μ3 = 0

2. 

(-0.11x – 0.08y + 0.09) μ1 = 0
-x1 μ2 = 0 -x3 μ3 = 0

3. 

x + y = 1
0.11x + 0.08y ≥ 0.09
x≥0, y≥0

4. 

μ1≥0, μ2≥0, μ3≥0

Al considerar el esquema de activación de restricciones, siempre debe estar activa la ecuación x+y =1 y lo que cabe entonces es no activar ninguna inecuación o a lo sumo activar una de ellas.

Los diferentes casos que se podrían llegar a analizar son:

1. Ninguna inecuación activa.

Tomamos μ1=0, μ2=0, μ3=0 y resolvemos:

0.32x + 0.20y + λ1 = 0
0.18y + 0.20x + λ1 = 0
x + y = 1

Cuya solución resulta ser: x=-0.2 e y=1.2 que es infactible.

2. Activando sólo la inecuación 0.11x + 0.08y ≥ 0.09.

Tomamos μ2=0, μ3=0 y resolvemos:

0.32x + 0.20y + λ1 – 0.11μ1 = 0
0.18y + 0.20x + λ1 – 0.08μ1 = 0
x + y = 1
0.11x + 0.08y = 0.09

Cuya solución resulta ser: x=1/3 e y=2/3 con multiplicadores λ1=0,04444453 y μ1=1,777777502, con lo cual tenemos un punto que cumple con todas las condiciones del teorema.

3. Activando sólo la inecuación x≥0.

Tomamos μ1=0, μ3=0 y resolvemos:

0.32x + 0.20y + λ1 – μ2 = 0
0.18y + 0.20x + λ1 = 0
x + y = 1
x = 0

Cuya solución resulta ser: x=0 e y=1 con multiplicadores λ1=-0.18 y μ2 = 0.02 pero no verifica 0.11x + 0.08y = 0.08 ≥ 0.09.

4. Activando sólo la inecuación y≥0.

Tomamos μ1=0, μ2=0 y resolvemos:

0.32x + 0.20y + λ1 = 0
0.18y + 0.20x + λ1 – μ3 = 0
x + y = 1
y = 0

Cuya solución resulta ser: x=1 e y=0 con multiplicadores λ1=-0.32 y μ3=-0.12 y este último no cumple con la no-negatividad.

En consecuencia, la solución óptima es aquella obtenida en el caso 2 pues el problema es convexo: x=1/3 e y=2/3. Dicha solución corresponde al par ordenado etiquetado con la letra A en la gráfica anterior. El valor óptimo es 0.102222 y se obtiene simplemente al evaluar la solución óptima en la función objetivo.
