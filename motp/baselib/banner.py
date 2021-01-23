#!/usr/bin/env python3
#Encoding: UTF-8
"""
Status: New, not tested yet, not published
Input: Bannerfile (txt)
        
Output-Example: 
{
}

To-Do, Ideas:
maybe add footer
Generate banner.txt automatically
templates (Operating System, hostname, basic example banners, etc.)
"""
############################################################################8############
# Imports                                                                              #
########################################################################################
import logging
from pathlib import Path
from os.path import dirname, basename, isfile, join
import sys
from .. import scraper
from . import base
import os 

base.log_start
########################################################################################
# Metadata                                                                             #
########################################################################################
__author__ = "Hiroyugane"
__copyright__ = ""
__credits__ = ["Hiroyugane"]
__license__ = "GNU"
__version__ = "0.1"
__maintainer__ = "Hiroyugane"
__email__ = "Dennis@IT-Hiro.de"
__status__ = "WIP"
########################################################################################
# In-File Config                                                                       #
########################################################################################
bannerPath = os.path.join(
    os.path.dirname(__file__), '..', 'config', 'banner.txt'
    )
BannerStart = 10 #Start read on Line X
function_fallbackReturn = {
}
########################################################################################
# Functions, Methods (Code)                                                            #
########################################################################################
# description of function
def read_file():
    base.log_start()
    Banner = {}
    BannerLines = []
    BannerLength = 0
    try:
        m = 0
        txtBanner = open(bannerPath)
        for n in txtBanner:
            if m < BannerStart-1:
                pass
            else: 
                BannerLines.append(n)
                if len(n) > BannerLength:
                    BannerLength = len(n) 
            m += 1 
        
        Banner["Height"] = len(BannerLines)
        Banner["Length"] = BannerLength
        Banner["Lines"] = BannerLines
    except Exception:  
        base.log_exception()
        return "Error"
    else:
        base.log_end()
        return Banner
########################################################################################
# Main                                                                                 #
########################################################################################
def main():
    base.log_start()
    print(read_file())
    base.log_end()
########################################################################################
# Default clause                                                                       #
########################################################################################
if __name__ == "__main__":
    main()

base.log_end()
#EOF