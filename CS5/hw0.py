# *************
# Homework 1
# *************
import math

# Inverse
def inverse(n):
   return 1.0 / n

# Exponential
def e(n):
    summation = 1
    numbers = range(1,n+1)
    facts = map( math.factorial, numbers )
    invers = map( inverse, facts )

    return 1 + sum(invers)
# Error
def error(n):
    return abs( math.e - e(n) )

# Factorial
def mult(x,y):
    """Returns the product of x and y """
    return x*y

def factorial(n):
    numbers = range(1,n+1)
    return reduce( mult, numbers)

# mean
def add( x, y):
    return x + y

def mean( input ):
    n = len( input )
    added = reduce( add, input )
    return  float( added ) / n

# Extra credit
def div(k):
    return 42 % k == 0

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    dv = divides(n)
    results = map( dv, range(2,n) )
    return not (sum( results ) > 0)
# Main
def main():
    print "Print evaluations of functions used"
    print inverse(3)
    print e(1)
    print e(2)
    print e(3)
    print e(10)
    print error(1)
    print error(2)
    print error(3)
    print error(10)
    print factorial(5)
    print mean([1, 2, 3, 4])
    print div(21)
    print div(25)
    print "Changes!"
    dp = divides( 121 )
    print dp( 11 )
    print dp( 3 )
    print "Check prime"
    print prime(71)
    print prime(25)
    
# Call main    
if __name__ == "__main__":
    main()

    
