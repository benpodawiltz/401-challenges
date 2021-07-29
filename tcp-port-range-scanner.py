# !/usr/bin/env python3
#
# script name:  TCP Port Range Scanner - interactive packet manipulation program
# author:       ben_podawiltz
# revision:     7.28.21
#
######################################
#
# Purpose:
# Part 1
# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
# [x] Utilize the scapy library
# [x] Define Host IP
# [x] Define port range or specific set of ports to scan
# [x] Test each port in specified range using a fot loop
#       * If flag 0x12 received send a RST packet to graciously close the open connection
#       * Notify the user the port is open
#       * If flag 0x14 received, notify user the port is closed
#       * If no flag is received, notify the user the port is filtered and silently dropped
# [ ] Utilize the random library
# [ ] Randomize the TCP source port in hopes of obfusticating the source of the scan
#
#
#
##########################################
#
# Libraries
import sys
import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

##########################################
#
#
# Variables:

host_IP = "scanme.nmap.org" # defines target host
port_range_scan = [20, 21, 22]


###########################################
#
# 
for dst_port in port_range_scan:
    srcPort = 22
    tcpResponse = sr1(IP(dst=host_IP)/TCP(sport=srcPort,dport=dst_port,flags="S"),timeout=1,verbose=0)

    if tcpResponse == None:
        print("The Port...." + str(dst_port) + "....is filtered and silently dropped.")
        print(tcpResponse)

    elif (tcpResponse.haslayer(TCP)):
            if(tcpResponse.getlayer(TCP).flags == 0x12):
                print("The Port...." + str(dst_port) + "....is open. Sending RST packet to close.")
                send_rst = sr(IP(dst=host_IP)/TCP(sport=srcPort,dport=dst_port,flags="R"),timeout=10)
                print(tcpResponse)
            elif (tcpResponse.getlayer(TCP).flags == 0x14):
                print("The Port...." + str(dst_port) + "....is closed.")
                print(tcpResponse)



############################################
#
# Sources: https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/
# https://santanderglobaltech.com/en/guide-using-scapy-with-python/
#
#
#NULL = 0x00
# END = 0x01
# SYN = 0x02
# RST = 0x04
# PSH = 0x08
# ACK = 0x10
# SYN + ACK = 0x12
# RST + ACK = 0x14
# PSH + ACK = 0x18
#
#
#
#
#
#
#
#
#
#
#
# End