#!/usr/bin/env python3
#
# script name:  Uptime Sensor tool 1/2
# author:       ben_podawiltz
# revision:     7.7.21
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
# [] Email message should clearly indicate host status change, status before & after, timestamp
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
ping_text = open("ping_state.txt", "w")

#######################################
#
# Functions:
#


def ping_state():
    # if/else statment to evaluate boolean value of ping output
    # set the boolean value of the output of ping_test variable to false
    if ping_test.success(SuccessOn.One) == False:
        print(ping_test.success(SuccessOn.One),  # print(function)ping_test (variable).success (method)(SuccessOn(class).One (variable))
              time_now, "Network is Down:", ip_addr, file=ping_text)

    else:
        print(ping_test.success(SuccessOn.One),
              time_now, "Network is Up:", ip_addr, file=ping_text)


print("")
ping_state()

####################################################
#
# Send ping state to an administrator's email address
#


admin_email = input("Please enter administrator email address:")
sent_from = "colin@gmail.com"
gmail_pass = input("Please enter password:")
to = admin_email
body = ("Attached is a document indicating a server is up or down and the network address" +
        input("Please enter additional network status event information for admistrator:"))
subject = "Network status notification"
email_text = """\
    From: %s
    To: %s
    Subject : %s

    %s
    """ % (sent_from, ",".join(to), subject, body)


try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(admin_email, gmail_pass)
    server.sendmail(sent_from, to, email_text)

    print("Email sent")

except:
    print("Connection not established")


#
########################################

########################################
#
# Comment:  Still working on this one. I have a workable email template but I don't care for how the string in the server.sendmail is diplayed in the GUI email inbox. This script still needs
# 1. the ping_state.txt attached
# 2. Some logic to determine the Network up/down state to be sent in the body of the email
# 3. Date/time stamp attached to attachment
# 4. The text file doesn't display results till after the email has sent despite the function being called prior to email
#
# End
