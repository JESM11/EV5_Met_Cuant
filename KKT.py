import numpy as np
from scipy.optimize import fsolve

# Función objetivo
def f(x, lambdas):
    return x[0] * x[1] + lambdas[0] * (x[0] * x[1] - 100) + lambdas[1] * (x[0] - 1) + lambdas[2] * (x[1] - 1)

# Restricciones
def g(x, lambdas):
    return np.array([x[0] * x[1] - 100, x[0] - 1, x[1] - 1])

# Jacobiano de las restricciones
def dg(x, lambdas):
    return np.array([[x[1], x[0]], [-1, 0], [0, -1]])

# Valores iniciales para x y lambdas
x0 = np.array([2, 2]) # Inicialización con una caja cuadrada
lambdas0 = np.array([1, 1, 1])

# Función para resolver el sistema KKT
def kkt_system(x_lambdas):
    x = x_lambdas[:2]
    lambdas = x_lambdas[2:]
    return np.concatenate((
        np.array([2*x[0] + lambdas[0] + lambdas[1], 2*x[1] + lambdas[0] + lambdas[2]]),
        np.dot(dg(x, lambdas), x) - np.array([100, 0, 0])
    ))

# Resuelve el sistema KKT
solution = fsolve(kkt_system, np.concatenate((x0, lambdas0)), maxfev=10000)

# Extrae la solución para x y lambdas
x_solution = solution[:2]
lambdas_solution = solution[2:]

print("Solución para x", x_solution)
print("Solución para lambdas:", lambdas_solution)