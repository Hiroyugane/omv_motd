#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet


# CPU: scrape load avg and split
raw_loadavg = run_cmd("cat /proc/loadavg").split()
# CPU: convert load to float
load = {'1min': float(raw_loadavg[0]),
        '5min': float(raw_loadavg[1]),
        '15min': float(raw_loadavg[2])}
