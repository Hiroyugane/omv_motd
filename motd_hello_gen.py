#!/usr/bin/env python
import os
import subprocess
import socket
import platform
import sys
import re

def hostname():
#    with open('/etc/motd', 'w') as motd:
#          motd.write(socket.gethostname())
    return socket.gethostname()

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
        cmd_ver = 'rpm -qa --queryformat "%{VERSION}" docker'
        proc_version = subprocess.Popen(cmd_ver, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        docker_ver = proc_version.communicate()[0].decode('utf-8').strip()

        cmd_run = '/usr/bin/docker ps -q $1 | wc -l'
        proc_running = subprocess.Popen(cmd_run, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        docker_run = proc_running.communicate()[0].decode('utf-8').strip()
        if service_active('docker.service'):
            print("docker: [active]" + " " + "version: [%s] running: [%s]" % (docker_ver, docker_run))
        else:
            print("docker: [inactive]")

def platform_version():
    cmd_product = 'rpm --eval %product_product'
    cmd_version = 'rpm --eval %product_version'
    proc_version = subprocess.Popen(cmd_product, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    proc_product = subprocess.Popen(cmd_version, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    print("OS: %s %s for [%s]" % (proc_version, proc_product, platform.machine()))

def getloadavg():
	r = os.getloadavg()
	return('{} {} {}'.format(r[0],r[1],r[2]))

def get_processes():
    cmd_ps = '/bin/ps -Afl | wc -l'
    proc_ps = subprocess.Popen(cmd_ps, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    print("Processes: [%s]" % (proc_ps))

def uptime():
    try:
        f = open( "/proc/uptime" )
        contents = f.read().split()
        f.close()
    except:
       return "Cannot open uptime file: /proc/uptime"
    total_seconds = float(contents[0])
    # Helper vars:
    MINUTE  = 60
    HOUR    = MINUTE * 60
    DAY     = HOUR * 24

    # Get the days, hours, etc:
    days    = int( total_seconds / DAY )
    hours   = int( ( total_seconds % DAY ) / HOUR )
    minutes = int( ( total_seconds % HOUR ) / MINUTE )
    seconds = int( total_seconds % MINUTE )
    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
    string = ""
    if days > 0:
        string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
    if len(string) > 0 or hours > 0:
        string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
    if len(string) > 0 or minutes > 0:
        string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" )
    return string;

def fail2ban_status():
    if(os.path.isfile("/usr/bin/fail2ban-client")):
        if service_active('fail2ban.service'):
           # get_fail2ban=$(fail2ban-client status sshd | grep -i "Total banned" | awk '{printf $4}')
           # amount of banned ips
           cmd_f2b = '/usr/bin/fail2ban-client status sshd'
           f2ban_proc = subprocess.Popen(cmd_f2b, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
           category_match = re.search('\W*Total banned[^:]*:\D*(\d+)', f2ban_proc)
           category_match2 = re.search('\W*Currently banned[^:]*:\D*(\d+)', f2ban_proc)
           # returns 0 if nothing there
           banned = category_match.group(1)
           banned_cur = category_match2.group(1)
           print("fail2ban: [active], total banned [%s], currently banned [%s]" % (banned, banned_cur) )

def users():
    cmd_run = '/usr/bin/who | /usr/bin/cut -d" " -f1 | /usr/bin/uniq'
    proc_running = subprocess.Popen(cmd_run, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    users = proc_running.communicate()[0].decode('utf-8').strip()
    return(users)

def print_motd():
    print("Hostname:", (hostname()))
    print("Public IP:", (public_ip()))
    docker_status()
    platform_version()
    get_processes()
    fail2ban_status()
    print("Uptime: ", (uptime()))
    print("Load Averages: ", (getloadavg()))
    print("Logged users:", users())

#hostname()
#public_ip()
print_motd()
#fail2ban_status()
#docker_status()
