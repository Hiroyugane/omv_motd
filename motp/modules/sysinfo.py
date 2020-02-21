#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

# counts processes.  make it more detailed
# (who owns how many processes, etc. with ratios maybe)
# put it to CPU section or to misc.
proc_ps = run_cmd('/bin/ps -Afl | wc -l')
# OS
# rpm doesn't exist in ubuntu, changing to non-rpm/lsb-command
proc_release = run_cmd('cat /etc/os-release').split("\n")
# not sure? is it still needed with ubuntu-version?
os_release = proc_release[0] + ' ' + proc_release[1]

# UPTIME
raw_uptime = run_cmd('uptime')
uptime = raw_uptime.split(',')[0].split('up')[1].strip()
#came from combining. put in actual variable-output
rows.append(['Kernel', run_cmd('uname -or')])

# time
# other stuff you'd put in a crash report