# Import ADC chip library
from DAH import MCP3208
 
# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )

# Read all ADC channels in Volts.
print( ADC0.analogReadAllVolt() )

# Play with the following methods
ADC0.analogCount()
ADC0.analogResolution()
ADC0.analogMaximum()
ADC0.analogReference()
ADC0.analogRead( channel )
ADC0.analogReadFloat( channel )
ADC0.analogReadVolt( channel )
ADC0.analogReadAll()
ADC0.analogReadAllFloat()
ADC0.analogReadAllVolt()
