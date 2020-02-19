#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

#part for fail2ban (recommended program)
def fail2ban_status():
    #if fail2ban is installed
    if(os.path.isfile("/usr/bin/fail2ban-client")):
        # was already commented out? -> # get_fail2ban=$(fail2ban-client status sshd | grep -i "Total banned" | awk '{printf $4}')
        # amount of banned ips
        # f2ban_proc -> raw-file (also rename to raw)
        f2ban_proc = run_cmd('/usr/bin/fail2ban-client status sshd')
        # total banned searched in raw
        category_match = re.search(r'\W*Total banned[^:]*:\D*(\d+)', f2ban_proc)
        # currently banned searched in raw
        category_match2 = re.search(r'\W*Currently banned[^:]*:\D*(\d+)', f2ban_proc)
        # total banned
        # returns 0 if nothing there
        banned = category_match.group(1)
        #current banned
        banned_cur = category_match2.group(1)
        #give out output, "status" not useful since not shown if inactive?
        f2ban = {'status': 'status: %s, ' % (str('[active]')),
                 'total': 'banned total [%s] ' % (str(banned)),
                 'current': 'currently banned: [%s]' % (str(banned_cur))}
        return(f2ban)
    #notice: isfile-clause for dynamic output recommended
    # maybe stderror-print if not found? tell to disable in config?