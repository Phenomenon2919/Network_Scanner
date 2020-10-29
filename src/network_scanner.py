#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def scan_network(ip_address):

    arp_request = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    client_info_list = []

    for packet_list in answered:
        packet_dict = {"ip":packet_list[1].psrc,"mac":packet_list[1].hwsrc}
        client_info_list.append(packet_dict)

    return client_info_list

def print_client_info(client_info_list):

    print("IP Address\t\t\tMAC Address\n--------------------------------------------------------")

    for client_info in client_info_list:
        print(client_info["ip"] + "\t\t\t" + client_info["mac"])

    print("--------------------------------------------------------")

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--ip", help="Provide IP Address \ne.g 10.0.2.0 or 10.0.2.1/16", dest="ip_address")
    options = arg_parser.parse_args()

    if not options.ip_address:
        arg_parser.print_help()
        exit()
    return options

if __name__ == "__main__":

    options = get_args()
    client_info_list = scan_network(options.ip_address)

    print_client_info(client_info_list)