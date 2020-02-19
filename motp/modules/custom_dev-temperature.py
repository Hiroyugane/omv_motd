#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

def show_hdd_temp():
    # find hard drives?
    for path in glob('/sys/block/*/device'):
        # seems to search for find mass storage-names?
        name = re.sub('.*/(.*?)/device', r'\g<1>', path)
        # so this calls for the internal-devices? so that's the loop?
        device_state(name)
    #so now it has all mass storage devices and loops em (hdd is wrong term, replace)
    for hdd in internal_devices:
        #looks up temperature
        #hddtemp is not natively supported by ubuntu, so try and find sth else
        temperature = run_cmd('hddtemp -u C -nq /dev/%s' % hdd)
        #prints device-name (hdd) and temperature
        print("Disk: [/dev/%s] temperature [%sC]" % (hdd, temperature))
        #why does it print AND returns status af it'd be used again? as only thing
        status = {
                  'disk': 'disk: [%s]' % (str(hdd)),
                  'temp': '[%s]C ' % (str(temperature)),
                 }
        return(status)

# completely misleading def-name. just checks if hddtemp is installed, if not, hddtemp wont be called
def print_motd():
    if(os.path.isfile("/usr/bin/hddtemp")):
        show_hdd_temp()

# definitely put in if-clause since hdd_temp not present in VMs (no SMART)