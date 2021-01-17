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
######################################################
# In-File Config
######################################################
__all__ = ["base"]
######################################################
# Functions
######################################################
######################################################
# Default clause
######################################################
logging.debug('Finished Running '+str(Path(__file__).resolve()) if __name__ == '__main__' else 'Finished Importing '+str(Path(__file__).resolve()))
#EOF

