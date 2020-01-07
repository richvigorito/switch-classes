class Device: 
  
    def __init__(self, uid, name, room, commands):
        pass

    def initiateCommand(self,command,times=  0):
        pass

    def validateCommand(self,command):
        return command in self.commands
    
    def __str__(self):
        return self.room +": " + self.name + "(" + self.uid + ") -- " + self.protocol +  "protocol"


