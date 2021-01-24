#!/usr/bin/env python3
# Base Module which is being used in every other python module
# Status: being reworked
#######################################################################
# Info-Documentation
######################################################
# Input: -
#         
# Output-Example: 
# {
# }
#
# To-Do, Ideas:
#      

######################################################
# Imports
######################################################
import math
import subprocess
import os
import re
import socket
import urllib.request
from glob import glob
from configparser import ConfigParser
import calendar
import datetime
import sys
import shutil
######################################################
# Foundation, do not change
######################################################
import logging
from pathlib import Path
import inspect
######################################################
# logwork-functions
######################################################
def whoami():
    try:
        whoami_result = inspect.stack()[2][3]
        return whoami_result
    except:
        return "whoami not found"
def whosparent():
    try:
        whosparent_result = inspect.stack()[3][3]
        return whosparent_result
    except:
        return "whosparent not found"

def log_start():
    return logging.debug((
        'Running ' if __name__ == '__main__' 
        else 'Importing/using '
        )
        +str(Path(__file__).resolve())
        +str(": {} ({})".format(whoami(), whosparent()))
        )
def log_end(): 
    return logging.debug((
        'Finished Running ' if __name__ == '__main__' 
        else 'Finished Importing/using '
        )
        +str(Path(__file__).resolve())
        +str(": {} ({})".format(whoami(), whosparent()))
        )
def log_exception(): 
    return logging.critical((
        'Exception while Running ' if __name__ == '__main__' 
        else 'Exception while Importing/using '
        )
        +str(Path(__file__).resolve())
        +str(": {} ({})".format(whoami(), whosparent())))

log_start()
######################################################
# In-File Config, prework
######################################################
#Read Config
config = ConfigParser()
global configPath
configPath = os.path.join(os.path.dirname(__file__), '..', 'config')
try:
    config.read(os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'config', 
        'config_main.ini'
        ))
except Exception:
    try:
        shutil.copyfile(
            os.path.join(configPath, 'config_main.ini.bak'), 
            os.path.join(configPath, 'config_main.ini')
            )
    except Exception:
        logging.critical(
            """config_main.ini not found, 
            backup couldn't be restored, aborting"""
            )
    else:
        logging.warn(
            """copied config_main.ini.bak to config_main.ini 
            because python couldn't find a valid config"""
            )
else:
    logging.debug("read config_main.ini successfully")
# format color dictionary
colors_raw = config._sections['colors']
colors = {}
for color in colors_raw:
    colors[color] = chr(0x1b) + colors_raw[color]
######################################################
# Functions, Methods (Code)
######################################################
# run commands as if they'd be used shell
def colored(col:str, s:str):
    log_start()
    try:
        colored_result = colors[col] + s + colors['reset']
    except: 
        logging.critical("Critical Error message")
        return
    else:
        log_end()
        return colored_result

# takes int of bytes and puts them into the right unit (/1024). 
# Keeps returns mostly to 3 digits (excl. dot).
def humanise_byte(int_:int):
    log_start()
    try:
        for x in [
            'B', 'KiB', 'MiB', 
            'GiB', 'TiB', 'PiB', 
            'EiB', 'ZiB', 'YiB'
            ]:
            if int_ < 1024.0:
                if int_ < 1:
                    int_return = "%1.3f %s" % (int_, x)
                    break
                elif int_ < 10:
                    int_return = "%1.2f %s" % (int_, x)
                    break
                elif int_ < 100:
                    int_return = "%1.1f %s" % (int_, x)
                    break
                else:
                    int_return = "%0.0f %s" % (int_, x)
                    break
            else: int_ /= 1024.00
    except Exception:
        logging.critical("Critical Error with humanising: "+int_)
        return
    else:
        log_end()
        return int_return

# takes int of bits and puts them into the right unit (/1000). 
# returns are mostly 3 digit (excluding dot).
def humanise_bit(int_:int):
    log_start()
    try:
        for x in [
            'bit', 'Kbit', 'Mbit', 
            'Gbit', 'Tbit', 'Pbit', 
            'Ebit', 'Zbit', 'Ybit'
            ]:
            if int_ < 1000.0:
                if int_ < 1:
                    int_return = "%1.3f %s" % (int_, x)
                    break
                elif int_ < 10:
                    int_return = "%1.2f %s" % (int_, x)
                    break
                elif int_ < 100:
                    int_return = "%1.1f %s" % (int_, x)
                    break
                else:
                    int_return = "%0.0f %s" % (int_, x)
                    break
            else: int_ /= 1000.00
    except Exception:
        logging.critical("Critical Error with humanising: "+int_)
        return
    else:
        log_end()
        return int_return

# smart length: check the length of the line as it'd be output
def smartlen(line:str):
    log_start()
    try:
        line = line.replace("\t", ' '*4)
        for color in colors.keys():
            line = line.replace(colors[color], '')
    except Exception: 
        log_exception()
        return
    else:
        log_end()
        return len(line)

# make commands run as if they're ran on terminal
def run_cmd(cmd):
    log_start()
    try:
        cmd_output = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.PIPE
            ).decode('utf-8').strip()
    except Exception: 
        log_exception()
        return
    else:
        log_end()
        return cmd_output

# Function Test
def color_test():
    log_start()
    colortest_result = []
    try:
        for color in colors:
            colortest_message = colored(color, color)
            colortest_result.append(colortest_message)
    except Exception: 
        log_exception()
        return "Error"
    else:
        for colormessage in colortest_result:
            print(colormessage)
        log_end()
        return 

# description of function
def templatefunction():
    log_start()
    try:
        #some stuff
        ""
    except Exception: 
        log_exception()
        return "Error"
    else:
        log_end()
        return
######################################################
# Main
######################################################
def main():
    log_start()
    color_test()
    log_end()
######################################################
# Default clause
######################################################
if __name__ == "__main__":
    main()
log_end()
#EOF