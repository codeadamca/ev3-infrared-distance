#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, InfraredSensor)
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Initialize EV3 touch sensor and motors
motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
infrared = InfraredSensor(Port.S1)

# Create a loop to react to distance
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        motorLeft.stop()
        motorRight.stop()
        break

    # React to the distance
    if infrared.distance() < 30:
        motorLeft.stop()
        motorRight.stop()

    else:
        motorLeft.dc(50)
        motorRight.dc(50)

    # Uncomment to display the current status of the remote buttons
    # print("Distance: ", infrared.distance())

    wait(10)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
