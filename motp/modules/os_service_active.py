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
