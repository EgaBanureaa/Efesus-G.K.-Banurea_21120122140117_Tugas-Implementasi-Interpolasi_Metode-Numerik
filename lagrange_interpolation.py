import numpy as np
import matplotlib.pyplot as plt

# Data dari soal
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Lagrange
def lagrange_interpolation(x_values, y_values, x):
    def basis(i, x):
        term = [(x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if j != i]
        return np.prod(term, axis=0)

    return sum(y_values[i] * basis(i, x) for i in range(len(x_values)))

# Plotting the results
x_range = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_range]

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_range, y_lagrange, label='Lagrange Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi dengan Polinom Lagrange')
plt.grid(True)
plt.show()
