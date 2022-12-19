#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

# Initialize server
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started


# Initialize EV3 touch sensor and motors

def sov():
    time.sleep(0.005)

# The server must be started before the client!
print('Waiting for connection...')
server.wait_for_connection()
print('Connected!')
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Create a loop to react to buttons
while True:
   
    
    # FERDIG

    if Button.UP in ev3.buttons.pressed():
        # Console output
        print("Bak")
        sov()
        mbox.send('D = 1')
    else:
        sov()
        mbox.send('D = 0')
    
    if Button.DOWN in ev3.buttons.pressed():
        # Console output
        print("Fram")
        sov()
        mbox.send('F = 1')
    else:
        time.sleep(0.05)
        mbox.send('F = 0')
    
    if Button.UP in ev3.buttons.pressed() and Button.RIGHT in ev3.buttons.pressed():
        # Console output
        print("Fram Høyre")
        sov()
        mbox.send('FH = 1')
    else:
        sov()
        mbox.send('FH = 0')
    
    if Button.UP in ev3.buttons.pressed() and Button.LEFT in ev3.buttons.pressed():
        # Console output
        print("Fram VENSTRE")
        sov()
        mbox.send('FV = 1')
    else:
        sov()
        mbox.send('FV = 0')

    if Button.RIGHT in ev3.buttons.pressed():
        # Console output
        print("Høyre")
        sov()
        mbox.send('H = 1')
    else:
        sov()
        mbox.send('H = 0')
    
    if Button.LEFT in ev3.buttons.pressed():
        # Console output
        print("Venstre")
        sov()
        mbox.send('L = 1')
    else:
        sov()
        mbox.send('L = 0')
    
    






    if Button.CENTER in ev3.buttons.pressed():
        # Console output
        print("Midten")
        sov()
        mbox.send('M = 1')
    else:
        sov()
        mbox.send('M = 0')

    


# Send message to client to stop
mbox.send('FERDIG')

# Use the speech tool to signify the program has finished
# ev3.speaker.say("Program complete")

# Write your program here.
ev3.speaker.beep()
