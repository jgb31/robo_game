""" 
This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.

"""
from bluedot import BlueDot
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
from signal import pause
import numpy as np
 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor B, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 19		# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 21	# IN2 - Reverse Drive

# Motor A, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 13	# ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 5	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive
 
# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)
 
# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)
 
def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0
 
def forwardDrive():
	forwardLeft.value = 1.0
	reverseLeft.value = 0.0
	forwardRight.value = 1.0
	reverseRight.value = 0.0
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def spinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.1
	driveRight.value = 0.9
 
def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.9
	driveRight.value = 0.1
 
def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.5
	driveRight.value = 1.5
 
def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.5
	driveRight.value = 0.5
	
def dpad(pos):
    if pos.top:
        print("up")
        forwardDrive()
        sleep(0.25)
    elif pos.bottom:
        print("down")
        reverseDrive()
        sleep(0.25)
    elif pos.left:
        print("left")
        #spinLeft()
        forwardTurnLeft()
        sleep(0.25)
    elif pos.right:
        print("right")
        #SpinRight()
        forwardTurnRight()
        sleep(0.25)
    elif pos.middle:
        print("stop")
        allStop()

def main():
		
	#Bluetooth Initialization
    bd = BlueDot()

    while True:
        bd.when_pressed = dpad

    pause()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
