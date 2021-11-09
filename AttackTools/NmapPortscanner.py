#!/usr/bin/python3
#
# script name:  Attack Tools - Nmap port scanning 2 of 3
# author:       ben_podawiltz
# revision:     11.7.21
#
#######################################
#
# Libraries

import nmap

#######################################
#
# Globals
scanner = nmap.PortScanner()
#######################################

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scam       \n""") 
print("You have selected option: ", resp)

range = input("Please enter port range for scanning:  ")
### DONE: Prompt the user to type in a port range for this tool to scan

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())   
 
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS -sV -sC -A -O')
    # sS for SYN, sv probe open ports, O is for OS type
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
elif resp >= '4':
    print("Error, please make another selection: ")



# End

# Source: https://www.pythonpool/com/python-nmap/


