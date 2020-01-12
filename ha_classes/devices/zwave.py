from .device import * 

class ZWave(Device): 

    def __init__(self, uid, name, room, commands):
        self.uid = uid
        self.name = name
        self.room = room
        self.commands = commands
        self.protocol = 'x10'

    def initiateCommand(self,command, times=  0):
        if self.validateCommand(command):
            return 1
        return 0
