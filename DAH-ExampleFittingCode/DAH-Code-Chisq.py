import sys
import numpy as np 
import pylab as pl
from scipy.optimize import minimize


#------------------
#Read in the data
#Python works out that the fiule has three numbers per line, and returns a list-of-lists

def readData(file):
    data = np.loadtxt(sys.argv[1])
    print '\n Data is in formmat  [x, y, error] '
    print data
    return data



#----------------------------------
# define the straight line function

#Here is a conventional funciton which works
#def linear( datapoint, parameters ):
#    #x = datappint[0]
#    #m = parameters[0]
#    #c = parameters[1]
#    return parameters[0]*datapoint[0] + parameters[1]

#Here is a slightly simpler way of doing it
linear = lambda datapoint, parameters : parameters[0]*datapoint[0] + parameters[1]



#----------------------------------
# define a generic function for use in fitting.
# I do this in order to promise a set of methods together as per an interface
# In partiucular it was convenient to have  method which evaluates a single value, and one which evaluates a vector.

class FitFunction:

    def __init__( self, func ):
        self.func =  lambda datapoint, parameters : parameters[0]*datapoint[0] + parameters[1]
        #self.integral =  lambda datapoint, parameters : 0.5 * parameters[0]*datapoint[0]**2 + parameters[1]*datapoint[0]

    def evaluate( self, datapoint, parameters ):
        return self.func( datapoint, parameters )

    def evaluateVector( self, data, parameters ):
        yvec = [self.func( datapoint, parameters ) for datapoint in data ]
        return yvec





#------------------------------
# define a generic chisq object (this works for any function object which has an evaluate method)
class Chisq:

    def __init__(self, function, data ):
        self.data = data
        self.function = function

    def evaluate( self,parameters ):
        chisq = 0
        for datapoint in self.data:
            ymeas = datapoint[1]
            ytheory = self.function.evaluate( datapoint, parameters )
            diff = (ymeas-ytheory)/datapoint[2]
            chisq += diff**2
        return chisq



#-------------------------------
#Main code
def main() :

    #Read in the data
    data = readData(sys.argv[1])

    #Make a fit function object using the linear (straight line) function
    #Note that fitFunction is a generic class (it doesnt itself know anytihng about the form of the function)
    #It bundles a set of methods.
    #It is constructed with a specific functon in its constructor
    fitFunction = FitFunction( linear )
    
    
    #Make a chisq object
    #It is constructed with the fitFunction object.
    chisq = Chisq( fitFunction, data )


    #Set initial parameters for the function and look at the initial chisq for fun
    parameters = [0,1]
    print '\n The initial chisq is ', chisq.evaluate(parameters)


    #Now minimise the chisq using the scipy.optimize.minimise function.
    #This returns a result object.
    result = minimize( chisq.evaluate, parameters, method='nelder-mead', options={'xtol': 1e-8, 'disp': True} )

    finalResult = result.x
    print '\n The final best fit parameters are ', finalResult


    #Plot the input date
    x = [elem[0] for elem in data ]
    y = [elem[1] for elem in data ]
    ex = np.zeros(len(x))
    ey = [elem[2] for elem in data ]
    pl.figure()
    pl.xlim([min(x)-0.5,max(x)+0.5])
    pl.ylim([min(y)-0.5,max(y)+0.5])
    pl.errorbar( x,y, xerr=ex, yerr=ey, fmt='o' )
    pl.title("Input data and best fit ")

    #Plot the best fit line on top of the data
    yresult = fitFunction.evaluateVector( data, finalResult )
    pl.plot( x, yresult )

    pl.show()

    #pl.plot( data )
    #Simple example to produce a histogram of the errors
    #pl.hist(data[:], bins=50)
    #pl.savefig('outputHistogram.pdf')


#-------------
#Do it
main()
