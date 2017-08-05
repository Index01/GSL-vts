from toolbox import makeConn, getPorts, createDict, autoDiscover

def main():
    activeConnections = []
    connObjList = []
    while True:
        autoDiscover(activeConnections, connObjList)



if __name__ == "__main__":
    main()
