from devices.device  import  *
from devices.x10  import  *
from devices.zwave  import  *

class House: 
  
    devices = None
    
    def __init__(self, name):
        self.name = name
        self.devices = {}

    def addDevice(self, device):
        self.devices[device.uid] = device

