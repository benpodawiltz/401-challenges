#!/usr/bin/env python3
#
# script name:  Uptime Sensor tool 1/2
# author:       ben_podawiltz
# revision:     6.29.21
#
######################################
#
# purpose:
# Monitor events taking place throughout the day. Write an uptime sensor tool that checks systems are responding.
# Useful for tracking the status of critical infrastructure, such as web servers
#
######################################
#
# Requirements:
# [+] Transmit a single ICMP packet to a specifc IP every two seconds
# [+] Evaluate the response as either success or failure
# [+] Assign success or failure to a status variable
# [+] For every ICMP tansmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested: EX. 2020-10-05 17:45:45:510261 Network Active to 8.8.8.8
#
#######################################
#
# Import Library:
from typing import NoReturn
from pythonping import network, ping  # Used pythonping library to import ping
import datetime

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
#
#######################################
#
# Functions:
#


def ping_state():

    if ping_test.success(SuccessOn.One) == False:
        print(ping_test.success(SuccessOn.One),
              time_now, "Network is Down:", ip_addr)

    else:
        print(ping_test.success(SuccessOn.One),
              time_now, "Network is Up:", ip_addr)


#
#
#######################################
#
#
# Main
#
ping_state()
#
#
# End
