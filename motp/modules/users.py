#!/usr/bin/env python3
# Status:   copied over existing code that will be reworked here.
#           Rework is being worked on; Will be example-module when finished.
#           Open for suggestions
from baselibrary import run_cmd
#from baselibrary import 

# Returns count of users logged in past 7 days
def logins_recent(days):
    #prepare
    users_recentLogins = []
    # Fetches logged-in users and 
    loggedInList = run_cmd('/usr/bin/users | sort -u').split(' ')
    users_loggedInList = []
    users_loggedInList.append(loggedInList)
    # Lastlog prints rows of users with some info of them. Fetching and processing input to array:
    recentLogins = run_cmd('lastlog -t %d' % 5).split('\n')
    # removes header
    recentLogins.pop(0)
    # Loops through rows, cuts the columns and creates matrix'
    for n in range(len(recentLogins)):
        users_recentLogins.append(recentLogins[n].split(None, 3))
        users_recentLogins[n][3] = users_recentLogins[n][3].split()
    #Put matrix in documentation
    return users_loggedInList, users_recentLogins



## Legacy-Returnvalue // Kept for reference
# users = {
#             'active': len(set(logged_users)),
#             'logged': str(logged_names)
#         }


## Commands to use
#w | awk 'FNR>=2{print $1, "|", $3, "|", $8}' | column -t
#lastlog -t 7