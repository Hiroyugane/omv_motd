#!/usr/bin/env python3
#Encoding: UTF-8
"""
This module will be scraping everything to do with RAM
Status: reworked and functional
Input: -
Output-Example: 
{
    "mem": {
        "total": 26837749760,
        "used": 136314880,
        "free": 26426757120,
        "shared": 73728,
        "buff": 274677760,
        "available": 26367692800,
        "p_used": 0.005079221664223461,
        "p_free": 0.9846860245856917,
        "total-rs": "mem_total",
        "used-rs": "mem_used",
        "free-rs": "mem_free",
        "shared-rs": "mem_shared",
        "buff-rs": "mem_buff",
        "available-rs": "mem_available",
        "p_used-rs": "mem_p_used",
        "p_free-rs": "mem_p_free",
    },
    "swap": {
        "total": 7516192768,
        "used": 0,
        "free": 7516192768,
        "p_used": 0.0,
        "p_free": 1.0,
        "total-rs": "swap_total",
        "used-rs": "swap_used",
        "free-rs": "swap_free",
        "p_used-rs": "swap_p_used",
        "p_free-rs": "swap_p_free",
    },
    "total": {
        "total": 34353942528,
        "used": 136314880,
        "free": 33942949888,
        "p_used": 0.003967954475353077,
        "p_free": 0.9880365218732894,
        "total-rs": "total_total",
        "used-rs": "total_used",
        "free-rs": "total_free",
        "p_used-rs": "total_p_used",
        "p_free-rs": "total_p_free",
    },
}
To-Do, Ideas:
    Improve ruleset-appending to dictionary
"""
########################################################################################
# Imports                                                                              #
########################################################################################
import logging
from ..baselib import base

base.log_start
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
allocation_return_fallback = {
    "mem": {
        "total": 0,
        "used": 0,
        "free": 0,
        "shared": 0,
        "buff": 0,
        "available": 0,
        "p_used": float(0),
        "p_free": float(0),
        "total-rs": "error",
        "used-rs": "error",
        "free-rs": "error",
        "shared-rs": "error",
        "buff-rs": "error",
        "available-rs": "error",
        "p_used-rs": "error",
        "p_free-rs": "error"
    },
    "swap": {
        "total": 0,
        "used": 0,
        "free": 0,
        "p_used": float(0),
        "p_free": float(0),
        "total-rs": "error",
        "used-rs": "error",
        "free-rs": "error",
        "p_used-rs": "error",
        "p_free-rs": "error"
    },
    "total": {
        "total": 0,
        "used": 0,
        "free": 0,
        "p_used": float(0),
        "p_free": float(0),
        "total-rs": "error",
        "used-rs": "error",
        "free-rs": "error",
        "p_used-rs": "error",
        "p_free-rs": "error"
    }
}
########################################################################################
# Functions, Methods (Code)                                                            #
########################################################################################
# scrapes ram-splits in bytes
def allocation():
    base.log_start()
    try:
        values_raw = base.run_cmd("free -bt").split()
        allocation_return = {
            "mem": {
                "total": int(values_raw[7]),
                "used": int(values_raw[8]),
                "free": int(values_raw[9]),
                "shared": int(values_raw[10]),
                "buff": int(values_raw[11]),
                "available": int(values_raw[12]),
                "p_used": float(int(values_raw[8]) / int(values_raw[7])),
                "p_free": float(int(values_raw[9]) / int(values_raw[7])),
                "total-rs": "mem_total",
                "used-rs": "mem_used",
                "free-rs": "mem_free",
                "shared-rs": "mem_shared",
                "buff-rs": "mem_buff",
                "available-rs": "mem_available",
                "p_used-rs": "mem_p_used",
                "p_free-rs": "mem_p_free"
            },
            "swap": {
                "total": int(values_raw[14]),
                "used": int(values_raw[15]),
                "free": int(values_raw[16]),
                "p_used": float(int(values_raw[15]) / int(values_raw[14])),
                "p_free": float(int(values_raw[16]) / int(values_raw[14])),
                "total-rs": "swap_total",
                "used-rs": "swap_used",
                "free-rs": "swap_free",
                "p_used-rs": "swap_p_used",
                "p_free-rs": "swap_p_free"
            },
            "total": {
                "total": int(values_raw[18]),
                "used": int(values_raw[19]),
                "free": int(values_raw[20]),
                "p_used": float(int(values_raw[19]) / int(values_raw[18])),
                "p_free": float(int(values_raw[20]) / int(values_raw[18])),
                "total-rs": "total_total",
                "used-rs": "total_used",
                "free-rs": "total_free",
                "p_used-rs": "total_p_used",
                "p_free-rs": "total_p_free"
            }
        }
    except Exception:  
        base.log_exception()
        logging.critical("command 'free -bt' didn't work, are you using a supported OS?")
        return allocation_return_fallback
    else:
        base.log_end()
        return allocation_return
########################################################################################
# Main                                                                                 #
########################################################################################
def main():
    base.log_start()
    print(allocation())
    base.log_end()
########################################################################################
# Default clause                                                                       #
########################################################################################
if __name__ == "__main__":
    main()

base.log_end()
#EOF