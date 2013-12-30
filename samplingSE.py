import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import random

def c( w,m ):
    cw = np.cos(w)
    return np.sign(cw)*math.pow(  np.abs(cw), m )

def s( w,m ):
    sw = np.sin(w)
    return np.sign(sw)*math.pow(  np.abs(sw), m )

def SQ( N, a1, a2, a3, t,r ):
    
    samples = np.zeros((N,3))


    for i in range(N):
        v = random.uniform( -1.57, 1.57 )
        u = random.uniform( -3.1416, 3.1416 )
        samples[i,0] = a1*c(v,2.0/t)*c(u,2.0/r)
        samples[i,1] = a2*c(v,2.0/t)*s(u,2.0/r)
        samples[i,2] = a3*s(v,2.0/t) 
        print samples[i,0],", ", samples[i,1],", ", samples[i,2],", "
    
    return samples


def main():
    a1 = 3.0
    a2 = 3.0
    a3 = 4.0
    t = 2.5
    r = 2.0
    N = 500
    samples = SQ( N, a1, a2, a3, t, r)
    
    X = samples[:,0]
    Y = samples[:,1]
    Z = samples[:,2]

    fig = plt.figure()
    ax = fig.add_subplot( 1, 1, 1, projection='3d' )
    ax.scatter( X,Y,Z, c='b', marker='o' )
    plt.show()
    
if __name__ == "__main__":
    main()
    
