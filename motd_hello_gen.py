#!/usr/bin/env python
import os
import subprocess
import re
import socket
import math
import urllib.request
from glob import glob

# Defines colors in a DICT for easier use
COLORS = {
    'bold': "\033[01m",
    'black': "\033[30m",
    'red': "\033[31m",
    'green': "\033[32m",
    'yellow': "\033[33m",
    'blue': "\033[34m",
    'purple': "\033[35m",
    'cyan': "\033[36m",
    'white': "\033[37m",
    'reset': "\033[0m",
    'system': "\033[38;5;120m"}


# colorize a string and reset color afterwards 
def colored(col, s):
    return COLORS[col] + s + COLORS['reset']

# divide bytes by 1024 and change suffix to Datasize "1GB is easier than 1024MB etc"
def humanise(byte_int):
    for x in ['bytes', 'KiB', 'MiB', 'GiB', 'TiB']:
        #if bigger than 1024, divide, go a size further, till under 1024
        if byte_int < 1024.0:
            #have a minimum of 3-digit-numbers incl. decimals
            if byte_int < 10:
                return "%1.2f%s" % (byte_int, x)
            else:
                return "%4.1f%s" % (byte_int, x)
        byte_int /= 1024.0

# smart length: check the length of the line as it'd be output
def smartlen(line):
    # replace tabs with 4 whitespaces
    line = line.replace("\t", ' '*4)
    #remove colorcodes
    for color in COLORS.keys():
        line = line.replace(COLORS[color], '')
    return len(line)

# Fluid Column-Layout code (doesnt make sense to put it here already since rows wouldn't be filled)
# takes the rows of info (name,value) and amount of columns and puts out balanced rows in Row-array-result
def column_display(rows, num_columns=2):
    columns = []
    column = []
    #add row to column 
    for row in rows:
        column.append(row)
        #if the column has the right amount so that rows are balanced -> put column to columns and clear
        if len(column) >= math.floor(float(len(rows))/num_columns):
            columns.append(column)
            column = []
    #put remaining column in columnlist
    if len(column) > 0: columns.append(column)
    column = 0

    # go through rowkeys and rowvalues and set lengths/padding 
    col_texts = []
    for column in columns:
        coltext = []
        #max length for keys is the longest row in the column
        max_keylen = max([len(row[0]) for row in column])
        for row in column:
            #fill with padding and finish off row with values
            padding = ' '*(max_keylen-len(row[0]))
            coltext.append("%s: %s%s" % (row[0], padding, row[1]))
        col_texts.append(coltext)

    result = ""
    # as many times as the length of a row (shouldnt that be for every row?)
    for i in range(len(col_texts[0])):
        line = ""
        #for all columntexts
        for j, coltext in enumerate(col_texts):
            #if iteration-number if small than length of columntext
            if i < len(coltext):
                #if it's not the first row
                if j > 0:
                    #maximum value-length = the highest from the list (containing the length of all the first rows in the column that's at the index of the 2nd iterable number down one ) 
                    #maximum value-length = the highest of (lengths of all 1st rows in the column that's at the index of the 2nd iterable number down one ) 
                    max_vallen = max([len(row[1]) for row in columns[j-1]])
                    #length of the value of row i in column j-1 
                    vallen = len(columns[j-1][i][1])
                    #prepend appropriate amount of tabstops
                    line += "\t"*max([1, int(math.floor(float(max_vallen-vallen)/4))])
                #put in value for row 
                line += coltext[i]
        #line is added to result
        result += line + "\n"
    #result is all rows in n*columns
    return result

# takes the width of XYZ and something uncentered? and returns a result
def center_by(width, uncentered):
    result = ""
    #lines is an array of the uncentered things 
    lines = uncentered.split("\n")
    #length is highest raw-length of rows in lines 
    length = max([smartlen(line) for line in lines])
    for line in lines:
        #put every line in results and prepend half of width minus highest length
        result += ' '*int((width-length)/2) + line + "\n"
    return result

# is used to use commands easier. BASE DEF
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()


# return public ip by checking ident.me as a site
# probably expand that to "IP-Addresses" with a list consisting of internal ip, public ip, ips of routers etc. maybe also ports
# maybe build in api.ipify.org or similar as fallback
def public_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip


# this definition return true if the service requested is running
# maybe add a function to search for services?
# why cant it use use_cmd()?
def service_active(service):
    cmd = '/bin/systemctl is-active %s' % service
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.communicate()
    if proc.returncode == 0:
        return True
    return False

#part for docker-container-info
def docker_status():
    if(os.path.isfile("/usr/bin/docker")):
        # scrape docker version
        docker_ver = run_cmd('docker version')
        #docker_ver = run_cmd('rpm -qa --queryformat "%{VERSION}" docker')
        # scrape running containers
        docker_run = int(run_cmd('/usr/bin/docker ps -q $1 | wc -l'))
        # scrape wiped(?)/exited Containers? probably which arent running but registered, further look into it
        docker_wipe = int(run_cmd('docker ps -a -q -f status=exited | wc -l'))
        #save info into docker associative-array/dictionary(?) noob in python c:
        docker = {'status': 'status: %s, ' % (str('[active]')),
                  'version': 'version [%s]' % (str(docker_ver)),
                  'wipe': 'exited containers [%s], ' % (str(docker_wipe)),
                  'running': 'running containers: [%s], ' % (str(docker_run))}
        return(docker)

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

#mandriva-based nginx-docker used. Completely left out for now since standard system wont have webservers
r''' (raw-string for preventing pylint-warnings)
#find certificates and their status
def certificate_status():
    # cert file to use, maybe put fallback-search in but put main input in config file
    cert_file = '/var/lib/openmandriva/omv/docker-nginx/abf.openmandriva.org-chain.pem'
    if(os.path.isfile(cert_file)):
        # scrape certificate text (whatever that means?)
        certificate_text = run_cmd('openssl x509 -noout -in ' + cert_file +' -text')
        # search some match for the renew-date?
        category_match = re.search('\W*Not After[^:]*:(.+)', certificate_text)
        # scrape due-date from match
        due_date = category_match.group(1)
        # return when cert is going to expire
        certificate = {'cert_expiration': '[%s]' % (str(due_date))}
        return(certificate)
'''

# big block - maybe/probably split up?
def sysinfo():
    # CPU: scrape load avg and split
    raw_loadavg = run_cmd("cat /proc/loadavg").split()
    # CPU: convert load to float
    load = {'1min': float(raw_loadavg[0]),
            '5min': float(raw_loadavg[1]),
            '15min': float(raw_loadavg[2])}
    # DISKS: /home
    # uhm scrape some data from non-human and human? 
    # should automatically register mountpoints anyway
    raw_home = run_cmd("/bin/df -P /home | tail -1").split()
    raw_home_human = run_cmd("/bin/df -Ph /home | tail -1").split()
    home = {'used': int(raw_home[2]),
            'total': int(raw_home[1]),
            'used_human': raw_home_human[2],
            'total_human': raw_home_human[1]}
    home['ratio'] = float(home['used'])/home['total']
    # ratio should then be graphically displayed in form of "+////------+" <- 40% f.e.but thats printout

    # MEMORY
    # /bin/free not working for ubuntu, swapped for free -m, check if output right
    # MEMORY: seems to have a problem with size conversion, shows 3.7kib instead of gib
    raw_free = run_cmd("free -m").split("\n")
    raw_mem = raw_free[1].split()
    raw_swap = raw_free[2].split()
    # MEMORY: puts memorydata and ratio in array 
    memory = {'used': int(raw_mem[1])-int(raw_mem[2]),
              'total': int(raw_mem[1])}
    memory['ratio'] = float(memory['used'])/memory['total']
    # MEMORY: same as above for swap
    swap = {'used': int(raw_swap[2]),
            'total': int(raw_swap[1])}
    swap['ratio'] = 0.0 if swap['total'] == 0 else float(swap['used'])/swap['total']

    # (CPU?) don't know what that does? count processes? if so, make it more detailed
    # (who owns how many processes, etc. with ratios maybe)
    # if it's processes then put it to CPU section or to misc.
    proc_ps = run_cmd('/bin/ps -Afl | wc -l')

    # USERS: looks for all existing users
    logged_users = run_cmd('/usr/bin/users')
    logged_names = run_cmd('/usr/bin/users | sort -u')
    # USERS: not sure whats the difference between users and names? 
    users = {
             'active': len(set(logged_users)),
             'logged': str(logged_names)
            }

    # OS
    # rpm doesn't exist in ubuntu, changing to non-rpm/lsb-command
    proc_release = run_cmd('cat /etc/os-release').split("\n")
    # not sure? is it still needed with ubuntu-version?
    os_release = proc_release[0] + ' ' + proc_release[1]

    # UPTIME
    raw_uptime = run_cmd('uptime')
    uptime = raw_uptime.split(',')[0].split('up')[1].strip()

    # ALL combine
    rows = []
    # Originate commented this -> # rows.append(['Total Users', str(users['total'])])
    rows.append(['Active Users', str(users['active']) + ' [' + str(users['logged']) + ']'])
    rows.append(['Process Count', str(proc_ps)])
    rows.append(['Uptime', uptime])
    rows.append(['OS', os_release])
    rows.append(['Public ip', public_ip()])
    rows.append(['Hostname', socket.gethostname()])
    # the thing below doesn't belong here. no run_cmd in append-section. NO. thanks.
    rows.append(['Kernel', run_cmd('uname -or')])

    # ALL COMBINE: colorize for normal values
    # all values in motd should be in colorized-section, with if-clause if config for that is present, if not -> default color
    # pretty default but can be optimized with switchcases or oneline-ifs
    # COLORIZE: load
    if load['1min'] < 0.4: load['color'] = 'green'
    elif load['1min'] < 0.8: load['color'] = 'yellow'
    else: load['color'] = 'red'
    rows.append(['System Load', colored(load['color'], str(load['1min']))])

    # COLORIZE: home
    if home['ratio'] < 0.4: home['color'] = 'green'
    elif home['ratio'] < 0.8: home['color'] = 'yellow'
    else: home['color'] = 'red'
    rows.append(["/home Usage", colored(home['color'], "%d%% of %s" % (home['ratio']*100, home['total_human']))])

    # COLORIZE: memory
    # in config: put in option to either use percentage or absolute values
    if memory['ratio'] < 0.4: memory['color'] = 'green'
    elif memory['ratio'] < 0.8: memory['color'] = 'yellow'
    else: memory['color'] = 'red'
    rows.append(['Memory Usage', colored(memory['color'], "%d%% of %s" % (memory['ratio']*100, humanise(memory['total'])))])

    #COLORIZE: swap
    if swap['ratio'] < 0.4: swap['color'] = 'green'
    elif swap['ratio'] < 0.8: swap['color'] = 'yellow'
    else: swap['color'] = 'red'
    rows.append(["Swap Usage", colored(swap['color'], "%d%%" % (swap['ratio']*100))])

    #optional failban, docker, certificate
    #make hdd temp optional, too. VMs dont have SMART
    if service_active('fail2ban.service'):
       rows.append(['fail2ban', str(fail2ban_status()['status']) + str(fail2ban_status()['total']) +  str(fail2ban_status()['current'])])
    if service_active('docker.service'):
       rows.append(['Docker', str(docker_status()['status']) + str(docker_status()['running']) + str(docker_status()['wipe']) + str(docker_status()['version'])])
    # from originator(and below) -> fix me
    #rows.append(['Certificate valid', str(certificate_status()['cert_expiration'])])
    #rows.append(['HDD status', str(show_hdd_temp()['temp']) + str(show_hdd_temp()['disk'])])

    return(rows)

# What's this? doesnt work when testing, maybe also mandriva-special? if found what its for, add here
#
# notice its not in the actual codeblock nor in a definition
# <> seems to be a prerequisite for device_state which is for hdd temp?
rootdir_pattern = re.compile('^.*?/devices')
internal_devices = []

# this one looks up hotplug-busses and puts them in the list 
# I suspect this is another mandriva-specific one. Don't know if you'd really want/need that
# especially VMs don't need that since they neither have usb nor firewire nor anything else 
def device_state(name):
    #open hotplug-devicefiles and read
    with open('/sys/block/%s/device/block/%s/removable' % (name, name)) as f:
        # (probably) exit if none there
        if f.read(1) == '1':
            return

    #set path to... uhm... something something
    path = rootdir_pattern.sub('', os.readlink('/sys/block/%s' % name))
    # define valid buses to show (put in cfg)
    hotplug_buses = ("usb", "ieee1394", "mmc", "pcmcia", "firewire")
    #go through every type of bus...
    for bus in hotplug_buses:
        #...and if bus exists in OS..
        if os.path.exists('/sys/bus/%s' % bus):
            #...go through all devices with that bus
            for device_bus in os.listdir('/sys/bus/%s/devices' % bus):
                #save device-link
                device_link = rootdir_pattern.sub('', os.readlink('/sys/bus/%s/devices/%s' % (bus, device_bus)))
                #if there is something with search X, go out of function? 
                if re.search(device_link, path):
                    return
    #This appends only one device since it's not in for-loop?
    #<> whole function gets called for every device
    internal_devices.append(name)

# definitely put in if-clause since hdd_temp not present in VMs (no SMART)
def show_hdd_temp():
    # find hard drives?
    for path in glob('/sys/block/*/device'):
        # seems to search for find mass storage-names?
        name = re.sub('.*/(.*?)/device', r'\g<1>', path)
        # so this calls for the internal-devices? so that's the loop?
        device_state(name)
    #so now it has all mass storage devices and loops em (hdd is wrong term, replace)
    for hdd in internal_devices:
        #looks up temperature
        #hddtemp is not natively supported by ubuntu, so try and find sth else
        temperature = run_cmd('hddtemp -u C -nq /dev/%s' % hdd)
        #prints device-name (hdd) and temperature
        print("Disk: [/dev/%s] temperature [%sC]" % (hdd, temperature))
        #why does it print AND returns status af it'd be used again? as only thing
        status = {
                  'disk': 'disk: [%s]' % (str(hdd)),
                  'temp': '[%s]C ' % (str(temperature)),
                 }
        return(status)

# completely misleading def-name. just checks if hddtemp is installed, if not, hddtemp wont be called
def print_motd():
    if(os.path.isfile("/usr/bin/hddtemp")):
        show_hdd_temp()

#Main-process
#if-clause if process is main or used as a library
if __name__ == "__main__":
    # banner is the logo on top (figlet f.e.) (rename banner to sth. like Header. Banner is a legal notice usually)
    banner_file = '~/log.log'
    # banner is the file banner but with the color called "system"
    banner = colored('system', open(banner_file).read())
    # the bannerlength is the length of the longest line in the banner
    banner_length = max([smartlen(line) for line in banner.split("\n")])
    #The info is the centered, in fluid-column-arranged sysInfo, in one column (put in cfg) (where's certificate stuff?)
    info = center_by(banner_length, column_display(sysinfo(), num_columns=1))
    # output is the banner and all infostuff
    output = banner + "\n" + info
    # do fail2ban stuff (why is it all so inconsistent?)
    fail2ban_status()
    #oben bannerfile and put all info in there? Wouldn't it result in nested info? 
    f = open(banner_file, 'w')
    f.write(info)
    f.close()
    # finally print it all out 
    print(output)

# whatevever the originator wanted to say with that below, maybe the order of things?
#
# -----
#sysinfo()
#hostname()
#show_hdd_temp()
#public_ip()
#print_motd()
#fail2ban_status()
#docker_status()
