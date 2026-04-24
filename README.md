#Python Network Packet Sniffer
Overview

This project is a simple network packet sniffer built with Python and Scapy. The tool captures live network packets from the local machine and extracts key information such as source and destination IP addresses, protocol types, and port numbers.

It also performs basic service identification by detecting common web traffic such as HTTP and HTTPS based on port numbers.

Packet analysis is an important technique in cybersecurity for understanding network behavior, monitoring traffic, and detecting suspicious activity.

Features

• Captures live network packets
• Extracts source and destination IP addresses
• Identifies TCP, UDP, and ICMP protocols
• Displays source and destination ports
• Detects common services:
HTTP (port 80)
HTTPS (port 443)
• Runs for a limited time to avoid infinite packet capture

How It Works

The program uses Scapy to capture packets from the network interface.
For each packet:
The script checks if the packet contains an IP layer.
It extracts the source IP and destination IP addresses.
It determines whether the packet uses TCP, UDP, or ICMP.
If the packet uses TCP or UDP, the script extracts port numbers.
Common web services such as HTTP and HTTPS are identified using their standard ports.

Possible Improvements

Future improvements could include:

• Logging captured packets to a file
• Filtering packets by protocol or port
• Detecting DNS queries and domain names
• Adding timestamps to packets
• Creating a graphical dashboard for traffic visualization

Learning Outcomes

Through this project I learned:
• How packet sniffing works
• How network packets contain protocol and port information
• How to analyze live network traffic using Python
• How service identification can be done using port numbers

