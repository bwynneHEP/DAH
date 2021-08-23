# Import I/O expander chip library
from DAH import PCF8574A

# Setup chip
pcf = PCF8574A(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)

# Insert your code here
