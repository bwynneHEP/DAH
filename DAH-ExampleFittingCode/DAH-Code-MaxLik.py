import sys
import numpy as np 
import pylab as pl
from scipy.optimize import minimize


#------------------
#Read in the data
#Python works out that the fiule has three numbers per line, and returns a list-of-lists

def readData(file):
    data = np.loadtxt(sys.argv[1])
    print '\nRead input data file ',sys.argv[1]
    print 'The first few entries in the data are ', data[0:10:1]
    return data



#----------------------------------
# define the straight line function

#Here is a conventional funciton which works
#def linear( datapoint, parameters ):
#    #x = datappint[0]
#    #m = parameters[0]
#    #c = parameters[1]
#    return parameters[0]*datapoint[0] + parameters[1]

exponential = lambda datapoint, parameters : (1./parameters[0]) * np.exp( - datapoint/parameters[0] )


#----------------------------------
# define a Linear PDF for use in ML fitting.

class Pdf:

    def __init__( self, func  ):
        self.func =  func

    def evaluate( self, datapoint, parameters ):
        return self.func( datapoint, parameters )

    def evaluateVector( self, data, parameters ):
        yvec = [self.func( datapoint, parameters ) for datapoint in data ]
        return yvec



#------------------------------
# define a generic negative log likelihood class (this works for any pdf object which has a evaluatePdf method)
class NLL:

    def __init__(self, pdf, data ):
        self.data = data
        self.pdf = pdf

    def evaluateNLL( self,parameters ):
        ll = 0
        for datapoint in self.data:
            ll += np.log( self.pdf.evaluate( datapoint, parameters ) )
        return -ll



#-------------------------------
#Main code
def main() :

    #Read in the data
    data = readData(sys.argv[1])

    #Make a fit function object using the linear (straight line) function
    #Note that fitFunction is a generic class (it doesnt itself know anytihng about the form of the function)
    #It bundles a set of methods.
    #It is constructed with a specific functon in its constructor
    exponentialPdf = Pdf(exponential)
    
    
    #Make a chisq object
    #It is constructed with the fitFunction object.
    nll = NLL( exponentialPdf, data )


    #Set the initial parameters
    parameters = [2.0]
    print '\n The initial parameter value(s) are ', parameters

    #Now minimise the chisq using the scipy.optimize.minimise function.
    #This returns a result object.
    result = minimize( nll.evaluateNLL, parameters, method='nelder-mead', options={'xtol': 1e-8, 'disp': True} )

    finalResult = result.x
    print '\n The final best fit parameters are ', finalResult


    #Plot the input data
    pl.figure()
    yvals, bins, patches = pl.hist( data, 50 )
    pl.title("Input data and best fit ")

    #Plot the best fit line on top of the data. A scale factor is needed to overlay them.
    yresult = exponentialPdf.evaluateVector( bins, finalResult )
    scaleFactor =  yvals[0] / yresult[0]
    yresult[:] =  [ y*scaleFactor for y in yresult]
    pl.plot( bins, yresult )

    pl.show()


#-------------
#Do it
main()
