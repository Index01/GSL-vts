import cereal
from serial import SerialException
from serial.tools import list_ports
from datetime import datetime

def createDict(aList, *args):
    '''
     Accepts a list and adds each item as a key to a dictionary with
     a current UTC timestamp as its value
    '''
    newDict = {}
    for i in aList:
        tStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow())
        newDict[i] = tStamp
    return(newDict)

def getPorts():
    '''
    Returns a list of activated USB ports detected by the os
    '''
    portList = []
    for i in list_ports.comports():
        portList.append(i.name)
    return(portList)

def makeConn(device, activeConnections=[], connObjList=[]):
    '''
    Takes device name, and two working lists as input, creates a serial
    connection to the device and returns updated tracking list
    as well as updated list of serial objects
    '''
    try:
        port = "/dev/"+device
        newConn = cereal.Cereal(device, port)
        activeConnections.append(device)
        connObjList.append(newConn)
        print(activeConnections)
        print(connObjList)
#        print(port, "connected as", device)
        return(activeConnections,connObjList)

    except SerialException, e:
        print("getPorts output: " + ','.join(getPorts()))
        print("attempted connection failed for some reason: "+ device)

def autoDiscover(activeConnections, connObjList):
    try:
        # checks if tracking list is larger than list reported by getPorts
        if len(activeConnections) > len(getPorts()):
            # remove corresponding entries from both lists
            for i in list(set(activeConnections)-set(getPorts())):
                activeConnections.remove(i)
                for entry in connObjList:
                    if entry.name == "/dev/"+i:
                        connObjList.remove(entry)
            print(activeConnections)
            print(connObjList)
        # checks if getPorts list is larger than tracking list
        elif len(getPorts()) > len(activeConnections):
            # if so, call makeConn function to create new connection and update lists
            for device in list(set(getPorts())-set(activeConnections)):
                makeConn(device, activeConnections, connObjList)
        else:
            pass
    except SerialException, e:
        print("something")

