#import serial
#from cereal import *
from toolbox import makeConn, getPorts, createDict, autoDiscover
#from serial import SerialException
#from serial.tools import list_ports
#from datetime import datetime

def main():
    activeConnections = []
    connObjList = []
    while True:
        autoDiscover(activeConnections, connObjList)



if __name__ == "__main__":
    main()
