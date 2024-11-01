import numpy as np
import matplotlib.pyplot as plt

## Defining parameters
# drift coefficent
MU = 0.1
# number of steps
N = 100
# time in years
T = 1
# number of sims
M = 100
# initial stock price
Y0 = 100
# volatility
SIGMA = 0.3

##########################################################################################################################
def simulate(self, T, N):
    dt = T / N #each time step
    times = np.linspace(0, T, N)
    Y = np.zeros(N)
    Y[0] = self.Y0
    for t in range(1, N):
        dBt = np.random.normal(0, np.sqrt(dt), size=(M,N)).T
        Y[t] = Y[t-1] * np.exp((self.mu - self.sigma ** 2 / 2) * dt + self.sigma * dBt)
    return times, Y


# calc each time step
dt = T/N
# simulation using numpy arrays
St = np.exp(
    (MU - SIGMA ** 2 / 2) * dt
    + SIGMA * np.random.normal(0, np.sqrt(dt), size=(M,N)).T
)
# include array of 1's
St = np.vstack([np.ones(M), St])
# multiply through by S0 and return the cumulative product of elements along a given simulation path (axis=0). 
St = S0 * St.cumprod(axis=0)

##########################################################################################################################