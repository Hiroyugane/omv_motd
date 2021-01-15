#!/usr/bin/env python3
# Base Module which is being used in every other python module
# Status: being reworked
######################################################
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
# In-File Config, prework
######################################################
#Read Config
config = ConfigParser()
configpath = os.path.join(os.path.dirname(__file__), '..', 'config')
try:
    config.read(os.path.join(os.path.dirname(__file__), '..', 'config', 'config_main.ini'))
except Exception:
    try:
        shutil.copyfile(os.path.join(configpath, 'config_main.ini.back'), os.path.join(configpath, 'config_main.ini'))
    except Exception:
        logging.critical("config_main.ini not found and backup couldn't be restored, aborting")
    else:
        logging.warn("copied config_main.ini.bak to config_main.ini because python couldn't find a valid config")
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
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        colored_result = colors[col] + s + colors['reset']
    except: 
        logging.critical("Critical Error message")
        return
    else:
        logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return colored_result

# takes int of bytes and puts them into the right unit (/1024). Keeps values mostly to 3 digits
def humanise_byte(int_:int):
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        for x in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']:
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
        logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return int_return

# takes int of bits and puts them into the right unit (/1000). Keeps values mostly to 3 digits
def humanise_bit(int_:int):
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        for x in ['bit', 'Kbit', 'Mbit', 'Gbit', 'Tbit', 'Pbit', 'Ebit', 'Zbit', 'Ybit']:
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
        logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return int_return



































# description of function
def templatefunction():
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        #some stuff
        print()
    except: 
        logging.critical("Critical Error message")
        return
    else:
        logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return
######################################################
# Main
######################################################
def main():
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    print("this is a template, if it is main, it will print out the output of all functions for testing purposes")
    logging.debug("Finishing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
######################################################
# Default clause
######################################################
if __name__ == "__main__":
    main()

logging.debug('Finished Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Finished Importing '+str(Path(__file__).resolve()))
#EOF

















































# smart length: check the length of the line as it'd be output
def smartlen(line):
    # replace tabs with 4 whitespaces
    line = line.replace("\t", ' '*4)
    #remove colorcodes
    for color in colors.keys():
        line = line.replace(colors[color], '')
    return len(line)

# is used to use commands easier. BASE DEF
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()

# Functiontests
def color_test():
    colortest_result = []
    for color in colors:
        colortest_message = colored(color, color)
        colortest_result.append(print(colortest_message))
    return colortest_result

if __name__ == "__main__":
    color_test()