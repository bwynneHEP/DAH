import pylab
import matplotlib.animation as animation
import datetime

# Empty arrays of time and measurement values to plot
timeValues = [ ]
measurements = [ ]

# Set up the plot object
plotFigure = pylab.figure()

# The function to call each time the plot is updated
def updatePlot( i ):

    timeValues.append( datetime.datetime.now() ) # Store time
    measurements.append( MEASUREMENT )           # Store temperature
    plotFigure.clear()                           # Clear the old plot
    pylab.plot( timeValues, measurements )       # Make the new plot

# Make the animated plot
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000 )
pylab.show()
