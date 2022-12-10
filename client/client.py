#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait

# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

newMessage = ""
middleButton = "Off"
leftButton = 'Off'
rightButton = 'Off'
backButton = 'Off'
forwardButton = 'Off'

# Motor
motorA = Motor(Port.A)
motorB = Motor(Port.B)

def stopmotor():
    motorA.stop()
    motorB.stop()

# Initialize the EV3 Brick
ev3 = EV3Brick()


# Initialize EV3 touch sensor and motors
#motor = Motor(Port.A)

print('Establishing connection...')
client.connect(SERVER)
print('Connected!')


# Initialize a loop taht waits for instructions from the server
while True:
    mbox.wait()
    newMessage = mbox.read()
    

    # Fram
    if newMessage == "D = 1":
        motorA.dc(1000)
        motorB.dc(1000)
    if newMessage == "D = 0":
        stopmotor()

    # Bakover
    if newMessage == "F = 1":
        motorA.dc(-1000)
        motorB.dc(-1000)
    if newMessage == "F = 0":
        stopmotor()

    # Fram Høyre
    if newMessage == "FH = 1":
        motorA.dc(1000)
        motorB.dc(250)
    if newMessage == "FH = 0":
        stopmotor()
    
    # Fram Venstre
    if newMessage == "FV = 1":
        motorA.dc(250)
        motorB.dc(1000)
    if newMessage == "FV = 0":
        stopmotor()

    
    # Høyre
    if newMessage == "H = 1":
        motorA.dc(1000)
        motorB.dc(0)
    if newMessage == "H = 0":
        stopmotor()
    
    # Venstre
    if newMessage == "L = 1":
        motorA.dc(0)
        motorB.dc(1000)
    if newMessage == "L = 0":
        stopmotor()
    
    
    


    # KRIG

    if newMessage == "M = 1":
        print("KRIG!")





    
    


  

"""
# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
"""
