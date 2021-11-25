import numpy as np
import matplotlib.pyplot as plt
from interp import lagrange


filenames = ['all_diseased', 'dead', 'healed', 'diseased']
colors = ['blue', 'black', 'green', 'lightblue']
X = None
Y = None

for k in range(4):

    with open(f'number_of_{filenames[k]}.txt', 'r') as f:
        Y = np.array(list(map(int, f.read().split())))
    X = np.arange(1, len(Y) + 1)

    for i in range(len(Y) - 1):
        P = lagrange(X[i: i+2], Y[i: i+2])
        x = np.linspace(X[i], X[i+1], 1000)
        y = np.zeros(1000)

        for j in range(2):
            y += P[j] * x**(1-j)

        plt.plot(x, y, c=colors[k])
    plt.plot(X, Y, '.', c='red')


plt.grid()
plt.legend()
plt.show()
