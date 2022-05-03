![](https://github.com/Phenomenon2919/Network_Scanner/workflows/CI/badge.svg?branch=beta&event=push)
![](https://github.com/Phenomenon2919/Network_Scanner/workflows/CI/badge.svg?branch=master&event=push)

# Network Scanner - Python3 Script

Modular python3 code to list all the IP and MAC Addresses of the devices present in the network.

- Makes use of _scapy_ package.
- **scan_network(ip_address)** : Returns list of IP and corresponding MAC Addresses

## Usage

### Using Source Code

In ./src;

        python3 network_scanner.py -i \<ip_address/netmask>

### Using Executable

        ./Simple.Network.Scanner -i \<ip_address/netmask>
