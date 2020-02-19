#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

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