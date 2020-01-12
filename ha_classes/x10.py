from ha_classes.device import * 

class X10(Device): 

    def __init__(self, uid, name, room, commands):
        self.uid = uid
        self.name = name
        self.room = room
        self.commands = commands
        self.protocol = 'zwave'

    def initiateCommand(self,command, times= 0):
        if self.validateCommand(command):
            return 1
        return 0
