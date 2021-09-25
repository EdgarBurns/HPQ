# Import GPIO
import RPi.GPIO as GPIO

# Import sleep
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for Motor 1
Motor1A = 27
Motor1B = 24
Motor1Enable = 5

# Set up defined GPIO pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT) 

# Define GPIO pins for Motor 2
Motor2A = 6
Motor2B = 22
Motor2Enable = 17 

# Set up defined GPIO pins
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT) 

# Turn the motor 1 on forwards
GPIO.output(Motor1A,GPIO.HIGH) # GPIO high to send power to the + terminal
GPIO.output(Motor1B,GPIO.LOW) # GPIO low to ground the - terminal
GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

# Turn the motor 2 on forwards
GPIO.output(Motor2A,GPIO.HIGH) # GPIO high to send power to the + terminal
GPIO.output(Motor2B,GPIO.LOW) # GPIO low to ground the - terminal
GPIO.output(Motor2Enable,GPIO.HIGH) # GPIO high to enable this motor

# Leave the motor on for 3 seconds
sleep(3)

# Turn the motor 1 on backwards
GPIO.output(Motor1A,GPIO.LOW) # GPIO high to send power to the + terminal
GPIO.output(Motor1B,GPIO.HIGH) # GPIO low to ground the - terminal
GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

# Turn the motor 2 on backwards
GPIO.output(Motor2A,GPIO.LOW) # GPIO high to send power to the + terminal
GPIO.output(Motor2B,GPIO.HIGH) # GPIO low to ground the - terminal
GPIO.output(Motor2Enable,GPIO.HIGH) # GPIO high to enable this motor


# Leave the motor on for 3 seconds
sleep(3)

# Stop the motor by 'turning off' the enable GPIO pin
GPIO.output(Motor1Enable,GPIO.LOW)

# Always end this script by cleaning the GPIO
GPIO.cleanup()
