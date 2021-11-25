import numpy as np
import matplotlib.pyplot as plt
from interp import lagrange


def draw_parabola(R, start=0, end=1):
    X = np.linspace(start, end, 1000)
    Y = np.zeros(1000)
    n = len(R)
    for i in range(n):
        Y += R[i]*X**(n-i-1)

    plt.plot(X, Y)


X = None
Y = None

with open(f'number_of_all_diseased.txt', 'r') as f:
    Y = np.array(list(map(int, f.read().split())))
X = np.arange(1, len(Y) + 1)

for i in range(1, len(Y) - 1):
    Result = lagrange(X[i-1:i+2], Y[i-1:i+2])
    draw_parabola(Result, start=i, end=i+2)

plt.grid()
plt.show()
