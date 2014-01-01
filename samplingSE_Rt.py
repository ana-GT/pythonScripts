# ******************************************************************
# Generate superellipsoids with rotation and translations changed
# ******************************************************************
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import random

# Cw
def c( w,m ):
    cw = np.cos(w)
    return np.sign(cw)*math.pow(  np.abs(cw), m )

# Sw
def s( w,m ):
    sw = np.sin(w)
    return np.sign(sw)*math.pow(  np.abs(sw), m )

# Super Quadric
def SQ( N, a1, a2, a3, t,r ):
    
    samples = np.zeros((N,3))

    for i in range(N):
        v = random.uniform( -1.57, 1.57 )
        u = random.uniform( -3.1416, 3.1416 )
        samples[i,0] = a1*c(v,2.0/t)*c(u,2.0/r)
        samples[i,1] = a2*c(v,2.0/t)*s(u,2.0/r)
        samples[i,2] = a3*s(v,2.0/t) 
    
    return samples

# Apply rotation aa and translation t
def setAppTrans( t ) :
    def applyTrans( p ) :
        return [p[0] + t[0], p[1] + t[1], p[2] + t[2] ]
    return applyTrans

# Rotate v around axis k an angle of theta
def setAppRot(k, theta) :
    def applyRot(v):
        ct = np.cos(theta)
        st = np.sin(theta)
        return ct*v  + st*np.cross(k,v) + (np.inner(k,v)*(1-ct))*k
    return applyRot

def rotTrans( samples, aa, theta, t ) :
    
    translate = setAppTrans( t )
    samplesT = np.array( map(translate, samples) )
    rotate = setAppRot( aa, theta )
    samplesRT = np.array( map(rotate, samplesT) )
    return samplesRT


# Main
def main():
    a1 = 3.0; a2 = 3.0; a3 = 4.0
    t = 2.5; r = 2.0
    N = 500
    samples = SQ( N, a1, a2, a3, t, r)

    AA_axis = np.array([0,1,0])
    AA_angle = 0.3
    trans = [0.2, 0.3, 0.0]
    samples_rt = rotTrans( samples, AA_axis, AA_angle, trans )

    X = samples_rt[:,0]
    Y = samples_rt[:,1]
    Z = samples_rt[:,2]

    fig = plt.figure()
    ax = fig.add_subplot( 1, 1, 1, projection='3d', aspect='equal' )
    ax.scatter( X,Y,Z, c='b', marker='o' )
    plt.show()
    
if __name__ == "__main__":
    main()
    
