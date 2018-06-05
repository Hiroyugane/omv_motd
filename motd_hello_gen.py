#!/usr/bin/env python
import os
import subprocess
import socket
import platform
import sys
import re
import math
import random
import textwrap
from glob import glob

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

# colorize
def colored(col, s):
    return COLORS[col] + s + COLORS['reset']

def humanise(num):
    """Human-readable size conversion."""
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0

def smartlen(line):
    line = line.replace("\t", ' '*4)
    for color in COLORS.keys():
        line = line.replace(COLORS[color], '')
    return len(line)

def column_display(rows, num_columns=2):
    """Horrible fluid column layout code ahoy!"""
    columns = []

    column = []
    for row in rows:
        column.append(row)
        if len(column) >= math.floor(float(len(rows))/num_columns):
            columns.append(column)
            column = []
    if len(column) > 0: columns.append(column)

    col_texts = []
    for col in columns:
        coltext = []
        max_keylen = max([len(row[0]) for row in col])
        for row in col:
            padding = ' '*(max_keylen-len(row[0]))
            coltext.append("%s: %s%s" % (row[0], padding, row[1]))
        col_texts.append(coltext)

    result = ""
    for i in range(len(col_texts[0])):
        line = ""

        for j, coltext in enumerate(col_texts):
            if i < len(coltext):
                if j > 0:
                    max_vallen = max([len(row[1]) for row in columns[j-1]])
                    vallen = len(columns[j-1][i][1])
                    line += "\t"*max([1, int(math.floor(float(max_vallen-vallen)/4))])
                line += coltext[i]
        result += line + "\n"

    return result

def center_by(width, uncentered):
    result = ""
    lines = uncentered.split("\n")
    length = max([smartlen(line) for line in lines])
    for line in lines:
        result += ' '*int((width-length)/2) + line + "\n"
    return result

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()

# return ip from external interace
def public_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def service_active(service):
    """Return True if service is running/waiting"""
    cmd = '/bin/systemctl is-active %s' % service
    proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.communicate()
    if proc.returncode == 0:
       return True
    return False

def docker_status():
    if(os.path.isfile("/usr/bin/docker")):
        # docker version
        docker_ver = run_cmd('rpm -qa --queryformat "%{VERSION}" docker')
        # running containers
        docker_run = int(run_cmd('/usr/bin/docker ps -q $1 | wc -l'))
        docker_wipe = int(run_cmd('docker ps -a -q -f status=exited | wc -l'))
        docker = {'status': 'status: %s, ' % (str('[active]')),
                  'version': 'version [%s]' % (str(docker_ver)),
                  'wipe': 'exited containers [%s], ' % (str(docker_wipe)),
                  'running': 'running containers: [%s], ' % (str(docker_run))}
        return(docker)

def fail2ban_status():
    if(os.path.isfile("/usr/bin/fail2ban-client")):
        # get_fail2ban=$(fail2ban-client status sshd | grep -i "Total banned" | awk '{printf $4}')
        # amount of banned ips
        f2ban_proc = run_cmd('/usr/bin/fail2ban-client status sshd')
        category_match = re.search('\W*Total banned[^:]*:\D*(\d+)', f2ban_proc)
        category_match2 = re.search('\W*Currently banned[^:]*:\D*(\d+)', f2ban_proc)
        # returns 0 if nothing there
        banned = category_match.group(1)
        banned_cur = category_match2.group(1)
        f2ban = {'status': 'status: %s, ' % (str('[active]')),
                 'total': 'banned total [%s] ' % (str(banned)),
                 'current': 'currently banned: [%s]' % (str(banned_cur))}
        return(f2ban)

def sysinfo():
    raw_loadavg = run_cmd("cat /proc/loadavg").split()
    # load
    load = {'1min': float(raw_loadavg[0]),
            '5min': float(raw_loadavg[1]),
            '15min': float(raw_loadavg[2])}
    # /home
    raw_home = run_cmd("/bin/df -P /home | tail -1").split()
    raw_home_human = run_cmd("/bin/df -Ph /home | tail -1").split()
    home = {'used': int(raw_home[2]),
            'total': int(raw_home[1]),
            'used_human': raw_home_human[2],
            'total_human': raw_home_human[1],}
    home['ratio'] = float(home['used'])/home['total']
    # memory
    raw_free = run_cmd("/bin/free -b").split("\n")
    raw_mem = raw_free[1].split()
    raw_swap = raw_free[2].split()

    memory = {'used': int(raw_mem[1])-int(raw_mem[2]),
              'total': int(raw_mem[1])}

    memory['ratio'] = float(memory['used'])/memory['total']
    swap = {'used': int(raw_swap[2]),
            'total': int(raw_swap[1])}

    swap['ratio'] = 0.0 if swap['total'] == 0 else float(swap['used'])/swap['total']
    proc_ps = run_cmd('/bin/ps -Afl | wc -l')

    logged_users = run_cmd('/usr/bin/users')
    users = {
             'active': len(set(logged_users))
            }
    proc_product = run_cmd('rpm --eval %product_product')
    proc_version = run_cmd('rpm --eval %product_version')
    os_release = proc_product + ' ' + proc_version

    rows = []
    raw_uptime = run_cmd('uptime')
    uptime = raw_uptime.split(',')[0].split('up')[1].strip()
   # rows.append(['Total Users', str(users['total'])])
    rows.append(['Active Users', str(users['active'])])
    rows.append(['Process Count', str(proc_ps)])
    rows.append(['Uptime', uptime])
    rows.append(['OS', os_release])
    rows.append(['Hostname', socket.gethostname()])

    # colorize
    if load['1min'] < 0.4: load['color'] = 'green'
    elif load['1min'] < 0.8: load['color'] = 'yellow'
    else: load['color'] = 'red'

    rows.append(['System Load', colored(load['color'], str(load['1min']))])

    if home['ratio'] < 0.4: home['color'] = 'green'
    elif home['ratio'] < 0.8: home['color'] = 'yellow'
    else: home['color'] = 'red'

    rows.append(["/home Usage", colored(home['color'], "%d%% of %s" % (home['ratio']*100, home['total_human']))])

    if memory['ratio'] < 0.4: memory['color'] = 'green'
    elif memory['ratio'] < 0.8: memory['color'] = 'yellow'
    else: memory['color'] = 'red'

    rows.append(['Memory Usage', colored(memory['color'], "%d%% of %s" % (memory['ratio']*100, humanise(memory['total'])))])

    if service_active('fail2ban.service'):
       rows.append(['fail2ban', str(fail2ban_status()['status']) + str(fail2ban_status()['total']) +  str(fail2ban_status()['current'])])
    if service_active('docker.service'):
       rows.append(['Docker', str(docker_status()['status']) + str(docker_status()['running']) + str(docker_status()['wipe']) +  str(docker_status()['version'])])

    return(rows)

rootdir_pattern = re.compile('^.*?/devices')
internal_devices = []

def device_state(name):
    with open('/sys/block/%s/device/block/%s/removable' % (name, name)) as f:
        if f.read(1) == '1':
            return

    path = rootdir_pattern.sub('', os.readlink('/sys/block/%s' % name))
    hotplug_buses = ("usb", "ieee1394", "mmc", "pcmcia", "firewire")
    for bus in hotplug_buses:
        if os.path.exists('/sys/bus/%s' % bus):
            for device_bus in os.listdir('/sys/bus/%s/devices' % bus):
                device_link = rootdir_pattern.sub('', os.readlink(
                    '/sys/bus/%s/devices/%s' % (bus, device_bus)))
                if re.search(device_link, path):
                    return
    internal_devices.append(name)

def show_hdd_temp():
    for path in glob('/sys/block/*/device'):
        name = re.sub('.*/(.*?)/device', '\g<1>', path)
        device_state(name)
    for hdd in internal_devices:
        temperature = run_cmd('hddtemp -u C -nq /dev/%s' % hdd)
        print("Disk: [/dev/%s] temperature [%sC]" % (hdd, temperature))

def print_motd():
    print("Hostname:", (hostname()))
    print("Public IP:", (public_ip()))
    docker_status()
    platform_version()
    get_processes()
    fail2ban_status()
    print("Uptime:", (uptime()))
#    print("Load Averages:", (sysinfo()))
    print("Logged users:", users())
    if(os.path.isfile("/usr/bin/hddtemp")):
       show_hdd_temp()

if __name__ == "__main__":
    banner = colored('system', open("/tmp/motd_banner").read())
    banner_length = max([smartlen(line) for line in banner.split("\n")])
    info = center_by(banner_length, column_display(sysinfo(), num_columns=1))
    output = banner + "\n" + info
    fail2ban_status()
    print(output)

#sysinfo()
#hostname()
#show_hdd_temp()
#public_ip()
#print_motd()
#fail2ban_status()
#docker_status()
