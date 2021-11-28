import numpy as np
import matplotlib.pyplot as plt


filename = ['all_diseased', 'dead', 'healed', 'diseased']

X = None
Y = None

for i in range(4):

    with open(f'number_of_{filename[i]}.txt', 'r') as f:
        Y = np.array(list(map(int, f.read().split())))
    X = np.arange(1, len(Y) + 1)
