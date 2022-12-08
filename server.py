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

# Initialize server
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started


# Initialize EV3 touch sensor and motors
middleButton = "Off"
leftButton = 'Off'
rightButton = 'Off'
backButton = 'Off'
forwarButton = 'Off'

# The server must be started before the client!
print('Waiting for connection...')
server.wait_for_connection()
print('Connected!')
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Create a loop to react to buttons
ev3.screen.print("Midten = ", middleButton)
while True:
    
    #print(middleButton)
    
    
    # Setter variabelen for knappen i midten
    if Button.CENTER in ev3.buttons.pressed():
        print("Midten er trykket")
        middleButton = 'On'
        ev3.screen.print("Midten = ", middleButton)
    else:
        middleButton = 'Off'
        ev3.screen.print("Midten = ", middleButton)
    
    if Button.LEFT in ev3.buttons.pressed():
        print("Venstre er trykket")
        leftButton = 'On'
        ev3.screen.print("Venstre = ", leftButton)
    else:
        leftButton = 'Off'
        ev3.screen.print("Venstre = ", leftButton)
        
    # Hvis knappen i midten er på
    if middleButton == "On":
        # Send meldingen at knappen er på
        mbox.send('MIDTEN')
    # Ellers hvis den ikke er på
    elif middleButton == "Off":
        # Send melding at den er av
        mbox.send('MIDTENAV')
        
    if Button.LEFT in ev3.buttons.pressed():
        mbox.send('EXIT')
        break

# Send message to client to stop
mbox.send('FERDIG')

# Use the speech tool to signify the program has finished
# ev3.speaker.say("Program complete")
