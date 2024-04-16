import numpy as np
import matplotlib.pyplot as plt
from math import ceil, floor

def collatz(n):
    count = 0
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    return count

min_int = 5 
max_int = 1000 

collatz_steps = np.empty(max_int - min_int + 1)

for i in range(min_int, max_int + 1):
    collatz_steps[i - min_int] = collatz(i)

n =10
N = 100, 1000, 10000, 100000

for i in range(len(N)):
    rand_steps = np.random.choice(collatz_steps, (N[i], n))
    mean_steps = np.mean(rand_steps, axis=1)

    plt.subplot(ceil(len(N)/2), ceil(len(N)/2), i + 1)
    plt.hist(mean_steps, bins=np.arange(floor(min(mean_steps)), ceil(max(mean_steps)), 1), label=f"N = {N[i]}")
    plt.legend()

plt.show()