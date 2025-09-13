import numpy as np
from scipy.differentiate import derivative
from scipy.integrate import quad
from scipy.optimize import minimize, Bounds, NonlinearConstraint
from sympy import symbols, diff, sin, log, integrate

def F(x):
    return np.sin(np.log(x))

def f(x):
    return np.cos(np.log(x))/x

def objective(x):
    return (x[0] - 3)**2 + x[1]

def constraint(x):
    return -2*x[0] + 3*x[1] - 4

x0 = 4
a = 3
b = 8
first_deriv = derivative(F, x0)
second_deriv = derivative(f, x0)
print("Первая производная в точке х0:", first_deriv.df)
print("Вторая производная в точке х0:", second_deriv.df)

x = symbols('x')
y = sin(log(x))
first_deriv = diff(y,x)
second_deriv = diff(y, x, 2)
print("\nПервая производная:", first_deriv)
print("Вторая производная:", second_deriv)

integral_quad, error = quad(f, b, a)
print("\nОпределенный интеграл в области [a, b] равен:", integral_quad)

integral_quad = integrate(y, x)
print("\nНеопределенный интеграл имеет вид:", integral_quad, "+ C")

bounds = Bounds([0, 0], [np.inf, np.inf])
nonlinear_constraint = NonlinearConstraint(constraint, 0, np.inf)
x0 = [1.0, 2.0]
result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=[nonlinear_constraint])
print("\nx1 =" ,result.x[0], " х2 =", result.x[1])