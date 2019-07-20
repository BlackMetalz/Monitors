#!/usr/bin/python
# Python2
#Author: Bui Thanh Minh
#Description: Script force recheck a service in Nagios.
#Update to OMD by: kienlt
import pynag.Model
import time,sys
now=int(time.time())
service="Check_MK"
all_hosts = pynag.Model.Host.objects.all
commandfile="/omd/sites/sysadmin/tmp/run/nagios.cmd"
try:
	fh=open(commandfile,'w')
except Exception,e:
	print e
	sys.exit(2)
for host in all_hosts:
	hostname=host.host_name
	msg="[%s] SCHEDULE_FORCED_SVC_CHECK;%s;%s;%s\n" % (now,hostname,service,now)
	print msg
	fh.write(msg)
fh.close()
