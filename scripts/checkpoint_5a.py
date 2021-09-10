# Import
from DAH import DS18B20

# Readout temperature sensor
tmp0 = DS18B20( address="10-00080265b6d6" )
tmp0.getCelsius()
