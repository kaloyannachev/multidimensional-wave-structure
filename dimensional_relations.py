import numpy as np
from .constants import c_3D

def c_D(D):
    return c_3D * np.sqrt(D/3.0)

def E_massive_ratio(D):
    return D/3.0

def E_photon_ratio(D):
    return np.sqrt(D/3.0)

def R_ratio(D):
    return 3.0 / D
