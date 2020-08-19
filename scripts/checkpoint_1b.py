import time

# Loop for ever
while True:

    value = not GPIO.input(LED0) # Store inverted LED value
    GPIO.output(LED0, value)     # Use inverted value
    time.sleep(2)                # Wait 2 seconds
