# !/usr/bin/env python3
#
# script name:  File_Encryption_02 with Added Logging for Event Logging Tool part I
# author:       ben_podawiltz
# revision:     9.13.21
#
######################################
#
# 
# Libraries:

from cryptography.fernet import Fernet
# import glob
import os
import logging


######################################
# Logging:
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

# Functions:

def main_menu():
    print("[1.] Encrypt a file")
    print("[2.] Decrypt a file")
    print("[3.] Encrypt a message")
    print("[4.] Decrypt a message")
    print("[5.] Encrypt a folder and its contents")
    print("[6.] Decryt a folder and its contents")
    print("[7.] Quit")
    user_input = input(
        "Welcome to the encryption script please select method above:")

    if user_input == "1":
        e_datapath()
    elif user_input == "2":
        d_datapath()
    elif user_input == "3":
        e_message()
    elif user_input == "4":
        d_message()
    elif user_input == "5":
        e_folder()
    elif user_input == "6":
        d_folder()
    elif user_input == "7":
        exit
    else:
        print("Error, make another selection")


#######################################
#
# write and load key functions for encryption processes:


def save_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
       
                
def load_key():
    return open("key.key", "rb").read()


# code borrowed from https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python #
save_key()
key = load_key()
fclass = Fernet(key)


def e_datapath():
    print("Please provide path-to-file for target encryption:")
    e_path = input("Target file for encryption:")
    # opens, reads contents of file then writes encrypted file to it
    with open(e_path, "rb") as e_file:
        myfiledata = e_file.read()
    encrypted_data = fclass.encrypt(myfiledata)
    with open(e_path, "wb") as enc_file:
        enc_file.write(encrypted_data)
    enc_file.close()
    print("**********File is Encrypted**********")
    print("")
    main_menu()


def d_datapath():
    print("Please provide path-to-file for target decryption:")
    d_path = input("Target file for decryption:")
    # opens, reads encrypted data in file then decrypts and writes to file
    with open(d_path, "rb") as d_file:
        enc_datafile = d_file.read()
        decrypted_data = fclass.decrypt(enc_datafile)

    with open(d_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    dec_file.close()
    print("*********File is Decrypted***********")
    print("")
    main_menu()


def e_message():
    msg_input = input("Input Message for encryption:")
    # encodes input message then prints to stndout
    enc_str = msg_input.encode()
    encrypted = fclass.encrypt(enc_str)
    print("*****Message is Encrypted*************")
    print(encrypted)
    main_menu()


def d_message():
    msg_input = input("Input String for decryption:")
    # decrypts ciphertext and prints cleartext to stndout
    d_str = str.encode(msg_input)
    decrypted = fclass.decrypt(d_str)
    print("***********Message is Decrypted**********")
    print(decrypted)
    main_menu()


def e_folder():
    user_dir = input("Enter path-to-folder for encryption:")
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            filename = os.path.join(root, file)
            print(filename)
            with open(filename, 'rb') as og_file:
                og = og_file.read()
                encrypted = fclass.encrypt(og)
            with open(filename, 'wb') as e_file:
                e_file.write(encrypted)
                print(filename, "was encrypted")
    print("\n********Folder Encrypted***********")
    main_menu()


def d_folder():
    user_dir = input("Enter path-to-folder for decryption:")
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            print(os.path.join(root, file))
            filename = os.path.join(root, file)
            with open(filename, 'rb') as og_file:
                og = og_file.read()
                decrypted = fclass.decrypt(og)
            with open(filename, 'wb') as d_file:
                d_file.write(decrypted)
                print(filename, "was encrypted")
                d_file.close()
    print('\n**********Folder Decrypted****************')
    main_menu()



#########################################################
# Call functions:


main_menu()


##########################################################

# Sources: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# https://stackoverflow.com/questions/28583565/str-object-has-no-attribute-decode-python-3-error
# https://medium.com/@abhishake21/encrypt-and-decrypt-files-and-folder-with-a-password-and-salt-of-your-choice-using-python-7101840b2753
# End
