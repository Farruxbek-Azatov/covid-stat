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
