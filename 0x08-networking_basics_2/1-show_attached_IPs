#!/usr/bin/env bash
# Bash script that displays all active IPv4 IPs on the machine it’s executed on.

# Use the 'ip' command to retrieve active IPv4 addresses
ipv4_addresses=$(ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
echo "$ipv4_addresses"
