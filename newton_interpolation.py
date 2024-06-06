import numpy as np
import matplotlib.pyplot as plt

# Data dari soal
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Newton
def newton_interpolation(x_values, y_values, x):
    def divided_diff(x_values, y_values):
        n = len(y_values)
        coef = np.zeros([n, n])
        coef[:,0] = y_values
        
        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_values[i+j] - x_values[i])
                
        return coef[0, :]
    
    coef = divided_diff(x_values, y_values)
    n = len(x_values) - 1 
    p = coef[n]
    
    for k in range(1,n+1):
        p = coef[n-k] + (x - x_values[n-k])*p
        
    return p

# Plotting the results
x_range = np.linspace(5, 40, 400)
y_newton = [newton_interpolation(x, y, xi) for xi in x_range]

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_range, y_newton, label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi dengan Polinom Newton')
plt.grid(True)
plt.show()
