# Server koden må kjøres før klienten!

# Noe kode blir gulet ut her men det er siden jeg har lagt sammen de to main.py
# filene i samme mappe. Det er bare for å gjøre det lettere å se og jobbe på
# de to filene samtidig.

# Importerer bibliotekene for prosjektet
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait

# Dette er navnet til den fjernkontrolerte EV3 som vi kobler oss til med
SERVER = 'ev3dev'

# Konfigurerer denne klienten til Bluetooth
client = BluetoothMailboxClient()

# Meldingsboksen blir konfigurert som en tekst boks. Denne vil gi mer mening senere
mbox = TextMailbox('greeting', client)

# Ny melding er alltid tom 
newMessage = ""

# Starter med alt sammen av som ikke roboten bare kjører vekk med en gang
middleButton = "Off"
leftButton = 'Off'
rightButton = 'Off'
backButton = 'Off'
forwardButton = 'Off'

# Konfigurerer motor på port A til en bestemt variabel
motorA = Motor(Port.A)
# Det samme med motor B
motorB = Motor(Port.B)

motorC = Motor(Port.C)
motorD = Motor(Port.D)

# Funksjon for å stoppe alle motorene. 
# Dette er for å istedenfor å kalle på alle motorene hver gang, kan jeg bare tilkalle
# denne funksjonen 

def stopmotor():
    motorA.stop()
    motorB.stop()
   

# Initialisere EV3 klossen
ev3 = EV3Brick()

# Når den har kommet så langt, printer den ut dette i terminalen 
print('Establishing connection...')

# Så prøver den å koble til serveren som er lagret i variabelen SERVER
client.connect(SERVER)

# Hvis den klarer å koble seg til printer den ut "Connected" i terminalen 
# Hvis den ikke klarer å koble seg til, exiter koden uansett.
print('Connected!')


# Lager en evig loop som venter på instrukser fra serveren
while True:
    
    # Venter på ny melding
    mbox.wait()
    
    # Leser av meldingen og lagrer denne i en liten periode som newMessage
    newMessage = mbox.read()
    

    # Hvis meldingen er drive = 1 
    if newMessage == "D = 1":
        # Start en bevegelse 100% med begge motorene
        motorA.dc(100)
        motorB.dc(100)
    
    # Hvis meldingen er drive = 0 (altså ikke sant)
    if newMessage == "D = 0":
        # Stop motoren
        stopmotor()
        

    # Dette gjelder for alle mulige inputs bare med at et annet input gir en annen 
    # effekt på motorene om de kjører 100% eller 50% frem eller -100% (bakover)
    if newMessage == "F = 1":
        motorA.dc(-100)
        motorB.dc(-100)
       
    if newMessage == "F = 0":
        stopmotor()

    # Denne er kul siden noen ganger vil du kjøre frem og litt til høyre
    if newMessage == "FH = 1":
        # Derfor er motor A på 100% og B på 100%
        motorA.dc(100)
        motorB.dc(75)
      
    if newMessage == "FH = 0":
        stopmotor()
    
    if newMessage == "FV = 1":
        motorA.dc(75)
        motorB.dc(100)
       
    if newMessage == "FV = 0":
        stopmotor()

    if newMessage == "H = 1":
        motorA.dc(100)
        motorB.dc(-100)
      
    if newMessage == "H = 0":
        stopmotor()
    
    if newMessage == "L = 1":
        motorA.dc(-100)
        motorB.dc(100)
   
    if newMessage == "L = 0":
        stopmotor()
        
    if newMessage == "M = 1":
        print("KRIG!")
        motorC.dc(100)
        motorD.dc(100)
    
    if newMessage == "M = 0":
        stopmotor()

print("Programmet er ferdig") 