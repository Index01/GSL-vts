import siteTransact
from toolbox import makeConn, getPorts, createDict, autoDiscover

def runOnce():
    sessionObj = siteTransact.Connection('home', 'http://localhost:5000/Z2F0ZUF1dG9tYXRlZENoZWNraW4=')
    return(sessionObj)
    
def main():
    runOnce()
    activeConnections = []
    connObjList = []
    while True:
        autoDiscover(activeConnections, connObjList)



if __name__ == "__main__":
    main()
