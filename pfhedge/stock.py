import numpy as np

class stock:
    def __init__(self, vol, dt):
        self.vol = vol
        self.dt = dt

    def simulate(self, n_paths=2):
        return np.random.normal(0, self.vol, (n_paths, self.dt))
    