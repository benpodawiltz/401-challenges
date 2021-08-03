# Ops Challenge: Network Security Tool with Scapy Part 2 of 3
## Overview
> Tools like Nmap are quite useful on their own, but what about customizing its capabilities? Because we know a little Python, we can explore creating our own network scanning tool with the Python library Scapy. Today you’ll continue development of your own network scanning tool.

## Part One
* In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

1. Utilize the scapy library
2. Define host IP
3. Define port range or specific set of ports to scan
4. Test each port in the specified range using a for loop
5. If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
6. If flag 0x14 received, notify user the port is closed.
7. If no flag is received, notify the user the port is filtered and silently dropped.
8. Utilize the random library
9. Randomize the TCP source port in hopes of obfusticating the source of the scan 

## Part Two
* Generating a Range of IP Addresses from a CIDR Address in Python
## Requirements
* Add the following features to your Network Security Tool:

1. User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
ICMP Ping Sweep tool
2. Prompt user for network address including CIDR block, for example “10.10.0.0/24”
__Careful not to populate the host bits!__

3. Create a list of all addresses in the given network
4. Ping all addresses on the given network except for network address and broadcast address
5. If no response, inform the user that the host is down or unresponsive.
6. If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
8. Otherwise, inform the user that the host is responding.
Count how many hosts are online and inform the user.