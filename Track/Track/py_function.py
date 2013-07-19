'''py_function.py - Python source designed to '''
'''demonstrate the use of python embedding'''
import socket
import time 

def multiply():
    TCP_IP = "192.168.2.50"
    TCP_PORT = 503
    BUFFER_SIZE = 20
    motor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    motor.connect((TCP_IP,TCP_PORT))
    motor.send("MR 1000000\r\n")
    time.sleep(2)
    motor.send("SL\r\n")



def test():
    TCP_IP = "192.168.2.50"
    TCP_PORT = 503
    BUFFER_SIZE = 20
    motor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    motor.connect((TCP_IP,TCP_PORT))
    time.sleep(3)
    motor.send("MR 2000000\r\n")
    time.sleep(3)
    motor.send("SL\r\n")
    time.sleep(5)
    motor.send("MR 1000000\r\n")
    time.sleep(3)
    
