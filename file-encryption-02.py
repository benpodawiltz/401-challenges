# !/usr/bin/env python3
#
# script name:  File_Encryption_02
# author:       ben_podawiltz
# revision:     7.14.21
#
######################################
#
# Purpose:
# Part 1
# Create a script that utilizes the cryptography library to:
# 1. Encrypt a file (mode 1)
# 2. Decrypt a file (mode 2)
# 3. Encrypt a message (mode 3)
# 4. Decrypt a message (mode 4)
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#
# You’ll need to create four functions:
# 1. Encrypt the target file if in mode 1.
# 2. Delete the existing target file and replace it entirely with the encrypted version.
# 3. Decrypt the target file if in mode 2.
# 4. Delete the encrypted target file and replace it entirely with the encrypted version.
# 5. Encrypt the string if in mode 3.
# 6. Print the ciphertext to the screen.
# 7. Decrypt the string if in mode 4.
# 8. Print the cleartext to the screen.
#
# Part 2
# Add to the script:
# 1. Recursively encrypt a single folder and all its contents.
# 2. Recursively decrypt a single folder that was encrypted by this tool.
#
######################################
#
# Libraries:

from cryptography.fernet import Fernet
# import glob
import os

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
    for filenames in os.listdir(user_dir):
        # iterate over files
        for filename in filenames:
            print("File:", os.path.join(filename))

        contents = os.path.join(user_dir, filenames)
        with open(contents, "rb") as file:
            openfile = file.read()
            e_file = fclass.encrypt(openfile)
        with open(contents, "wb") as file:
            file.write(e_file)
            print(e_file)
            main_menu()


def d_folder():
    user_dir = input("Enter path-to-folder for decryption:")
    for filenames in os.listdir(user_dir):
        # iterate over files
        for filename in filenames:
            print("File:", os.path.join(filename))

        contents = os.path.join(user_dir, filenames)
        with open(contents, "rb") as file:
            openfile = file.read()
            d_file = fclass.decrypt(openfile)
        with open(contents, "wb") as file:
            file.write(d_file)
            print(d_file)
            main_menu()
#########################################################
# Call functions:


main_menu()


##########################################################

# Sources: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# https://stackoverflow.com/questions/28583565/str-object-has-no-attribute-decode-python-3-error
#
# End
