from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

server = BluetoothMailboxServer()
mbox = TextMailbox('drive_command', server)
ev3 = EV3Brick()

print('Waiting for connection...')
server.wait_for_connection()
print('Connected!')
ev3.speaker.set_volume(100)
ev3.speaker.beep()  # Bekreftelsestone når tilkoblet

def sleep_delay():
    time.sleep(0.1)

while True:
    if Button.UP in ev3.buttons.pressed():
        print("Sending FRAM")
        mbox.send('FRAM')
    elif Button.DOWN in ev3.buttons.pressed():
        print("Sending BAK")
        mbox.send('BAK')
    else:
        # Ingen knapper er trykket, send ingen kommando
        mbox.send('STOP')

    # Vent litt for å stabilisere meldingssendingen
    sleep_delay()
