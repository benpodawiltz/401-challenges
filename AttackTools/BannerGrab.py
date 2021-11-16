#!/usr/bin/python3
# script name:  Attack Tools - Ops Challenge 45 - Create a Banner Grabber
# author:       ben_podawiltz
# revision:     11.15.21
#
#######################################
#
# Libraries

import socket

#######################################

def bannergrab(host):
        port = input("Please enter port number to scan:  ")
        port = int(port)  
        socmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET corresponds to ipv4 // SOCK_STEAM corresponds to TCP = a tcp socket for ipv4 is created and saved to an object
        timeout = 0
        socmod.settimeout(timeout)
      
         # connect to the host
        socmod.connect((host, port))   
        print("Socket successfully created")
        print(socmod.recv(1024)) 
       
        

def portscan(host):
        port = input("Please enter port number to scan:  ")
        port = int(port)
        socmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = 20
        socmod.settimeout(timeout) 
        connection = socmod.connect_ex((host, port))
        if connection == 0:
            print("The Port is open")
        else:
            print("The Port is closed")

host = input("Please enter IP address to scan:  ")    
print("You have chosen to scan:", host)

if __name__== "__main__":
    while True:
        user_input = input("""\nPlease select a scan to run:  
                    [1.] Banner Grab
                    [2.] Port Scan with tcp socket connection\n""")
        if user_input == "1":
            bannergrab(host)
        elif user_input == "2":
            portscan(host)
        else:
            print("Error, make another selection")

# End
