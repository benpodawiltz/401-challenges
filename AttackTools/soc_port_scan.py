#!/usr/bin/python3
# Script name: Ops Challenge 44 - python scanner using sockets
# Name: Ben podawiltz
# Date: 11.15.21
# 
# Libraries: 
import socket
###########################################


sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket object with tcp connection & ipv4 address 
timeout = 10
sockmod.settimeout(timeout)

hostip = input("Please enter an ip address for scanning:  ")
portno = int(input("Please enter a port for scanning:  "))

def portScanner(portno):
    connection = sockmod.connect_ex((hostip, portno))
    if connection == 0:
        print("The Port is open")
    else:
        print("The Port is closed")

portScanner(portno)


###########################################

# Resources: https://wwww.geeksforgeeks.org/socket-programming-python/


# End
