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

from baselib import threshold_color

# read config
config = ConfigParser()
config.read('../config/config_main.ini')
colors = config._sections['colors']







# colorize a string and reset color afterwards 
def colored(col, s):
    return colors[col] + s + colors['reset']


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
    for color in colors.keys():
        line = line.replace(colors[color], '')
    return len(line)

# is used to use commands easier. BASE DEF
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()
