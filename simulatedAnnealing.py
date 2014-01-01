# =========================
# Simulated Annealing
# =========================

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np
import time

mpl.rcParams['legend.fontsize'] = 10

# getRandomNeighbor
def getRandomNeighbor( x, y, max_x, max_y):
    
    dx, dy = 0,0
    
    while dx == 0 and dy == 0:
        if x != 0 and x != max_x: 
            dx = random.randint(-1,1)            
        elif x== 0:
            dx = random.randint(0,1)
        elif x==max_x:
            dx = random.randint(-1,0)    
        
        if y != 0 and y != max_y:
            dy = random.randint(-1,1)
        elif y == 0:
            dy = random.randint(0,1)        
        elif y == max_y:
            dy = random.randint(-1,0)
       
        
    return x+dx, y+dy
    
# *******************
# Main function
# *******************
def main():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # A finite set S
    vs = -5
    vf = 5
    numSamples = 100
    x = np.linspace( vs, vf, numSamples )
    y = np.linspace( vs, vf, numSamples )
    X,Y = np.meshgrid(x,y)
    Z = X**2 + Y**2 +1.5

    # Graph function
    ax.plot_wireframe( X, Y, Z, label="Example of unknown function")
    # Show
    plt.ion() # Put in interactive mode
    #plt.show(block=False)
    
    #########################
    # Find minimum

    # Start with a initial point 
    x0 = random.randint( 0, numSamples )
    y0 = random.randint( 0, numSamples )
    z0 = Z[x0][y0]

    numIterations = 200
    xc = x0
    yc = y0
    
    for i in range(numIterations):
    
        # Get a random neighbor
        xn, yn = getRandomNeighbor(xc, yc, numSamples-1, numSamples-1 )
        
        # Let's see if neighbor will be the new current state:
        
        # If energy of xn,yn is smaller than xc,yc then for sure
        if Z[xn][yn] < Z[xc][yc]:
            xc,yc = xn, yn
        else:
            # If not, we accept it with some probability
            xc,yc = xc,yc

        ax.scatter( X[0][xc],Y[yc][0],Z[xc][yc], s=400, c='r')    
        plt.draw()
        time.sleep(0.01)    

    print("Done!")
    plt.show()    
    
if __name__ == "__main__":
     main()   
	
