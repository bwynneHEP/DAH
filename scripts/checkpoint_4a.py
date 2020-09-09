# Imports
import webiopi
from webiopi.devices.digital.pcf8574 import PCF8574A

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Setup chip
mcp = PCF8574A(slave=0x38)

# Set which PCF8574 GPIO pin is connected to the LED
LED0 = 0

# Set pin as output
mcp.setFunction(LED0, GPIO.OUT)

# Turn on the LED
mcp.digitalWrite(LED0, GPIO.LOW)
 
# Insert your code here
