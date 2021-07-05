#!/bin/bash

# Tello drones do not have the functionality to operate in swarm mode and provide a video feed.
# These commands are used on separate machines (raspberry pis) to connect to a single drone and route packets to another machine.
# This way one machine can communicate with and control all drones, while receiving video feeds from all of them individually.

sudo iptables -F
sudo iptables -t nat -F

# 192.168.0.0/24 says anything from that network
sudo iptables -t nat -A PREROUTING -s 192.168.0.0/24 -i eth0 -j DNAT --to-destination 192.168.10.1
# Destination 192.168.0.11 can be whatever address you want to handle responses
sudo iptables -t nat -A PREROUTING -s 192.168.10.1 -i wlan0 -j DNAT --to-destination 192.168.0.11 

sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'

sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
