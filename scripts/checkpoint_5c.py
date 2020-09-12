# Import
from webiopi.devices.sensor.onewiretemp import DS18S20

# Readout temperature sensor
tmp0 = DS18S20("10-00080265b6d6")
tmp1 = DS18S20("10-000802cb3b5c")
print ( str( tmp0.getCelsius() ) + ", " + str( tmp1.getCelsius() ) )
