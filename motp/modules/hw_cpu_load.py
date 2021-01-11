#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet
#
#
#
#
#
from ..baselib import *


# scrape load avg, split and output as list
def cpu_load():
        loadAvg_raw = baselib.run_cmd("cat /proc/loadavg").split()
        cpu_load = {
                '1m': float(loadAvg_raw[0]),
                '5m': float(loadAvg_raw[1]),
                '15m': float(loadAvg_raw[2])
        }
        return cpu_load

if __name__ == "__main__":
        cpu_load()