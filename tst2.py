import numpy as np
from itertools import product
from matplotlib import pyplot as plt

k = 1  # Boltzman Constant

possible_spins = [+1, -1]
lattice_points = 4

T = 0.1
J = 1
h = 0.1

configuarations = np.array(list(product(possible_spins, repeat=lattice_points)))

for i in range(len(configuarations)):
    print(configuarations[i])


def absolute_energy(configuarations, J, h):
    H = np.zeros(len(configuarations))

    for i in range(len(configuarations)):
        for j in range(len(configuarations[i])):
            H[i] -= (
                J * configuarations[i][j - 1] * configuarations[i][j]
                + h * configuarations[i][j]
            )

    return H


energy = absolute_energy(configuarations, J, h)

for i in range(len(configuarations)):
    print(configuarations[i], "\t", energy[i])


def partition_function(configuarations, T):
    energy = absolute_energy(configuarations, J, h)

    Z = 0
    for i in range(len(configuarations)):
        Z += np.exp(-energy[i] / (k * T))

    return Z


print("Partition Function:", partition_function(configuarations, T))


def configuaration_probabilities(configuarations, T):
    energy = absolute_energy(configuarations, J, h)
    Z = partition_function(configuarations, T)

    probabilities = np.empty(len(configuarations))
    for i in range(len(configuarations)):
        probabilities[i] = np.exp(-energy[i] / (k * T)) / Z

    return probabilities


probabilities = configuaration_probabilities(configuarations, T)

for i in range(len(configuarations)):
    print(configuarations[i], "\t", probabilities[i])


def average_energy(configuarations, T):
    energy = absolute_energy(configuarations, J, h)
    probabilities = configuaration_probabilities(configuarations, T)

    E = 0
    for i in range(len(configuarations)):
        E += energy[i] * probabilities[i]

    return E


print("Average Energy:", average_energy(configuarations, T))


def absolute_magnetisation(configuarations):
    M = np.empty(len(configuarations))

    for i in range(len(configuarations)):
        M[i] = np.sum(configuarations[i]) / len(configuarations)

    return M


M = absolute_magnetisation(configuarations)

for i in range(len(configuarations)):
    print(configuarations[i], "\t", M[i])


def average_magnetisation(configuarations, T):
    magnetisation = absolute_magnetisation(configuarations)
    probabilities = configuaration_probabilities(configuarations, T)

    M = 0
    for i in range(len(configuarations)):
        M += magnetisation[i] * probabilities[i]

    return M


print("Average Magnetisation:", average_magnetisation(configuarations, T))

T_i = 0.01
T_f = 10

T = np.linspace(T_i, T_f, 1000)
E = np.empty(len(T))

for i in range(len(T)):
    E[i] = average_energy(configuarations, T[i])

plt.subplot(2, 1, 1)
plt.plot(T, E)
plt.title("Average Energy vs Temperature")

M = np.empty(len(T))

for i in range(len(T)):
    M[i] = average_magnetisation(configuarations, T[i])

plt.subplot(2, 1, 2)
plt.plot(T, M)
plt.title("Average Magnetisation vs Temperature")

plt.show()
