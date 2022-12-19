# Før du kjører dette programmet, sørg for at klient- og server EV3-klossene er
# paret med Bluetooth, men IKKE koble dem til. Programmet vil ta vare
# for å etablere forbindelsen.

# Serveren må startes opp før klienten!

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

# Initialisere serveren
server = BluetoothMailboxServer()

# Sette meldingsboks som en string til variabelen mbox
mbox = TextMailbox('greeting', server)

# Initialisere
ev3 = EV3Brick()

# En funksjon for soving siden jeg kan endre tiden imellom hvert signal samlet inni her 
def sov():
    time.sleep(0.005)


print('Waiting for connection...')

# Venter på et signal
server.wait_for_connection()
print('Connected!')
# Når den har koblet seg til vil jo koden kjøre videre og dette vet vi med at roboten piper 
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Create a loop to react to buttons
while True:
    
    # Forklarer denne delen bare en gang, dette gjelder for mesteparten av koden
    
    # Hvis knappen opp er trykket
    if Button.UP in ev3.buttons.pressed():
        # Print Bak i terminalen 
        print("Bak")
        # Denne sove funksjonen er her for å forhindre en buffer overflow i koden
        # Roboten tåler ikke å bli sendt 500 meldinger i sekundet og den får for mye informasjon på 
        # en gang, og den bare slutter til slutt
        # Derfor har jeg denne her at den sender ut oppdateringer av status i intervaller
        sov()
        # Sende signalet 
        mbox.send('D = 1')
    else:
        # Hvis ikke det så må den sove litt og sende signalet D = 0
        sov()
        mbox.send('D = 0')
    
    # D er egentlig DRIVE men når den kjører bakover går motorene raskerer (jeg vet ikke hvorfor)
    # Derfor bare flippet jeg dette om som roboten kjører raskere frem
    
    # Det samme som den øvre delen bare motsatt
    if Button.DOWN in ev3.buttons.pressed():
        # Console output
        print("Fram")
        sov()
        mbox.send('F = 1')
    else:
        time.sleep(0.05)
        mbox.send('F = 0')
    
    # Sjekker om både knappen opp OG om knappet til høyre er trykket
    if Button.UP in ev3.buttons.pressed() and Button.RIGHT in ev3.buttons.pressed():
        # Se over for forklaring
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
