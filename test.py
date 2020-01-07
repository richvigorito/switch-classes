from house import *
from devices.device  import  *
from devices.x10  import  *
from devices.zwave  import  *

h = House('radpad')
d = X10('a1','front-porch','living room',['on','off'])
h.addDevice(d)
d = X10('a2','living room ceiling light','living room',['on','off','dim','bright'])
h.addDevice(d)
d = ZWave('a3','table lamp','living room',['on','off'])
h.addDevice(d)

print(h.devices)

for key in h.devices: 
    print(h.devices[key]) 
    print(h.devices[key].initiateCommand('on'))
    print(h.devices[key].initiateCommand('off'))
    print(h.devices[key].initiateCommand('bright'))
    print(h.devices[key].initiateCommand('dim'))



