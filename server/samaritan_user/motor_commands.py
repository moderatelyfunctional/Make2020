#!/usr/bin/env python

# TODO Raspberry Pi NoIp DUC: https://www.noip.com/support/knowledgebase/install-ip-duc-onto-raspberry-pi/


# Import required modules
import time
import RPi.GPIO as GPIO

# Look at this to connect the various parts
# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB
left_speed = GPIO.PWM(7, 50)
right_speed = GPIO.PWM(18, 50)
left_speed.start(0)
right_speed.start(0)

def move_both(left, right):
    """
    Accepts (left, right) values between -1.0 and 1.0

    if `left` is less than 0, then it goes into the backwards configuration,
    otherwise it goes into the forward regime. Same logic for `right`.

    sets the pwm value for each of them to the correct value.

    """

    if left < 0:
        # Motor A:
        GPIO.output(12, GPIO.HIGH) # Set AIN1
        GPIO.output(11, GPIO.LOW) # Set AIN2
    else:
        # Motor A:
        GPIO.output(12, GPIO.LOW) # Set AIN1
        GPIO.output(11, GPIO.HIGH) # Set AIN2

    if right < 0:
        # Motor B:
        GPIO.output(15, GPIO.HIGH) # Set BIN1
        GPIO.output(16, GPIO.LOW) # Set BIN2
    else:
        # Motor B:
        GPIO.output(15, GPIO.LOW) # Set BIN1
        GPIO.output(16, GPIO.HIGH) # Set BIN2

    # Set the motor speeds
    # Motor A:
    left_speed.ChangeDutyCycle(abs(left))
    # GPIO.output(7, GPIO.HIGH) # Set PWMA
    # Motor B:
    right_speed.ChangeDutyCycle(abs(right))
    # GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

def setup():
    # Look at this to connect the various parts
    # Declare the GPIO settings
    GPIO.setmode(GPIO.BOARD)

    # set up GPIO pins
    GPIO.setup(7, GPIO.OUT) # Connected to PWMA
    GPIO.setup(11, GPIO.OUT) # Connected to AIN2
    GPIO.setup(12, GPIO.OUT) # Connected to AIN1
    GPIO.setup(13, GPIO.OUT) # Connected to STBY
    GPIO.setup(15, GPIO.OUT) # Connected to BIN1
    GPIO.setup(16, GPIO.OUT) # Connected to BIN2
    GPIO.setup(18, GPIO.OUT) # Connected to PWMB
    left_speed = GPIO.PWM(7, 50)
    right_speed = GPIO.PWM(18, 50)
    left_speed.start(0)
    right_speed.start(0)

def clockwise():
    # Drive the motor clockwise
    # Motor A:
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.HIGH) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(7, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

def counterclockwise():
    # Drive the motor counterclockwise
    # Motor A:
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.HIGH) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.HIGH) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(7, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

def forward(): # TODO: Make sure correct
    # Drive the motor counterclockwise
    # Motor A:
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.HIGH) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(7, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

def backwards(): # TODO: Make sure correct
    # Drive the motor counterclockwise
    # Motor A:
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.HIGH) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.HIGH) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(7, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)


def stop():
    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    # GPIO.output(7, GPIO.LOW) # Set PWMA
    left_speed.ChangeDutyCycle(0)
    GPIO.output(13, GPIO.LOW) # Set STBY
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2
    # GPIO.output(18, GPIO.LOW) # Set PWMB
    right_speed.ChangeDutyCycle(0)


# Test script:

# Move backwards
move_both(-50.0, -50.0)
time.sleep(2)

# Move forwards
move_both(50.0, 50.0)
time.sleep(2)

# Move left
move_both(-50.0, 50.0)
time.sleep(2)

# Move right
move_both(50.0, -50.0)
time.sleep(2)

# Stop
move_both(0.0, 0.0)

# # Move backwards
# move_both(-1.0, -1.0)
# time.sleep(2)
#
# # Move forwards
# move_both(1.0, 1.0)
# time.sleep(2)
#
# # Move left
# move_both(-1.0, 1.0)
# time.sleep(2)
#
# # Move right
# move_both(1.0, -1.0)
# time.sleep(2)
#
# # Stop
# move_both(0.0, 0.0)
