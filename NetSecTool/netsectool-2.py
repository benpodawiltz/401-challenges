# !/usr/bin/env python3
#
# script name:  Network Security Tool with TCP Port Range Scanner - interactive packet manipulation program & ICMP sweep
# author:       ben_podawiltz
# revision:     8.4.21
#
######################################

##########################################
#
# Libraries
import random
from typing import List
import scapy 
from scapy.all import *
from ipaddress import IPv4Network

##########################################
#
#
# Variables:
print("Welcome to the Network Security Tool")
host_IP = input("Please enter a network address with CIDR Block in this format[123.456.789.012/00]")
port_range_scan = [20, 22, 80, 443, 3389]
addr = IPv4Network(host_IP)
liveCT = 0
###########################################
#
# Functions:


def prt_scan(host: str, ports: List[int]):
    for dst_port in ports:
        srcPort = random.randint(1, 65534)
    RP = sr1(IP(dst=host_IP)/TCP(sport=srcPort,dport=dst_port,flags="S"),timeout=1,verbose=0)

    if RP == None:
                print("The Port...." + str(dst_port) + "....is filtered and silently dropped.")
                print(RP)

    elif (RP.haslayer(TCP)):
        if(RP.getlayer(TCP).flags == 0x12):
            print("The Port...." + str(dst_port) + "....is open. Sending RST packet to close.")
            send_rst = sr(IP(dst=host_IP)/TCP(sport=srcPort,dport=dst_port,flags="R"),timeout=1)
            print(RP)
        elif (RP.getlayer(TCP).flags == 0x14):
                print("The Port...." + str(dst_port) + "....is closed.")
                print(RP)
    
    elif (RP.haslayer(ICMP)):
                if(int(RP.getlayer(ICMP).type)==3 and int(RP.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                    print(f"{host} is filtered and silently dropped.")

# icmp request

for host in addr:    # does not include network and broadcast addresses
    if (host in (addr.network_address, addr.broadcast_address)):
        continue

    
    ping = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)

    if ping is None:
           print(f"{host} is down and/or unresponsive...")
    elif (int(ping.getlayer(ICMP).type)==3 and int(ping.getlayer(ICMP).code) in [1,2,3,9,10,13]):
           print(f"{host} is actively blocking ICMP.")
    else:
            prt_scan(str(host), port_range_scan)
            print(f"{host} is responding.")
            liveCT += 1

print(f"{liveCT}/{addr.num_addresses} hosts are online.")

############################################
#
# Main

# Sources: https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/
# https://santanderglobaltech.com/en/guide-using-scapy-with-python/
#
# Sources: 
# https://docs.python.org/3/library/ipaddress.html
# https://thepacketgeek.com/scapy/building-network-tools/part-10/


# NULL = 0x00
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
# Adding user input range: 
# https://stackoverflow.com/questions/19821273/limiting-user-input-to-a-range-in-python
#
# Scapy Cheat sheet:
# https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
#
#
#
# 
#
#
# End