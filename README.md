## About this fork 
This fork will become a customized and more structurized approach to the original motd(-python)-script 

## This is the goal to achieve (NOT ACTUAL OUTPUT FROM BRANCH (yet))
![Alt text](/image/demo.png?raw=true "OpenMandriva /etc/motd")



## Current version (synced fork)
Copy script to bindir

```bash
# cp -v motd_hello_gen /usr/bin/
```

Copy motd service and timer files to systemd service dir

```bash
# cp motd.service motd.timer /etc/systemd/system/
```

Enable timer

```bash
# systemctl enable motd.timer
```

![Alt text](/image/motd.png?raw=true "OpenMandriva /etc/motd")
