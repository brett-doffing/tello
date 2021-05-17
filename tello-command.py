"""
This will prompt a user to enter a command for a Tello drone.

Tello SDK v1.0.0 commands = "https://dl-cdn.ryzerobotics.com/downloads/tello/0228/Tello+SDK+Readme.pdf"
Tello SDK v1.3.0 commands = "https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20编程相关/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf"
Tello SDK v2.0 User Guide = "https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf"
Mission Pad User Guide v1.0 = "https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20Mission%20Pad%20User%20Guide.pdf"
"""

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_addr = ("192.168.10.1", 8889)
sock.bind(("", 9000))

while True:
    try:
        msg = input("Enter a command: ")
        if not msg:
            break
        if "end" in msg:
            sock.close()
            break
        msg = msg.encode()
        print(msg)

        sent = sock.sendto(msg, tello_addr)
        response = sock.recv(1024)
        print(response)
    except Exception as err:
        print(err)
        sock.close()
        break
