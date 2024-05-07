#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Button
from pybricks.ev3devices import Motor
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

print(''' 
 __    __  _______    ______   __    __       
|  \  /  \|       \  /      \ |  \  |  \      
| $$ /  $$| $$$$$$$\|  $$$$$$\| $$\ | $$      
| $$/  $$ | $$__| $$| $$__| $$| $$$\| $$      
| $$  $$  | $$    $$| $$    $$| $$$$\ $$      
| $$$$$\  | $$$$$$$\| $$$$$$$$| $$\$$ $$      
| $$ \$$\ | $$  | $$| $$  | $$| $$ \$$$$      
| $$  \$$\| $$  | $$| $$  | $$| $$  \$$$      
 \$$   \$$ \$$   \$$ \$$   \$$ \$$   \$$      
''')


server = BluetoothMailboxServer()
mbox = TextMailbox('motion_command', server)
liftbox = TextMailbox('lift_command', server)
clawbox = TextMailbox('claw_command', server)

ev3 = EV3Brick()

print('[+] Waiting for connection...')
server.wait_for_connection(2)
# server.wait_for_connection()
print('[+] Connected!')
ev3.speaker.set_volume(1000)
ev3.speaker.beep()


driving = Motor(Port.A)
oppned = Motor(Port.B)

def sleep_delay():
    time.sleep(0.025)

driving.reset_angle(0)
oppned.reset_angle(0)

klype = False
print(klype)

while True:
    driving_angle = driving.angle()
    oppned_angle = oppned.angle()   
 
    if Button.CENTER in ev3.buttons.pressed():
        klype = not klype
        clawbox.send(klype)  
        # print(klype)      
        wait(250)
    # else:
    #     clawbox.send('STOP')

    if driving_angle >= 45:
        mbox.send('FRAM')
    elif driving_angle <= -45:
        mbox.send('BAK')
    else:
        mbox.send('STOP')
        
    if oppned_angle >= 45:
        liftbox.send('OPP')
    elif oppned_angle <= -45:
        liftbox.send('NED')
    else:
        liftbox.send('STOP')

    # print("{:<15} {:<15} {:<10}".format(driving_angle, oppned_angle, klype))

    sleep_delay()
