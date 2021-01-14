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
import warnings
import logging
from pathlib import Path

from ..baselib import base

logging.info('Running' if __name__ == '__main__' else 'Importing' + str(Path(__file__).resolve()))
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
# Code, Functions
######################################################
# scrape load avg, split and output as list
def loadavg():
        logging.debug("calling loadavg")
        try:
                loadAvg_raw = base.run_cmd("cat /proc/loadavg").split() 
        except Exception: 
                warnings.warn("/proc/loadavg not found, are you using a supported OS?")
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
                return cpu_load
######################################################
# Main
######################################################
def main():
        print(dir(__file__))
        print(loadavg())
######################################################
# Default clause
######################################################
if __name__ == "__main__":
        main()