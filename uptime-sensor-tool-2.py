#!/usr/bin/env python3
#
# script name:  Uptime Sensor tool 1/2
# author:       ben_podawiltz
# revision:     6.30.21
#
######################################
#
# purpose:
# Monitor events taking place throughout the day. Write an uptime sensor tool that checks systems are responding.
# Useful for tracking the status of critical infrastructure, such as web servers
#
######################################
# 1/2
# Requirements:
# [+] Transmit a single ICMP packet to a specifc IP every two seconds
# [+] Evaluate the response as either success or failure
# [+] Assign success or failure to a status variable
# [+] For every ICMP tansmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested: EX. 2020-10-05 17:45:45:510261 Network Active to 8.8.8.8
#
# 2/2
# Requirements:
# [+] Send an email to an administrator if host changes 'up' to 'down'
# [+] Send an email to an administrator if host changes 'down' to 'up'
# [+] Email message should clearly indicate host status change, status before & after, timestamp
#
####################################
#
# Import Libraries:
#
from typing import NoReturn
from pythonping import network, ping  # Used pythonping library to import ping
import datetime
import smtplib
import ssl
from email.message import EmailMessage
from pythonping.executor import SuccessOn
#
#
#######################################
#
# Variables:
#
ip_addr = input("Enter the desired Ip address for ping:")
# ping function with ip variable target and other parameters added
ping_test = ping(ip_addr, timeout=2, verbose=True)
# current date and time function saved to variable
time_now = datetime.datetime.now()
#
#######################################
#
# Functions:
#


def ping_state():
    # if/else statment to evaluate boolean value of ping output
    # set the boolean value of the output of ping_test variable to false
    if ping_test.success(SuccessOn.One) == False:
        print(ping_test.success(SuccessOn.One),  # print(function)ping_test (variable).success (method)(SuccessOn(class).One (variable))
              time_now, "Network is Down:", ip_addr)

    else:
        print(ping_test.success(SuccessOn.One),
              time_now, "Network is Up:", ip_addr)


ping_state()

print("")
####################################################
#
# Send ping state to an administrator's email address
#
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
emailAccount = input("Please enter sender's email address:")
emailPassword = input("Please enter password for email:")
# Enter receiver address
receiver_email = input("Please enter receiver's email address:")
message = input(
    "Body of message needs to include: 1. Ip Address 2. Network status [Up/Down] 3. Status before and after alert:")
print("")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(emailAccount, emailPassword)
    server.sendmail(emailAccount, receiver_email, message)

#######################################
#
#
#
#
# End
