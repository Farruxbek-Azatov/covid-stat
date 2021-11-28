import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


filenames = ['all_diseased', 'dead', 'healed', 'diseased']

X = None
Y = None

# for k in range(4):

with open(f'my_file.txt', 'r') as f:
    Y = np.array(list(map(int, f.read().split())))
X = np.arange(1, len(Y) + 1, dtype='d')

a = sym.Symbol('a')
b = sym.Symbol('b')
c = sym.Symbol('c')

eq1 = a * sum(X**4) + b * sum(X**3) + c * sum(X**2) - sum(X**2 * Y)
eq2 = a * sum(X**3) + b * sum(X**2) + c * sum(X) - sum(X * Y)
eq3 = a * sum(X**2) + b * sum(X) + c * len(X) - sum(Y)

r = sym.solve((eq1, eq2, eq3), a, b, c)
print(r)

x = np.linspace(0, 625, 1000)
y = r[a] * x**2 + r[b] * x + r[c]

plt.plot(X, Y, '.')
plt.plot(x, y)

plt.grid()
plt.show()
