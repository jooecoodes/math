import sympy as sp
import math as m

# Define the variable and the function
x = sp.Symbol('x')
f = x**5 * sp.sin(x) + sp.exp(x) * sp.cos(x)


print(f"Equation: {f}")

# 1st derivative
first_derivative = sp.diff(f, x)
print(f"1st Derivative: {first_derivative}")

# 2nd derivative
second_derivative = sp.diff(f, x, 2)
print(f"2nd Derivative: {second_derivative}")

# 3rd derivative
third_derivative = sp.diff(f, x, 3)
print(f"3rd Derivative: {third_derivative}")

# Indefinite integral of the function
indefinite_integral = sp.integrate(f, x)
print(f"Indefinite Integral: {indefinite_integral}")

# Definite integral of the function from 0 to 1
definite_integral = sp.integrate(f, (x, 0, 1))

print(f"Definite Integral from 0 to 1: {definite_integral}")

