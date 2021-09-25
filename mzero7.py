
import RPi.GPIO as GPIO
import socket
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for Motor 1
Motor1A = 27
Motor1B = 24
Motor1Enable = 5

# Define GPIO pins for Motor 2
Motor2A = 6
Motor2B = 22
Motor2Enable = 17 

def initialise():

	print "Initialising"

	# Set up defined GPIO pins
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1Enable,GPIO.OUT, initial=GPIO.LOW) 
	
	# Set up defined GPIO pins
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2Enable,GPIO.OUT, initial=GPIO.LOW) 

def motor1forward():

	# Turn the motor 1 on forwards
	GPIO.output(Motor1A,GPIO.HIGH) # GPIO high to send power to the + terminal
	GPIO.output(Motor1B,GPIO.LOW) # GPIO low to ground the - terminal
	GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

def motor1backward():

	# Turn the motor 1 on backwards
	GPIO.output(Motor1A,GPIO.LOW) # GPIO high to send power to the + terminal
	GPIO.output(Motor1B,GPIO.HIGH) # GPIO low to ground the - terminal
	GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

def motor1stop():

	GPIO.output(Motor1Enable,GPIO.LOW) # GPIO low to disable this motor

def motor2forward():

	# Turn the motor 2 on forwards
	GPIO.output(Motor2A,GPIO.HIGH) # GPIO high to send power to the + terminal
	GPIO.output(Motor2B,GPIO.LOW) # GPIO low to ground the - terminal
	GPIO.output(Motor2Enable,GPIO.HIGH) # GPIO high to enable this motor

def motor2backward():

	# Turn the motor 2 on backwards
	GPIO.output(Motor2A,GPIO.LOW) # GPIO high to send power to the + terminal
	GPIO.output(Motor2B,GPIO.HIGH) # GPIO low to ground the - terminal
	GPIO.output(Motor2Enable,GPIO.HIGH) # GPIO high to enable this motor

def motor2stop():

	GPIO.output(Motor2Enable,GPIO.LOW) # GPIO low to disable this motor

UDP_IP = "192.168.0.72"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

initialise()

while True :

	data, addr = sock.recvfrom(1024)
	raw=data

	if raw == "forward":
		print "forward"
		motor1forward()
		motor2forward()

	if raw == "backward":
		print "backward"
		motor1backward()
		motor2backward()

	if raw == "left":
		print "left"
		motor1forward()
		motor2backward()

	if raw == "right":
		print "right"
		motor1backward()
		motor2forward()

	if raw == "stop":
		print "stop"
		motor1stop()
		motor2stop()

	if raw == "Action 1":
		print "Exit"
		break

# Stop the motor by 'turning off' the enable GPIO pin
motor1stop()
motor2stop()

# Always end this script by cleaning the GPIO
GPIO.cleanup()
