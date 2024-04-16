import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k


def planck_distribution(T, wavelength_i, wavelength_f, n=1000):
    wavelength = np.linspace(wavelength_i, wavelength_f, n)
    distribution = ((8 * np.pi * h * c) / wavelength**5) * (1 / (np.exp((h * c) / (wavelength * k * T)) - 1))

    return wavelength, distribution


wavelength_i = 0.1e-6
wavelength_f = 3e-6

T = 4500, 5000, 5500, 6000

for i in range(len(T)):
    wavelength, distribution = planck_distribution(T[i], wavelength_i, wavelength_f)

    plt.plot(wavelength, distribution, label=f"$T={T[i]}K$")

plt.legend()

def integrate_planck_distribution(T_i, T_f, n=100):
    T = np.linspace(T_i, T_f, n)
    R = np.empty(len(T))

    for i in range(len(T)):
        wavelength, distribution = planck_distribution(
            T[i], wavelength_i, wavelength_f)

        R[i] = np.trapz(distribution, x=wavelength)

    return T, R

T_i = 2000
T_f = 4000

T, R = integrate_planck_distribution(T_i, T_f)

lnT = np.log(T)
lnR = np.log(R)

A = np.array([[sum(lnT**2), sum(lnT)], [sum(lnT), len(lnT)]])
b = np.array([sum(lnT*lnR), sum(lnR)])

N, lnS = np.linalg.solve(A, b)

print(f"The value of the N is {N:.2f}")

plt.show()
