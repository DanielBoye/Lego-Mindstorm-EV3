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
 __    __  __                               
|  \  /  \|  \                              
| $$ /  $$| $$ __    __   ______    ______  
| $$/  $$ | $$|  \  |  \ /      \  /      \ 
| $$  $$  | $$| $$  | $$|  $$$$$$\|  $$$$$$\
| $$$$$\  | $$| $$  | $$| $$  | $$| $$    $$
| $$ \$$\ | $$| $$__/ $$| $$__/ $$| $$$$$$$$
| $$  \$$\| $$ \$$    $$| $$    $$ \$$     \
 \$$   \$$ \$$ _\$$$$$$$| $$$$$$$   \$$$$$$$
              |  \__| $$| $$                
               \$$    $$| $$                
                \$$$$$$  \$$                
''')

SERVER = 'server'

client = BluetoothMailboxClient()

ev3 = EV3Brick()
print('Establishing connection...')
client.connect(SERVER)
print('Connected!')
ev3.speaker.set_volume(100)
ev3.speaker.beep()

claw_box = TextMailbox('claw_command', client)

def sleep_delay():
    time.sleep(0.05)

motorA = Motor(Port.A)


def stop_motors():
    motorA.stop()

while True:
    claw_message = claw_box.read()
    print("claw: ", claw_message)
    if claw_message == 'True':
        start_time = time.time()
        end_time = start_time + 1
        count = 0
        while time.time() < end_time:
            motorA.dc(-100)
        # motorA.stop()
    elif claw_message == 'False': 
        start_time = time.time()
        end_time = start_time + 1
        count = 0
        while time.time() < end_time:
            motorA.dc(100)
        # motorA.stop()
    
    # else:
    #     motorA.stop()

    # sleep_delay()