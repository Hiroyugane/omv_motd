# Changelog

## 0.0.1pre4 // 11.10.2019

* finished commenting and started documenting organization-structures for the program and other stuff in doc/organization.md
* deleted repository and reforked since it didn't display right and that annoyed me. Also put (probably) not needed files from fork into archive-folder. Folderstructure will be an important part of the project for now

## 0.0.1pre3

* replaced docker_ver-command
  * notice: all replaced commands should be commented out so they can be reused for the distro they're made for again
* sysinfo:
  * put uptime out of rows.append-part
  * reorganized colorization-part a little

## 0.0.1pre2 // 10.10.2019

* further commenting added (about 40% done)
* added Todo-File with roadmap and other stuff
* redone public ip-findout since used method doesn't work (for home-servers)
  * added urllib.request import

## 0.0.1pre1 // 09.10.2019

* added various descriptive comments
* converted serveral (mostly regex-including) strings to raw-strings to remove pylint-warnings
* humanise:
  * changed varname 'num' to 'byte_int'
  * added function for smaller ints to get an additional decimal
  * changed main from 3-wide int to 4-wide for numbers 1000-1024
  * changed list from KB/MB/etc. to KiB/MiB/etc. for scientific accurracy
* column_display
  * changed var "col" to "column" (Inconsistend var-names are bad manners)

## 0.0.1pre0 // 08.10.2019

* initial fork
