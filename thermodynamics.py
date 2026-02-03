import numpy as np
class ReentryThermalEngine:
    def calculate_flux(self, rho, v, rn=0.1):
        k = 1.7415e-4
        return k * np.sqrt(rho / rn) * (v**3)

    def get_temp(self, q):
        sig = 5.67e-8; eps = 0.8
        return (q / (eps * sig))**0.25 - 273.15