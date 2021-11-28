import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


filenames = ['all_diseased', 'dead', 'healed', 'diseased']

X = None
Y = None

# for k in range(4):

with open('my_file.txt', 'r') as f:
    Y = np.array(list(map(int, f.read().split())))
X = np.arange(1, len(Y) + 1)

a = sym.Symbol('a')
b = sym.Symbol('b')

eq1 = a * sum(X**2) + b * sum(X) - sum(X * Y)
eq2 = a * sum(X) + b * len(X) - sum(Y)

result = sym.solve((eq1, eq2), a, b)

x = np.linspace(0, 625, 10000)
y = result[a] * x + result[b]

plt.plot(X, Y, '.')
plt.plot(x, y)

plt.grid()
plt.show()
