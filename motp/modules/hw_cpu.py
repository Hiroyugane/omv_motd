#!/usr/bin/env python3
#Encoding: UTF-8
"""
Status: Reworked, functional
Input: -
        
Output-Example: 
{
      '1m': 0.52, 
      '5m': 0.58, 
      '15m': 0.59, 
      '1m-rs': 'cpu_load', 
      '5m-rs': 'cpu_load', 
      '15m-rs': 'cpu_load'
}

To-Do, Ideas:
      put in more functions for CPU-related stuff
"""
########################################################################################
# Imports                                                                              #
########################################################################################
import os
import logging

from ..baselib import base

base.log_start()
########################################################################################
# Metadata                                                                             #
########################################################################################
__author__ = "Hiroyugane"
__copyright__ = ""
__credits__ = ["Fedya", "Hiroyugane"]
__license__ = "GNU"
__version__ = "0.1"
__maintainer__ = "Hiroyugane"
__email__ = "Dennis@IT-Hiro.de"
__status__ = "WIP"
########################################################################################
# In-File Config                                                                       #
########################################################################################
loadAvg_fallbackReturn = {
    '1m': float("9.99"),
    '5m': float("9.99"),
    '15m': float("9.99"),
    '1m-rs': "error",
    '5m-rs': "error",
    '15m-rs': "error"
}
########################################################################################
# Functions, Methods (Code)                                                            #
########################################################################################
# scrape load avg, split and output as dict
def loadavg():
    base.log_start()
    try:
        loadAvg_raw = base.run_cmd("cat /proc/loadavg").split() 
    except Exception:
        logging.critical(
            "/proc/loadavg not found, are you using a supported OS?")
        return loadAvg_fallbackReturn
    else:
        cpu_load = {
            '1m': float(loadAvg_raw[0]),
            '5m': float(loadAvg_raw[1]),
            '15m': float(loadAvg_raw[2]),
            '1m-rs': "cpu_load",
            '5m-rs': "cpu_load",
            '15m-rs': "cpu_load"
        }
        base.log_end()
        return cpu_load
########################################################################################
# Main                                                                                 #
########################################################################################
def main():
    base.log_start()
    print(loadavg())
    base.log_end()
########################################################################################
# Default clause                                                                       #
########################################################################################
if __name__ == "__main__":
    main()

base.log_end()
#EOF