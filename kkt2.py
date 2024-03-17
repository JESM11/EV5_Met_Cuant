from sympy import symbols, Eq, solve

# Definir las variables
x, y, λ1, μ1, μ2, μ3 = symbols('x y λ1 μ1 μ2 μ3')

# Definir las ecuaciones para cada caso
eq1 = Eq(0.32*x + 0.20*y + λ1 - 0.11*μ1 - μ2, 0)
eq2 = Eq(0.18*y + 0.20*x + λ1 - 0.08*μ1 - μ3, 0)
eq3 = Eq(x + y, 1)

# Caso i) Ninguna inecuación activa
solution = solve((eq1.subs({μ1: 0, μ2: 0}), eq2.subs({μ1: 0, μ3: 0}), eq3), (x, y, λ1))
print('Caso i) solución:', solution)

# Caso ii) Activando sólo la inecuación 0.11x + 0.08y ≥ 0.09
eq4 = Eq(0.11*x + 0.08*y, 0.09)
solution = solve((eq1.subs({μ2: 0, μ3: 0}), eq2.subs({μ2: 0, μ3: 0}), eq3, eq4), (x, y, λ1, μ1))
print('Caso ii) solución:', solution)

# Caso iii) Activando sólo la inecuación x≥0
solution = solve((eq1.subs({μ1: 0, μ3: 0}), eq2.subs({μ1: 0, μ3: 0}), eq3, Eq(x, 0)), (x, y, λ1, μ2))
print('Caso iii) solución:', solution)

# Caso iv) Activando sólo la inecuación y≥0
solution = solve((eq1.subs({μ1: 0, μ2: 0}), eq2.subs({μ1: 0, μ2: 0}), eq3, Eq(y, 0)), (x, y, λ1, μ3))
print('Caso iv) solución:', solution)

# Definir la función objetivo
def objective(x, y):
    return 0.16*x**2 + 0.2*x*y + 0.09*y**2

# Obtener la solución óptima del caso ii)
x_opt, y_opt = 1/3, 2/3

# Calcular el valor óptimo
optimal_value = objective(x_opt, y_opt)

print('El valor óptimo es:', optimal_value)