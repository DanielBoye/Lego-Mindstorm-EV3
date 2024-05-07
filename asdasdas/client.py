#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.parameters import Port
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
import time

print('''
 __    __  __    __   ______  
|  \  |  \|  \  |  \ /      \ 
| $$  | $$| $$  | $$|  $$$$$$\
| $$__| $$| $$  | $$| $$___\$$
| $$    $$| $$  | $$ \$$    \ 
| $$$$$$$$| $$  | $$ _\$$$$$$\
| $$  | $$| $$__/ $$|  \__| $$
| $$  | $$ \$$    $$ \$$    $$
 \$$   \$$  \$$$$$$   \$$$$$$ 
''')

SERVER = 'server'

client = BluetoothMailboxClient()

ev3 = EV3Brick()
print('Establishing connection...')
client.connect(SERVER)
print('Connected!')
ev3.speaker.set_volume(100)
ev3.speaker.beep()

motion_box = TextMailbox('motion_command', client)
lift_box = TextMailbox('lift_command', client)

def sleep_delay():
    time.sleep(0.05)

motorA = Motor(Port.A)
motorB = Motor(Port.B)
motorC = Motor(Port.C)

def stop_motors():
    motorA.stop()
    motorB.stop()
    motorC.stop()

while True:
    # Sjekker om det er nye meldinger uten å vente
    motion_message = motion_box.read()
    print("m: ",motion_message)
    if motion_message == 'FRAM':
        motorA.dc(100)
        motorB.dc(100)
    elif motion_message == 'BAK':
        motorA.dc(-100)
        motorB.dc(-100)
    else:
        motorA.stop()
        motorB.stop()

    lift_message = lift_box.read()
    print("lift: ",lift_message)
    if lift_message == 'OPP':
        motorC.dc(100)
    elif lift_message == 'NED':
        motorC.dc(-100)
    else:
        motorC.stop()

    sleep_delay()