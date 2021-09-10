import serial
import numpy

# open the serial port with baud rate 115200bps
# this is the rate used by the Arduino microcontroller
# Arduino will be on port ttyACM0 by default
ser=serial.Serial('/dev/ttyACM0',115200, timeout=5)  

# a small delay may be necessary
# to give the Arduino time to respond
# you may want to experimentally find the shortest
# delay that makes the code work
time.sleep(1)

# clear the serial port buffer
# this is sometimes required to 
# initialize communication between R-Pi and Arduino
ser.flushInput()  

# a small delay may be necessary, again
time.sleep(1)

# tell the Arduino to start sampling at a given frequency
# the first value can be anything between 4 and 255
# the larger the value the slower the sampling will be
# the second value should always be 2
ser.write(bytes([4,2]))

# a small delay may be necessary, again
time.sleep(1)

# read data sample from Arduino ADC
# (1024 bytes, 8-bit resolution)
data=ser.read(1024)

# convert data to an array of integers
# (value = 0..255, 0 = zero voltage, 255 = +5V)
values=numpy.frombuffer(data,dtype=numpy.uint8)
