from toolbox import makeConn, getPorts, createDict, autoDiscover

def runOnce():
    activeConnections = []
    connObjList = []
    sessionObj = siteTransact.Connection('home', 'localhost:5050')
    
def main():
    runOnce()
    while True:
        autoDiscover(activeConnections, connObjList)



if __name__ == "__main__":
    main()
