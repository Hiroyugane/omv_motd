#!/usr/bin/env python3
# Status: Reworked, functional
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
import warnings
import logging
from pathlib import Path
from ..baselib import base
logging.info('Running' if __name__ == '__main__' else 'Importing' + str(Path(__file__).resolve()))
######################################################
# Imports
######################################################
# global imports here

####################
# local imports here

######################################################
# In-File Config
######################################################
function_fallbackReturn = {
}
######################################################
# Code, Functions
######################################################
# description of function
def templatefunction():
        try:
            #some stuff
            logging.critical("templatefunction finished successful")
            return 
        except: 
            logging.critical("Critical Error message")
            return
######################################################
# Main
######################################################
def main():
        print("this is a template, if it is main, it will print out the output of all functions for testing purposes")
######################################################
# Default clause
######################################################
if __name__ == "__main__":
        main()