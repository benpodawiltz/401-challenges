#!/usr/bin/python3
#
# script name:  Attack Tools - Nmap port scanning 2 of 3
# author:       ben_podawiltz
# revision:     11.12.21
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


def SynAck ():
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
def UDP ():
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())   
def Comp ():
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, range, '-v -sS -sV -sC -A -O')
        # sS for SYN, sv probe open ports, O is for OS type
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
# Menu options

print("Nmap Automation Tool")
print("--------------------")
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)
range = input("Please enter port range for scanning:  ")

if __name__== "__main__":
    while True:
        resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan        
                4) Exit                    \n""") 
        print("You have selected option: ", resp)
    

        if (resp == "1"):
            SynAck()
        elif (resp == "2"):
            UDP ()
        elif (resp == "3"):
            Comp ()
        elif (resp == "4"):
            print("____Quiting____")
            break
        else:
            print("Error, make another selection:")




    


# Source: https://www.pythonpool/com/python-nmap/


# End