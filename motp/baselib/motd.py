#!/usr/bin/env python3
# Will be the mainfile that will put together scraping and formats
# All content is raw leftovers from original fork. 
# Will be reworked completely.
# Status:   copied over existing code and split up code to module.
#######################################################################
# Info-Documentation
######################################################
# To-Do, Ideas:
#       put in more functions for CPU-related stuff
######################################################
# Foundation, do not change
######################################################
import logging
from pathlib import Path
from os.path import dirname, basename, isfile, join
import sys
from .. import scraper
from . import base
import os 

# try:
#     os.mkdir(join("motp", "logs"))
# except FileExistsError:
#     pass
# finally:
#     logging.config.fileConfig(join(
#         dirname(__file__), 
#         "config", 
#         "logging.conf")
#         )


base.log_start()
######################################################
# Imports
######################################################

from glob import glob
import importlib



# dynamically read existing .py-Files in modules/ and import them
allScraper = glob(join(dirname(__file__), "..", "scraper", "*.py"))
motd_scraperList = [ basename(f)[:-3] 
    for f in allScraper if isfile(f) and not f.endswith('__init__.py')]
for moduleItem in motd_scraperList:
    importlib.import_module('.scraper.'+moduleItem, "motp")
######################################################
# In-File Config
######################################################


######################################################
# Functions
######################################################

######################################################
# Main
######################################################
def main():
    print(base.colored("bblue", str(scraper.hw_cpu.loadavg())))
    print(base.colored("bggreen", str(scraper.hw_ram.allocation())))
######################################################
# Default end
######################################################
if __name__ == "__main__":
        main()

base.log_end()
logging.info("finished program")
















# # ALL combine (replace with calling of functions) // 1. gathering, 2. formatting
# rows = []
# # Originate commented this -> # rows.append(['Total Users', str(users['total'])])
# rows.append(['Active Users', str(users['active']) + ' [' + str(users['logged']) + ']'])
# rows.append(['Process Count', str(proc_ps)])
# rows.append(['Uptime', uptime])
# rows.append(['OS', os_release])
# rows.append(['Public ip', public_ip()])
# rows.append(['Hostname', socket.gethostname()])
# # colorIZE: load
# rows.append(['System Load', colored(load['color'], str(load['1min']))])
# # colorIZE: home
# rows.append(["/home Usage", colored(home['color'], "%d%% of %s" % (home['ratio']*100, home['total_human']))])
# # colorIZE: memory
# # in config: put in option to either use percentage or absolute values
# rows.append(['Memory Usage', colored(memory['color'], "%d%% of %s" % (memory['ratio']*100, humanise(memory['total'])))])
# #colorIZE: swap
# rows.append(["Swap Usage", colored(swap['color'], "%d%%" % (swap['ratio']*100))])
# #optional failban, docker, certificate
# #make hdd temp optional, too. VMs dont have SMART
# if service_active('fail2ban.service'):
#     rows.append(['fail2ban', str(fail2ban_status()['status']) + str(fail2ban_status()['total']) +  str(fail2ban_status()['current'])])
# if service_active('docker.


# # whatevever the originator wanted to say with that below, maybe the order of things?
# #
# # -----
# #sysinfo()
# #hostname()
# #show_hdd_temp()
# #public_ip()
# #print_motd()
# #fail2ban_status()
# #docker_status()


# def main():
#     # banner is the logo on top (figlet f.e.) (rename banner to sth. like Header. Banner is a legal notice usually)
#     banner_file = '~/log.log'
#     # banner is the file banner but with the color called "system"
#     banner = colored('system', open(banner_file).read())
#     # the bannerlength is the length of the longest line in the banner
#     banner_length = max([smartlen(line) for line in banner.split("\n")])
#     #The info is the centered, in fluid-column-arranged sysInfo, in one column (put in cfg) (where's certificate stuff?)
#     info = center_by(banner_length, column_display(sysinfo(), num_columns=1))
#     # output is the banner and all infostuff
#     output = banner + "\n" + info
#     # do fail2ban stuff (why is it all so inconsistent?)
#     fail2ban_status()
#     #oben bannerfile and put all info in there? Wouldn't it result in nested info? 
#     f = open(banner_file, 'w')
#     f.write(info)
#     f.close()
#     # finally print it all out 
#     print(output)