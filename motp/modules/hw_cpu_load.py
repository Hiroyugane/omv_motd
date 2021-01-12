#!/usr/bin/env python3
# Status: Reworked, not tested
#         
# Output: 
#
#
#
#
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#
from ..baselib import base


# scrape load avg, split and output as list
def cpu_load():
        loadAvg_raw = base.run_cmd("cat /proc/loadavg").split()
        cpu_load = {
                '1m': float(loadAvg_raw[0]),
                '5m': float(loadAvg_raw[1]),
                '15m': float(loadAvg_raw[2]),
                '1m-rs': "cpu_load",
                '5m-rs': "cpu_load",
                '15m-rs': "cpu_load"
        }
        print(cpu_load)
        return cpu_load

if __name__ == "__main__":
        cpu_load()