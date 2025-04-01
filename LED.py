# Using a ‘library’ to tell it how to work with the Raspberry Pi’s GPIO pins
import RPi.GPIO as GPIO

# We can pause the script later on
import time

# Tell the program which naming convention is to be used
GPIO.setmode(GPIO.BCM)

# Close the warning
GPIO.setwarnings(False)

# Set the pin 18 to output
GPIO.setup(18,GPIO.OUT)

# Print "LED on" to the terminal
print "LED on"

# Turn the pin on
GPIO.output(18,GPIO.HIGH)

# Pause for 1 second
time.sleep(1)

# Print "LED off" to the terminal
print "LED off"

# Turn the pin off so it is no longer supplying any power
GPIO.output(18,GPIO.LOW)
