#from device import  *
#from ha_classes.x10 import  *
#from ha_classes.zwave import  *

class House: 
  
    devices = None
    
    def __init__(self, name):
        self.name = name
        self.devices = {}

    def addDevice(self, device):
        self.devices[device.uid] = device

