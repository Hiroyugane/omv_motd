#!/usr/bin/env python3
# Status: New, not tested yet, not published
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
# Prework
######################################################
import warnings
import logging
import logging.config
from pathlib import Path
import os
from os.path import dirname, basename, isfile, join
import inspect
from .baselib import base

try:
    os.mkdir(join("motp", "logs"))
except FileExistsError:
    pass
finally:
    logging.config.fileConfig(join(
        dirname(__file__), 
        "config", 
        "logging.conf")
        )

base.log_start()
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
######################################################
# In-File Config
######################################################
######################################################
# Functions
######################################################
######################################################
# Default clause
######################################################
base.log_end()
#EOF

