import numpy as np
import pygame, time, math
import pylab as pl

# Some constants
outputRate = 44100
maxAmplitude = np.iinfo( np.int16 ).max

# Create an array containing a sine wave
def SineWave( pitch, volume, duration ):

    global outputRate, maxAmplitude

    # Create the output buffer
    totalSamples = int( outputRate * duration )
    outputBuffer = np.zeros( ( totalSamples, 2 ), dtype=np.int16 )

    # Calculate amplitude
    amplitude = int( maxAmplitude * volume )

    # Calculate change in the wave for each output sample
    waveStep = float( pitch / outputRate ) * 2.0 * math.pi

    # Fill buffer
    for i in range( totalSamples ):

        # Left channel
        outputBuffer[i][0] = amplitude * np.sin( i * waveStep )

        # Right channel
        outputBuffer[i][1] = amplitude * np.sin( i * waveStep )

    return outputBuffer

# Set up the audio output - only once!
# 2-channel (stereo), 16-bit signed integer value output at 44khz
pygame.mixer.init( frequency=outputRate, channels=2, size=-16)

# ...
# Create a note (C5)
sin523 = SineWave( 523, 1.0, 1.0 )

# Make a plot of the wave if you like
pl.plot( sin523[0:100] ) # Just the first 100 values for clarity
pl.show()

# Play sound
noteC5 = pygame.mixer.Sound( buffer=sin523 )
noteC5.play()

# Keep the program active until the note is complete
time.sleep(2)

