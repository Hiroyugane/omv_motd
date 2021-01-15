#!/usr/bin/env python3
# Status: Reworked, functional
######################################################
# Info-Documentation
######################################################
# Input: -
#         
# Output-Example: 
# {
#       '1m': 0.52, 
#       '5m': 0.58, 
#       '15m': 0.59, 
#       '1m-rs': 'cpu_load', 
#       '5m-rs': 'cpu_load', 
#       '15m-rs': 'cpu_load'
# }
#
# To-Do, Ideas:
#       put in more functions for CPU-related stuff
######################################################
# Foundation, do not change
######################################################
import logging
from pathlib import Path
import inspect

from ..baselib import base

logging.debug('Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Importing '+str(Path(__file__).resolve()))
def whoami():
    return inspect.stack()[1][3]
def whosparent():
    return inspect.stack()[2][3]
######################################################
# Imports
######################################################
import os

######################################################
# In-File Config
######################################################
loadAvg_fallbackReturn = {
    '1m': float("9.99"),
    '5m': float("9.99"),
    '15m': float("9.99"),
    '1m-rs': "cpu_error",
    '5m-rs': "cpu_error",
    '15m-rs': "cpu_error"
}
######################################################
# Functions
######################################################
# scrape load avg, split and output as dict
def loadavg():
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        loadAvg_raw = base.run_cmd("cat /proc/loadavg").split() 
    except Exception: 
        logging.critical("/proc/loadavg not found, are you using a supported OS?")
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
        logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return cpu_load
######################################################
# Main
######################################################
def main():
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    print(loadavg())
    logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
######################################################
# Default clause
######################################################
if __name__ == "__main__":
    main()

logging.debug('Finished Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Finished Importing '+str(Path(__file__).resolve()))
#EOF