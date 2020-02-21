#!/usr/bin/env python3
# Status:   copied over existing code that will be reworked here.
#           Rework is being worked on; Will be example-module when finished.
#           Open for suggestions
from ..common.library import run_cmd
from ..common import library
import datetime
import calendar
from operator import itemgetter
#from baselibrary import 

# Returns list with currently logged in-users + who logged in the past <days> days
def logins_recent(days):
    # Fetches logged-in users and 
    loggedInList = run_cmd('/usr/bin/users | sort -u').split(' ')
    users_loggedInList = []
    users_loggedInList.append(loggedInList)
    # Lastlog prints rows of users with some info of them. Fetching and processing input to array:
    users_recentLogins = []
    recentLogins = run_cmd('lastlog -t %d' % 5).split('\n')
    # removes header
    recentLogins.pop(0)
    # Loops through rows, cuts the columns and creates matrix'
    for n in range(len(recentLogins)):
        users_recentLogins.append(recentLogins[n].split(None, 3))
        users_recentLogins[n][3] = users_recentLogins[n][3].split()
        # convert existing data to naive timestamp 
        # move year to front
        users_recentLogins[n][3].insert(0, users_recentLogins[n][3].pop(5))
        # move day after date
        users_recentLogins[n][3].insert(3, users_recentLogins[n][3].pop(1))
        users_recentLogins[n][3].insert(1, list(calendar.month_abbr).index(users_recentLogins[n][3][1]))
        users_recentLogins[n].insert(4, datetime.datetime.timestamp(datetime.datetime(year=int(users_recentLogins[n][3][0]), month=int(users_recentLogins[n][3][1]), day=int(users_recentLogins[n][3][3]), hour=int(users_recentLogins[n][3][5][0:2]), minute=int(users_recentLogins[n][3][5][3:5]), second=int(users_recentLogins[n][3][5][6:8]))))
    # return-value will be a list with the values (nested)
    return users_loggedInList, users_recentLogins

# returns info about the user who logged in
def user():
    # find out whose login-time is the 'highest' (newest)
    users = logins_recent(1)[1]
    users_username = max(users, key=itemgetter(-1))
    uid = run_cmd('id %' %users_username).split()











    return users_user







## Legacy-Returnvalue // Kept for reference
# users = {
#             'active': len(set(logged_users)),
#             'logged': str(logged_names)
#         }


## Commands to use
#w | awk 'FNR>=2{print $1, "|", $3, "|", $8}' | column -t