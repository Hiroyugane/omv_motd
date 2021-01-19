#!/usr/bin/env python3
#Encoding: UTF-8
"""
Status: New, not tested yet, not published
Input: -
        
Output-Example: 
{
}

To-Do, Ideas:

"""
########################################################################################
# Imports                                                                              #
########################################################################################
import logging

from ..baselib import base

base.log_start
########################################################################################
# Metadata                                                                             #
########################################################################################
__author__ = "Hiroyugane"
__copyright__ = ""
__credits__ = ["fedya", "Hiroyugane"]
__license__ = "GNU"
__version__ = "0.1"
__maintainer__ = "Hiroyugane"
__email__ = "Dennis@IT-Hiro.de"
__status__ = "WIP"
########################################################################################
# In-File Config                                                                       #
########################################################################################
function_fallbackReturn = {
}
########################################################################################
# Functions, Methods (Code)                                                            #
########################################################################################
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
########################################################################################
# Main                                                                                 #
########################################################################################
def main():
    base.log_start()
    print("""
        this is a template, 
        if it is main, 
        it will print out the output of all functions - 
        for testing purposes
        try to not get above 80 characters per line, please.
        For more info, read PEP0008
        """)
    base.log_end()
########################################################################################
# Default clause                                                                       #
########################################################################################
if __name__ == "__main__":
    main()

base.log_end()
#EOF