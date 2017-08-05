import cereal
from serial import SerialException
from serial.tools import list_ports
from datetime import datetime

# Accepts a list and adds each item as a key to a dictionary with
# a current UTC timestamp as its value


def createDict(aList, *args):
    newDict = {}
    for i in aList:
        tStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow())
        newDict[i] = tStamp
    return(newDict)

def getPorts():
    portList = []
    for i in list_ports.comports():
        portList.append(i.name)
    return(portList)

def makeConn(device, activeConnections=[], connObjList=[]):
    try:
        port = "/dev/"+device
        print("connecting to " + port)
        newConn = cereal.Cereal(device, port)
        print("ok")
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
        if len(activeConnections) > len(getPorts()):
            for i in list(set(activeConnections)-set(getPorts())):
                activeConnections.remove(i)
                for entry in connObjList:
                    if entry.name == "/dev/"+i:
                        connObjList.remove(entry)
            print(activeConnections)
            print(connObjList)
        elif len(getPorts()) > len(activeConnections):
            for device in list(set(getPorts())-set(activeConnections)):
                makeConn(device, activeConnections, connObjList)
        else:
            pass
    except SerialException, e:
        print("something")

