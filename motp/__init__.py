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
# Foundation, do not change
######################################################
import warnings
import logging
from pathlib import Path
from os.path import dirname, basename, isfile, join
import inspect


logdir = join(Path(dirname(__file__)), Path("log.log"))
logging.basicConfig(filename=logdir, level=logging.DEBUG)
logging.debug('Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Importing '+str(Path(__file__).resolve()))
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
logging.debug('Finished Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Finished Importing '+str(Path(__file__).resolve()))
#EOF

