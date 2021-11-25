import numpy as np
import matplotlib.pyplot as plt
from interp import lagrange


def draw_graph(R, leg=None):
    n = len(R)
    X = np.linspace(1, n, 1000)
    Y = np.zeros(1000)
    for i in range(n):
        Y += R[i]*X**(n-i-1)

    plt.plot(X, Y, label=f'{leg}')


filename = ['all_diseased', 'dead', 'healed', 'diseased']

X = None
Y = None

for i in range(4):

    with open(f'number_of_{filename[i]}.txt', 'r') as f:
        Y = np.array(list(map(int, f.read().split())))
    X = np.arange(1, len(Y) + 1)

    R = lagrange(X, Y)
    draw_graph(R, filename[i])

plt.grid()
plt.legend()
plt.show()
