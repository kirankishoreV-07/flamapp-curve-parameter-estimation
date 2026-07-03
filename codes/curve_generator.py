import numpy as np

def curve_gen(theta_deg,M,X,points=1000):
    theta = np.radians(theta_deg)

    t = np.linspace(6,60,points)

    x = (t*np.cos(theta)-np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta)+X)

    y = (42+t*np.sin(theta)+np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta))

    return x, y