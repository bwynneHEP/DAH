def reading():
 
    # remember to change the GPIO values below to match your sensors
    # GPIO output = the pin that's connected to "Trig" on the sensor
    # GPIO input = the pin that's connected to "Echo" on the sensor 
    TRIG = 17
    ECHO = 27
    
    import time
    import RPi.GPIO as GPIO
    
    # Disable any warning message such as GPIO pins in use
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Setup the GPIO pins for TRIG and ECHO, including defining
    # if these are input or output pins

    # Insert your code here

    time.sleep(0.3)
    
    # sensor manual says a pulse length of 10Us will trigger the 
    # sensor to transmit 8 cycles of ultrasonic burst at 40kHz and 
    # wait for the reflected ultrasonic burst to be received
    
    # to get a pulse length of 10Us we need to start the pulse, then
    # wait for 10 microseconds, then stop the pulse. This will 
    # result in the pulse length being 10Us.
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # listen to the input pin. 0 means nothing is happening. Once a
    # signal is received the value will be 1 so the while loop
    # stops and has the last recorded time the signal was 0
    while GPIO.input(ECHO) == 0:
      signaloff = time.time()
    
    # listen to the input pin. Once a signal is received, record the
    # time the signal came through
    while GPIO.input(ECHO) == 1:
      signalon = time.time()
    
    # work out the difference in the two recorded times above to 
    # calculate the distance of an object in front of the sensor
    timepassed = signalon - signaloff
    
    # we now have our distance but it's not in a useful unit of
    # measurement. So now we convert this distance into centimetres
    # Define relation between "distance" and "timepassed"

    # Insert your code here
    
    # return the distance of an object in front of the sensor in cm
    return distance
    
    # we're no longer using the GPIO, so tell software we're done
    GPIO.cleanup()
       
print( reading() )
 

