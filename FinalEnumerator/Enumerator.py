#!/usr/bin/python3
# script name:  Enumerator Tools - Final
# author:       ben_podawiltz
# revision:     11.28.21
#
#######################################
#
# Libraries

import socket, sys
import nmap
import os
#######################################

nm = nmap.PortScanner()

def port_scan(host):
    try:
        port = input("Please enter port number to scan:  ")
        port = int(port)
        socmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = 30
        socmod.settimeout(timeout) 
        connection = socmod.connect((host, port))
        if connection == 0:
            print("The Port is open")
        else:
            print("The Port is closed")
    except socket.error as socketerror:
        print("Error: ", socketerror)

def os_version():
        ports=input("Input port range [1-1024]: ")
        print("Nmap Version: ", nm.nmap_version())
        nm.scan(host, ports, '-O -sU')
        print(nm.scaninfo())
        print("Ip Status: ", nm[host].state())
        print("Protocols:", nm[host].all_protocols())
        print("Open Ports: ", nm[host]['udp'].keys())
        print("*" * 25)
        print("")


def bannergrab(host):
        port = input("Please enter port number to scan:  ")
        port = int(port)  
        socmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET corresponds to ipv4 // SOCK_STEAM corresponds to TCP = a tcp socket for ipv4 is created and saved to an object
        timeout = 30
        socmod.settimeout(timeout)
         # connect to the host
        socmod.connect((host, port))   
        print("Socket successfully created")
        print(socmod.recv(1024)) 
        socmod.close()

def get_cookie():
    print("*" * 25)
    nm.scan(host, '--script=/home/benjamin/github/401/401-challenges/AttackTools/cookie.nse')
    print(nm.scaninfo())
    print("*" * 25)

def vuln():
    portrange = input("Please enter port range to scan [1-1024]: ")
    print("*" * 5 + "Nmap is scanning for Vulnerabilities" + "*" * 5)
    nm.scan('--script vuln', host, portrange) 
    print(nm.scaninfo())
    print("*" * 25)
    print("")
   

########################################
print("*" * 25)
print("Welcome to the Enumerator")
host = input("Please enter IP address to scan:  ")    
print("You have chosen to scan:", host)

if __name__== "__main__":
    while True:
        user_input = input("""\nPlease select a scan to run:  
                    [1.] OS version
                    [2.] Port Scan
                    [3.] Banner Grab
                    [4.] NSE - Lua Cookie
                    [5.] NSE - Vuln Scanner
                    [6.] Exit\n""")
        print("*" * 25)
    
        if user_input == "1":
            os_version()
        elif user_input == "2":
            port_scan(host)
        elif user_input == "3":
            bannergrab(host)
        elif user_input == "4":
            get_cookie()
        elif user_input == "5":
            vuln()
        elif user_input == "6":
            sys.exit()
        else:
            print("Error, make another selection")
########################################

# End