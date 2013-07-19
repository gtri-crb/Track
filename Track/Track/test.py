import socket
import time
def tester:
    TCP_IP = "192.168.2.50"
    TCP_PORT = 503
    BUFFER_SIZE = 20
    motor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    motor.connect((TCP_IP,TCP_PORT))
    motor.send("MR 1000000\r\n")
    time.sleep(2)
    return 0
    
