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

from ..baselib import base

base.log_start
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
    base.log_start()
    try:
        #some stuff
        print()
    except Exception:  
        base.log_exception()
        return "Error"
    else:
        base.log_end()
        return
######################################################
# Main
######################################################
def main():
    base.log_start()
    print("this is a template, if it is main, it will print out the output of all functions for testing purposes")
    base.log_end()
######################################################
# Default clause
######################################################
if __name__ == "__main__":
    main()

base.log_end()
#EOF