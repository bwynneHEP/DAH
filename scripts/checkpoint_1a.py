# Import GPIO library
import RPi.GPIO as GPIO

# Configure standard GPIO mode
# "BCM" refers to the Broadcom processor
GPIO.setmode(GPIO.BCM)

# A variable to store the pin number for the LED
LED0 = 24 

# Control the LED
GPIO.setup(LED0, GPIO.OUT)   # Set pin as output
GPIO.output(LED0, GPIO.HIGH) # Turn on the LED
GPIO.output(LED0, GPIO.LOW)  # Turn off the LED
