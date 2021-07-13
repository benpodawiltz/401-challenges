# !/usr/bin/env python3
#
# script name:  File_Encryption
# author:       ben_podawiltz
# revision:     7.12.21
#
######################################
#
# Purpose:
# Create a script that utilizes the cryptography library to:
# Prompt the user to select a mode:
# 1. Encrypt a file (mode 1)
# 2. Decrypt a file (mode 2)
# 3. Encrypt a message (mode 3)
# 4. Decrypt a message (mode 4)
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# Depending on the selection, perform one of the below functions.
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
######################################
#
# Variables:

from cryptography.fernet import Fernet


def main_menu():
    print("[1.] Encrypt a file")
    print("[2.] Decrypt a file")
    print("[3.] Encrypt a message")
    print("[4.] Decrypt a message")
    print("[5.] Quit")
    user_input = input(
        "Welcome to the encryption script please select method above:")

    if user_input == "1":
        e_datapath
    elif user_input == "2":
        d_datapath
    elif user_input == "3":
        e_message
    elif user_input == "4":
        d_mesage
    else:
        print("Error, make another selection")


main_menu()
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

    with open(e_path, "rb") as e_file:
        myfiledata = e_file.read()
        encrypted_data = fclass.encrypt(myfiledata)
    with open(e_path, "wb") as enc_file:
        enc_file.write(encrypted_data)

        print("**********File is Encrypted**********")
        print("")


e_datapath()


def d_datapath():
    print("Please provide path-to-file for target decryption:")
    d_path = input("Target file for decryption:")

    with open(d_path, "rb") as d_file:
        enc_datafile = d_file.read()
        decrypted_data = fclass.decrypt(enc_datafile)

    with open(d_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

        print("*********File is Decrypted***********")
        print("")


d_datapath()
main_menu()


def e_message():
    print("Input string for encryption:")
    msg_input = input("Message for encryption:").encode()
    print(str(msg_input.decode('utf-8')))
    enc_str = fclass.encrypt(msg_input)
    print("*****Message is Encrypted*************")


def d_message():
    print("Input string for decryption:")
    msg_input = input("Message for decryption:").decode()
    print(str(msg_input.decode('utf-8')))
    enc_str = fclass.encrypt(msg_input)
    print(enc_str.decode("utf-8"))
    print("***********Message is Decrypted**********")


##########################################################
main_menu()
# End
