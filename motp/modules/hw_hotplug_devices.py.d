#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#

# What's this? doesnt work when testing, maybe also mandriva-special? if found what its for, add here
#
# notice its not in the actual codeblock nor in a definition
# <> seems to be a prerequisite for device_state which is for hdd temp?
rootdir_pattern = re.compile('^.*?/devices')
internal_devices = []

# this one looks up hotplug-busses and puts them in the list 
# I suspect this is another mandriva-specific one. Don't know if you'd really want/need that
# especially VMs don't need that since they neither have usb nor firewire nor anything else 
def device_state(name):
    #open hotplug-devicefiles and read
    with open('/sys/block/%s/device/block/%s/removable' % (name, name)) as f:
        # (probably) exit if none there
        if f.read(1) == '1':
            return

    #set path to... uhm... something something
    path = rootdir_pattern.sub('', os.readlink('/sys/block/%s' % name))
    # define valid buses to show (put in cfg)
    hotplug_buses = ("usb", "ieee1394", "mmc", "pcmcia", "firewire")
    #go through every type of bus...
    for bus in hotplug_buses:
        #...and if bus exists in OS..
        if os.path.exists('/sys/bus/%s' % bus):
            #...go through all devices with that bus
            for device_bus in os.listdir('/sys/bus/%s/devices' % bus):
                #save device-link
                device_link = rootdir_pattern.sub('', os.readlink('/sys/bus/%s/devices/%s' % (bus, device_bus)))
                #if there is something with search X, go out of function? 
                if re.search(device_link, path):
                    return
    #This appends only one device since it's not in for-loop?
    #<> whole function gets called for every device
    internal_devices.append(name)