import serial

class ObjectsDetected(object):

    def __init__(self, port):
        self.port = port
        #########################self.data = serial.Serial('/dev/tty.usbmodm1d11', self.port)
        self.counter = 32
        self.objects = []
        self.itsangles = []
        self.all = [self.objects, self.itsangles]

    def decodeJsonToOther(self):
        self.counter += 1
        if self.counter == 255:
            self.counter = 32

    def returnList(self):
        return self.all
