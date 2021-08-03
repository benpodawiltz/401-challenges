# !/usr/bin/env python3
#
# script name:  TCP Port Range Scanner - interactive packet manipulation program
# author:       ben_podawiltz
# revision:     8.2.21
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
# Part 2
# [x] User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
# [x] ICMP Ping Sweep tool -  Prompt user for network address including CIDR block, for example “10.10.0.0/24”
# [x] Create a list of all addresses in the given network
# [x] Ping all addresses on the given network except for network address and broadcast address
#     * [x] If no response, inform the user that the host is down or unresponsive.
#     * [x] If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
#     * [x] Otherwise, inform the user that the host is responding.
#     * [x] Count how many hosts are online and inform the user.
##########################################
#
# Libraries
import sys
import logging
from scapy import main 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import ipaddress
##########################################
#
#
# Variables:

host_IP = "scanme.nmap.org" # defines target host
port_range_scan = [20, 22, 80, 443, 3389]

###########################################
#
# 

def main_menu():
    print("[1.] TCP Port Range Scanner mode")
    print("[2.] ICMP Ping Sweep mode")
    print("[3.] Quit")

    user_input = input(
        "Welcome to the Network Security Tool please select method above:")

    if user_input == "1":
        tcpPortRange()
    elif user_input == "2":
        ICMPsweep()
    elif user_input == "3":
        exit
    else:
        print("Error, make another selection")
        main_menu()


def tcpPortRange():
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
                main_menu()

def ICMPsweep():
    netAddr = input("Please enter a network address with CIDR Block in this format[123.456.789.012/00]")
    net_list = ipaddress.ip_network(netAddr)
    print("THIS IS THE ICMP PING SWEEP...")
    liveCT = 0
    for host in net_list.hosts():    # does not include network and broadcast addresses
        ping = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)
    
        if ping is None:
            print(f"{host} is down and/or unresponsive...")
        elif (int(ping.getlayer(ICMP).type)==3 and int(ping.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host} is actively blocking ICMP.")
        else:
            print(f"{host} is responding.")
        liveCT += 1
    
    print(liveCT/net_list.num_addresses + "hosts are online.")
    main_menu()


############################################
# Main
main_menu()

############################################
#
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