#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

# DISKS: /home
# uhm scrape some data from non-human and human? 
# should automatically register mountpoints anyway
raw_home = run_cmd("/bin/df -P /home | tail -1").split()
raw_home_human = run_cmd("/bin/df -Ph /home | tail -1").split()
home = {'used': int(raw_home[2]),
        'total': int(raw_home[1]),
        'used_human': raw_home_human[2],
        'total_human': raw_home_human[1]}
home['ratio'] = float(home['used'])/home['total']
# ratio should then be graphically displayed in form of "+////------+" <- 40% f.e.but thats printout
