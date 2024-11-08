import argparse
from .gbm import GeometricBrownianMotion
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Simulate Geometric Brownian Motion")
    parser.add_argument('--y0', type=float, default=1.0, help='Initial value of the process')
    parser.add_argument('--mu', type=float, default=0.1, help='Drift coefficient')
    parser.add_argument('--sigma', type=float, default=0.2, help='Diffusion coefficient')
    parser.add_argument('--T', type=float, default=1.0, help='Time horizon')
    parser.add_argument('--n', type=int, default=1000, help='Number of time steps')
    parser.add_argument('--M', type=int, default=1, help='Number of simulation paths')
    parser.add_argument('--output', type=str, help='Filename to save the plot (e.g., gbm_plot.png)')

    args = parser.parse_args()

    # Create an instance of GeometricBrownianMotion
    gbm = GeometricBrownianMotion(y0=args.y0, mu=args.mu, sigma=args.sigma)
    # Simulate the paths
    y = gbm.simulate(T=args.T, n=args.n, M= args.M)

    # Plot the simulated paths
    times = np.linspace(0, args.T, args.n + 1)
    for i in range(args.M):
        plt.plot(times, y[:, i])
    plt.title("Simulated Geometric Brownian Motion Paths")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.show()

# __name__ is a var python uses and this line provides a safety check. In case someone imports this file, the main function will not execute this.
if __name__ == "__main__":
    main()