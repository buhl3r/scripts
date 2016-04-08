#!/usr/bin/python
import os
from commands import getoutput

#string = str(os.popen("ip addr show eth0 | grep 'inet [1-254]\(.\)'").readlines())
#ip = string.split()[2]         #'192.168.1.228/24'
#ip2 = ip.rsplit('.',1)[0]      #'192.168.1'
#for i in range(1,254):
#       print 'os.system("ping %ip2+'.'+i -c 1 | grep 'time=' | cut -d ':' -f 1 | cut -d ' ' -f 4")'


########################################
##OR
#
#
command = "ip addr show eth0 | grep 'inet [1-254]\(.\)' | awk -F ' ' ' {print $2; }'"
process = os.popen(command)
ip = str(process.read())
ip2 =ip.rsplit('.',1)[0]

for i in range(1,254):
        ping = getoutput("ping -c1 %s" % ip2+"."+str(i))
        if ping.find("bytes from")>-1:
                ip_final = ping.split(' ')[1]
                print ip_final

