from house.house import *
from devices.device  import  *
from devices.x10  import  *
from devices.zwave  import  *
import json


def buildFromFile(conf):
    with open(conf) as json_data_file:
        data = json.load(json_data_file)

    myHouse = House(data['houseName'])

    for device in data['devices']:
        if 'active' != device['status']: 
            continue

        if 'x10' == device['protocol']: 
            d = X10(device['uid'],device['name'],device['room'],device['commands'])
        elif 'zwave' == device['protocol']: 
            d = ZWave(device['uid'],device['name'],device['room'],device['commands'])
        myHouse.addDevice(d)
    return myHouse


if __name__ == "__main__":
    myHouse = buildFromFile('../conf/conf.json')
    for key in myHouse.devices: 
        print(myHouse.devices[key]) 
        print(myHouse.devices[key].initiateCommand('on'))
        print(myHouse.devices[key].initiateCommand('off'))
        print(myHouse.devices[key].initiateCommand('bright'))
        print(myHouse.devices[key].initiateCommand('dim'))

    print(myHouse.devices['a1'].name)


