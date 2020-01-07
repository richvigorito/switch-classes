from house import *
from devices.device import  *
from devices.x10 import  *
from devices.zwave import *

h = House('radpad')
d = X10('a1','front-porch','living room',['on','off'])
h.addDevice(d)
d = X10('a2','living room ceiling light','living room',['on','off','dim','bright'])
h.addDevice(d)
d = ZWave('a3','table lamp','living room',['on','off'])
h.addDevice(d)

print(h.devices)

for dd in h.devices: 
    print(dd) 
    print(dd.initiateCommand('on'))
    print(dd.initiateCommand('off'))
    print(dd.initiateCommand('bright'))
    print(dd.initiateCommand('dim'))



