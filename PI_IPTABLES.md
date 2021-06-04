### iptables commands for Raspberry Pi(s) to enable a network transmission model for recording video with a Tello drone swarm.

`sudo iptables -t nat PREROUTING -s 192.168.1.100 -i eth0 -j DNAT --to-destination 192.168.10.1`

`sudo iptables -t nat PREROUTING -s 192.168.10.1 -i wlan0 -j DNAT --to-destination 192.168.1.100`

`sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'`

`sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT`

`sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT`

`sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`

`sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE`
