#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome to Atronix IT Tech's Nmap Automation Tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("You have selected option: ", resp)
resp_dict = {'1': ['-v -sS', 'tcp'], '2': ['-v -sU', 'udp'], '3': ['-v -sS -sV -sC -A -O', 'tcp']}
if resp not in resp_dict.keys():
    print("Enter a valid option")
else:
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])  # the numbers are port range to scan, the last part is the scan type
    print(scanner.scaninfo())
    if scanner[ip_addr].state() == 'up':
        print("Scanner Status: ", scanner[ip_addr].state())
        print("Protocols: ", scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr][resp_dict[resp][1]].keys())  # display all open ports
