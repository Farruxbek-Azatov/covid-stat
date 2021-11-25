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

    for i in range(1, len(Y) - 2):
        Y1 = lagrange(X[i-1:i+2], Y[i-1:i+2])
        Y2 = lagrange(X[i:i+3], Y[i:i+3])
        x = np.linspace(X[i], X[i+1], 1000)
        S3 = np.zeros(1000)

        for j in range(3):
            S3 += ((1/2)-x) * (Y1[j] * x**(2-j)) + \
                ((1/2)+x) * (Y2[j] * x**(2-j))

        plt.plot(x, S3, c=colors[k])
    plt.plot(X, Y, '.', c='red')


plt.grid()
plt.legend()
plt.show()
