import numpy as np
from scipy import integrate

def my_function(x):
    return x**2

lower_limit = 0
upper_limit = 5

print("about to execute integrate.quad()")
integral_value, error_estimate = integrate.quad(my_function, lower_limit, upper_limit)

print (
    f"The definite integral of x^2 from "
    f"{lower_limit} to {upper_limit} is approximately: {integral_value}"
)
print(f"Estimated error: {error_estimate}")

import matplotlib.pyplot as plt

x = np.linspace(lower_limit, upper_limit, 100)
y = my_function(x)

plt.figure(figsize=(8,6))
plt.plot(x, y, label='$f(x) = x^2$')
plt.fill_between(x, y, color='lightblue', alpha=0.5, label='Area under the curve')
plt.axvline(lower_limit, color='gray', linestyle='--', label=f'Lower Limit: {lower_limit}')
plt.axvline(upper_limit, color='gray', linestyle='--', label=f'Upper Limit: {upper_limit}')
plt.title('numerical integration using SciPy')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
