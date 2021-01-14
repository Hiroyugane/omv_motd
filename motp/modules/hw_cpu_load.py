#!/usr/bin/env python3
# Status: Reworked, functional
# 
# 
# Input: -
#         
# Output: 
# {
#       '1m': 0.52, 
#       '5m': 0.58, 
#       '15m': 0.59, 
#       '1m-rs': 'cpu_load', 
#       '5m-rs': 'cpu_load', 
#       '15m-rs': 'cpu_load'
# }
#
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#
from warnings import warn
from os import path

from ..baselib import base

# Semi-configurable stuff
fallbackReturn = {
        '1m': float("9.99"),
        '5m': float("9.99"),
        '15m': float("9.99"),
        '1m-rs': "cpu_error",
        '5m-rs': "cpu_error",
        '15m-rs': "cpu_error"
}


# scrape load avg, split and output as list
def cpu_load():
        try:
                loadAvg_raw = base.run_cmd("cat /proc/loadavg").split() 
                cpu_load = {
                        '1m': float(loadAvg_raw[0]),
                        '5m': float(loadAvg_raw[1]),
                        '15m': float(loadAvg_raw[2]),
                        '1m-rs': "cpu_load",
                        '5m-rs': "cpu_load",
                        '15m-rs': "cpu_load"
                }
                if __name__ == "__main__":
                        print(cpu_load)
                return cpu_load
        except: 
                warn("/proc/loadavg not found, are you using a supported OS?")
                return fallbackReturn


if __name__ == "__main__":
        cpu_load()