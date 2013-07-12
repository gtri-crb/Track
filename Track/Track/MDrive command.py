#Pranav Shenoy
#July 12, 2013


#motor connection things
#initialization 
def connectToMotor():
    TCP_IP = "192.168.2.50"
    TCP_PORT = 503
    BUFFER_SIZE = 20
    motor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    motor.connect((TCP_IP,TCP_PORT))


#motor functions
#variables
acceleration = 1000000
deceleration = 1000000
microstepResolution = 0
position = 0
initialVelocity = 1000
maximumVelocity = 68000


#mutators
def changeAcceleration ():
    motor.send ("A %d \r\n") % self.acceleration

def changeDeceleration ():
    motor.send ("D %d \r\n") % self.deceleration

def changeDecelerationToAcceleration ():
    motor.send ("D=A\r\n")

def changeInitialVelocity():
    motor.send ("VI %d \r\n") % self.initialVelocity

def changeMaximumVelocity():
    motor.send ("VM=%d \r\n") % self.maximumVelocity

def resetPositionCounter():        
    motor.send ("P=0\r\n")


#Accessors
def getAcceleration ():
    motor.send ("PR A\r\n")

def getPosition ():
    motor.send ("PR P")

def getVelocity ():
    motor.send ("PR V")

def getAccelerationAndDeceleration ():
    motor.send ("A=%d\r\nD=%d") % self.acceleration, self.deceleration

#Movement
def moveAmount(number): 
    motor.send("MR %d\r\n") % number

def moveConstantSpeed(number):
    motor.send ("SL %d\r\n") % number

def movingTest ():
    motor.send("MR 1000000\r\n")

def stop():
    motor.send ("SL\r\n")

