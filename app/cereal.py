import serial

class Cereal(serial.Serial):
    def __init__(self, name, device, baud=19200, time=5):
        self.name = name
        self.device = device
        self.baud = baud
        self.time = time

        super(Cereal, self).__init__(port=self.device, baudrate=self.baud, timeout=self.time, writeTimeout=self.time)
 
    def cRead():
        '''
        Read current data from RFID sensor and return list of tags.
        '''
        tagList = self.readlines()
        return(tagList)

    def cConfig():
        pass
    
'''
Special class of serial
'''
