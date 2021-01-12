#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#

# return public ip by checking ident.me as a site
# probably expand that to "IP-Addresses" with a list consisting of internal ip, public ip, ips of routers etc. maybe also ports
# maybe build in api.ipify.org or similar as fallback
def public_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip