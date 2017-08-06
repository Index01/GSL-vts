import json
import cereal
from serial import SerialException
from serial.tools import list_ports
from datetime import datetime

def createDict(RFID_number, tStamp = 0):
    '''
     Accepts a string and creates a dictionary:
     {'tagID': <string>, 'utc': <timestamp>}
    '''
    newDict = {}
    if tStamp == 0:
        tStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow())
    newDict['tagID'] = RFID_number
    newDict['utc'] = tStamp
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
        print("Error")

def dataPull(connObjList):
    tempList = []
    for connObj in connObjList:
        try:
            for item in connObj.cRead():
                tempList.append(item)
        except:
            pass
    for tItem in set(tempList):
        dictList.append(createDict(tItem))
    try:
        y = open('./fail.txt', 'r')
        x = y.read()
        if x != '':
            x = x[:-1]
            for i in x.split('\n'):
                dictList.append(createDict(i.split(',')[0], i.split(',')[1]))
        y.close()
    except IOError e:
        pass
    return(dictList)

def dataPost(dictList):
    if len(dictList) > 0:
        jsonData = json.loads(json.dumps(dictList))
        response = sessionObj.send_post(jsonData)
        verifyResponse(response, dictList)
    else:
        pass

def verifyResponse(response, dictList):
    if response.status_code == 200:
        tmpFile = open('./fail.txt', 'w')
        tmpFile.close()
    else:
        tmpFile = open('./fail.txt', 'w')
        for dictItem in dictList:
            tmpFile.write(dictItem['tagID']+","+dictItem['utc']+"\n")

