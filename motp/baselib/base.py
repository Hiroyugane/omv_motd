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
######################################################
# Functions, Methods (Code)
######################################################
# run commands as if they'd be used shell
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
















































# format color dictionary
COLORS_raw = config._sections['colors']
COLORS = {}
for color in COLORS_raw:
    COLORS[color] = chr(0x1b) + COLORS_raw[color]


##; Functions

# colorize a string and reset color afterwards 
def colored(col, s):
    return COLORS[col] + s + COLORS['reset']


# divide bytes by 1024 and change suffix to Datasize "1GB is easier than 1024MB etc"
def humanise(byte_int):
    for x in ['bytes', 'KiB', 'MiB', 'GiB', 'TiB']:
        #if bigger than 1024, divide, go a size further, till under 1024
        if byte_int < 1024.0:
            #have a minimum of 3-digit-numbers incl. decimals
            if byte_int < 10:
                return "%1.2f%s" % (byte_int, x)
            else:
                return "%4.1f%s" % (byte_int, x)
        byte_int /= 1024.00


# smart length: check the length of the line as it'd be output
def smartlen(line):
    # replace tabs with 4 whitespaces
    line = line.replace("\t", ' '*4)
    #remove colorcodes
    for color in COLORS.keys():
        line = line.replace(COLORS[color], '')
    return len(line)

# is used to use commands easier. BASE DEF
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()

# Functiontests
def color_test():
    colortest_result = []
    for color in COLORS:
        colortest_message = colored(color, color)
        colortest_result.append(print(colortest_message))
    return colortest_result

if __name__ == "__main__":
    color_test()