import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import random


def Sphere( N, r, x0 = 0, y0 = 0, z0 = 0 ):
    
    samples = np.zeros((N,3))


    for i in range(N):
        theta = random.uniform( 0, 6.28 )
        gamma = random.uniform( 0, 3.1416 )
        samples[i,0] = x0 + r*np.cos(theta)*np.sin(gamma)
        samples[i,1] = y0 + r*np.sin(theta)*np.sin(gamma)
        samples[i,2] = z0 + r*np.cos(gamma)
        #print samples[i,0],", ", samples[i,1],", ", samples[i,2],", "
    
    return samples


def main():
    N = 500
    x0 = 0
    y0 = 0
    z0 = 0
    r = 0.3
    samples = Sphere( N, r, x0, y0,z0 )
    
    X = samples[:,0]
    Y = samples[:,1]
    Z = samples[:,2]

    fig = plt.figure()
    ax = fig.add_subplot( 1, 1, 1, projection='3d' )
    ax.scatter( X,Y,Z, c='b', marker='o' )
    plt.show()
    
if __name__ == "__main__":
    main()
    
