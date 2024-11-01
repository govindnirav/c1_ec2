import numpy as np

class StochasticProcess:
    """
    Base class for all stochastic processes.
    """

    def __init__(self, y0, mu, sigma):
        self.y0 = y0  # Initial value 
        self.mu = mu  # Expected return 
        self.sigma = sigma  # Volatility

    def simulate(self, T, n, M):
        """
        Simulate the stochastic process (to be implemented by subclasses).
        Acts as a placeholder for simulation logic, which has to be implemented by all subclasses.
         - Subclasses can implement their own version of the function but it still has to follow the rules set here.
        """
        raise NotImplementedError("Subclasses must implement this method") 
        """If a subclass does not implement its own version of simulate 
        and someone tries to call simulate on an instance of that subclass, 
        the program will throw a NotImplementedError. This error clearly indicates that the method has not been implemented.
        """

class GeometricBrownianMotion(StochasticProcess):
    """
    Subclass of Stochastic Process used to simulate GBM
    """

    def simulate(self, T, n, M):
        """
        Has its own simulate function (satisfying the above placeholder) with a more specific functional form
        according to that of GBM (from ec2.pdf)
        Simulate Geometric Brownian Motion.
         - parameter T: Time horizon
         - parameter n: Number of time steps
         - parameter M: Number of simulation paths
         - return: Array of simulated paths
        """
        dt = T / n #each time step
        times = np.linspace(0, T, n+1)
        y = np.zeros((n+1, M))
        y[0] = self.y0
        for t in range(1, n + 1):
            dbt = np.random.normal(0, np.sqrt(dt), size=M)
            y[t] = y[t-1] * np.exp((self.mu - self.sigma ** 2 / 2) * dt + self.sigma * dbt)
        return y

