import numpy as np
import matplotlib.pyplot as plt


def lagrange(X, Y):
    n = len(Y)
    Result = np.zeros(n)

    for counter in range(n):
        T = np.zeros(n)
        T[0] = 1
        qoshimcha_massiv = np.zeros(n)
        qoshimcha_massiv[0] = 1
        p = 1.0
        for i in range(n):
            if(counter != i):
                p *= (X[counter]-X[i])
        p = Y[counter]/p
        j = 1
        for k in range(n):

            if (counter != k):
                for i in range(j):
                    T[i+1] += float(qoshimcha_massiv[i]*-X[k])
                for i in range(1, j+1):
                    qoshimcha_massiv[i] = T[i]
                j += 1

        for i in range(n):
            Result[i] += (T[i]*p)

    return Result


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
