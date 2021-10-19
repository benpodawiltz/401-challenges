# !/usr/bin/env python3
#
# script name:  Web Application Fingerprinting tool pary 1 of 3
# author:       ben_podawiltz
# revision:     10.18.21
#
######################################


######################################
#
# Libraries
import os
######################################

ip_addr = input("Please input ip address for service fingerprinting: ")
port = input ("Please input port number for service fingerprinting: ")
    # 80 

def netcat (ip_addr, port):
    print("_" * 5 + "Netcat is scanning" + "_" * 5)
    os.system("nc -v " + ip_addr + " " + port) 
    print("*" * 25)
    print("")

def telnet (ip_addr, port):
    os.system("telnet " + ip_addr + " " + port)
    print("*" * 25)
    print("")

def nmap(ip_addr, port):
    os.system("nmap -p 1-1023 -script=banner " + ip_addr)
    print("*" * 25)
    print("")
########################################

netcat(ip_addr, port)
telnet(ip_addr, port)
nmap(ip_addr, port)


########################################

# Resource: https://www.putorius.net/banner-grabbing.html
# End