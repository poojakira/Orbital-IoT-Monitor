import numpy as np
class OrbitalPhysics:
    def get_density(self, alt):
        rho0 = 1.225; H = 8500
        return rho0 * np.exp(-alt / H)
    
    def calculate_torque(self, i, alpha):
        return i * alpha # T = I * alpha