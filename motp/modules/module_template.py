#!/usr/bin/env python3
# Status: New, not tested yet, not published
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

######################################################
# In-File Config
######################################################
function_fallbackReturn = {
}
######################################################
# Functions, Methods (Code)
######################################################
# description of function
def templatefunction():
    logging.debug("Executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
    try:
        #some stuff
        print()
    except Exception:  
        logging.critical("Error executing "+str(Path(__file__).resolve())+": "+whoami()+" ("+whosparent()+")")
        return "Error"
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